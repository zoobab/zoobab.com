# Picture


[[=image pl1217207-82mm_google_tv_box_android_4_0_cloud_stick_with_wifi_support_multi_languages.jpg size="medium"]]

# Lsusb



    Bus 002 Device 014: ID 18d1:deed Google Inc.


# Dmesg



    [21027.171095] usb 2-4: new high-speed USB device number 14 using ehci_hcd
    [21027.286080] usb 2-4: New USB device found, idVendor=18d1, idProduct=deed
    [21027.286092] usb 2-4: New USB device strings: Mfr=2, Product=3, SerialNumber=4
    [21027.286100] usb 2-4: Product: HDMI_DONGLE
    [21027.286107] usb 2-4: Manufacturer: telechips
    [21027.286114] usb 2-4: SerialNumber: F100120905105840128E
    [21027.295851] scsi12 : usb-storage 2-4:1.0
    [21028.305149] scsi 12:0:0:0: Direct-Access     Linux    File-CD Gadget   0000 PQ: 0 ANSI: 2
    [21028.315105] scsi 12:0:0:1: Direct-Access     Linux    File-CD Gadget   0000 PQ: 0 ANSI: 2
    [21028.383899] sd 12:0:0:0: Attached scsi generic sg1 type 0
    [21028.384813] sd 12:0:0:1: Attached scsi generic sg2 type 0
    [21028.409682] sd 12:0:0:0: [sdc] Attached SCSI removable disk
    [21028.410491] sd 12:0:0:1: [sdd] Attached SCSI removable disk


# Adb shell


Works fine.

# Cpuinfo



    shell@android:/ $ cat /proc/cpuinfo                                          
    Processor       : ARMv7 Processor rev 1 (v7l)
    BogoMIPS        : 531.66
    Features        : swp half thumb fastmult vfp edsp thumbee neon vfpv3 
    CPU implementer : 0x41
    CPU architecture: 7
    CPU variant     : 0x0
    CPU part        : 0xc05
    CPU revision    : 1
    
    Hardware        : tcc8920st
    Revision        : 2000
    Serial          : 0000000000000000


# Meminfo



    shell@android:/ # cat /proc/meminfo                                        
    MemTotal:         524288 kB
    MemFree:           89084 kB
    Buffers:             200 kB
    Cached:           114360 kB
    SwapCached:            0 kB
    Active:           115212 kB
    Inactive:         100380 kB
    Active(anon):     101056 kB
    Inactive(anon):      248 kB
    Active(file):      14156 kB
    Inactive(file):   100132 kB
    Unevictable:           0 kB
    Mlocked:               0 kB
    HighTotal:             0 kB
    HighFree:              0 kB
    LowTotal:         383024 kB
    LowFree:           89084 kB
    SwapTotal:             0 kB
    SwapFree:              0 kB
    Dirty:                 0 kB
    Writeback:             0 kB
    AnonPages:        101056 kB
    Mapped:            44100 kB
    Shmem:               272 kB
    Slab:               9340 kB
    SReclaimable:       2528 kB
    SUnreclaim:         6812 kB
    KernelStack:        3224 kB
    PageTables:         5236 kB
    NFS_Unstable:          0 kB
    Bounce:                0 kB
    WritebackTmp:          0 kB
    CommitLimit:      191512 kB
    Committed_AS:    4873708 kB
    VmallocTotal:     253952 kB
    VmallocUsed:       31296 kB
    VmallocChunk:     196612 kB


# Mount



    # mount
    rootfs / rootfs ro,relatime 0 0
    tmpfs /dev tmpfs rw,nosuid,relatime,mode=755 0 0
    devpts /dev/pts devpts rw,relatime,mode=600 0 0
    proc /proc proc rw,relatime 0 0
    sysfs /sys sysfs rw,relatime 0 0
    none /acct cgroup rw,relatime,cpuacct 0 0
    tmpfs /mnt/asec tmpfs rw,relatime,mode=755,gid=1000 0 0
    tmpfs /mnt/obb tmpfs rw,relatime,mode=755,gid=1000 0 0
    none /dev/cpuctl cgroup rw,relatime,cpu 0 0
    /dev/block/mtdblock2 /system yaffs2 ro,relatime 0 0
    /dev/block/mtdblock5 /data yaffs2 rw,nosuid,nodev,relatime 0 0
    /dev/block/mtdblock4 /cache yaffs2 rw,nosuid,nodev,relatime 0 0
    /sys/kernel/debug /sys/kernel/debug debugfs rw,relatime 0 0
    /dev/block/vold/240:1 /mnt/sdcard vfat rw,dirsync,nosuid,nodev,relatime,uid=1000,gid=1015,fmask=0702,dmask=0702,allow_utime=0020,codepage=cp437,iocharset=iso8859-1,shortname=mixed,utf8,errors=remount-ro 0 0
    /dev/block/vold/240:1 /mnt/secure/asec vfat rw,dirsync,nosuid,nodev,relatime,uid=1000,gid=1015,fmask=0702,dmask=0702,allow_utime=0020,codepage=cp437,iocharset=iso8859-1,shortname=mixed,utf8,errors=remount-ro 0 0
    tmpfs /mnt/sdcard/.android_secure tmpfs ro,relatime,size=0k,mode=000 0 0


# Rooted by default



    $ ./adb shell
    shell@android:/ $ busybox whoami                                               
    whoami: unknown uid 2000
    1|shell@android:/ $ su
    shell@android:/ # busybox whoami
    whoami: unknown uid 0
    1|shell@android:/ #


# Dmesg



    <6>[    0.000000] Initializing cgroup subsys cpu
    <5>[    0.000000] Linux version 3.0.8-tcc (root@robin) (gcc version 4.4.3 (GCC) ) #217 PREEMPT Thu Aug 9 14:04:08 CST 2012
    <4>[    0.000000] CPU: ARMv7 Processor [410fc051] revision 1 (ARMv7), cr=10c53c7f
    <4>[    0.000000] CPU: VIPT nonaliasing data cache, VIPT aliasing instruction cache
    <4>[    0.000000] Machine: tcc8920st
    <4>[    0.000000] kernel start display option [output:1] [resolution:5] [hdmi_r:5] [composite_r:0] [component_r:0] [hdmi_m:0]
    <7>[    0.000000] Total reserved memory: base=0x98200000, size=0x7e00000
    <4>[    0.000000] Memory policy: ECC disabled, Data cache writeback
    <6>[    0.000000] L310 cache controller enabled
    <6>[    0.000000] l2x0: 16 ways, CACHE_ID 0x410000c6, AUX_CTRL 0x70130001, Cache size: 262144 B
    <6>[    0.000000]     pll_0:  594000 kHz (Fixed)
    <6>[    0.000000]     pll_1:  500000 kHz (Fixed)
    <6>[    0.000000]     pll_2:  728000 kHz (Fixed)
    <6>[    0.000000]     pll_3:  672000 kHz (Fixed)
    <6>[    0.000000]     pll_4:  memory clcok source
    <6>[    0.000000]     pll_5:  cpu clcok source
    <6>[    0.000000] div_pll_0:  0 kHz (Fixed)
    <6>[    0.000000] div_pll_1:  0 kHz (Fixed)
    <6>[    0.000000] div_pll_2:  0 kHz (Fixed)
    <6>[    0.000000] div_pll_3:  0 kHz (Fixed)
    <6>[    0.000000] div_pll_4:  memory clcok source
    <6>[    0.000000] div_pll_5:  cpu clcok source
    <6>[    0.000000]       xin:  12000 kHz (Fixed)
    <7>[    0.000000] On node 0 totalpages: 98816
    <7>[    0.000000] free_area_init_node: node 0, pgdat c065e528, node_mem_map c07a9000
    <7>[    0.000000]   Normal zone: 1024 pages used for memmap
    <7>[    0.000000]   Normal zone: 0 pages reserved
    <7>[    0.000000]   Normal zone: 97792 pages, LIFO batch:31
    <7>[    0.000000] pcpu-alloc: s0 r0 d32768 u32768 alloc=1*32768
    <7>[    0.000000] pcpu-alloc: [0] 0 
    <4>[    0.000000] Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 97792
    <5>[    0.000000] Kernel command line: vmalloc=256M console=null androidboot.serialno=F100120905105840128E androidboot.wifimac=20:59:A0:07:F0:99 androidboot.btaddr=2059A007F099 androidboot.bootmode= androidboot.memtype=2
    <6>[    0.000000] PID hash table entries: 2048 (order: 1, 8192 bytes)
    <6>[    0.000000] Dentry cache hash table entries: 65536 (order: 6, 262144 bytes)
    <6>[    0.000000] Inode-cache hash table entries: 32768 (order: 5, 131072 bytes)
    <6>[    0.000000] Memory: 386MB = 386MB total
    <5>[    0.000000] Memory: 381492k/381492k available, 142796k reserved, 0K highmem
    <5>[    0.000000] Virtual kernel memory layout:
    <5>[    0.000000]     vector  : 0xffff0000 - 0xffff1000   (   4 kB)
    <5>[    0.000000]     fixmap  : 0xfff00000 - 0xfffe0000   ( 896 kB)
    <5>[    0.000000]     DMA     : 0xff600000 - 0xffe00000   (   8 MB)
    <5>[    0.000000]     vmalloc : 0xe0800000 - 0xf0000000   ( 248 MB)
    <5>[    0.000000]     lowmem  : 0xc0000000 - 0xe0000000   ( 512 MB)
    <5>[    0.000000]     pkmap   : 0xbfe00000 - 0xc0000000   (   2 MB)
    <5>[    0.000000]     modules : 0xbf000000 - 0xbfe00000   (  14 MB)
    <5>[    0.000000]       .init : 0xc0008000 - 0xc002e000   ( 152 kB)
    <5>[    0.000000]       .text : 0xc002e000 - 0xc061b934   (6071 kB)
    <5>[    0.000000]       .data : 0xc061c000 - 0xc065ef60   ( 268 kB)
    <5>[    0.000000]        .bss : 0xc065ef84 - 0xc07a89c8   (1319 kB)
    <6>[    0.000000] Preemptible hierarchical RCU implementation.
    <6>[    0.000000] NR_IRQS:161
    <7>[    0.000000] tcc_init_irq
    <6>[    0.000000] Console: colour dummy device 80x30
    <6>[    0.000204] Calibrating delay loop... 531.66 BogoMIPS (lpj=2658304)
    <6>[    0.060144] pid_max: default: 32768 minimum: 301
    <6>[    0.060391] Mount-cache hash table entries: 512
    <6>[    0.060845] Initializing cgroup subsys debug
    <6>[    0.060863] Initializing cgroup subsys cpuacct
    <6>[    0.060888] Initializing cgroup subsys freezer
    <6>[    0.060935] CPU: Testing write buffer coherency: ok
    <6>[    0.066051] print_constraints: dummy: 
    <6>[    0.066318] NET: Registered protocol family 16
    <6>[    0.068003] TCC8920ST GPIO initialized
    <6>[    0.071445] TCC clock driver initialized
    <4>[    0.072411] adc_init
    <4>[    0.072460] tcc_adc_probe
    <4>[    0.072506] attached TCC adc driver
    <6>[    0.072740] TCC rotation driver initializing
    <6>[    0.073269] TCC scaler driver initializing
    <6>[    0.073741] TCC scaler1 driver initializing
    <6>[    0.074230] TCC Scaler-2 Driver Initializing. 
    <6>[    0.074716] TCC WMIXER Driver Initializing. 
    <6>[    0.154692] bio: create slab <bio-0> at 0
    <4>[    0.155663] hdmi1280x720_init
    <4>[    0.156215] i2c-core: driver [rn5t614] using legacy suspend method
    <4>[    0.156232] i2c-core: driver [rn5t614] using legacy resume method
    <5>[    0.157511] SCSI subsystem initialized
    <6>[    0.158059] usbcore: registered new interface driver usbfs
    <6>[    0.158321] usbcore: registered new interface driver hub
    <6>[    0.158631] usbcore: registered new device driver usb
    <4>[    0.261285] ######## rn5t614_pmic_probe: 0 ########
    <6>[    0.261905] print_constraints: vdd_core range: 950 <--> 1500 mV at 1250 mV 
    <6>[    0.262271] print_constraints: vdd_hdmi_pll: 1200 mV 
    <6>[    0.262644] print_constraints: vdd_hdmi_osc: 3300 mV 
    <6>[    0.262902] rn5t614 0-0032: RN5T614 regulator driver loaded
    <6>[    0.593189] Advanced Linux Sound Architecture Driver Version 1.0.24.
    <6>[    0.594171] Bluetooth: Core ver 2.16
    <6>[    0.594450] NET: Registered protocol family 31
    <6>[    0.594466] Bluetooth: HCI device and connection manager initialized
    <6>[    0.594486] Bluetooth: HCI socket layer initialized
    <6>[    0.594500] Bluetooth: L2CAP socket layer initialized
    <6>[    0.594545] Bluetooth: SCO socket layer initialized
    <6>[    0.595417] cfg80211: Calling CRDA to update world regulatory domain
    <6>[    0.596228] Switching to clocksource oscr
    <6>[    0.600857] Switched to NOHz mode on CPU #0
    <6>[    0.618598] NET: Registered protocol family 2
    <6>[    0.618965] IP route cache hash table entries: 4096 (order: 2, 16384 bytes)
    <6>[    0.620232] TCP established hash table entries: 16384 (order: 5, 131072 bytes)
    <6>[    0.620608] TCP bind hash table entries: 16384 (order: 6, 327680 bytes)
    <6>[    0.621468] TCP: Hash tables configured (established 16384 bind 16384)
    <6>[    0.621486] TCP reno registered
    <6>[    0.621511] UDP hash table entries: 256 (order: 1, 12288 bytes)
    <6>[    0.621568] UDP-Lite hash table entries: 256 (order: 1, 12288 bytes)
    <6>[    0.622065] NET: Registered protocol family 1
    <6>[    0.622725] RPC: Registered named UNIX socket transport module.
    <6>[    0.622742] RPC: Registered udp transport module.
    <6>[    0.622754] RPC: Registered tcp transport module.
    <6>[    0.622766] RPC: Registered tcp NFSv4.1 backchannel transport module.
    <6>[    0.623061] Unpacking initramfs...
    <6>[    0.746584] Freeing initrd memory: 1380K
    <4>[    0.747322] supported LCD panel type 16
    <4>[    0.747626] hdmi1280x720_probe
    <4>[    0.747900] tcc8920_init_mmc
    <4>[    0.747914] tcc8920_init_mmc(1)
    <4>[    0.748199] tcc8920_init_tcc_dxb_ctrl (built Aug  9 2012 14:02:14)
    <4>[    0.748475] tcc8920_init_hdmi (built Aug  9 2012 14:02:15)
    <6>[    0.758567] ashmem: initialized
    <6>[    0.760636] fuse init (API version 7.16)
    <7>[    0.761112] yaffs: yaffs built Aug  9 2012 14:03:48 Installing.
    <6>[    0.761168] msgmni has been set to 747
    <6>[    0.762840] io scheduler noop registered (default)
    <6>[    0.762856] start plist test
    <6>[    0.767816] end plist test
    <6>[    0.767842] TCC Overlay driver initializing
    <6>[    0.768815] TCC Overlay driver initializing
    <6>[    0.770463]  tccfb_init (built Aug  9 2012 14:04:04)
    <6>[    0.770481]  tcc892X tca_fb_init (built Aug  9 2012 14:04:04)
    <4>[    0.770502] VIOC_OUTCFG_SetOutConfig : addr:f3100200, nType:4 nDisp:0 0x8100000a 
    <4>[    0.770521] VIOC_OUTCFG_SetOutConfig : addr:f3100200, nType:0 nDisp:1 0x8100000a 
    <4>[    0.771009]  tca_fb_init LCDC:0  pRDMABase:f3000400  pWMIXBase:f3001800 pDISPBase:f3000000 end 
    <4>[    0.771025]  tccfb_init  
    <6>[    0.771098] LCD panel is Telechips HDMI1280x720 1280 x 720
    <4>[    0.771113] tccfb_probe, screen_width=1280, screen_height=720
    <4>[    0.771336] map_video_memory (fbi=d7dfb288) used map memory,map dma:0x9f800000 size:00709000
    <6>[    0.780642] fb0: tccfb frame buffer device
    <6>[    0.781407] tcc_viqe_init
    <6>[    0.782030] tcc-uart.0: ttyTCC0 at MMIO 0xf7370000 (irq = 64) is a uart0
    <6>[    0.796405] tcc-uart.1: ttyTCC1 at MMIO 0xf7380000 (irq = 65) is a uart1
    <6>[    0.816963] TCCXX JPEG Encoder driver initializing
    <4>[    0.819354] tcc_intr: init (ver 2.0)
    <6>[    0.819460] HDMI Audio Driver ver. 1.1 (built Aug  9 2012 14:02:37)
    <6>[    0.820092] HDMI Driver ver. 1.2.1 (built Aug  9 2012 14:02:39)
    <4>[    0.820415] tcc_hdmi_power  tcc8920st  pwr:0 system_rev:0x2000 
    <4>[    0.820437] tcc_hdmi_power  tcc8920st  pwr:1 system_rev:0x2000 
    <4>[    0.820453] tcc_hdmi_power  tcc8920st  pwr:2 system_rev:0x2000 
    <6>[    0.820756] cec_probe
    <6>[    0.820780] CEC Driver ver. 1.0 (built Aug  9 2012 14:02:37)
    <6>[    0.821558] input: telechips remote controller as /devices/virtual/input/input0
    <6>[    0.821882] HPD Driver ver. 1.2 (built Aug  9 2012 14:02:40)
    <4>[    0.822419] tcc_output_starter_init
    <4>[    0.823244] tcc_output_starter_hdmi LCDC NUM:1 hdmi_mode=0
    <4>[    0.823271] VIOC_OUTCFG_SetOutConfig : addr:f3100200, nType:0 nDisp:1 0x8100000a 
    <4>[    0.847789] tcc_output_starter_memclr fb_paddr=0x9f800000 fb_laddr=0xe2000000
    <4>[    0.847809] tcc_output_starter_memclr attach_paddr=0xa0000000 attach_laddr=0x00000000
    <6>[    0.848005] hdmi_phy_reset phy is ready : 10us * 7
    <4>[    0.906338] VIOC_OUTCFG_SetOutConfig : addr:f3100200, nType:0 nDisp:1 0x8100000a 
    <6>[    0.908371] tcc_clockctrl_init
    <4>[    0.908390] <hk> drivers/char/cx_led.c(95) cx_led_init:  
    <4>[    0.908946] UMP<2>: Inserting UMP device driver. Compiled: Aug  9 2012, time: 14:02:50
    <4>[    0.909565] UMP<2>: Using OS memory backend, allocation limit: 67108864
    <4>[    0.909590] UMP<2>: Using dedicated memory backend
    <4>[    0.909603] UMP<2>: Requesting dedicated memory: 0x99200000, size: 25165824
    <4>[    0.909640] UMP: UMP device driver  loaded
    <4>[    0.911839] Mali: Mali device driver r2p4-02rel0 loaded
    <6>[    0.918284] loop: module loaded
    <6>[    0.920386] PPP generic driver version 2.4.2
    <6>[    0.920986] PPP Deflate Compression module registered
    <6>[    0.921005] PPP BSD Compression module registered
    <6>[    0.921785] PPP MPPE Compression module registered
    <6>[    0.921803] NET: Registered protocol family 24
    <6>[    0.923329] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
    <6>[    0.966302] tcc-ehci tcc-ehci: Telechips EHCI HS
    <6>[    0.966363] tcc-ehci tcc-ehci: new USB bus registered, assigned bus number 1
    <6>[    0.966504] tcc-ehci tcc-ehci: irq 49, io mem 0xf2200000
    <6>[    0.986309] tcc-ehci tcc-ehci: USB 0.0 started, EHCI 1.00
    <6>[    0.987454] hub 1-0:1.0: USB hub found
    <6>[    0.987490] hub 1-0:1.0: 1 port detected
    <6>[    0.987995] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
    <6>[    0.988100] tcc-ohci tcc-ohci.1: TCC OHCI
    <6>[    0.988143] tcc-ohci tcc-ohci.1: new USB bus registered, assigned bus number 2
    <6>[    0.988193] tcc-ohci tcc-ohci.1: irq 49, io mem 0xf2300000
    <6>[    1.051345] hub 2-0:1.0: USB hub found
    <6>[    1.051381] hub 2-0:1.0: 1 port detected
    <6>[    1.051852] Initializing USB Mass Storage driver...
    <6>[    1.052202] usbcore: registered new interface driver usb-storage
    <6>[    1.052217] USB Mass Storage support registered.
    <7>[    1.052228] Module dwc_common_port init
    <4>[    1.052355] wakelock init for otg
    <6>[    1.052373] dwc_otg: version 2.81a 04-FEB-2009 (DualRole)
    <6>[    1.052385] Working version No 007 - 10/24/2007
    <4>[    1.052591] Core Release: 2.81a
    <4>[    1.052607] Setting default values for core params
    <4>[    1.052650] dwc_otg: failed to get USB 3.3V regulator
    <4>[    1.052666] dwc_otg: failed to get USB 1.2V regulator
    <4>[    1.057973] Using Buffer DMA mode
    <4>[    1.057988] Periodic Transfer Interrupt Enhancement - disabled
    <4>[    1.058001] Multiprocessor Interrupt Enhancement - disabled
    <4>[    1.058020] Dedicated Tx FIFOs mode
    <6>[    1.058232] dwc_otg dwc_otg.0: DWC OTG Controller
    <6>[    1.058279] dwc_otg dwc_otg.0: new USB bus registered, assigned bus number 3
    <6>[    1.058324] dwc_otg dwc_otg.0: irq 48, io mem 0x00000000
    <6>[    1.059420] hub 3-0:1.0: USB hub found
    <6>[    1.059454] hub 3-0:1.0: 1 port detected
    <6>[    1.064496] android_usb gadget: Mass Storage Function, version: 2009/09/11
    <6>[    1.064516] android_usb gadget: Number of LUNs=2
    <6>[    1.064532]  lun0: LUN: removable file: (no medium)
    <6>[    1.064546]  lun1: LUN: removable file: (no medium)
    <6>[    1.065165] android_usb gadget: android_usb ready
    <6>[    1.065722] GPIO Input Driver: Start gpio inputs for tcc-gpiokey in polling mode
    <6>[    1.066232] input: tcc-gpiokey as /devices/virtual/input/input1
    <4>[    1.068316] TCC RTC, (c) 2012, Telechips 
    <4>[    1.068409] OLD INTCON[0x1701] iLoop [1000] RTCCON[0x3]=================================
    <4>[    1.068428] SET INTCON[0x8001] iLoop [1000] RTCCON[0x3]=================================
    <4>[    1.068448] RTC Invalied Time, Set 2012.01.26
    <4>[    1.068465] tcc_rtc: alarm irq 43
    <4>[    1.068503] read time 2012/01/26 02:30:01
    <4>[    1.068517] tcc_rtc_getalarm
    <4>[    1.068528]  alrm->enabled = 0, alm_en = 0
    <4>[    1.068545] read alarm 00 00/00/00 00:00:00
    <4>[    1.068565] read time 2012/01/26 02:30:01
    <6>[    1.069274] using rtc device, tcc-rtc, for alarms
    <6>[    1.069299] tcc-rtc tcc-rtc: rtc core: registered tcc-rtc as rtc0
    <6>[    1.069695] i2c /dev entries driver
    <6>[    1.071516] Linux video capture interface: v2.00
    <6>[    1.072044] usbcore: registered new interface driver uvcvideo
    <6>[    1.072059] USB Video Class driver (v1.1.0)
    <4>[    1.072071] tcc_battery_init
    <4>[    1.183039] USB RESET
    <4>[    1.266299] Set ID to device mode(0)
    <4>[    1.266337] usb connected.
    <4>[    1.289706] USB RESET
    <6>[    1.296408] android_work: sent uevent USB_STATE=CONNECTED
    <4>[    1.340778] TCC Battery Driver Load
    <6>[    1.341385] device-mapper: uevent: version 1.0.3
    <6>[    1.341882] device-mapper: ioctl: 4.20.0-ioctl (2011-02-02) initialised: dm-devel@redhat.com
    <6>[    1.341963] Bluetooth: HCI UART driver ver 2.2
    <6>[    1.341979] Bluetooth: HCI H4 protocol initialized
    <6>[    1.341991] Bluetooth: HCI BCSP protocol initialized
    <6>[    1.342003] Bluetooth: HCIATH3K protocol initialized
    <4>[    1.403590] USB RESET
    <4>[    1.446691] tcc-sdhc: SDHC0 init
    <6>[    1.449996] usbcore: registered new interface driver usbhid
    <6>[    1.450013] usbhid: USB HID core driver
    <6>[    1.450913] logger: created 256K log 'log_main'
    <6>[    1.451233] logger: created 256K log 'log_events'
    <6>[    1.451544] logger: created 256K log 'log_radio'
    <6>[    1.451849] logger: created 256K log 'log_system'
    <6>[    1.453233] usbcore: registered new interface driver snd-usb-audio
    <6>[    1.453558] usbcore: registered new interface driver snd-usb-caiaq
    <4>[    1.454914] tcc_iec958_probe()   ret: 0
    <3>[    1.456431] tcc-wm8524 tcc-wm8524: Failed to add route LHPOUT->Headset Jack
    <4>[    1.506724] USB RESET
    <6>[    1.566318] asoc: wm8524-hifi <-> tcc-dai-i2s mapping ok
    <6>[    1.618735] mmc0: new SDIO card at address 0001
    <4>[    1.621854] USB RESET
    <6>[    1.676320] asoc: IEC958 <-> tcc-dai-spdif mapping ok
    <6>[    1.677574] ALSA device list:
    <6>[    1.677590]   #0: Telechips Board
    <6>[    1.677709] Netfilter messages via NETLINK v0.30.
    <6>[    1.677805] nf_conntrack version 0.5.0 (5982 buckets, 23928 max)
    <6>[    1.679064] ctnetlink v0.93: registering with nfnetlink.
    <6>[    1.679157] NF_TPROXY: Transparent proxy support initialized, version 4.1.0
    <6>[    1.679172] NF_TPROXY: Copyright (c) 2006-2007 BalaBit IT Ltd.
    <6>[    1.679758] xt_time: kernel timezone is -0000
    <6>[    1.683166] ip_tables: (C) 2000-2006 Netfilter Core Team
    <6>[    1.683390] arp_tables: (C) 2002 David S. Miller
    <6>[    1.683478] TCP cubic registered
    <6>[    1.683803] NET: Registered protocol family 10
    <6>[    1.691440] Mobile IPv6
    <6>[    1.691516] ip6_tables: (C) 2000-2006 Netfilter Core Team
    <6>[    1.691832] IPv6 over IPv4 tunneling driver
    <6>[    1.701406] NET: Registered protocol family 17
    <6>[    1.701471] NET: Registered protocol family 15
    <6>[    1.701664] Bluetooth: RFCOMM TTY layer initialized
    <6>[    1.701696] Bluetooth: RFCOMM socket layer initialized
    <6>[    1.701710] Bluetooth: RFCOMM ver 1.11
    <6>[    1.701723] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
    <6>[    1.701738] Bluetooth: HIDP (Human Interface Emulation) ver 1.2
    <6>[    1.702098] VFP support v0.3: implementor 41 architecture 2 part 30 variant 5 rev 1
    <6>[    1.702130] ThumbEE CPU extension supported.
    <6>[    1.702465] TCC cpufreq driver initialized
    <4>[    1.702660] TCC_HIGHSPEED: change to 812MHz
    <4>[    1.709762] read time 2012/01/26 02:30:01
    <6>[    1.709804] tcc-rtc tcc-rtc: setting system clock to 2012-01-26 02:30:01 UTC (1327545001)
    <4>[    1.709979] Warning: unable to open an initial console.
    <6>[    1.710058] Freeing init memory: 152K
    <3>[    1.713375] init: could not import file init.tcc8920st.fs.rc
    <4>[    1.725758] tcc_nand: module license 'Proprietary' taints kernel.
    <4>[    1.725779] Disabling lock debugging due to kernel taint
    <4>[    1.736866] USB RESET
    <4>[    1.743482] 
    <4>[    1.743491] =============================================
    <4>[    1.743505] [NAND Physical Invalid Block Info]
    <4>[    1.743515] =============================================
    <4>[    1.743531] CS#0: (30/1024)Blocks - (120/4096)Blocks
    <4>[    1.743542] =============================================
    <4>[    1.743553] [NAND FTL Invalid Block Info]
    <4>[    1.743562] =============================================
    <4>[    1.743579] 
    <4>[    1.743583] CS#0: (30/1024)Blocks - (120/4096)Blocks
    <4>[    1.743596] [Total Physical Invalid Block Info]
    <4>[    1.743602] (120/4096)Blocks
    <4>[    1.743613] [Total FTL Invalid Block Info]
    <4>[    1.743619] (60/2048)Blocks
    <4>[    1.743628] =============================================
    <4>[    1.747141] [TNFTL NewMTD] [GoodBlockNum:1700] [BadBlockNum:2] [CurrBlock:1730]
    <4>[    1.796316] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[    1.898573] 
    <4>[    1.898580] [NAND        ] [PORT CONFIG - CS[0, 1] [NAND Data Port: GPIO_B Hw4 ~ Hw11]
    <4>[    1.898611] [NAND        ] [BClk 242MHZ][1Tick 42][RE-S:0,P:10,H:5][WR-S:0,P:6,H:5][COM-S:3,P:15,H:15]
    <4>[    1.898629] [NAND        ] [NB Area:4MB][DT Area:2120MB][HD Area0:0MB][MTD Size:1700MB]
    <4>[    1.898654] [NAND        ] [BadBlockNum: 5]
    <4>[    1.898664] [NAND        ] [Blk:2 8 52 93 1704 ]
    <4>[    1.903462] [Golden Info] [Devide :0] [Bad Block:  7]
    <4>[    1.903478] [Golden Info] [Nand Total Bad Block:  7]
    <4>[    1.903495] [MTD TCC] [PartName:      boot] [StBlk :  28] [ChipNo:0]
    <4>[    1.903512] [MTD TCC] [PartName:      boot] [EndBlk:  37] [ChipNo:0]
    <4>[    1.903527] [MTD TCC] [PartName:    kpanic] [StBlk :  38] [ChipNo:0]
    <4>[    1.903542] [MTD TCC] [PartName:    kpanic] [EndBlk:  42] [ChipNo:0]
    <4>[    1.903557] [MTD TCC] [PartName:    system] [StBlk :  43] [ChipNo:0]
    <4>[    1.903582] [MTD TCC] [PartName:    system] [BadBlk: 105] [ChipNo:0]
    <4>[    1.903610] [MTD TCC] [PartName:    system] [BadBlk: 186] [ChipNo:0]
    <4>[    1.903652] [MTD TCC] [PartName:    system] [EndBlk: 344] [ChipNo:0]
    <4>[    1.903666] [MTD TCC] [PartName:    splash] [StBlk : 345] [ChipNo:0]
    <4>[    1.903681] [MTD TCC] [PartName:    splash] [EndBlk: 348] [ChipNo:0]
    <4>[    1.903696] [MTD TCC] [PartName:     cache] [StBlk : 349] [ChipNo:0]
    <4>[    1.903736] [MTD TCC] [PartName:     cache] [EndBlk: 498] [ChipNo:0]
    <4>[    1.903750] [MTD TCC] [PartName:  userdata] [StBlk : 499] [ChipNo:0]
    <4>[    1.903974] [MTD TCC] [PartName:  userdata] [EndBlk:1717] [ChipNo:0]
    <4>[    1.903988] [MTD TCC] [PartName:  recovery] [StBlk :1718] [ChipNo:0]
    <4>[    1.904005] [MTD TCC] [PartName:  recovery] [EndBlk:1727] [ChipNo:0]
    <4>[    1.904019] [MTD TCC] [PartName:      misc] [StBlk :1728] [ChipNo:0]
    <4>[    1.904034] [MTD TCC] [PartName:      misc] [EndBlk:1728] [ChipNo:0]
    <4>[    1.904048] [MTD TCC] [PartName:       tcc] [StBlk :1729] [ChipNo:0]
    <4>[    1.904063] [MTD TCC] [PartName:       tcc] [EndBlk:1729] [ChipNo:0]
    <4>[    1.904078] [MTD TCC] [MTDTotalBlk:1700] [MTDBadBlk: 2] [MTDStBlk: 28] [MTDEdBlk:1730]
    <4>[    1.904094] [MTD TCC] NAND device: Manufacturer ID: 0xec, Chip ID: 0xd7
    <6>[    1.904111] tcc_nand: blocksize 1048576, pagesize 8192, oobsize 640
    <5>[    1.904130] Creating 9 MTD partitions on "tcc_mtd":
    <5>[    1.904151] 0x000000000000-0x000000a00000 : "boot"
    <5>[    1.909844] 0x000000a00000-0x000000f00000 : "kpanic"
    <5>[    1.913602] 0x000000f00000-0x000013b00000 : "system"
    <4>[    1.988131] USB RESET
    <5>[    2.029413] 0x000013b00000-0x000013f00000 : "splash"
    <5>[    2.032831] 0x000013f00000-0x00001d500000 : "cache"
    <4>[    2.095144] USB RESET
    <5>[    2.097533] 0x00001d500000-0x000069800000 : "userdata"
    <4>[    2.224241] USB RESET
    <4>[    2.330204] USB RESET
    <4>[    2.459210] USB RESET
    <4>[    2.593245] USB RESET
    <5>[    2.603898] 0x000069800000-0x00006a200000 : "recovery"
    <5>[    2.609224] 0x00006a200000-0x00006a300000 : "misc"
    <5>[    2.611282] 0x00006a300000-0x00006a400000 : "tcc"
    <6>[    2.616068] ndd_init: initializing NAND block device driver
    <6>[    2.694630]  ndda: ndda1
    <4>[    2.695512] [tcc_nand] init ndd(TCC8920, V7081)
    <5>[    2.714258] ufsd: Prepare to load NTFS File System - Telechips Inc..
    <4>[    2.714299] Authentication is complete!!
    <5>[    2.714318] ufsd: driver 8.5 (Apr 18 2012 16:52:37) LBD=ON with delayalloc with ioctl loaded at bf180000
    <5>[    2.714329] NTFS support included
    <5>[    2.714334] Built_for__tcc_android_ice_cream_2011-12-23
    <5>[    2.714341] 
    <4>[    2.714819] init (1): /proc/1/oom_adj is deprecated, please use /proc/1/oom_score_adj instead.
    <6>[    2.977878] yaffs: dev is 32505858 name is "mtdblock2" rw
    <6>[    2.977893] yaffs: passed flags ""
    <7>[    2.977908] yaffs: Attempting MTD mount of 31.2,"mtdblock2"
    <4>[    2.996424] TCC_HIGHSPEED: change to 716MHz
    <4>[    3.096414] TCC_HIGHSPEED: change to 812MHz
    <7>[    3.185216] yaffs: yaffs_read_super: is_checkpointed 1
    <6>[    3.185695] yaffs: dev is 32505861 name is "mtdblock5" rw
    <6>[    3.185710] yaffs: passed flags ""
    <7>[    3.185725] yaffs: Attempting MTD mount of 31.5,"mtdblock5"
    <4>[   11.896622] TCC_HIGHSPEED: ######### Change to limit highspeed status
    <4>[   11.896671] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[   11.896687] TCC_HIGHSPEED: change to 716MHz
    <7>[   15.318360] yaffs: yaffs_read_super: is_checkpointed 0
    <6>[   15.318648] yaffs: dev is 32505860 name is "mtdblock4" rw
    <6>[   15.318665] yaffs: passed flags ""
    <7>[   15.318682] yaffs: Attempting MTD mount of 31.4,"mtdblock4"
    <7>[   15.875935] yaffs: yaffs_read_super: is_checkpointed 0
    <3>[   16.486912] init: cannot find '/system/etc/install-recovery.sh', disabling 'flash_recovery'
    <6>[   16.977028] input: qwerty as /devices/virtual/input/input2
    <6>[   17.297416] VPU manager driver initializing
    <3>[   17.821898] init: service 'console' requires console
    <3>[   17.822128] android_usb: already disabled
    <6>[   17.826276] warning: `adbd' uses 32-bit capabilities (legacy support in use)
    <6>[   17.837081] adb_open
    <6>[   17.837122] adb_bind_config
    <4>[   17.837227] DWC_OTG Force Init!!(0)
    <4>[   17.837257] Setting default values for core params
    <4>[   17.837303] Using Buffer DMA mode
    <4>[   17.837318] Periodic Transfer Interrupt Enhancement - disabled
    <4>[   17.837332] Multiprocessor Interrupt Enhancement - disabled
    <4>[   17.961155] USB RESET
    <4>[   18.066862] USB RESET
    <6>[   18.178528] android_usb gadget: high speed config #1: android
    <6>[   18.217344] android_work: sent uevent USB_STATE=CONFIGURED
    <4>[   19.432191] TCC_OUTPUT_SetOutputResizeMode : mode_x = 3, mode_y = 3
    <4>[   19.441699] tcc_hdmi_power  tcc8920st  pwr:1 system_rev:0x2000 
    <6>[   19.442192] hdmi_phy_reset phy is ready : 10us * 7
    <4>[   19.442221] VIOC_OUTCFG_SetOutConfig : addr:f3100200, nType:0 nDisp:1 0x8100000a 
    <4>[   19.609125] UMP<2>: New session opened
    <4>[   20.742301] UMP<2>: New session opened
    <4>[   21.190609] [set_dma_outbuffer], original len[8192]
    <4>[   36.797431] TCC_HIGHSPEED: ######### Change to normal status
    <4>[   36.797503] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[   36.877499] TCC_HIGHSPEED: change to 812MHz
    <4>[   36.897418] TCC_HIGHSPEED: ######### Change to highspeed status
    <6>[   38.041931] request_suspend_state: wakeup (3->0) at 38034494573 (2012-01-26 02:30:37.828406569 UTC)
    <6>[   38.596818] acc_open
    <6>[   38.596862] acc_release
    <4>[   42.825300] UMP<2>: New session opened
    <4>[   43.155077] UMP<2>: New session opened
    <4>[   46.450185] rtl8189es driver version=v4.1.2_4787.20120801
    <4>[   46.450206] build time: Aug  6 2012 11:53:10
    <4>[   46.450219] ##########rtw_suspend_lock_init ###########
    <4>[   46.467780] register rtw_netdev_ops to netdev_ops
    <4>[   46.467815] rtw_wdev_alloc(padapter=e172f000)
    <4>[   46.484553] Chip Version Info: CHIP_8188E_Normal_Chip_TSMC_A_CUT_1T1R_RomVer(0)
    <4>[   46.484582] RF_Type is 3!!
    <4>[   46.484659] EEPROM type is E-FUSE
    <4>[   46.484669] =>_CardEnable
    <4>[   46.490760] SetHwReg8188ES: bMacPwrCtrlOn=1
    <4>[   46.490773] <=_CardEnable
    <4>[   46.490825] _ReadPROMContent: 9346CR=0x20, Boot from EFUSE, Autoload OK
    <4>[   46.897798] TCC_HIGHSPEED: ######### Change to limit highspeed status
    <4>[   46.897965] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[   46.897989] TCC_HIGHSPEED: change to 716MHz
    <4>[   46.968864] EEPROM ID=0x8129
    <4>[   46.968889] Hal_EfuseParseMACAddr_8188ES: Permanent Address = c6-0d-72-00-04-a5
    <4>[   46.968912] Hal_ReadPowerSavingMode88E...bHWPwrPindetect(0)-bHWPowerdown(0) ,bSupportRemoteWakeup(0)
    <4>[   46.968932] ### PS params=>  power_mgnt(1),usbss_enable(0) ###
    <4>[   46.968954] ======= Path 0, Channel 0 =======
    <4>[   46.968968] Index24G_CCK_Base[0][0] = 0x2d
    <4>[   46.968981] Index24G_BW40_Base[0][0] = 0x2d
    <4>[   46.968994] ======= Path 0, Channel 1 =======
    <4>[   46.969007] Index24G_CCK_Base[0][1] = 0x2d
    <4>[   46.969021] Index24G_BW40_Base[0][1] = 0x2d
    <4>[   46.969033] ======= Path 0, Channel 2 =======
    <4>[   46.969047] Index24G_CCK_Base[0][2] = 0x2d
    <4>[   46.969060] Index24G_BW40_Base[0][2] = 0x2d
    <4>[   46.969073] ======= Path 0, Channel 3 =======
    <4>[   46.969087] Index24G_CCK_Base[0][3] = 0x2d
    <4>[   46.969100] Index24G_BW40_Base[0][3] = 0x2d
    <4>[   46.969113] ======= Path 0, Channel 4 =======
    <4>[   46.969126] Index24G_CCK_Base[0][4] = 0x2d
    <4>[   46.969140] Index24G_BW40_Base[0][4] = 0x2d
    <4>[   46.969152] ======= Path 0, Channel 5 =======
    <4>[   46.969166] Index24G_CCK_Base[0][5] = 0x2d
    <4>[   46.969179] Index24G_BW40_Base[0][5] = 0x2d
    <4>[   46.969192] ======= Path 0, Channel 6 =======
    <4>[   46.969206] Index24G_CCK_Base[0][6] = 0x2d
    <4>[   46.969219] Index24G_BW40_Base[0][6] = 0x2d
    <4>[   46.969232] ======= Path 0, Channel 7 =======
    <4>[   46.969245] Index24G_CCK_Base[0][7] = 0x2d
    <4>[   46.969259] Index24G_BW40_Base[0][7] = 0x2d
    <4>[   46.969271] ======= Path 0, Channel 8 =======
    <4>[   46.969285] Index24G_CCK_Base[0][8] = 0x2d
    <4>[   46.969298] Index24G_BW40_Base[0][8] = 0x2d
    <4>[   46.969311] ======= Path 0, Channel 9 =======
    <4>[   46.969325] Index24G_CCK_Base[0][9] = 0x2d
    <4>[   46.969338] Index24G_BW40_Base[0][9] = 0x2d
    <4>[   46.969351] ======= Path 0, Channel 10 =======
    <4>[   46.969364] Index24G_CCK_Base[0][10] = 0x2d
    <4>[   46.969378] Index24G_BW40_Base[0][10] = 0x2d
    <4>[   46.969391] ======= Path 0, Channel 11 =======
    <4>[   46.969404] Index24G_CCK_Base[0][11] = 0x2d
    <4>[   46.969418] Index24G_BW40_Base[0][11] = 0x2d
    <4>[   46.969431] ======= Path 0, Channel 12 =======
    <4>[   46.969444] Index24G_CCK_Base[0][12] = 0x2d
    <4>[   46.969458] Index24G_BW40_Base[0][12] = 0x2d
    <4>[   46.969470] ======= Path 0, Channel 13 =======
    <4>[   46.969484] Index24G_CCK_Base[0][13] = 0x2d
    <4>[   46.969497] Index24G_BW40_Base[0][13] = 0x2d
    <4>[   46.969510] ======= Path 0, Channel 14 =======
    <4>[   46.969524] Index24G_CCK_Base[0][14] = 0x2d
    <4>[   46.969537] Index24G_BW40_Base[0][14] = 0x2d
    <4>[   46.969549] ======= TxCount 0 =======
    <4>[   46.969561] CCK_24G_Diff[0][0]= 0
    <4>[   46.969573] OFDM_24G_Diff[0][0]= 4
    <4>[   46.969585] BW20_24G_Diff[0][0]= 2
    <4>[   46.969596] BW40_24G_Diff[0][0]= 0
    <4>[   46.969607] ======= TxCount 1 =======
    <4>[   46.969619] CCK_24G_Diff[0][1]= -2
    <4>[   46.969631] OFDM_24G_Diff[0][1]= -2
    <4>[   46.969643] BW20_24G_Diff[0][1]= -2
    <4>[   46.969655] BW40_24G_Diff[0][1]= -2
    <4>[   46.969666] ======= TxCount 2 =======
    <4>[   46.969678] CCK_24G_Diff[0][2]= -2
    <4>[   46.969690] OFDM_24G_Diff[0][2]= -2
    <4>[   46.969702] BW20_24G_Diff[0][2]= -2
    <4>[   46.969714] BW40_24G_Diff[0][2]= -2
    <4>[   46.969725] ======= TxCount 3 =======
    <4>[   46.969737] CCK_24G_Diff[0][3]= -2
    <4>[   46.969749] OFDM_24G_Diff[0][3]= -2
    <4>[   46.969761] BW20_24G_Diff[0][3]= -2
    <4>[   46.969773] BW40_24G_Diff[0][3]= -2
    <4>[   46.969784] EEPROMRegulatory = 0x0
    <4>[   46.969796] mlmepriv.ChannelPlan = 0x20
    <4>[   46.969808] CrystalCap: 0x20
    <4>[   46.969819] EEPROM Customer ID: 0x 0
    <4>[   46.969829] Board Type: 0x 0
    <4>[   46.969840] ThermalMeter = 0x1a
    <4>[   46.969854] <==== ReadAdapterInfo8188ES in 480 ms
    <4>[   46.971314] rtw_register_early_suspend
    <4>[   46.971407] rtw_macaddr_cfg MAC Address  = c6:0d:72:00:04:a5
    <4>[   46.971426] bDriverStopped:0, bSurpriseRemoved:0, bup:0, hw_init_completed:0
    <4>[   46.987863] start rtl8188es_xmit_thread
    <4>[   47.106397] rtw_android_priv_cmd: Android private cmd "BLOCK 1" on wlan0
    <4>[   48.395830] cfg80211_rtw_change_iface call netdev_open
    <4>[   48.395859] +871x_drv - drv_open, bup=0
    <4>[   48.395873] +rtl8188es_hal_init
    <4>[   48.395884] =>_InitPowerOn
    <4>[   48.395895] =>_CardEnable
    <4>[   48.395907] <=_CardEnable
    <4>[   48.422294] <=_InitPowerOn
    <4>[   48.460064] rtl8188e_FirmwareDownload: fw_ver=4 fw_subver=0 sig=0x88e1
    <4>[   48.858412] _FWFreeToGo: Checksum report OK! REG_MCUFWDL:0x00030004
    <4>[   48.861443] _FWFreeToGo: Polling FW ready success!! REG_MCUFWDL:0x000300c6
    <4>[   48.861464] HalDetectPwrDownMode(): PDN=0
    <4>[   48.861476] Set RF Chip ID to RF_6052 and RF type to 1T1R.
    <4>[   49.078748] <hk> drivers/char/cx_led.c(44) cx_led_open:  
    <4>[   49.078781] <hk> drivers/char/cx_led.c(62) cx_led_ioctl: Cmd:1, arg:0 
    <4>[   49.078826] <hk> drivers/char/cx_led.c(53) cx_led_release:  
    <4>[   49.170926] pDM_Odm TxPowerTrackControl = 1
    <4>[   49.240945] Mali: Page fault detected at 0x4010e200 from bus id 6 of type read on Mali-400 MMU for PP
    <4>[   49.240985] Mali: Active page directory at 0x97609000
    <4>[   49.241002] Mali: Info from page table for VA 0x4010e200:
    <4>[   49.241019] Mali: DTE entry: PTE at 0x9760a000 marked as present
    <4>[   49.241038] Mali: PTE entry: Page at 0x0, not present  
    <4>[   49.245147] UMP<2>: Session closed
    <4>[   49.875977] DISABLE_BB_RF=0
    <4>[   49.875994] IS_HARDWARE_TYPE_8188ES=1
    <4>[   49.876005] -rtl8188es_hal_init
    <4>[   49.876018] rtl8188es_hal_init in 1480ms
    <4>[   49.876035] MAC Address = c6:0d:72:00:04:a5
    <4>[   49.881642] rtw_cfg80211_init_wiphy:rf_type=3
    <4>[   49.881665] -871x_drv - drv_open, bup=1
    <4>[   49.881682] cfg80211_rtw_change_iface, old_iftype=6, new_iftype=2
    <4>[   49.881834] +871x_drv - drv_open, bup=1
    <4>[   49.881850] -871x_drv - drv_open, bup=1
    <4>[   49.883806] cfg80211_rtw_set_power_mgmt
    <6>[   49.883986] ADDRCONF(NETDEV_UP): wlan0: link is not ready
    <4>[   49.979181] cfg80211_rtw_flush_pmksa
    <4>[   49.998088] cfg80211_rtw_change_station
    <4>[   49.998283] cfg80211_rtw_change_station
    <4>[   49.998411] cfg80211_rtw_change_station
    <4>[   49.998669] rtw_android_priv_cmd: Android private cmd "P2P_DEV_ADDR" on wlan0
    <4>[   50.015955] rtw_android_priv_cmd: Android private cmd "BLOCK 0" on wlan0
    <4>[   50.207988] rtw_android_priv_cmd: Android private cmd "BTCOEXSCAN-STOP" on wlan0
    <4>[   50.209582] rtw_android_priv_cmd: Android private cmd "RXFILTER-ADD 3" on wlan0
    <4>[   50.210382] rtw_android_priv_cmd: Android private cmd "RXFILTER-START" on wlan0
    <4>[   50.212095] rtw_android_priv_cmd: Android private cmd "RXFILTER-STOP" on wlan0
    <4>[   50.212804] rtw_android_priv_cmd: Android private cmd "RXFILTER-REMOVE 2" on wlan0
    <4>[   50.213389] rtw_android_priv_cmd: Android private cmd "RXFILTER-START" on wlan0
    <4>[   50.216797] rtw_android_priv_cmd: Android private cmd "SETBAND 0" on wlan0
    <4>[   50.218553] rtw_android_priv_cmd: Android private cmd "SCAN-ACTIVE" on wlan0
    <4>[   50.223842] rtw_android_priv_cmd: Android private cmd "SCAN-PASSIVE" on wlan0
    <4>[   50.999552] cfg80211_rtw_change_station
    <4>[   51.529743] survey done event(28)
    <4>[   52.217932] ==>pwr_state_check_handler .fw_state(8)
    <4>[   52.217957] ==> rtw_ps_cmd  , enqueue CMD 
    <4>[   52.218022] ==>rtw_ps_processor .fw_state(8)
    <4>[   52.218036] ==>ips_enter cnts:1
    <4>[   52.219106] ==>power_saving_ctrl_wk_hdl change rf to OFF...LED(0x00028282).... 
    <4>[   52.219118] 
    <4>[   52.219131] ===> rtw_ips_pwr_down...................
    <4>[   52.219146] ====> rtw_ips_dev_unload...
    <4>[   52.248149] =>rtl8188es_hal_deinit
    <4>[   52.248169] =>CardDisableRTL8188ESdio
    <4>[   52.254990] SetHwReg8188ES: bMacPwrCtrlOn=0
    <4>[   52.255863] <=CardDisableRTL8188ESdio
    <4>[   52.255878] <=rtl8188es_hal_deinit
    <4>[   52.255891] <=== rtw_ips_pwr_down..................... in 30ms
    <4>[   71.898504] TCC_HIGHSPEED: ######### Change to normal status
    <4>[   71.898565] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[   81.878980] TCC_HIGHSPEED: change to 812MHz
    <4>[   81.898843] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[   82.278887] TCC_HIGHSPEED: change to 716MHz
    <4>[   92.199136] TCC_HIGHSPEED: ######### Change to normal status
    <4>[   92.199192] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  112.359931] TCC_HIGHSPEED: change to 812MHz
    <4>[  112.399815] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  112.759834] TCC_HIGHSPEED: change to 716MHz
    <4>[  122.700088] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  122.700144] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  142.880889] TCC_HIGHSPEED: change to 812MHz
    <4>[  142.900759] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  143.280829] TCC_HIGHSPEED: change to 716MHz
    <4>[  153.201043] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  153.201103] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  173.351838] TCC_HIGHSPEED: change to 812MHz
    <4>[  173.401717] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  173.761740] TCC_HIGHSPEED: change to 716MHz
    <4>[  183.701998] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  183.702052] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  203.882815] TCC_HIGHSPEED: change to 812MHz
    <4>[  203.902657] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  204.282712] TCC_HIGHSPEED: change to 716MHz
    <4>[  214.202947] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  214.203011] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  234.293731] TCC_HIGHSPEED: change to 812MHz
    <4>[  234.303616] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  234.793644] TCC_HIGHSPEED: change to 716MHz
    <4>[  244.703903] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  244.703975] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  254.804323] TCC_HIGHSPEED: change to 812MHz
    <4>[  254.904216] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  254.904299] TCC_HIGHSPEED: change to 716MHz
    <4>[  264.754681] TCC_HIGHSPEED: change to 812MHz
    <4>[  265.254609] TCC_HIGHSPEED: change to 716MHz
    <4>[  265.404548] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  265.404611] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  292.437654] 
    <4>[  292.437663]  rfpwrstate_check call ips_leave....
    <4>[  292.437685] ==>ips_leave cnts:1
    <4>[  292.437697] ===>  rtw_ips_pwr_up..............
    <4>[  292.437715] ===> ips_netdrv_open.........
    <4>[  292.437729] +rtl8188es_hal_init
    <4>[  292.437741] =>_InitPowerOn
    <4>[  292.437752] =>_CardEnable
    <4>[  292.444082] SetHwReg8188ES: bMacPwrCtrlOn=1
    <4>[  292.444099] <=_CardEnable
    <4>[  292.444427] <=_InitPowerOn
    <4>[  292.463520] rtl8188e_FirmwareDownload: fw_ver=4 fw_subver=0 sig=0x88e1
    <4>[  292.595459] TCC_HIGHSPEED: change to 812MHz
    <4>[  292.605391] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  292.620183] _FWFreeToGo: Checksum report OK! REG_MCUFWDL:0x00030004
    <4>[  292.623047] _FWFreeToGo: Polling FW ready success!! REG_MCUFWDL:0x000300c6
    <4>[  292.623066] HalDetectPwrDownMode(): PDN=0
    <4>[  292.623077] Set RF Chip ID to RF_6052 and RF type to 1T1R.
    <4>[  292.695441] TCC_HIGHSPEED: change to 716MHz
    <4>[  292.877412] pDM_Odm TxPowerTrackControl = 1
    <4>[  292.995459] TCC_HIGHSPEED: change to 812MHz
    <4>[  293.110189] DISABLE_BB_RF=0
    <4>[  293.110202] IS_HARDWARE_TYPE_8188ES=1
    <4>[  293.110212] -rtl8188es_hal_init
    <4>[  293.110223] rtl8188es_hal_init in 670ms
    <4>[  293.110317] <===  rtw_ips_pwr_up.............. in 670ms
    <4>[  293.110451] ==> ips_leave.....LED(0x00028282)...
    <4>[  293.110466] =>rtw_wx_set_essid
    <4>[  293.110477] ssid=zoobab, len=6
    <4>[  293.110525] Set SSID under fw_state=0x00000008
    <4>[  293.110551] [by_bssid:0][assoc_ssid:zoobab][to_roaming:0] new candidate: zoobab(00:0e:2e:7d:a1:aa) rssi:-66
    <4>[  293.110574] rtw_select_and_join_from_scanned_queue: candidate: zoobab(00:0e:2e:7d:a1:aa)
    <4>[  293.110621] link to Realtek 96B
    <4>[  293.112805] <=rtw_wx_set_essid, ret 0
    <4>[  293.116937] +rtw_wx_set_enc, flags=0x0
    <4>[  293.116955] rtw_wx_set_enc, key=0
    <4>[  293.116965] rtw_wx_set_enc():erq->flags=0x0
    <4>[  293.116983] ==> rtw_set_key algorithm(1),keyid(0),key_mask(1)
    <4>[  293.174757] link to Realtek 96B
    <4>[  293.174784] issue_deauth to 00:0e:2e:7d:a1:aa
    <4>[  293.174823] issue_auth
    <4>[  293.178393] OnAuthClient
    <4>[  293.178423] network.SupportedRates[0]=82
    <4>[  293.178434] network.SupportedRates[1]=84
    <4>[  293.178445] network.SupportedRates[2]=0B
    <4>[  293.178456] network.SupportedRates[3]=16
    <4>[  293.178466] network.SupportedRates[4]=0C
    <4>[  293.178477] network.SupportedRates[5]=12
    <4>[  293.178488] network.SupportedRates[6]=18
    <4>[  293.178498] network.SupportedRates[7]=24
    <4>[  293.178509] network.SupportedRates[8]=30
    <4>[  293.178519] network.SupportedRates[9]=48
    <4>[  293.178530] network.SupportedRates[10]=60
    <4>[  293.178541] network.SupportedRates[11]=6C
    <4>[  293.178553] bssrate_len = 12
    <4>[  293.180985] OnAssocRsp
    <4>[  293.181007] report_join_res(4)
    <4>[  293.181020] rtw_joinbss_update_network
    <4>[  293.181046] rtw_joinbss_update_stainfo
    <4>[  293.181058] ### Set STA_(0) info
    <4>[  293.181078] rtw_cfg80211_indicate_connect(padapter=e172f000)
    <4>[  293.181091] pwdev->sme_state(b)=0
    <4>[  293.181113] pwdev->sme_state(a)=0
    <4>[  293.181226] HW_VAR_BASIC_RATE: BrateCfg(0x15f)
    <6>[  293.184115] ADDRCONF(NETDEV_CHANGE): wlan0: link becomes ready
    <4>[  293.190186] HTOnAssocRsp
    <4>[  293.191552] UpdateHalRAMask8188ESdio => mac_id:0, networkType:0x03, mask:0x00000fff
    <4>[  293.191562] 	 ==> rssi_level:0, rate_bitmap:0x00000ff5
    <4>[  293.191583] ### MacID(0),Set Max Tx RPT MID(1)
    <4>[  293.191638] ### rtl8188e_set_FwMediaStatus_cmd: MStatus=1 MACID=0 
    <4>[  293.192045] rtl8188e_set_FwJoinBssReport_cmd mstatus(1)
    <4>[  293.192213] HalDownloadRSVDPage(): There is an Adapter is sending beacon.
    <4>[  293.192324] SetFwRsvdPagePkt
    <4>[  293.192510] SetFwRsvdPagePkt: Set RSVD page location to Fw
    <4>[  293.192794] rtl8188e_set_FwJoinBssReport_cmd: 1 Download RSVD success! DLBcnCount:1, poll:1
    <4>[  293.192967] Set RSVD page location to Fw.
    <4>[  293.193016] =>mlmeext_joinbss_event_callback
    <4>[  293.195676] TCC_HIGHSPEED: change to 716MHz
    <4>[  295.305645] TCC_HIGHSPEED: change to 812MHz
    <4>[  295.705548] TCC_HIGHSPEED: change to 716MHz
    <4>[  298.117591] UpdateHalRAMask8188ESdio => mac_id:0, networkType:0x03, mask:0x00000fff
    <4>[  298.117605] 	 ==> rssi_level:2, rate_bitmap:0x00000ff0
    <4>[  303.205733] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  303.205804] TCC_HIGHSPEED: ######### cpufreq_work_func
    <7>[  303.525749] wlan0: no IPv6 routers present
    <4>[  304.115908] rtw_set_ps_mode: Enter 802.11 power save
    <4>[  304.117813] rtl8188e_set_FwPwrMode_cmd: Mode=1 SmartPS=2 UAPSD=0
    <4>[  325.846599] TCC_HIGHSPEED: change to 812MHz
    <4>[  325.906472] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  326.246508] TCC_HIGHSPEED: change to 716MHz
    <4>[  336.206763] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  336.206818] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  350.237052] rtw_set_ps_mode: Leave 802.11 power save
    <4>[  350.237087] rtl8188e_set_FwPwrMode_cmd: Mode=0 SmartPS=2 UAPSD=0
    <4>[  351.609281] survey done event(a)
    <4>[  352.117375] rtw_set_ps_mode: Enter 802.11 power save
    <4>[  352.117411] rtl8188e_set_FwPwrMode_cmd: Mode=1 SmartPS=2 UAPSD=0
    <4>[  356.297552] TCC_HIGHSPEED: change to 812MHz
    <4>[  356.307422] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  356.697452] TCC_HIGHSPEED: change to 716MHz
    <4>[  366.607710] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  366.607774] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  386.808510] TCC_HIGHSPEED: change to 812MHz
    <4>[  386.908399] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  387.208411] TCC_HIGHSPEED: change to 716MHz
    <4>[  397.208664] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  397.208732] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  398.508816] TCC_HIGHSPEED: change to 812MHz
    <4>[  398.608705] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  398.609107] TCC_HIGHSPEED: change to 716MHz
    <4>[  408.609024] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  408.609092] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  417.239457] TCC_HIGHSPEED: change to 812MHz
    <4>[  417.309326] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  417.739359] TCC_HIGHSPEED: change to 716MHz
    <4>[  427.709620] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  427.709672] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  447.800405] TCC_HIGHSPEED: change to 812MHz
    <4>[  447.810274] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  448.200338] TCC_HIGHSPEED: change to 716MHz
    <4>[  458.110570] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  458.110632] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  478.221395] TCC_HIGHSPEED: change to 812MHz
    <4>[  478.311235] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  478.721268] TCC_HIGHSPEED: change to 716MHz
    <4>[  488.711532] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  488.711612] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  508.742347] TCC_HIGHSPEED: change to 812MHz
    <4>[  508.812182] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  509.142215] TCC_HIGHSPEED: change to 716MHz
    <4>[  519.112484] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  519.112552] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  539.263265] TCC_HIGHSPEED: change to 812MHz
    <4>[  539.313147] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  539.663173] TCC_HIGHSPEED: change to 716MHz
    <4>[  549.613428] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  549.613493] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  569.674209] TCC_HIGHSPEED: change to 812MHz
    <4>[  569.714090] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  570.174127] TCC_HIGHSPEED: change to 716MHz
    <4>[  580.114384] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  580.114448] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  600.215171] TCC_HIGHSPEED: change to 812MHz
    <4>[  600.315038] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  600.715103] TCC_HIGHSPEED: change to 716MHz
    <4>[  610.715336] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  610.715404] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  630.746124] TCC_HIGHSPEED: change to 812MHz
    <4>[  630.815998] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  631.146026] TCC_HIGHSPEED: change to 716MHz
    <4>[  641.116293] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  641.116352] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  650.247577] rtw_set_ps_mode: Leave 802.11 power save
    <4>[  650.247611] rtl8188e_set_FwPwrMode_cmd: Mode=0 SmartPS=2 UAPSD=0
    <4>[  651.628755] survey done event(c)
    <4>[  651.756784] TCC_HIGHSPEED: change to 812MHz
    <4>[  651.816663] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  651.856694] TCC_HIGHSPEED: change to 716MHz
    <4>[  652.126871] rtw_set_ps_mode: Enter 802.11 power save
    <4>[  652.126911] rtl8188e_set_FwPwrMode_cmd: Mode=1 SmartPS=2 UAPSD=0
    <4>[  661.277088] TCC_HIGHSPEED: change to 812MHz
    <4>[  661.676988] TCC_HIGHSPEED: change to 716MHz
    <4>[  662.216946] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  662.217010] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  691.798028] TCC_HIGHSPEED: change to 812MHz
    <4>[  691.817893] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  692.197933] TCC_HIGHSPEED: change to 716MHz
    <4>[  702.118198] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  702.118275] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  722.218999] TCC_HIGHSPEED: change to 812MHz
    <4>[  722.318860] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  722.718902] TCC_HIGHSPEED: change to 716MHz
    <4>[  732.719150] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  732.719212] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  752.769941] TCC_HIGHSPEED: change to 812MHz
    <4>[  752.819804] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  753.179844] TCC_HIGHSPEED: change to 716MHz
    <4>[  763.120102] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  763.120155] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  783.220893] TCC_HIGHSPEED: change to 812MHz
    <4>[  783.320776] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  783.720812] TCC_HIGHSPEED: change to 716MHz
    <4>[  793.721057] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  793.721133] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  813.741849] TCC_HIGHSPEED: change to 812MHz
    <4>[  813.821715] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  814.151742] TCC_HIGHSPEED: change to 716MHz
    <4>[  824.122010] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  824.122066] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  844.262797] TCC_HIGHSPEED: change to 812MHz
    <4>[  844.322672] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  844.662701] TCC_HIGHSPEED: change to 716MHz
    <4>[  854.622959] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  854.623025] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  857.688378] rtw_set_ps_mode: Leave 802.11 power save
    <4>[  857.688411] rtl8188e_set_FwPwrMode_cmd: Mode=0 SmartPS=2 UAPSD=0
    <4>[  862.133300] rtw_set_ps_mode: Enter 802.11 power save
    <4>[  862.133335] rtl8188e_set_FwPwrMode_cmd: Mode=1 SmartPS=2 UAPSD=0
    <4>[  873.729229] rtw_set_ps_mode: Leave 802.11 power save
    <4>[  873.729262] rtl8188e_set_FwPwrMode_cmd: Mode=0 SmartPS=2 UAPSD=0
    <4>[  874.703732] TCC_HIGHSPEED: change to 812MHz
    <4>[  874.723618] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  875.203668] TCC_HIGHSPEED: change to 716MHz
    <4>[  876.133735] rtw_set_ps_mode: Enter 802.11 power save
    <4>[  876.133769] rtl8188e_set_FwPwrMode_cmd: Mode=1 SmartPS=2 UAPSD=0
    <4>[  883.679058] rtw_set_ps_mode: Leave 802.11 power save
    <4>[  883.679091] rtl8188e_set_FwPwrMode_cmd: Mode=0 SmartPS=2 UAPSD=0
    <4>[  885.123920] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  885.123974] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  886.134043] rtw_set_ps_mode: Enter 802.11 power save
    <4>[  886.134077] rtl8188e_set_FwPwrMode_cmd: Mode=1 SmartPS=2 UAPSD=0
    <4>[  905.234696] TCC_HIGHSPEED: change to 812MHz
    <4>[  905.324566] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  905.634606] TCC_HIGHSPEED: change to 716MHz
    <4>[  915.624867] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  915.624935] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  935.765682] TCC_HIGHSPEED: change to 812MHz
    <4>[  935.825529] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  936.165584] TCC_HIGHSPEED: change to 716MHz
    <4>[  940.236272] rtw_set_ps_mode: Leave 802.11 power save
    <4>[  940.236305] rtl8188e_set_FwPwrMode_cmd: Mode=0 SmartPS=2 UAPSD=0
    <4>[  942.135821] rtw_set_ps_mode: Enter 802.11 power save
    <4>[  942.135856] rtl8188e_set_FwPwrMode_cmd: Mode=1 SmartPS=2 UAPSD=0
    <4>[  945.316704] rtw_set_ps_mode: Leave 802.11 power save
    <4>[  945.316737] rtl8188e_set_FwPwrMode_cmd: Mode=0 SmartPS=2 UAPSD=0
    <4>[  946.125818] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  946.125885] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  948.135984] rtw_set_ps_mode: Enter 802.11 power save
    <4>[  948.136019] rtl8188e_set_FwPwrMode_cmd: Mode=1 SmartPS=2 UAPSD=0
    <4>[  950.256606] rtw_set_ps_mode: Leave 802.11 power save
    <4>[  950.256640] rtl8188e_set_FwPwrMode_cmd: Mode=0 SmartPS=2 UAPSD=0
    <4>[  951.628088] survey done event(d)
    <4>[  952.136120] rtw_set_ps_mode: Enter 802.11 power save
    <4>[  952.136155] rtl8188e_set_FwPwrMode_cmd: Mode=1 SmartPS=2 UAPSD=0
    <4>[  966.186585] TCC_HIGHSPEED: change to 812MHz
    <4>[  966.226490] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  966.696516] TCC_HIGHSPEED: change to 716MHz
    <4>[  976.626778] TCC_HIGHSPEED: ######### Change to normal status
    <4>[  976.626849] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[  980.697084] rtw_set_ps_mode: Leave 802.11 power save
    <4>[  980.697117] rtl8188e_set_FwPwrMode_cmd: Mode=0 SmartPS=2 UAPSD=0
    <4>[  984.137150] rtw_set_ps_mode: Enter 802.11 power save
    <4>[  984.137184] rtl8188e_set_FwPwrMode_cmd: Mode=1 SmartPS=2 UAPSD=0
    <4>[  996.727564] TCC_HIGHSPEED: change to 812MHz
    <4>[  996.827432] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[  997.127467] TCC_HIGHSPEED: change to 716MHz
    <4>[ 1007.127726] TCC_HIGHSPEED: ######### Change to normal status
    <4>[ 1007.127796] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[ 1027.268510] TCC_HIGHSPEED: change to 812MHz
    <4>[ 1027.328388] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[ 1027.668421] TCC_HIGHSPEED: change to 716MHz
    <4>[ 1037.628682] TCC_HIGHSPEED: ######### Change to normal status
    <4>[ 1037.628738] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[ 1057.729449] TCC_HIGHSPEED: change to 812MHz
    <4>[ 1057.829336] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[ 1058.229381] TCC_HIGHSPEED: change to 716MHz
    <4>[ 1062.710273] rtw_set_ps_mode: Leave 802.11 power save
    <4>[ 1062.710306] rtl8188e_set_FwPwrMode_cmd: Mode=0 SmartPS=2 UAPSD=0
    <4>[ 1064.139627] rtw_set_ps_mode: Enter 802.11 power save
    <4>[ 1064.139660] rtl8188e_set_FwPwrMode_cmd: Mode=1 SmartPS=2 UAPSD=0
    <4>[ 1068.229637] TCC_HIGHSPEED: ######### Change to normal status
    <4>[ 1068.229706] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[ 1088.250420] TCC_HIGHSPEED: change to 812MHz
    <4>[ 1088.330296] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[ 1088.650325] TCC_HIGHSPEED: change to 716MHz
    <4>[ 1098.630588] TCC_HIGHSPEED: ######### Change to normal status
    <4>[ 1098.630643] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[ 1118.701373] TCC_HIGHSPEED: change to 812MHz
    <4>[ 1118.731258] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[ 1119.201285] TCC_HIGHSPEED: change to 716MHz
    <4>[ 1129.131541] TCC_HIGHSPEED: ######### Change to normal status
    <4>[ 1129.131596] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[ 1149.232321] TCC_HIGHSPEED: change to 812MHz
    <4>[ 1149.332199] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[ 1149.642220] TCC_HIGHSPEED: change to 716MHz
    <4>[ 1159.632498] TCC_HIGHSPEED: ######### Change to normal status
    <4>[ 1159.632553] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[ 1179.683285] TCC_HIGHSPEED: change to 812MHz
    <4>[ 1179.733162] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[ 1180.183195] TCC_HIGHSPEED: change to 716MHz
    <4>[ 1190.133452] TCC_HIGHSPEED: ######### Change to normal status
    <4>[ 1190.133521] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[ 1210.229552] TCC_HIGHSPEED: change to 812MHz
    <4>[ 1210.234090] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[ 1210.624139] TCC_HIGHSPEED: change to 716MHz
    <4>[ 1220.534395] TCC_HIGHSPEED: ######### Change to normal status
    <4>[ 1220.534467] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[ 1240.775195] TCC_HIGHSPEED: change to 812MHz
    <4>[ 1240.835059] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[ 1241.175140] TCC_HIGHSPEED: change to 716MHz
    <4>[ 1250.267138] rtw_set_ps_mode: Leave 802.11 power save
    <4>[ 1250.267173] rtl8188e_set_FwPwrMode_cmd: Mode=0 SmartPS=2 UAPSD=0
    <4>[ 1251.135358] TCC_HIGHSPEED: ######### Change to normal status
    <4>[ 1251.135423] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[ 1251.637397] survey done event(f)
    <4>[ 1252.145484] rtw_set_ps_mode: Enter 802.11 power save
    <4>[ 1252.145519] rtl8188e_set_FwPwrMode_cmd: Mode=1 SmartPS=2 UAPSD=0
    <4>[ 1271.236162] TCC_HIGHSPEED: change to 812MHz
    <4>[ 1271.336014] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[ 1271.636124] TCC_HIGHSPEED: change to 716MHz
    <4>[ 1281.636306] TCC_HIGHSPEED: ######### Change to normal status
    <4>[ 1281.636363] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[ 1301.727086] TCC_HIGHSPEED: change to 812MHz
    <4>[ 1301.736961] TCC_HIGHSPEED: ######### Change to highspeed status
    <6>[ 1302.127061] usb 1-1: new high speed USB device number 2 using tcc-ehci
    <4>[ 1302.226990] TCC_HIGHSPEED: change to 716MHz
    <6>[ 1302.798660] scsi0 : usb-storage 1-1:1.0
    <5>[ 1303.924921] scsi 0:0:0:0: Direct-Access     JetFlash Transcend 4GB    1100 PQ: 0 ANSI: 4
    <5>[ 1303.932287] sd 0:0:0:0: [sda] 7680000 512-byte logical blocks: (3.93 GB/3.66 GiB)
    <5>[ 1303.932823] sd 0:0:0:0: Attached scsi generic sg0 type 0
    <5>[ 1303.933381] sd 0:0:0:0: [sda] Write Protect is off
    <7>[ 1303.933409] sd 0:0:0:0: [sda] Mode Sense: 43 00 00 00
    <3>[ 1303.934225] sd 0:0:0:0: [sda] No Caching mode page present
    <3>[ 1303.934249] sd 0:0:0:0: [sda] Assuming drive cache: write through
    <3>[ 1303.950480] sd 0:0:0:0: [sda] No Caching mode page present
    <3>[ 1303.950506] sd 0:0:0:0: [sda] Assuming drive cache: write through
    <6>[ 1303.951647]  sda: sda1
    <3>[ 1304.008741] sd 0:0:0:0: [sda] No Caching mode page present
    <3>[ 1304.008767] sd 0:0:0:0: [sda] Assuming drive cache: write through
    <5>[ 1304.008791] sd 0:0:0:0: [sda] Attached SCSI removable disk
    <4>[ 1304.037138] TCC_HIGHSPEED: change to 812MHz
    <4>[ 1304.337098] TCC_HIGHSPEED: change to 716MHz
    <4>[ 1304.537185] TCC_HIGHSPEED: change to 812MHz
    <4>[ 1304.737113] TCC_HIGHSPEED: change to 716MHz
    <4>[ 1304.937217] TCC_HIGHSPEED: change to 812MHz
    <4>[ 1305.937136] TCC_HIGHSPEED: change to 716MHz
    <4>[ 1313.637309] TCC_HIGHSPEED: ######### Change to normal status
    <4>[ 1313.637367] TCC_HIGHSPEED: ######### cpufreq_work_func
    <4>[ 1332.238056] TCC_HIGHSPEED: change to 812MHz
    <4>[ 1332.337921] TCC_HIGHSPEED: ######### Change to highspeed status
    <4>[ 1332.637944] TCC_HIGHSPEED: change to 716MHz
    <4>[ 1342.638208] TCC_HIGHSPEED: ######### Change to normal status
    <4>[ 1342.638277] TCC_HIGHSPEED: ######### cpufreq_work_func


# Links 


* <https://github.com/cnxsoft/telechips-linux>  