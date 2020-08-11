# About 


I bought a bittorrent download box at [<http://www.dealextreme.com/p/standalone-bittorrent-bt-downloader-usb-printer-sharing-network-lan-server-57591>   DealExtreme for 25EUR].

# Specifications


* RAM: 32MB
* Flash: 4MB (ST M25P32)
* SOC: Cavium Networks CNS2132 (250Mhz)

# Serial port


There is a serial port on the board, pinout is the following:

[[=image ritmo-serial.jpg size="medium"]]

# Serial output



    $ screen /dev/ttyUSB0 38400
    
    U-Boot 1.1.4 (Mar  3 2008 - 16:51:36)
    
    U-Boot code: 00000000 -> 0001A410  BSS: -> 0001F354
    IRQ Stack: 00e6ff7c
    FIQ Stack: 00e6ef7c
    RAM Configuration:
    Bank #0: 00000000 32 MB
    Flash Manufacturer: ST
    Flash:  4 MB
    DataFlash: ST M25P32
    Page Count: 16384
    Page Size: 256
    Size: 4194304 bytes
    Logical Address: 0x30000000
    Area 0: 30000000 to 3002FFFF 
    Area 1: 30030000 to 3003FFFF 
    Area 2: 30040000 to 3023FFFF 
    Area 3: 30240000 to 303FFFFF 
    *** Warning - bad CRC, using default environment
    
    In:    serial
    Out:   serial
    Err:   serial
    PLL clock at 250MHz
    CPU clock at 250MHz
    AHB clock at 125MHz
    APB clock at 62MHz
    Hit any key to stop autoboot:  3 
    kernel:30060000-301e0000                                                                                                                                                                      0 
    Star Equuleus #


The device does not seem to do TFTP. I cannot get the input to work on the bootloader side.

I quickly setuped a DHCP server with dnsmasq, the device got an IP address, then an nmap shows:


    root@buzek /home/zoobab [6]# nmap 192.168.12.101
    
    Starting Nmap 5.21 ( http://nmap.org ) at 2011-07-12 20:20 CEST
    Nmap scan report for 192.168.12.101
    Host is up (0.0030s latency).
    Not shown: 995 closed ports
    PORT      STATE SERVICE
    21/tcp    open  ftp
    80/tcp    open  http
    139/tcp   open  netbios-ssn
    515/tcp   open  printer
    49152/tcp open  unknown
    MAC Address: 08:00:50:48:AD:97 (Daisy Systems)
    
    Nmap done: 1 IP address (1 host up) scanned in 0.45 seconds


The default login/password was admin/admin.

# Links


* http://www.dealextreme.com/p/standalone-bittorrent-bt-downloader-usb-printer-sharing-network-lan-server-57591
* <http://ritmotech.com.au/satotech/product_info.php?cPath=21_29&products_id=577>  
* <http://groups.google.com/group/dealextreme-nas-/browse_thread/thread/b0763c3fdc412e4d?pli=1>  
* <http://75.95.181.105:86/Comp/650BT/650BT.html>  
* <http://www.jostdayan.com.br/2010/11/nas-ns-k330-goodlockbuy/>  
* <http://code.google.com/p/snake-os/wiki/SnakeOS_compatible_hardwares>  
* <http://tinyhack.com/2008/09/20/update-debian-on-agestar-firmware/>  
* <http://c4software.another-team.com/lb2/>  
* <http://www.kiblerelectronics.com/corner/ccii_11.html>  
* <http://www.embeddedarm.com/about/resource.php?item=414>  
* <http://tinyhack.com/2010/07/06/cns21xx-port-completed/>  
* <http://www.flickr.com/photos/yohanes/sets/72157623208918338/>  
* <http://devdelver.wordpress.com/2010/04/06/nova-versao-do-firmware-do-welland-me-747ans-v01r10-e-0-75a-03/>  
* <ftp://ftp.embeddedarm.com/ts-arm-sbc/ts-7500-linux>  
* <http://forum.ixbt.com/print/0011/040552.html>  