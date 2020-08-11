# About


The Zsun Wifi card reader is a USB card MicroSD reader with an integrated wifi chip running Linux.

# Lsusb



    root@sabayon /home/zoobab/lf/git [1]# lsusb
    Bus 002 Device 005: ID 05e3:0723 Genesys Logic, Inc. GL827L SD/MMC/MS Flash Card Reader


# Usage


It is exposed as an AP without any encryption ESSID "zsun-sd7F0087FE". I had problems to DHCP to it, but it finally gave my phone an IP in 10.168.168.100 with 10.168.168.1 as default gateway.

# Exploit?


I was looking on how to reflash this device with openwrt, there seems to be a serial port left on the board, but I don't know how to dissassemble the device cleanly. So maybe at the end, I will cut the nice plastic enclosure.

Another road is the web interface, which does not seem to resist to shell injection, just type `reboot` in the ESSID, and it will execute that command:

[[=image zsun-exploit-reboot-essid.png]]

When I press Confirm, the device actually reboots!

I was not able to pass more complex commands with spaces, but now there is a strange malformed telnet port open...

# Telnetd on port 11880


There is actually a telnet login prompt on port 11880, I cannot get in with the telnet client I have, so I use socat:


    zoobab@zoobab /Users/zoobab [9]$ socat - TCP4:10.168.168.1:11880
    ������!����
    (none) login: root
    root
    Password: zsun1188
    
    Welcome to
             -------      |            /    /--/        ___      |
              /           |           /|     \/        _____   --|--|
             /_____\      |---       --|--   //--/      /        /  |
              __|__       |           /|\    / \/      /___\    /   |
             ___|___   ___|____      / | \     /               /   \|
                            深圳至上移动科技有限公司
                            Shenzhen Zsun Cloud Technology Co., LTD.
                            www.zsuncloud.com
    
    
    BusyBox v1.01 (2014.12.27-02:50+0000) Built-in shell (ash)
    Enter 'help' for a list of built-in commands.
    
    ~ #


You can also use Putty, I tried it successfully.

# Dmesg


# Df


There is 16M flash and and 32M of RAM.

# Mount


To which directory does it mount its microSD card? It does mount the microsd card under /etc/XXX directory.

It is possible to reflash the device if you insert a VFAT formatted microsd card on the slot, and flash the content via some telnet commands.

There are some command line tool that use the built-in samba server, but it did not worked for me.

# Version



    ~ # cat /proc/version
    cat /proc/version
    Linux version 2.6.31--LSDK-9.2.0_U11.14 (root@jwyue) (gcc version 4.3.3 (GCC) ) #1 Wed Dec 17 15:53:04 CST 2014


# PCB pics


* <http://wp12362093.server-he.de/cloud/index.php/s/IutpWsMCpxNjOAs>  
* <http://wp12362093.server-he.de/cloud/index.php/s/xJzNPC7SSrQnrtk>  
* <http://wp12362093.server-he.de/cloud/index.php/s/fmiykeSpxuhQwC0>  
* <http://wp12362093.server-he.de/cloud/index.php/s/gANwpLbqwvaBczi>  

Those URLs are not working anymore, so I recopied the PCB pictures here:

[[gallery]]

# Links


* <http://www.cnx-software.com/2015/02/27/zsun-wifi-card-reader-adds-up-to-64gb-to-your-smartphone/>  
* <http://www.aliexpress.com/item/Wifi-card-reader-wirless-WLAN-2015-New-arrival-mobile-phone-extend-disk-for-iphone6-for-sumsang/32274710582.html>  
* <https://wiki.hackerspace.pl/projects>  :zsun-wifi-card-reader
* <https://github.com/zoobab/openwrt_zsun>  
* <http://phasenoise.livejournal.com/1500.html>  
* <https://zsunwifi.wordpress.com/u-boot/>  