

# ESP8266 serial bridge


It is possible to export the serial TTL console of most routers through Wifi via those cheap ESP8266 serial2wifi modules.

I am using an ESP8266-12E-Devkit from Aliexpress (NodeMcu Lua ESP8266 ESP-12E WIFI Development Board (SKU256450) EUR 8.92). It has a CP2102 usb-serial adaptor.

[[=image esp8266-12E-devkit.jpg size="medium"]]

# Pinout


[[=image esp8266-openwrt-glinet-wifi2serial.jpg size="medium"]]

In this example, we use the ESP-12 module powered over a 5V USB cable. As the ESP8266 works in 3.3V, and most openwrt routers works on 3.3V TTL, it is not necessary to do any voltage conversion. You can then connect the GND, TX, RX pins of the ESP8266 to the GND, RX, TX of the router respectively. Alternatively, you could also suck the 3.3V power from on the fourth pin of the serial header, usually labelled VCC.

# Firmware


The goal here is to document how to export serial consoles through the network with the ESP-LINK firmware.

<https://github.com/jeelabs/esp-link>  

# Screenshots


You can connect to the web interface, unfortunately the console only allows you to view the output of the openwrt console, not to input anything:

[[=image esp8266-openwrt-glinet-wifi2serial-webconsole.jpg size="medium"]]

For the input, you can telnet to the IP of the ESP8266 on port 23, via telnet or netcat or socat:

[[=image esp8266-openwrt-glinet-wifi2serial-telnet.jpg]]

However, if you launch programs like "top", you will have a hard time to exit, as CRTL-C does not seem to work...

In order to be able to use CTRL-C, you need to configure telnet with a .telnetrc in your home directory [<http://unix.stackexchange.com/questions/224735/telnet-why-application-doesnt-read-telnetrc>   with mode character], which takes the following syntax (the 192.168.0.10 is the IP address of the ESP):


    zoobab@chuchu /home/zoobab [1]$ cat .telnetrc 
    192.168.0.10
            mode character


# Other tools: socat, putty


With putty, it seems that the CTRL-C issue is better handeld, at least I can launch "top" and go out of it with CTRL-C:

[[=image esp8266-openwrt-glinet-wifi2serial-putty.jpg]]

You can also use socat instead of telnet:


    zoobab@chuchu /home/zoobab [23]$ socat stdio, tcp-connect:192.168.0.10:23
    root@GL-iNet:/#


Another way of using socat is to redirect the TCP to a /dev/tty entry like /dev/vmodem0 for example:


    root@chuchu /home/zoobab [6]#  socat pty,link=/dev/vmodem0,waitslave tcp:192.168.0.10:23


One socat is running, you can connect to the device (with CRTL-C working and being able to out of top) with screen:


    root@chuchu /home/zoobab [2]# screen /dev/vmodem0
    root@GL-iNet:/# 
    root@GL-iNet:/# ls


# Upload a file with serio


You can also upload a file with the [<https://github.com/devttys0/serio>   serio python program], but you have to first setup a virtual serial port with socat:


    zoobab@chuchu /home/zoobab [62]$ sudo socat pty,link=/dev/vmodem0,waitslave tcp:192.168.0.10:23


Then you have to comment the line containing "self.s.open()" as this might report an error like "ERROR: Port is already open.":


    zoobab@chuchu /home/zoobab [62]$ sudo ./serio.py -s /home/zoobab/memo -d /tmp/memo -p /dev/vmodem0
    ERROR: Port is already open.


Then you might be able to upload a file:


    root@chuchu /home/zoobab/soft/esp8266 [14]# ./serio.py -s /home/zoobab/memo -d /tmp/memo -p /dev/vmodem0 -b 115200
    20 / 1464
    40 / 1464
    60 / 1464
    80 / 1464
    100 / 1464
    [...]
    1440 / 1464
    1460 / 1464
    1464 / 1464
    Uploaded 1464 bytes from /home/zoobab/memo to /tmp/memo
    root@chuchu /home/zoobab/soft/esp8266 [15]#


As you can see, it uploads the file per packs of 20 bytes. This is an hardcoded value in the serio code "BYTES_PER_LINE = 20".

I have created a 100KB file with dd filed with random content, and uploaded it with serio to see how long it would take to upload:


    root@chuchu /home/zoobab/soft/serio [10]# time ./serio.py -s 100K -d /tmp/100K -p /dev/vmodem0
    
    [...]
    
    102360 / 102400
    102380 / 102400
    102400 / 102400
    Uploaded 102400 bytes from 100K to /tmp/100K
    
    real    8m34.360s
    user    0m1.062s
    sys     0m0.212s


Which is roughly 0.20KB/sec. A 1MB file would then take 85 minutes, or 1H25 to complete.

The ESP8266 can support faster baud rates on the serial console as mentioned on the [<https://hackaday.io/project/6490-a-versatile-labtool/log/27732-esp8266using-the-jeelabs-transparent-tcp-uart-bridge>   Hackaday.io project], the other question is whether the serial console of the Linux kernel could be set to a higher baud rate then 115200.

# Todo


* Try with some ESP01 modules (flashing was less easy as with the ESP12)
* Buy some ESP05 modules to provide a reconfigurable tiny 4 pins adaptor with a simple PCB like the ModernDevice FTDI
* Buy some RS232 with MAX232 chips for Cisco and other routers
* Input through the web console
* HTTPS cloud console, ajaxterm or similar
* Control reset buttons on the router
* Ser2net export
* Document the flashing procedure
* Suck power from the VCC
* Crtl-c and go out of top?

# Links


* <http://unix.stackexchange.com/questions/31741/how-can-i-use-command-line-telnet-client-to-open-a-raw-connection-like-putty>  
* <http://www.dest-unreach.org/socat/doc/socat-ttyovertcp.txt>  
* https://github.com/devttys0/serio
* <http://wiki.openwrt.org/esp8266-serial-bridge>  
* http://unix.stackexchange.com/questions/224735/telnet-why-application-doesnt-read-telnetrc
* https://hackaday.io/project/6490-a-versatile-labtool/log/27732-esp8266using-the-jeelabs-transparent-tcp-uart-bridge