

# Status


* **17 july 2014**: OpenWRT is releasing Barrier Braker, including support for the RaspberryPi: <http://downloads.openwrt.org/barrier_breaker/14.07-rc1/brcm2708/generic/>  
* **18 apr 2014**: The daily trunk is now finally available on <<http://downloads.openwrt.org/snapshots/trunk/>  brcm2708/>   . You should mirror those files if you want to use them because they are build daily.
* **23 oct 2012**: The Attitude Adjustement Beta2 has been released with Raspberry Pi support (don't know if it includes 1Ghz patches or userspace drivers for the graphical blobs): <http://downloads.openwrt.org/attitude_adjustment/12.09-beta2/brcm2708/generic/>  
* **04 sep 2012**: Since the Attitude Adjustement beta release, images are packages are available here: <<http://downloads.openwrt.org/attitude_adjustment/12.09-beta/brcm2708/generic/>  >  
* **24 Jul 2012**: RaspberryPi support is now in the openwrt trunk, so you just have to select it, and compile it yourself. Nevertheless, it is still not available through nightly builds at http://downloads.openwrt.org/snapshots/trunk/ .

# Download


You can find the images are packages here: http://downloads.openwrt.org/attitude_adjustment/12.09-beta/brcm2708/generic/
You can find some binary images I compiled [here](http://filez.zoobab.com/openwrt/raspberrypi/trunk-r33212/brcm2708/).

# Image


You have to checkout openwrt trunk with the latest trunk revision:

[[=image raspberry-pi-openwrt.png]]

You can copy the image to your SD card with dd:


    $ dd if=openwrt-brcm2708-sdcard-vfat-ext4_128.img of=/dev/mmcblk0


Note that you should make a dd over the main block device mmcblk0, not to existing partitions like mmcblk0p1.

There are several versions of the image (_128, _192, _224), depending on the amount of RAM you want to give to the system, while the GPU will eat the rest. With less memory, the GPU cannot drive a 1080p screen.

# Serial port pinout


[[=image raspberry-pi-serial-port-bis.jpg size="medium"]]
[[=image raspberry-pi-serial-port.jpg size="medium"]]

The serial port is on the P1 connector:


    # O 
    O O 
    O O GND
    O O TX
    O O RX
    O O 
    O O 
    O O 
    O O 
    O O 
    O O 
    O O 
    O O


# Serial output


The serial output at 115200 is here, it seems it does not go further then the kernel messages:


    [    0.000000] Booting Linux on physical CPU 0
    [    0.000000] Linux version 3.3.8 (zoobab@ci) (gcc version 4.6.3 20120201 (prerelease) (Linaro GCC 4.6-2012.02) ) #5 Sun Jul 1 16:33:10 GMT 2012
    [    0.000000] CPU: ARMv6-compatible processor [410fb767] revision 7 (ARMv7), cr=00c5387d
    [    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT nonaliasing instruction cache
    [    0.000000] Machine: BCM2708
    [    0.000000] Memory policy: ECC disabled, Data cache writeback
    [    0.000000] Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 32512
    [    0.000000] Kernel command line: dma.dmachans=0x3c bcm2708_fb.fbwidth=656 bcm2708_fb.fbheight=416 bcm2708.boardrev=0x2 bcm2708.serial=0xe0e04667 smsc95xx.macaddr=B8:27:EB:E0:46:67 dwc_otg.lpm_enable=0 rpitestmode=1 console=ttyAMA0,115200 kgdboc=ttyAMA0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 rootwait
    [    0.000000] PID hash table entries: 512 (order: -1, 2048 bytes)
    [    0.000000] Dentry cache hash table entries: 16384 (order: 4, 65536 bytes)
    [    0.000000] Inode-cache hash table entries: 8192 (order: 3, 32768 bytes)
    [    0.000000] Memory: 128MB = 128MB total
    [    0.000000] Memory: 125776k/125776k available, 5296k reserved, 0K highmem
    [    0.000000] Virtual kernel memory layout:
    [    0.000000]     vector  : 0xffff0000 - 0xffff1000   (   4 kB)
    [    0.000000]     fixmap  : 0xfff00000 - 0xfffe0000   ( 896 kB)
    [    0.000000]     vmalloc : 0xc8800000 - 0xff000000   ( 872 MB)
    [    0.000000]     lowmem  : 0xc0000000 - 0xc8000000   ( 128 MB)
    [    0.000000]     modules : 0xbf000000 - 0xc0000000   (  16 MB)
    [    0.000000]       .text : 0xc0008000 - 0xc037bf18   (3536 kB)
    [    0.000000]       .init : 0xc037c000 - 0xc0399000   ( 116 kB)
    [    0.000000]       .data : 0xc039a000 - 0xc03b98a0   ( 127 kB)
    [    0.000000]        .bss : 0xc03b98c4 - 0xc04055c8   ( 304 kB)
    [    0.000000] NR_IRQS:85
    [    0.000000] timer_set_mode: unhandled mode:1
    [    0.000000] timer_set_mode: unhandled mode:3
    [    0.000000] Console: colour dummy device 80x30
    [    0.000000] console [tty1] enabled
    [    1.392390] Calibrating delay loop... 697.95 BogoMIPS (lpj=3489792)
    [    1.451935] pid_max: default: 32768 minimum: 301
    [    1.452194] Mount-cache hash table entries: 512
    [    1.452667] CPU: Testing write buffer coherency: ok
    [    1.452965] Setting up static identity map for 0x2db678 - 0x2db6d4
    [    1.453790] devtmpfs: initialized
    [    1.455137] NET: Registered protocol family 16
    [    1.456130] vc-mem: mm_vc_mem_phys_addr = 0x00000000
    [    1.456175] vc-mem: mm_vc_mem_size      = 0x10000000 (256 MiB)
    [    1.456523] mailbox: Broadcom VideoCore Mailbox driver
    [    1.456621] bcm2708_vcio: mailbox at f200b880
    [    1.456690] bcm_power: Broadcom power driver
    [    1.456721] bcm_power_open() -> 0
    [    1.456741] bcm_power_request(0, 8)
    [    1.957413] bcm_mailbox_read -> 00000080, 0
    [    1.957443] bcm_power_request -> 0
    [    1.957463] Serial: AMBA PL011 UART driver
    [    1.957599] dev:f1: ttyAMA0 at MMIO 0x20201000 (irq = 83) is a PL011 rev3
    [    2.222682] console [ttyAMA0] enabled
    [    2.243297] bio: create slab <bio-0> at 0
    [    2.248257] SCSI subsystem initialized
    [    2.252221] usbcore: registered new interface driver usbfs
    [    2.257873] usbcore: registered new interface driver hub
    [    2.263381] usbcore: registered new device driver usb
    [    2.268765] Advanced Linux Sound Architecture Driver Version 1.0.24.
    [    2.275680] Switching to clocksource stc
    [    2.279912] FS-Cache: Loaded
    [    2.283062] CacheFiles: Loaded
    [    2.297260] NET: Registered protocol family 2
    [    2.301960] IP route cache hash table entries: 1024 (order: 0, 4096 bytes)
    [    2.309271] TCP established hash table entries: 4096 (order: 3, 32768 bytes)
    [    2.316571] TCP bind hash table entries: 4096 (order: 2, 16384 bytes)
    [    2.323137] TCP: Hash tables configured (established 4096 bind 4096)
    [    2.329500] TCP reno registered
    [    2.332675] UDP hash table entries: 256 (order: 0, 4096 bytes)
    [    2.338544] UDP-Lite hash table entries: 256 (order: 0, 4096 bytes)
    [    2.345154] NET: Registered protocol family 1
    [    2.350004] RPC: Registered named UNIX socket transport module.
    [    2.355951] RPC: Registered udp transport module.
    [    2.360699] RPC: Registered tcp transport module.
    [    2.365411] RPC: Registered tcp NFSv4.1 backchannel transport module.
    [    2.372026] bcm2708_dma: DMA manager at f2007000
    [    2.376746] bcm2708_gpio: bcm2708_gpio_probe c039feb8
    [    2.381969] gpiochip_add: registered GPIOs 0 to 53 on device: bcm2708_gpio
    [    2.388896] vc-mem: Videocore memory driver
    [    2.394546] VFS: Disk quotas dquot_6.5.2
    [    2.398599] Dquot-cache hash table entries: 1024 (order 0, 4096 bytes)
    [    2.405973] FS-Cache: Netfs 'nfs' registered for caching
    [    2.412034] msgmni has been set to 245
    [    2.416868] io scheduler noop registered
    [    2.420879] io scheduler deadline registered
    [    2.425281] io scheduler cfq registered (default)
    [    2.430246] BCM2708FB: registering framebuffer (656x416@16)
    [    2.436300] bcm2708_fb_set_par info(c78d2c00) 656x416 (656x416), 0, 16
    [    2.454460] BCM2708FB: start = c8900000,49387000 width=656, height=416, bpp=16, pitch=1312 size=548864 success=0
    [    2.458335] Console: switching to colour frame buffer device 82x26
    [    2.492942] BCM2708FB: register framebuffer (0)
    [    2.508264] brd: module loaded
    [    2.517806] loop: module loaded
    [    2.524079] vcos: [1]: vchiq_init_state: slot_zero = 0xffd80000, is_master = 0
    [    2.534499] vcos: [1]: vchiq_init_state: called
    [    2.542062] vcos: [1]: vchiq: initialised - version 2 (min 2), device 253.0
    [    2.551999] usbcore: registered new interface driver smsc95xx
    [    2.560289] usbcore: registered new interface driver cdc_ncm
    [    2.568129] dwc_otg: version 2.90b 6-MAY-2010 (platform bus)
    [    2.576361] Core Release: 2.80a
    [    2.581736] Setting default values for core params
    [    2.588688] Finished setting default values for core params
    [    2.596658] f2980008 -> 1
    [    2.801178] Using Buffer DMA mode
    [    2.806636] Periodic Transfer Interrupt Enhancement - disabled
    [    2.814715] Multiprocessor Interrupt Enhancement - disabled
    [    2.822563] Dedicated Tx FIFOs mode
    [    2.828431] dwc_otg bcm2708_usb: DWC OTG Controller
    [    2.835634] dwc_otg bcm2708_usb: new USB bus registered, assigned bus number 1
    [    2.845134] dwc_otg bcm2708_usb: irq 75, io mem 0x00000000
    [    2.852804] Init: Port Power? op_state=1
    [    2.858745] Init: Power Port (0)
    [    2.864111] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002
    [    2.873097] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
    [    2.882453] usb usb1: Product: DWC OTG Controller
    [    2.889234] usb usb1: Manufacturer: Linux 3.3.8 dwc_otg_hcd
    [    2.896918] usb usb1: SerialNumber: bcm2708_usb
    [    2.904341] hub 1-0:1.0: USB hub found
    [    2.910287] hub 1-0:1.0: 1 port detected
    [    2.917141] usbcore: registered new interface driver uas
    [    2.924581] Initializing USB Mass Storage driver...
    [    2.931790] usbcore: registered new interface driver usb-storage
    [    2.939943] USB Mass Storage support registered.
    [    2.946834] usbcore: registered new interface driver libusual
    [    2.955188] mousedev: PS/2 mouse device common for all mice
    [    2.962937] cpuidle: using governor ladder
    [    2.969137] cpuidle: using governor menu
    [    2.975199] sdhci: Secure Digital Host Controller Interface driver
    [    2.983492] sdhci: Copyright(c) Pierre Ossman
    [    2.990072] bcm_power_open() -> 1
    [    2.996820] mmc0: SDHCI controller on BCM2708_Arasan [platform] using PIO
    [    3.005832] mmc0: BCM2708 SDHC host at 0x20300000 DMA 2 IRQ 77
    [    3.013939] sdhci-pltfm: SDHCI platform and OF driver helper
    [    3.022377] usbcore: registered new interface driver usbhid
    [    3.030163] usbhid: USB HID core driver
    [    3.036749] ALSA device list:
    [    3.041832]   No soundcards found.
    [    3.047547] TCP cubic registered
    [    3.052875] NET: Registered protocol family 17
    [    3.059434] Registering the dns_resolver key type
    [    3.066361] VFP support v0.3: implementor 41 architecture 1 part 20 variant b rev 5
    [    3.079175] ### snd_bcm2835_alsa_probe c03a05b8 ############### PROBING FOR bcm2835 ALSA device (0):(1) ###############
    [    3.094457] Creating card...
    [    3.099529] Creating device/chip ..
    [    3.105543] Adding controls ..
    [    3.110829] Registering card ....
    [    3.118006] bcm2835 ALSA CARD CREATED!
    [    3.124384] ### BCM2835 ALSA driver init OK ### 
    [    3.131596] Waiting for root device /dev/mmcblk0p2...
    [    3.259548] mmc0: problem reading SD Status register.
    [    3.273748] mmc0: new high speed SD card at address 0001
    [    3.281825] mmcblk0: mmc0:0001 00000 1.89 GiB 
    [    3.290530]  mmcblk0: p1 p2
    [    3.309767] usb 1-1: new high-speed USB device number 2 using dwc_otg
    [    3.383427] EXT4-fs (mmcblk0p2): warning: mounting unchecked fs, running e2fsck is recommended
    [    3.403309] EXT4-fs (mmcblk0p2): mounted filesystem without journal. Opts: (null)
    [    3.415431] VFS: Mounted root (ext4 filesystem) on device 179:2.
    [    3.424665] Freeing init memory: 116K
    [    3.510308] usb 1-1: New USB device found, idVendor=0424, idProduct=9512
    [    3.519474] usb 1-1: New USB device strings: Mfr=0, Product=0, SerialNumber=0
    [    3.530737] hub 1-1:1.0: USB hub found
    [    3.536928] hub 1-1:1.0: 3 ports detected
    [    3.820171] usb 1-1.1: new high-speed USB device number 3 using dwc_otg
    [    3.930167] usb 1-1.1: New USB device found, idVendor=0424, idProduct=ec00
    [    3.939494] usb 1-1.1: New USB device strings: Mfr=0, Product=0, SerialNumber=0
    [    3.972639] smsc95xx v1.0.4
    [    4.054589] smsc95xx 1-1.1:1.0: eth0: register 'smsc95xx' at usb-bcm2708_usb-1.1, smsc95xx USB 2.0 Ethernet, b8:27:eb:e0:46:67
    [    8.925274] EXT4-fs (mmcblk0p2): re-mounted. Opts: (null)
    [    9.192096] PPP generic driver version 2.4.2
    [    9.256462] ip_tables: (C) 2000-2006 Netfilter Core Team
    [    9.378054] NET: Registered protocol family 24
    [    9.409065] nf_conntrack version 0.5.0 (1967 buckets, 7868 max)


# Cpuinfo



    root@OpenWrt:~# cat /proc/cpuinfo 
    Processor       : ARMv6-compatible processor rev 7 (v6l)
    BogoMIPS        : 697.95
    Features        : swp half thumb fastmult vfp edsp java tls 
    CPU implementer : 0x41
    CPU architecture: 7
    CPU variant     : 0x0
    CPU part        : 0xb76
    CPU revision    : 7
    
    Hardware        : BCM2708
    Revision        : 0002
    Serial          : 00000000e0e04667


# Meminfo


There seems to be only 128MB of RAM on this version of the Rpi:


    root@OpenWrt:~# cat /proc/meminfo 
    MemTotal:         125892 kB
    MemFree:          117184 kB
    Buffers:             316 kB
    Cached:             2624 kB
    SwapCached:            0 kB
    Active:             2724 kB
    Inactive:           1388 kB
    Active(anon):       1196 kB
    Inactive(anon):       40 kB
    Active(file):       1528 kB
    Inactive(file):     1348 kB
    Unevictable:           0 kB
    Mlocked:               0 kB
    SwapTotal:             0 kB
    SwapFree:              0 kB
    Dirty:                 0 kB
    Writeback:             0 kB
    AnonPages:          1196 kB
    Mapped:             1124 kB
    Shmem:                64 kB
    Slab:               2716 kB
    SReclaimable:        776 kB
    SUnreclaim:         1940 kB
    KernelStack:         312 kB
    PageTables:          216 kB
    NFS_Unstable:          0 kB
    Bounce:                0 kB
    WritebackTmp:          0 kB
    CommitLimit:       62944 kB
    Committed_AS:       3948 kB
    VmallocTotal:     892928 kB
    VmallocUsed:         748 kB
    VmallocChunk:     675956 kB


There seems to be a way to change the amount of RAM allocated to the GPU as explained on the [elinux Rpi advanced setup](http://elinux.org/RPi_Advanced_Setup) page.

# Old problems


## The network is not up by default


The network is not up by default, because the default openwrt config requires a bridge.


    root@OpenWrt:/# cat /etc/config/network 
    # Copyright (C) 2006 OpenWrt.org
    
    config interface loopback
            option ifname   lo
            option proto    static
            option ipaddr   127.0.0.1
            option netmask  255.0.0.0
    
    config interface lan
            option ifname   eth0
            option type     bridge
            option proto    static
            option ipaddr   192.168.1.1
            option netmask  255.255.255.0


Just comment out the "option type bridge" to have static eth0 interface:


    # Copyright (C) 2006 OpenWrt.org
    
    config interface loopback
            option ifname   lo
            option proto    static
            option ipaddr   127.0.0.1
            option netmask  255.0.0.0
    
    config interface lan
            option ifname   eth0
    #       option type     bridge
            option proto    static
            option ipaddr   192.168.1.1
            option netmask  255.255.255.0


Then restart the network config to have the eth0 interface properly configured:


    root@OpenWrt:/# /etc/init.d/network restart
    root@OpenWrt:/# ifconfig
    eth0      Link encap:Ethernet  HWaddr B8:27:EB:E0:46:67  
              inet addr:192.168.1.1  Bcast:192.168.1.255  Mask:255.255.255.0
              UP BROADCAST MULTICAST  MTU:1500  Metric:1
              RX packets:0 errors:0 dropped:0 overruns:0 frame:0
              TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000 
              RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
    
    lo        Link encap:Local Loopback  
              inet addr:127.0.0.1  Mask:255.0.0.0
              UP LOOPBACK RUNNING  MTU:16436  Metric:1
              RX packets:1296 errors:0 dropped:0 overruns:0 frame:0
              TX packets:1296 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:0 
              RX bytes:88128 (86.0 KiB)  TX bytes:88128 (86.0 KiB)


## Some SD cards do not work


Some SD cards did not work with the Rpi:


    [   56.822624] mmc0: error -84 whilst initialising SD card
    [   58.067574] mmc0: problem reading SD Status register.
    [   58.089540] mmc0: error -110 whilst initialising SD card
    [   58.340109] mmc0: problem reading SD Status register.
    [   58.364246] mmc0: error -110 whilst initialising SD card
    [   58.624842] mmc0: problem reading SD Status register.
    [   58.653192] mmc0: error -110 whilst initialising SD card
    [   58.949438] mmc0: problem reading SD Status register.
    [   58.990427] mmc0: error -110 whilst initialising SD card
    [   60.237629] mmc0: problem reading SD Status register.
    [   60.259777] mmc0: error -110 whilst initialising SD card
    [   60.510049] mmc0: problem reading SD Status register.
    [   60.534193] mmc0: error -110 whilst initialising SD card
    [   60.794822] mmc0: problem reading SD Status register.


## Kernel panic when plugging a USB keyboard


When I plugged in a USB keyboard, the kernel made an instant kernel panic:


    [    4.319811] usb 1-1.3: new low-speed USB device number 4 using dwc_otg
    [    4.512279] Unable to handle kernel paging request at virtual address 00550308
    [    4.522196] pgd = c0004000
    [    4.527477] [00550308] *pgd=00000000
    [    4.533630] Internal error: Oops: 5 [#1]
    [    4.540034] Modules linked in:
    [    4.545497] CPU: 0    Not tainted  (3.3.8 #1)
    [    4.552192] pc : [<c0200af0>]    lr : [<c01fe1d0>]    psr: 20000193
    [    4.552203] sp : c7b0fb98  ip : c02009ec  fp : f298054c
    [    4.568275] r10: 00000000  r9 : c79fde58  r8 : c7a9df20
    [    4.575750] r7 : c7b0fbc0  r6 : c7b0fbc4  r5 : 00550308  r4 : c78e96e0
    [    4.584522] r3 : c7972f08  r2 : c7b0fbc0  r1 : c78e96e0  r0 : c79fde40
    [    4.593281] Flags: nzCv  IRQs off  FIQs on  Mode SVC_32  ISA ARM  Segment user
    [    4.602767] Control: 00c5387d  Table: 07b10008  DAC: 00000015
    [    4.610830] Process hotplug2 (pid: 62, stack limit = 0xc7b0e268)
    [    4.619169] Stack: (0xc7b0fb98 to 0xc7b10000)
    [    4.625838] fb80:                                                       c79fde58 00000000
    [    4.638510] fba0: f298002c c79091e0 c7a9df60 c79701a0 c79fde40 c01fe1d0 c79fde40 c79fde58
    [    4.651099] fbc0: c79701c8 c01ff400 00000001 c79fde40 c79701c8 00000000 c79fde50 00000008
    [    4.663754] fbe0: c79fde88 c01ff184 c79fde40 c7909240 c79fde88 c79701a0 f2980540 c7a9df20
    [    4.676564] fc00: 00000002 c020119c c79fde40 c79fde58 f2980540 f2980540 c79fde40 00000000
    [    4.689709] fc20: c7909240 c0201d2c c7a9df20 00000002 c79fde40 c0202e10 f298052c c02011ac
    [    4.703096] fc40: c7b0fc4c 00000042 c7a9df20 00000022 00000000 c79fde40 f2980520 00000002
    [    4.716669] fc60: c79fde40 00000004 00000000 0000004b c03dc69c c03a51a4 00000001 c0203100
    [    4.730516] fc80: 00000002 00000000 c79fde40 00000002 00000000 c02031f4 a0000193 00000000
    [    4.744495] fca0: 00000000 c0200e90 c0200e84 c01e2950 c790faa0 c0047e50 c79fde40 00000002
    [    4.758599] fcc0: 00000000 c03a51a4 0000004b 00000000 c7b0fd44 00000000 00100100 c7af2528
    [    4.772934] fce0: 00200200 c0047fbc c03a51a4 c0049da0 c03aadcc c00478a8 00000055 c000e8bc
    [    4.787346] fd00: c0069e60 a0000013 f200b200 c000d594 c7af24f0 c7af24f0 00001000 c7af2528
    [    4.801755] fd20: c7af2520 c7af2520 c7af24f0 c7af2520 00000000 00100100 c7af2528 00200200
    [    4.816159] fd40: c03dc848 c7b0fd58 c0061574 c0069e60 a0000013 ffffffff c0061548 c7af24f0
    [    4.830598] fd60: f200b200 c7af2498 c7af24f0 c7af24f0 00008000 c7b0fdbc 00000000 00001000
    [    4.845028] fd80: 418004fc c0061574 00000000 c7aea080 000000a2 00000000 c7af24f0 c7afdca0
    [    4.859476] fda0: 00000000 c7aea080 c7b0fddc c006765c c7b0fdfc 00000000 c03aadcc c7afdca0
    [    4.873915] fdc0: 00000001 00000000 c017b334 60000013 00000000 00000400 c7b39000 c7afdcd8
    [    4.888325] fde0: c7afdcd8 00000000 60000013 c7afdca0 00000000 c7afdcd4 00000000 0000004a
    [    4.902723] fe00: c7aeb900 c7afdca0 00000000 00000000 c7afdcd4 00000000 c7aeb900 c0018370
    [    4.917126] fe20: 00000000 c7ae7820 c7afdca0 c001ba3c c7aeb900 418004fc c7aea124 00000009
    [    4.931553] fe40: c7b0e000 c7ae7820 c7b0e000 c001d090 00000004 c7ae7820 c7b0e000 00000001
    [    4.945990] fe60: 00000009 c7b0e000 c7b0fee0 c7b0e000 00000000 00000009 c7b0e000 c7b0fee0
    [    4.960428] fe80: c7b0e000 00000000 c7aea080 c7aeb900 418004fc c001d35c 00000009 c00266cc
    [    4.974860] fea0: c7b0ffb0 c7b0ff60 c0016dc0 c7b0ffb0 c000db68 c7b0e000 fffffdfe b6f31ff4
    [    4.989280] fec0: c7b0e000 b6f31ff0 be943e8c c0010038 c0016dc0 c0049ce4 c03aadcc 0000004b
    [    5.003679] fee0: 00000009 00000000 00000000 00000000 00000000 c000d594 00000000 c7b0ff50
    [    5.018089] ff00: 00000000 00000000 fffffdfe c7b0ff78 c7b0e000 be943de8 00000001 c7b0e000
    [    5.032501] ff20: be943df0 be943e8c 00000018 c7b0ff40 000b6261 c0083bdc 60000013 ffffffff
    [    5.046926] ff40: 00000006 2c784ae8 00000006 000b6261 00000006 2c784ae8 be943de8 c7b0ff78
    [    5.061360] ff60: 00000000 00000000 00000005 c0084898 c7b0ff78 00010a20 00000009 2383916a
    [    5.075801] ff80: 00000007 00000001 00008e2c be943df0 0000008e 00000000 c7b0e000 00000000
    [    5.090229] ffa0: be943e8c c00109a0 be943de8 c000da18 00000005 be943df0 00000000 00000000
    [    5.104633] ffc0: be943de8 00008e2c be943df0 0000008e 00000000 00000000 00000000 be943e8c
    [    5.119029] ffe0: 00000000 be943da8 0000f5d0 b6f31ff0 60000010 00000005 00100000 00500010
    [    5.133448] Function entered at [<c0200af0>] from [<c01fe1d0>]
    [    5.142437] Function entered at [<c01fe1d0>] from [<c01ff184>]
    [    5.151305] Function entered at [<c01ff184>] from [<c020119c>]
    [    5.160065] Function entered at [<c020119c>] from [<c0201d2c>]
    [    5.168711] Function entered at [<c0201d2c>] from [<c0202e10>]
    [    5.177260] Function entered at [<c0202e10>] from [<c0203100>]
    [    5.185679] Function entered at [<c0203100>] from [<c02031f4>]
    [    5.193983] Function entered at [<c02031f4>] from [<c0200e90>]
    [    5.202174] Function entered at [<c0200e90>] from [<c01e2950>]
    [    5.210249] Function entered at [<c01e2950>] from [<c0047e50>]
    [    5.218214] Function entered at [<c0047e50>] from [<c0047fbc>]
    [    5.226067] Function entered at [<c0047fbc>] from [<c0049da0>]
    [    5.233801] Function entered at [<c0049da0>] from [<c00478a8>]
    [    5.241432] Function entered at [<c00478a8>] from [<c000e8bc>]
    [    5.248936] Function entered at [<c000e8bc>] from [<c000d594>]
    [    5.256335] Function entered at [<c000d594>] from [<c0069e60>]
    [    5.263602] Function entered at [<c0069e60>] from [<c0061574>]
    [    5.270745] Function entered at [<c0061574>] from [<c006765c>]
    [    5.277759] Function entered at [<c006765c>] from [<c0018370>]
    [    5.284647] Function entered at [<c0018370>] from [<c001ba3c>]
    [    5.291403] Function entered at [<c001ba3c>] from [<c001d090>]
    [    5.298055] Function entered at [<c001d090>] from [<c001d35c>]
    [    5.304698] Function entered at [<c001d35c>] from [<c00266cc>]
    [    5.311334] Function entered at [<c00266cc>] from [<c0010038>]
    [    5.317978] Function entered at [<c0010038>] from [<c00109a0>]
    [    5.324630] Function entered at [<c00109a0>] from [<c000da18>]
    [    5.331281] Code: e59f0040 eb001c52 e5875000 ea000001 (e5953000) 
    [    5.338368] ---[ end trace 8b94e18742b3435b ]---
    [    5.344029] Kernel panic - not syncing: Fatal exception in interrupt


This is probably due to the crappy power circuit, need to try that over a USB powered hub instead.

# Urjtag with gpio cable


You can export the GPIOs 22 23 24 25 of the Rpi with a simple echo


    root@OpenWrt:/sys/class/gpio# echo 22 > export 
    root@OpenWrt:/sys/class/gpio# echo 23 > export 
    root@OpenWrt:/sys/class/gpio# echo 24 > export 
    root@OpenWrt:/sys/class/gpio# echo 25 > export 
    root@OpenWrt:/sys/class/gpio# ls
    export     gpio22     gpio24     gpiochip0
    gpio0      gpio23     gpio25     unexport


They correspond respectively to the following pins on the P1 connector: 14 16 18 22.


||~ GPIO ||~ P1 pin ||
|| 22 || 14 ||
|| 23 || 16 ||
|| 24 || 18 ||
|| 25 || 22 ||