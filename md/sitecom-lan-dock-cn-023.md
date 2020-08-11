[[=image sitecom-lan-dock-cn-023.jpg size="medium"]]

# About


It provides:

* 1 USB hub (3 ports)
* 1 USB ethernet port
* 1 Serial port
* 1 Parallel port
* 2 PS2 ports

It can be externally powered.

# Dmesg



    [31266.672199] usb 2-4.2: usbfs: USBDEVFS_CONTROL failed cmd mtp-probe rqt 128 rq 6 len 255 ret -110
    [31266.721431] udevd[14583]: renamed network interface eth1 to eth3
    [31266.745172] asix 2-4.2:1.0: eth3: link down
    [31266.748580] ADDRCONF(NETDEV_UP): eth3: link is not ready
    [31337.697350] usb 2-4: USB disconnect, device number 22
    [31337.697359] usb 2-4.1: USB disconnect, device number 23
    [31337.764481] usb 2-4.2: USB disconnect, device number 24
    [31337.764799] asix 2-4.2:1.0: eth3: unregister 'asix' usb-0000:00:1d.7-4.2, ASIX AX8817x USB 2.0 Ethernet
    [31337.780483] usb 2-4.5: USB disconnect, device number 25
    [31337.780616] usb 2-4.6: USB disconnect, device number 26
    [31337.780774] pl2303 ttyUSB0: pl2303 converter now disconnected from ttyUSB0
    [31337.780793] pl2303 2-4.6:1.0: device disconnected
    [31339.192105] usb 2-4: new high speed USB device number 27 using ehci_hcd
    [31339.326090] hub 2-4:1.0: USB hub found
    [31339.328058] hub 2-4:1.0: 7 ports detected
    [31339.600226] usb 2-4.1: new full speed USB device number 28 using ehci_hcd


# Lsusb



    Bus 002 Device 032: ID 182d:0023  
    Bus 002 Device 033: ID 0711:0240 Magic Control Technology Corp. PS/2 to USB Converter
    Bus 002 Device 034: ID 0b95:1720 ASIX Electronics Corp. 10/100 Ethernet
    Bus 002 Device 035: ID 067b:2305 Prolific Technology, Inc. PL2305 Parallel Port
    Bus 002 Device 036: ID 067b:2303 Prolific Technology, Inc. PL2303 Serial Port


# Ifconfig



    root@buzek /home/zoobab [117]# ifconfig eth3
    eth3      Link encap:Ethernet  HWaddr 00:80:00:00:80:24  
              UP BROADCAST MULTICAST  MTU:1500  Metric:1
              RX packets:0 errors:0 dropped:0 overruns:0 frame:0
              TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000 
              RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
