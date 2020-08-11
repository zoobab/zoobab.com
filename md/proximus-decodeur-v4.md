# About


The Proximus Decodeur v4 is given with the Scarlet default pack.

[[=image proximus-decodeur-v4.png]]

# Port scan



    $ sudo nmap 192.168.1.64
    Starting Nmap 7.60 ( https://nmap.org ) at 2020-05-10 20:56 CEST
    Nmap scan report for 192.168.1.64
    Host is up (0.0024s latency).
    Not shown: 997 closed ports
    PORT      STATE SERVICE
    22/tcp    open  ssh
    9001/tcp  open  tor-orport
    49152/tcp open  unknown
    MAC Address: 38:C8:5C:C2:50:22 (Cisco Spvtg)


A curl at this port 49152 reveals a box running a Linux kernel "Linux/2.6.31-3.3-isb6030 UPnP/1.0 DLNADOC/1.50 Portable SDK for UPnP devices/1.4.6-6":


    $ curl -vvv http://192.168.1.64:49152
    * Rebuilt URL to: http://192.168.1.64:49152/
    *   Trying 192.168.1.64...
    * TCP_NODELAY set
    * Connected to 192.168.1.64 (192.168.1.64) port 49152 (#0)
    > GET / HTTP/1.1
    > Host: 192.168.1.64:49152
    > User-Agent: curl/7.58.0
    > Accept: */*
    > 
    < HTTP/1.1 500 Internal Server Error
    < SERVER: Linux/2.6.31-3.3-isb6030 UPnP/1.0 DLNADOC/1.50 Portable SDK for UPnP devices/1.4.6-6
    < CONNECTION: close
    < CONTENT-LENGTH: 60
    < CONTENT-TYPE: text/html
    < 
    * Closing connection 0
    <html><body><h1>500 Internal Server Error</h1></body></html>


It is a Cisco ISB6030.

It runs a Dropbear SSH server:


    $ telnet 192.168.1.64 22
    Trying 192.168.1.64...
    Connected to 192.168.1.64.
    Escape character is '^]'.
    SSH-2.0-dropbear_0.52


# Serial port?


Looking at the PCB pictures, this 4 pins connectors looks like a good candidate for a serial console:

[[=image cisco-isb-6030-pcb-serialport.jpg size="medium"]]

After further analysis, it looks more like a USB connector.

A better picture of the PCB is available at <https://www.circuitsonline.net/forum/view/141264>  

On the top right, you can see a white 4 pins connector with UART written on the PCB:

[[=image cisco-isb6030-uart.jpeg]]

# Links


* <http://www.szetszedtem.hu/663stb/cisco6030.htm>  
* <http://mysettopbox.com/cisco-isb-6030-iptv-set-top-box.html>  
* <http://users.belgacom.net/rrd/>  
* <https://ciscodocs.technicolor.com/support/open_source/SPVTG-IPTV-LINUX-BROADCOM-MYRIO_rel4.reno.myrioi-19.saisb-bgc-SAIBP_7413_vm_1.1.5.2_secP.pdf>  
* <https://ciscodocs.technicolor.com/support/open_source/SPVTG-IPTV-LINUS-BRDCM-MYRIO_rel4.reno.myrioi-19.saisb-bgc-SAIBP_7413_vm_1.1.5.2_secP_OSD.pdf>  