# Lsusb



    Bus 002 Device 016: ID 0408:b009 Quanta Computer, Inc.


# Dmesg



    [85627.417647] scsi 17:0:0:0: Direct-Access     Medion   P9514            0000 PQ: 0 ANSI: 2
    [85627.479286] sd 17:0:0:0: Attached scsi generic sg2 type 0
    [85627.486517] sd 17:0:0:0: [sdb] Attached SCSI removable disk


# Mtpfs


You can mount the device in USB by using mtpfs (on ubuntu for ex):


    mtpfs /tmp/medion


# ADB shell


Even with USB develpoment activated, adb shell does not work, no way to detect the device

# Fastboot


Power it on, and press the Volume+ key, you will see a different ID in lsusb:


    Bus 002 Device 021: ID 18d1:b00a Google Inc.


You will obtain a menu "Android system recovery <3e>".

# Firmware update


By sniffing on the wifi, you will see that the device tries to do a firmware update by getting this file (300MB):

<http://cdce.ams002.internap.com/tapntap/medion/MD_LIFETAB_P9514.20111201.245-signed-ota-update-20111201040042.zip>  

# Dmesg



    zoobab@buzek /home/zoobab [1]$ ssh admin@192.168.42.167 -p 2222
    SSHDroid
    Use 'root' on rooted devices otherwise any username works
    Default password is 'admin'
    admin@192.168.42.167's password: 
    /data/data/berserker.android.apps.sshdroid/home $ dmesg
    [    0.000000] Initializing cgroup subsys cpu
    [    0.000000] Linux version 2.6.36.3-00097-g5b55949 (lcadmin@Bryony) (gcc version 4.4.3 (GCC) ) #1 SMP PREEMPT Mon Oct 24 13:33:26 CST 2011
    [    0.000000] CPU: ARMv7 Processor [411fc090] revision 0 (ARMv7), cr=10c53c7f
    [    0.000000] CPU: VIPT nonaliasing data cache, VIPT nonaliasing instruction cache
    [    0.000000] Machine: ventana
    [    0.000000] Tegra reserved memory:
    [    0.000000] LP0:                    1fbed000 - 1fbeefff
    [    0.000000] Bootloader framebuffer: 00000000 - ffffffff
    [    0.000000] Framebuffer:            2e800000 - 2effffff
    [    0.000000] 2nd Framebuffer:         2f000000 - 2fffffff
    [    0.000000] Carveout:               30000000 - 3fffffff
    [    0.000000] Memory policy: ECC disabled, Data cache writealloc
    [    0.000000] On node 0 totalpages: 190464
    [    0.000000] free_area_init_node: node 0, pgdat c05b8cc0, node_mem_map c067d000
    [    0.000000]   Normal zone: 1280 pages used for memmap
    [    0.000000]   Normal zone: 0 pages reserved
    [    0.000000]   Normal zone: 162560 pages, LIFO batch:31
    [    0.000000]   HighMem zone: 768 pages used for memmap
    [    0.000000]   HighMem zone: 25856 pages, LIFO batch:7
    [    0.000000] PERCPU: Embedded 7 pages/cpu @c0e86000 s5920 r8192 d14560 u65536
    [    0.000000] pcpu-alloc: s5920 r8192 d14560 u65536 alloc=16*4096
    [    0.000000] pcpu-alloc: [0] 0 [0] 1 
    [    0.000000] Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 188416
    [    0.000000] Kernel command line: nvmem=128M@384M mem=1024M@0M vmalloc=256M video=tegrafb console=none debug_uartport=lsport usbcore.old_scheme_first=1 lp0_vec=8192@0x1fbed000 tegraboot=sdmmc gpt 
    [    0.000000] PID hash table entries: 4096 (order: 2, 16384 bytes)
    [    0.000000] Dentry cache hash table entries: 131072 (order: 7, 524288 bytes)
    [    0.000000] Inode-cache hash table entries: 65536 (order: 6, 262144 bytes)
    [    0.000000] Memory: 744MB = 744MB total
    [    0.000000] Memory: 745972k/745972k available, 302604k reserved, 106496K highmem
    [    0.000000] Virtual kernel memory layout:
    [    0.000000]     vector  : 0xffff0000 - 0xffff1000   (   4 kB)
    [    0.000000]     fixmap  : 0xfff00000 - 0xfffe0000   ( 896 kB)
    [    0.000000]     DMA     : 0xff000000 - 0xffe00000   (  14 MB)
    [    0.000000]     vmalloc : 0xe8800000 - 0xf8000000   ( 248 MB)                                                                                                                    
    [    0.000000]     lowmem  : 0xc0000000 - 0xe8000000   ( 640 MB)                                                                                                                    
    [    0.000000]     pkmap   : 0xbfe00000 - 0xc0000000   (   2 MB)                                                                                                                    
    [    0.000000]     modules : 0xbf000000 - 0xbfe00000   (  14 MB)                                                                                                                    
    [    0.000000]       .init : 0xc0008000 - 0xc0032000   ( 168 kB)                                                                                                                    
    [    0.000000]       .text : 0xc0032000 - 0xc0547000   (5204 kB)                                                                                                                    
    [    0.000000]       .data : 0xc056e000 - 0xc05b9780   ( 302 kB)                                                                                                                    
    [    0.000000] Hierarchical RCU implementation.
    [    0.000000]  RCU dyntick-idle grace-period acceleration is enabled.
    [    0.000000]  RCU-based detection of stalled CPUs is disabled.
    [    0.000000]  Verbose stalled-CPUs detection is disabled.
    [    0.000000] NR_IRQS:448
    [    7.696028] Calibrating delay loop... 1998.84 BogoMIPS (lpj=9994240)
    [    7.965915] pid_max: default: 32768 minimum: 301
    [    7.966138] Mount-cache hash table entries: 512
    [    7.966545] Initializing cgroup subsys debug
    [    7.966560] Initializing cgroup subsys cpuacct
    [    7.966576] Initializing cgroup subsys freezer
    [    7.966612] CPU: Testing write buffer coherency: ok
    [    7.966786] Calibrating local timer... 249.87MHz, setting to 2.50MHz.
    [    8.056089] CPU1: Booted secondary processor
    [    8.326012] Brought up 2 CPUs
    [    8.326025] SMP: Total of 2 processors activated (3997.69 BogoMIPS).
    [    8.329670] regulator: core version 0.5
    [    8.329822] regulator: dummy: 
    [    8.330007] NET: Registered protocol family 16
    [    8.330646] host1x bus init
    [    8.330938] Tegra SKU: 8 Rev: A04 CPU Process: 1 Core Process: 2 Speedo ID: 1
    [    8.330952] Tegra Revision: (null) SKU: 8 CPU Process: 1 Core Process: 2
    [    8.331230] tegra2_init_sku_limits: Unknown sku clock avp.sclk
    [    8.331244] tegra2_init_sku_limits: Unknown sku clock bsea.sclk
    [    8.334501] Initializing Atmel touch driver
    [    8.455945] Initializing EETI touch driver
    [    8.456498] *** MPU START *** ventana_mpuirq_init...
    [    8.456507] *** MPU END *** ventana_mpuirq_init...
    [    8.456513] enter ventana_camera_init
    [    8.486056] ventana_emc_init: using ventana_siblings_emc_chips
    [    8.486073] tegra_init_emc: Memory not recognized, memory scaling disabled
    [    8.486082] tegra_init_emc: Memory vid     = 0x0606
    [    8.486089] tegra_init_emc: Memory rev_id1 = 0x0000
    [    8.486096] tegra_init_emc: Memory rev_id2 = 0x0000
    [    8.486102] tegra_init_emc: Memory pid     = 0x5454
    [    8.486277] tegra_arb_init: initialized
    [    8.486332] tegra_iovmm_register: added iovmm-gart
    [    8.491163] bio: create slab <bio-0> at 0
    [    8.491797] SCSI subsystem initialized
    [    8.491904] tegra-otg tegra-otg: otg transceiver registered
    [    8.492013] usbcore: registered new interface driver usbfs
    [    8.492080] usbcore: registered new interface driver hub
    [    8.492162] usbcore: registered new device driver usb
    [    8.497589] tps6586x 4-0034: VERSIONCRC is 2c
    [    8.501971] regulator: REG-SM_0: 725 <--> 1500 mV at 1275 mV normal standby
    [    8.503901] regulator: REG-SM_1: 725 <--> 1500 mV at 1000 mV normal standby
    [    8.507033] regulator: REG-SM_2: 3000 <--> 4550 mV at 3700 mV normal standby
    [    8.508511] regulator: REG-LDO_0: 1500 <--> 3300 mV at 1200 mV normal standby
    [    8.511216] regulator: REG-LDO_1: 725 <--> 1500 mV at 1100 mV normal standby
    [    8.512697] regulator: REG-LDO_2: 725 <--> 1500 mV at 1275 mV normal standby
    [    8.514954] regulator: REG-LDO_3: 1250 <--> 3300 mV at 3300 mV normal standby
    [    8.517656] regulator: REG-LDO_4: 1700 <--> 2475 mV at 1800 mV normal standby
    [    8.518708] regulator: REG-LDO_5: 1250 <--> 3300 mV at 2850 mV normal standby
    [    8.520196] regulator: REG-LDO_6: 1250 <--> 1800 mV at 2850 mV normal standby
    [    8.521695] regulator: REG-LDO_7: 1250 <--> 3300 mV at 3300 mV normal standby
    [    8.523187] regulator: REG-LDO_8: 1250 <--> 3300 mV at 1800 mV normal standby
    [    8.523796] regulator: REG-LDO_9: 1250 <--> 3300 mV at 2850 mV normal standby
    [    8.525146] Advanced Linux Sound Architecture Driver Version 1.0.23.
    [    8.525448] Bluetooth: Core ver 2.15
    [    8.525493] NET: Registered protocol family 31
    [    8.525499] Bluetooth: HCI device and connection manager initialized
    [    8.525510] Bluetooth: HCI socket layer initialized
    [    8.525605] Switching to clocksource timer_us
    [    8.526165] tegra-nvmap tegra-nvmap: created carveout iram (256KiB)
    [    8.656388] tegra-nvmap tegra-nvmap: created carveout generic-0 (262144KiB)
    [    8.657158] NET: Registered protocol family 2
    [    8.657261] IP route cache hash table entries: 32768 (order: 5, 131072 bytes)
    [    8.657603] TCP established hash table entries: 131072 (order: 8, 1048576 bytes)
    [    8.659122] TCP bind hash table entries: 65536 (order: 7, 786432 bytes)
    [    8.659953] TCP: Hash tables configured (established 131072 bind 65536)
    [    8.659962] TCP reno registered
    [    8.659972] UDP hash table entries: 512 (order: 2, 16384 bytes)
    [    8.660002] UDP-Lite hash table entries: 512 (order: 2, 16384 bytes)
    [    8.660157] NET: Registered protocol family 1
    [    8.660303] Unpacking initramfs...
    [    8.668572] Freeing initrd memory: 148K
    [    8.668638] PMU: registered new PMU device of type 0
    [    8.692418] highmem bounce pool size: 64 pages
    [    8.692558] ashmem: initialized
    [    8.693308] fuse init (API version 7.15)
    [    8.694097] io scheduler noop registered (default)
    [    8.786495] tegra_grhost tegra_grhost: initialized
    [    8.786540] host1x: tegradc tegradc
    [    9.295721] tegradc tegradc.0: probed
    [    9.296107] tegradc tegradc.0: probed
    [    9.296238] tegradc tegradc.0: registered overlay
    [    9.296250] host1x: tegradc tegradc
    [    9.296758] nvhdcp: using "always on" policy.
    [    9.296775] tegradc tegradc.1: probed
    [    9.297325] tegradc tegradc.1: probed
    [    9.297445] tegradc tegradc.1: registered overlay
    [    9.297785] Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
    [    9.298205] serial8250.0: ttyS0 at MMIO 0x70006300 (irq = 122) is a Tegra
    [    9.298374] tegra_uart.1: ttyHS1 at I/O 0x0 (irq = 69) is a unknown
    [    9.298452] Registered UART port ttyHS1
    [    9.298487] tegra_uart.2: ttyHS2 at I/O 0x0 (irq = 78) is a unknown
    [    9.298558] Registered UART port ttyHS2
    [    9.298602] Initialized tegra uart driver
    [    9.300310] loop: module loaded
    [    9.300504] i2c i2c-0: mpu3050: +kxtf9
    [    9.300513] i2c i2c-0: WARNING: Accel irq not assigned
    [    9.300521] i2c i2c-0: mpu3050: +ak8975
    [    9.300528] i2c i2c-0: WARNING: Compass irq not assigned
    [    9.300536] i2c i2c-0: mpu3050: No Pressure Present
    [    9.301005] mldl_cfg:Reset MPU3050
    [    9.335716] i2c i2c-0: Installing irq using 396
    [    9.335725] i2c i2c-0: Module Param interface = mpuirq
    [    9.335864] mpu_init
    [    9.338586] nct1008 4-004c: nct1008_probe: initialized
    [    9.339009] ================== 3G default enable ===============================================
    [    9.339778] PPP generic driver version 2.4.2
    [    9.339877] PPP Deflate Compression module registered
    [    9.339886] PPP BSD Compression module registered
    [    9.340385] PPP MPPE Compression module registered
    [    9.340396] NET: Registered protocol family 24
    [    9.340776] usbcore: registered new interface driver asix
    [    9.340813] usbcore: registered new interface driver cdc_ether
    [    9.340848] usbcore: registered new interface driver CDC NCM device
    [    9.340882] usbcore: registered new interface driver cdc_subset
    [    9.340904] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
    [    9.376810] tegra-ehci tegra-ehci.1: Tegra EHCI Host Controller
    [    9.376879] tegra-ehci tegra-ehci.1: new USB bus registered, assigned bus number 1
    [    9.405662] tegra-ehci tegra-ehci.1: irq 53, io mem 0xc5004000
    [    9.425656] tegra-ehci tegra-ehci.1: USB 2.0 started, EHCI 1.00
    [    9.425723] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002
    [    9.425735] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
    [    9.425744] usb usb1: Product: Tegra EHCI Host Controller
    [    9.425752] usb usb1: Manufacturer: Linux 2.6.36.3-00097-g5b55949 ehci_hcd
    [    9.425760] usb usb1: SerialNumber: tegra-ehci.1
    [    9.426047] hub 1-0:1.0: USB hub found
    [    9.426065] hub 1-0:1.0: 1 port detected
    [    9.426332] usbcore: registered new interface driver cdc_acm
    [    9.426340] cdc_acm: v0.26:USB Abstract Control Model driver for USB modems and ISDN adapters
    [    9.426388] usbcore: registered new interface driver cdc_wdm
    [    9.426395] Initializing USB Mass Storage driver...
    [    9.426473] usbcore: registered new interface driver usb-storage
    [    9.426480] USB Mass Storage support registered.
    [    9.426538] usbcore: registered new interface driver libusual
    [    9.426631] usbcore: registered new interface driver usbserial
    [    9.426639] usbserial: USB Serial Driver core
    [    9.426671] USB Serial support registered for GSM modem (1-port)
    [    9.426764] usbcore: registered new interface driver option
    [    9.426772] option: v0.7.2.2:USB Driver for GSM modems
    [    9.426803] USB Serial support registered for pl2303
    [    9.426854] usbcore: registered new interface driver pl2303
    [    9.426861] pl2303: Prolific PL2303 USB to serial adaptor driver
    [    9.426870] NVidia Tegra High-Speed USB SOC Device Controller driver (Apr 20, 2007)
    [    9.432502] tegra-otg tegra-otg: SUSPEND --> PERIPHERAL
    [    9.437625] android init
    [    9.437669] android_probe pdata: c058ef20
    [    9.437703] android_bind
    [    9.437709] android_bind_config
    [    9.437717] Gadget Android: controller 'fsl-tegra-udc' not recognized
    [    9.437825] android_usb gadget: android_usb ready
    [    9.437833] fsl-tegra-udc: bind to driver android_usb
    [    9.437868] f_adb init
    [    9.437874] android_register_function adb
    [    9.437880] f_mass_storage init
    [    9.437920] fsg_probe pdev: c058f698, pdata: c058ff04
    [    9.437957] android_register_function usb_mass_storage
    [    9.437964] f_mtp init
    [    9.437969] android_register_function mtp
    [    9.437974] f_rndis init
    [    9.438032] android_register_function rndis
    [    9.438039] f_accessory init
    [    9.438044] android_register_function accessory
    [    9.438055] rndis_function_bind_config MAC: 02:3B:3D:66:32:34
    [    9.438080] android_usb gadget: using random self ethernet address
    [    9.438096] android_usb gadget: using random host ethernet address
    [    9.438319] usb0: MAC 2e:1f:a2:48:29:85
    [    9.438326] usb0: HOST MAC c2:4c:c6:30:63:30
    [    9.438397] acc_bind_config
    [    9.438533] mtp_bind_config
    [    9.438739] adb_bind_config
    [    9.438994] android_usb gadget: Mass Storage Function, version: 2009/09/11
    [    9.439005] android_usb gadget: Number of LUNs=1
    [    9.439016]  lun0: LUN: removable file: (no medium)
    [    9.439383] input: gpio-keys as /devices/platform/gpio-keys.0/input/input0
    [    9.439535] maXTouch 0-005a: RRC:  i2c_check_functionality = 1
    [    9.439675] tegra-i2c tegra-i2c.0: I2c error status 0x00000008
    [    9.439685] tegra-i2c tegra-i2c.0: no acknowledge from address 0x5a
    [    9.439694] tegra-i2c tegra-i2c.0: Packet status 0x00010009
    [    9.440726] maXTouch 0-005a: Failure accessing maXTouch device
    [    9.440736] maXTouch 0-005a: Chip could not be identified
    [    9.440918] [egalax_i2c]:  Register egalax_i2c cdev, major: 250 
    [    9.440942] [egalax_i2c]:  /proc/egalax_dbg created
    [    9.440949] [egalax_i2c]:  Driver init done!
    [    9.440975] [egalax_i2c]:  Start probe
    [    9.441124] input: eGalax_Touch_Screen as /devices/virtual/input/input1
    [    9.441189] [egalax_i2c]:  Register input device done
    [    9.442389] [egalax_i2c]:  Request irq(366) gpio(174) with result:0
    [    9.442398] [egalax_i2c]:  Register early_suspend done
    [    9.442404] [egalax_i2c]:  I2C probe done
    [    9.442921] using rtc device, tps6586x-rtc, for alarms
    [    9.442942] tps6586x-rtc tps6586x-rtc.0: rtc core: registered tps6586x-rtc as rtc0
    [    9.444155] i2c /dev entries driver
    [    9.444654] lirc_dev: IR Remote Control driver registered, major 249 
    [    9.444664] IR LIRC bridge handler initialized
    [    9.444670] Linux video capture interface: v2.00
    [    9.444882] usbcore: registered new interface driver uvcvideo
    [    9.444890] USB Video Class driver (v0.1.0)
    [    9.444997] trpc_sema_init: registered misc dev 10:49
    [    9.445058] trpc_node_register: Adding 'local' to node list
    [    9.445271] trpc_node_register: Adding 'avp-remote' to node list
    [    9.445398] tegra_avp_probe: driver registered, kernel 30100000(e8a00000), msg area 27088000/27088110
    [    9.445535] tegra_camera: probe
    [    9.462802] yuv sensor_init
    [    9.462829] yuv sensor_probe
    [    9.462923] yuv sensor_init
    [    9.462954] yuv sensor_probe
    [    9.495153] bq27541-battery 2-0055: driver registered
    [    9.495372] device-mapper: uevent: version 1.0.3
    [    9.495555] device-mapper: ioctl: 4.18.0-ioctl (2010-06-29) initialised: dm-devel@redhat.com
    [    9.495594] Bluetooth: HCI UART driver ver 2.2
    [    9.495602] Bluetooth: HCI H4 protocol initialized
    [    9.495609] Bluetooth: HCILL protocol initialized
    [    9.495615] Bluetooth: BlueSleep Mode Driver Ver 1.1
    [    9.496007] cpuidle: using governor ladder
    [    9.496174] cpuidle: using governor menu
    [    9.496208] sdhci: Secure Digital Host Controller Interface driver
    [    9.496216] sdhci: Copyright(c) Pierre Ossman
    [    9.496286] mmc0: Invalid maximum block size, assuming 512 bytes
    [    9.501802] mmc0: SDHCI controller on tegra [sdhci-tegra.3] using ADMA
    [    9.501814] sdhci3: initialized irq 63 ioaddr fe600600
    [    9.501868] mmc1: Invalid maximum block size, assuming 512 bytes
    [    9.501889] mmc1: no vmmc regulator found
    [    9.501980] mmc1: SDHCI controller on tegra [sdhci-tegra.2] using ADMA
    [    9.502042] sdhci2: initialized irq 51 ioaddr fe600400
    [    9.502079] mmc2: Invalid maximum block size, assuming 512 bytes
    [    9.502098] mmc2: no vmmc regulator found
    [    9.502209] mmc2: SDHCI controller on tegra [sdhci-tegra.0] using ADMA
    [    9.502220] sdhci0: initialized irq 46 ioaddr fe600000
    [    9.502846] tegra-aes tegra-aes: registered
    [    9.503088] usbcore: registered new interface driver usbhid
    [    9.503096] usbhid: USB HID core driver
    [    9.503333] logger: created 64K log 'log_main'
    [    9.503400] logger: created 256K log 'log_events'
    [    9.503462] logger: created 64K log 'log_radio'
    [    9.503524] logger: created 64K log 'log_system'
    [    9.503589] isl29018 0-0044: Couldn't get regulator vdd_vcore_phtn
    [    9.506115] WM8903 0-001a: WM8903 revision 2
    [    9.594799] mmc0: new high speed MMC card at address 0001
    [    9.595004] mmcblk0: mmc0:0001 HYNIX  29.5 GiB 
    [    9.600930] Primary GPT is invalid, using alternate GPT.
    [    9.600962]  mmcblk0: p1 (体S) p2 (乌X) p3 (䙍G) p4 (偁P) p5 (䅃C) p6 (卍C) p7 (单P) p8 (䑕A)
    [    9.745704] usb 1-1: new full speed USB device using tegra-ehci and address 2
    [    9.782695] usb 1-1: not running at top speed; connect to a high speed hub
    [    9.791950] usb 1-1: New USB device found, idVendor=12d1, idProduct=1404
    [    9.791962] usb 1-1: New USB device strings: Mfr=3, Product=2, SerialNumber=0
    [    9.791971] usb 1-1: Product: HUAWEI MOBILE WCDMA EM770W
    [    9.791978] usb 1-1: Manufacturer: HUAWEI Technology
    [    9.827391] android_usb gadget: high speed config #1: android
    [    9.859040] fxz-option_probe: [(null)]
    [    9.859048] fxz-option_probe: !hw_udev
    [    9.859058] option 1-1:1.0: GSM modem (1-port) converter detected
    [    9.859289] usb 1-1: GSM modem (1-port) converter now attached to ttyUSB0
    [    9.859694] fxz-option_probe: [e7998800]
    [    9.859704] option 1-1:1.1: GSM modem (1-port) converter detected
    [    9.859859] usb 1-1: GSM modem (1-port) converter now attached to ttyUSB1
    [    9.860218] fxz-option_probe: [e7998800]
    [    9.860228] option 1-1:1.2: GSM modem (1-port) converter detected
    [    9.860395] usb 1-1: GSM modem (1-port) converter now attached to ttyUSB2
    [    9.860751] fxz-option_probe: [e7998800]
    [    9.860761] option 1-1:1.3: GSM modem (1-port) converter detected
    [    9.860918] usb 1-1: GSM modem (1-port) converter now attached to ttyUSB3
    [    9.861266] fxz-option_probe: [e7998800]
    [    9.861276] option 1-1:1.4: GSM modem (1-port) converter detected
    [    9.861438] usb 1-1: GSM modem (1-port) converter now attached to ttyUSB4
    [    9.861789] fxz-option_probe: [e7998800]
    [    9.861799] option 1-1:1.5: GSM modem (1-port) converter detected
    [    9.862016] usb 1-1: GSM modem (1-port) converter now attached to ttyUSB5
    [    9.862314] usb 1-1: USB disconnect, address 2
    [    9.862485] option: option_instat_callback: error -108
    [    9.862576] option1 ttyUSB0: GSM modem (1-port) converter now disconnected from ttyUSB0
    [    9.862618] option 1-1:1.0: device disconnected
    [    9.862810] option1 ttyUSB1: GSM modem (1-port) converter now disconnected from ttyUSB1
    [    9.862847] option 1-1:1.1: device disconnected
    [    9.863034] option1 ttyUSB2: GSM modem (1-port) converter now disconnected from ttyUSB2
    [    9.863071] option 1-1:1.2: device disconnected
    [    9.863257] option1 ttyUSB3: GSM modem (1-port) converter now disconnected from ttyUSB3
    [    9.863295] option 1-1:1.3: device disconnected
    [    9.863479] option1 ttyUSB4: GSM modem (1-port) converter now disconnected from ttyUSB4
    [    9.863517] option 1-1:1.4: device disconnected
    [    9.863718] option: option_instat_callback: error -108
    [    9.863803] option1 ttyUSB5: GSM modem (1-port) converter now disconnected from ttyUSB5
    [    9.863840] option 1-1:1.5: device disconnected
    [   10.056931] mmc1: new high speed SDHC card at address b368
    [   10.057152] mmcblk1: mmc1:b368 uSD   30.1 GiB 
    [   10.063024]  mmcblk1: p1
    [   10.145492] tegra_i2s_driver_probe
    [   10.145555] tegra_i2s_driver_probe
    [   10.145583] i2s_set_channel_bit_count: enabling non-symmetric mode
    [   10.145689] tegra_spdif_driver_probe
    [   10.146200] asoc: WM8903 <-> tegra-i2s-1 mapping ok
    [   10.146429] asoc: tegra_generic_voice_codec <-> tegra-i2s-2 mapping ok
    [   10.146667] asoc: tegra_generic_spdif_codec <-> tegra-spdif mapping ok
    [   10.565748] usb 1-1: new high speed USB device using tegra-ehci and address 3
    [   10.636075] usb 1-1: New USB device found, idVendor=12d1, idProduct=1404
    [   10.636087] usb 1-1: New USB device strings: Mfr=3, Product=2, SerialNumber=0
    [   10.636097] usb 1-1: Product: HUAWEI MOBILE WCDMA EM770W
    [   10.636106] usb 1-1: Manufacturer: HUAWEI Technology
    [   10.638622] fxz-option_probe: [(null)]
    [   10.638630] fxz-option_probe: !hw_udev
    [   10.638640] option 1-1:1.0: GSM modem (1-port) converter detected
    [   10.638849] usb 1-1: GSM modem (1-port) converter now attached to ttyUSB0
    [   10.645800] fxz-option_probe: [e70f0c00]
    [   10.645811] option 1-1:1.1: GSM modem (1-port) converter detected
    [   10.645973] usb 1-1: GSM modem (1-port) converter now attached to ttyUSB1
    [   10.646348] fxz-option_probe: [e70f0c00]
    [   10.646359] option 1-1:1.2: GSM modem (1-port) converter detected
    [   10.646525] usb 1-1: GSM modem (1-port) converter now attached to ttyUSB2
    [   10.646909] fxz-option_probe: [e70f0c00]
    [   10.646919] option 1-1:1.3: GSM modem (1-port) converter detected
    [   10.647085] usb 1-1: GSM modem (1-port) converter now attached to ttyUSB3
    [   10.647486] fxz-option_probe: [e70f0c00]
    [   10.647497] option 1-1:1.4: GSM modem (1-port) converter detected
    [   10.647672] usb 1-1: GSM modem (1-port) converter now attached to ttyUSB4
    [   10.648087] fxz-option_probe: [e70f0c00]
    [   10.648098] option 1-1:1.5: GSM modem (1-port) converter detected
    [   10.648335] usb 1-1: GSM modem (1-port) converter now attached to ttyUSB5
    [   11.346525] Audio:enable digital mic
    [   11.546135] input: tegra Wired Accessory Jack as /devices/platform/soc-audio/sound/card0/input2
    [   11.547123] ALSA device list:
    [   11.547133]   #0: tegra (WM8903)
    [   11.547210] GACT probability NOT on
    [   11.547223] Mirror/redirect action on
    [   11.547233] u32 classifier
    [   11.547239]     Actions configured
    [   11.547248] Netfilter messages via NETLINK v0.30.
    [   11.547303] nf_conntrack version 0.5.0 (11658 buckets, 46632 max)
    [   11.547608] ctnetlink v0.93: registering with nfnetlink.
    [   11.547732] xt_time: kernel timezone is -0000
    [   11.547923] ip_tables: (C) 2000-2006 Netfilter Core Team
    [   11.548017] arp_tables: (C) 2002 David S. Miller
    [   11.548063] TCP cubic registered
    [   11.548281] NET: Registered protocol family 10
    [   11.548779] lo: Disabled Privacy Extensions
    [   11.549150] Mobile IPv6
    [   11.549160] IPv6 over IPv4 tunneling driver
    [   11.549485] sit0: Disabled Privacy Extensions
    [   11.549833] ip6tnl0: Disabled Privacy Extensions
    [   11.549911] NET: Registered protocol family 17
    [   11.549944] NET: Registered protocol family 15
    [   11.550061] Bluetooth: L2CAP ver 2.15
    [   11.550069] Bluetooth: L2CAP socket layer initialized
    [   11.550085] Bluetooth: SCO (Voice Link) ver 0.6
    [   11.550092] Bluetooth: SCO socket layer initialized
    [   11.550169] Bluetooth: RFCOMM TTY layer initialized
    [   11.550191] Bluetooth: RFCOMM socket layer initialized
    [   11.550200] Bluetooth: RFCOMM ver 1.11
    [   11.550208] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
    [   11.550218] Bluetooth: HIDP (Human Interface Emulation) ver 1.2
    [   11.558580] Disabling clock audio left on by bootloader
    [   11.558592] Disabling clock stat_mon left on by bootloader
    [   11.558623] Disabling clock fuse_burn left on by bootloader
    [   11.558636] Disabling clock clk_d left on by bootloader
    [   11.558649] Disabling clock pll_c_out1 left on by bootloader
    [   11.558658] Disabling clock pll_c left on by bootloader
    [   11.558838] Tegra protected aperture disabled because nvmap is using system memory
    [   11.560527] VFP support v0.3: implementor 41 architecture 3 part 30 variant 9 rev 1
    [   11.563840] tps6586x-rtc tps6586x-rtc.0: setting system clock to 2011-12-18 20:13:41 UTC (1324239221)
    [   11.563856] QCI System Management Init.
    [   12.746089] option: option_instat_callback: error -2
    [   12.746317] option: option_instat_callback: error -2
    [   15.436024] Warning: unable to open an initial console.
    [   15.436133] Freeing init memory: 168K
    [   15.442247] init: /init.ventana.rc: 188: invalid command 'umount'
    [   15.608273] init: could not open /dev/keychord
    [   15.687780] EXT4-fs (mmcblk0p4): mounted filesystem with ordered data mode. Opts: (null)
    [   15.739774] EXT4-fs (mmcblk0p8): mounted filesystem with ordered data mode. Opts: (null)
    [   15.791133] EXT4-fs (mmcblk0p5): mounted filesystem with ordered data mode. Opts: (null)
    [   15.800313] EXT4-fs (mmcblk0p3): warning: maximal mount count reached, running e2fsck is recommended
    [   15.805834] EXT4-fs (mmcblk0p3): mounted filesystem with ordered data mode. Opts: (null)
    [   15.840089] EXT4-fs (mmcblk0p6): mounted filesystem with ordered data mode. Opts: (null)
    [   16.034782] init (1): /proc/1/oom_adj is deprecated, please use /proc/1/oom_score_adj instead.
    [   16.065863] init: cannot find '/system/etc/install-recovery.sh', disabling 'flash_recovery'
    [   16.067599] init: cannot find '/system/bin/osproxy.sh', disabling 'osproxy'
    [   16.190822] warning: `adbd' uses 32-bit capabilities (legacy support in use)
    [   16.190898] enabling adb
    [   16.209297] adb_open(adbd)
    [   16.346787] adb_release
    [   16.346839] adb_open(adbd)
    [   16.604950] android_usb gadget: high speed config #1: android
    [   17.849115] set mic unMute enable: 0
    [   17.850419] set mic unMute enable: 0
    [   17.852064] set mic unMute enable: 0
    [   17.853365] set mic unMute enable: 0
    [   18.897068] Audio:enable digital mic
    [   19.097246] avp_init: read firmware from 'nvrm_avp.bin' (33792 bytes)
    [   19.185721] avp_node_try_connect: can't connect to 'RPC_AVP_PORT'
    [   19.185783] avp_svc_thread: got remote peer
    [   19.186937] [AVP]: AVP kernel (Aug 11 2011 04:51:46)
    [   19.215683] avp_init: avp init done
    [   19.371112] avp_lib: Successfully loaded library nvmm_manager.axf (lib_id=1152f8)
    [   19.725933] option: option_instat_callback: error -2
    [   19.728291] option: option_instat_callback: error -2
    [   27.625881] avp_lib: Successfully unloaded 'nvmm_manager.axf'
    [   27.626283] avp_svc_thread: couldn't receive msg
    [   27.626294] avp_svc_thread: done
    [   27.626372] avp_uninit: avp teardown done
    [   34.381932] wifi_set_power = 1
    [   34.602424] wifi_set_carddetect = 1
    [   34.603268] 
    [   34.603271] Dongle Host Driver, version 4.218.248.23
    [   34.834050] init: cannot find '/system/bin/osproxy.sh', disabling 'osproxy'
    [   34.835809] request_suspend_state: wakeup (3->0) at 27130152458 (2011-12-18 20:14:04.767057546 UTC)
    [   34.849047] mmc2: new high speed SDIO card at address 0001
    [   34.854381] DHD: dongle ram size is set to 294912(orig 294912)
    [   34.989845] Firmware version = wl0: Feb 11 2011 17:01:05 version 4.218.248.23
    [   35.123244] wlan0: Broadcom Dongle Host Driver mac=74:2f:68:ba:d8:d8
    [   35.469558] wl_iw_set_cscan Ignoring CSCAN : First Scan is not done yet 1
    [   35.770215] STA connect received 1
    [   36.058215] wl_iw_set_country: set country for BE as BE rev -1 is OK
    [   39.143523] mtp_open
    [   46.075688] wlan0: no IPv6 routers present
    [  144.962387] init: untracked pid 1038 exited
    [  202.286164] init: no such service 'dhcpcd_:-h android_303d81e70d2958fd '
    [  202.367230] wifi_set_power = 0
    [  202.625359] wifi_set_carddetect = 0
    [  202.816012] mmc2: card 0001 removed
    [  203.702802] wifi_set_power = 1
    [  203.995191] wifi_set_carddetect = 1
    [  203.998741] 
    [  203.998745] Dongle Host Driver, version 4.218.248.23
    [  204.237855] mmc2: new high speed SDIO card at address 0001
    [  204.241116] DHD: dongle ram size is set to 294912(orig 294912)
    [  204.367551] Firmware version = wl0: Feb 11 2011 17:01:05 version 4.218.248.23
    [  204.491739] wlan0: Broadcom Dongle Host Driver mac=74:2f:68:ba:d8:d8
    [  204.918342] wl_iw_set_country: set country for BE as BE rev -1 is OK
    [  204.919866] wl_iw_set_cscan Ignoring CSCAN : First Scan is not done yet 1
    [  204.921467] wl_iw_set_cscan Ignoring CSCAN : First Scan is not done yet 2
    [  205.139980] STA connect received 1
    [  215.135663] wlan0: no IPv6 routers present
    [  395.048616] wl_iw_set_suspend: Suspend Flag 0 -> 1
    [  517.129264] wl_iw_set_suspend: Suspend Flag 1 -> 0
    [  517.132798] wl_iw_set_suspend: Suspend Flag 0 -> 1
    [  517.140728] wl_iw_set_suspend: Suspend Flag 1 -> 0
    [  564.669944] init: untracked pid 7880 exited
    [  582.869539] wl_iw_set_suspend: Suspend Flag 0 -> 1
    [ 1061.675903] option: option_instat_callback: error -2
    [ 1061.676537] option: option_instat_callback: error -2
    /data/data/berserker.android.apps.sshdroid/home $


# Links


* <http://www.handy-faq.de/forum/medion_lifetab_p9514/231010-medion_lifetab_p9514_tablet_stock_recovery_modus_starten-6.html>  