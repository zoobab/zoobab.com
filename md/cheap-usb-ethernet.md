# About


I needed an USB-ethernet adaptor, bought this one, based on the Davicom DM9601. According to the [<http://cateee.net/lkddb/web-lkddb/USB_NET_DM9601.html>   linux kernel driver page], this is a USB1.1 device.

# Picture


[[=image davicom-usb-ethernet.jpg]]

# Lsusb



    zoobab@buzek /home/zoobab/ [27]$ lsusb
    Bus 006 Device 002: ID 0fe6:8101 Kontron (Industrial Computer Source / ICS Advent) DM9601 Fast Ethernet Adapter


# Dmesg



    [24365.704554] dm9601 6-1:1.0: eth1: unregister 'dm9601' usb-0000:00:1d.0-1, Davicom DM9601 USB Ethernet
    [24367.760273] usb 6-1: new full-speed USB device number 3 using uhci_hcd
    [24367.934388] usb 6-1: New USB device found, idVendor=0fe6, idProduct=8101
    [24367.934400] usb 6-1: New USB device strings: Mfr=0, Product=2, SerialNumber=3
    [24367.934408] usb 6-1: Product: USB Network Controller
    [24367.964668] dm9601 6-1:1.0: eth1: register 'dm9601' at usb-0000:00:1d.0-1, Davicom DM9601 USB Ethernet, 50:13:50:a4:fc:ff


# Speed tests


Network speed went at max at 900KB/sec:


    root@buzek /home/zoobab [10]# wget http://192.168.30.1:8000/1G -O /dev/null 
    --2012-12-24 18:10:58--  http://192.168.30.1:8000/1G
    Connecting to 192.168.30.1:8000... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 1048576000 (1000M) [application/octet-stream]
    Saving to: ‘/dev/null’
    
     7% [===========>                       ] 73,770,000   887KB/s  eta 17m 45s


By comparison, the [[[sitecom-lan-dock-cn-023 | Sitecom LAN dock CN023]]] USB ethernet (based on the Asix chip 0b95:1720 ASIX Electronics Corp. 10/100 Ethernet) reached much better speeds at 11MB/sec:


    root@buzek /home/zoobab [20]# wget http://192.168.30.1:8000/1G -O /dev/null 
    --2012-12-24 18:24:30--  http://192.168.30.1:8000/1G
    Connecting to 192.168.30.1:8000... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 1048576000 (1000M) [application/octet-stream]
    Saving to: ‘/dev/null’
    
     2% [===>                                            ] 25,912,912  11.2MB/s


# Links


* <http://www.raspberrypi.org/phpBB3/viewtopic.php?t=10482&p=123166>  
* http://cateee.net/lkddb/web-lkddb/USB_NET_DM9601.html
* <http://olimex.wordpress.com/2012/09/18/evaluating-low-cost-usb-to-ethernet-converters/>  
* <http://dx.com/p/usb-2-0-wired-10-100mbps-high-speed-ethernet-network-adapter-dongle-white-92233>  