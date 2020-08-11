[[f>toc]]

# Serial console


You can obtain a serial console by connecting a special LOM adaptor (I used an ethernet cable and soldered a serial header).


    $ screen /dev/ttyUSB0 9600 8N1


# Ubuntu install CDs bugs


* 6.06: buggy ethernet driver
* 9.04: no support for ALI IDE chipset, does not see the cdrom and hard drives
* 9.10: does not boot, crashes the LOM and automatically restart
* 10.04: does not boot, crashing error: "SILO Version 1.4.14, Fast Data Access MMU Miss"

# Pictures


[[=image sun-fire-v100.jpg]]

# Logs



    top - 23:39:02 up 6 min,  1 user,  load average: 0.02, 0.12, 0.08
    Tasks:
      26 
    total,
       1 
    running,
      25 
    sleeping,
       0 
    stopped,
       0 
    zombie
    Cpu(s):
      2.3% 
      5.3% 
      0.0% 
     90.7% 
      1.7% 
      0.0% 
      0.0% 
    Mem: 
       514472k 
    total,
        38736k 
    used,
       475736k 
    free,
         2792k 
    buffers
    Swap:
      1510088k 
    total,
            0k 
    used,
      1510088k 
    free,
        19152k 
    cached
    [6;1H
    [7m  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND            
        1 root      16   0  1872  752  664 S  0.0  0.1   0:11.51 init               
        2 root      34  19     0    0    0 S  0.0  0.0   0:00.00 ksoftirqd/0        
        3 root      10  -5     0    0    0 S  0.0  0.0   0:00.00 events/0           
        4 root      10  -5     0    0    0 S  0.0  0.0   0:00.04 khelper            
        5 root      10  -5     0    0    0 S  0.0  0.0   0:00.00 kthread            
       16 root      10  -5     0    0    0 S  0.0  0.0   0:00.00 kblockd/0          
       15 root      25   0     0    0    0 S  0.0  0.0   0:00.00 powerd             
       19 root      10  -5     0    0    0 S  0.0  0.0   0:00.00 khubd              
       56 root      20   0     0    0    0 S  0.0  0.0   0:00.00 pdflush            
       57 root      15   0     0    0    0 S  0.0  0.0   0:00.00 pdflush            
       59 root      11  -5     0    0    0 S  0.0  0.0   0:00.00 aio/0              
       58 root      25   0     0    0    0 S  0.0  0.0   0:00.00 kswapd0            
      646 root      10  -5     0    0    0 S  0.0  0.0   0:00.00 kseriod            
     1742 root      15   0     0    0    0 S  0.0  0.0   0:00.00 kjournald          
     1880 root      11  -4  2952  704  448 S  0.0  0.1   0:00.32 udevd              
     2950 root      15   0     0    0    0 S  0.0  0.0   0:00.00 kjournald          
     3059 syslog    16   0  2376  960  768 S  0.0  0.2   0:00.03 syslogd            
    [6;1H
    top - 22:39:05 up 6 min,  1 user,  load average: 0.02, 0.12, 0.08
    Tasks:
      26 
    total,
       1 
    running,
      25 
    sleeping,
       0 
    stopped,
       0 
    zombie
    Cpu(s):
      0.0% 
      0.0% 
      0.0% 
     100.0% 
      0.0% 
      0.0% 
      0.0% 
    Mem: 
       514472k 
    total,
        38736k 
    used,
       475736k 
    free,
         2792k 
    buffers
    Swap:
    [25;1H
    root@brol:~# cat 
    [Kcat /proc/p
    [Kmeminfo 
    MemTotal:       514472 kB
    MemFree:        475736 kB
    Buffers:          2808 kB
    Cached:          19152 kB
    SwapCached:          0 kB
    Active:          20280 kB
    Inactive:         6216 kB
    HighTotal:           0 kB
    HighFree:            0 kB
    LowTotal:       514472 kB
    LowFree:        475736 kB
    SwapTotal:     1510088 kB
    SwapFree:      1510088 kB
    Dirty:             136 kB
    Writeback:           0 kB
    Mapped:           7248 kB
    Slab:             9464 kB
    CommitLimit:   1767320 kB
    Committed_AS:     8384 kB
    PageTables:        288 kB
    VmallocTotal:  4194304 kB
    VmallocUsed:       440 kB
    VmallocChunk:  4193864 kB
    HugePages_Total:     0
    HugePages_Free:      0
    Hugepagesize:     4096 kB
    ^[[Aroot@brol:~# cat /proc/meminfo 
    root@brol:~# 
    root@brol:~# 
    root@brol:~# 
    root@brol:~# ls
    [mroot@brol:~# reset
    [3g        
    H        
    H        
    H        
    H        
    H        
    H        
    H        
    H        
    [?3l
    [?4l
    [?5l
    [?7h
    [?8h
    root@brol:~# ls
    [mroot@brol:~# 
    [Jroot@brol:~# ls
    [mroot@brol:~# ls
    [mroot@brol:~# ps
      PID TTY          TIME CMD
     3147 ttyS0    00:00:00 login
     3175 ttyS0    00:00:00 bash
     3281 ttyS0    00:00:00 ps
    root@brol:~# ps aux
    USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
    root         1  2.4  0.1   1872   752 ?        S    22:32   0:11 init [2]      
    root         2  0.0  0.0      0     0 ?        SN   22:32   0:00 [ksoftirqd/0]
    root         3  0.0  0.0      0     0 ?        S<   22:32   0:00 [events/0]
    root         4  0.0  0.0      0     0 ?        S<   22:32   0:00 [khelper]
    root         5  0.0  0.0      0     0 ?        S<   22:32   0:00 [kthread]
    root        16  0.0  0.0      0     0 ?        S<   22:32   0:00 [kblockd/0]
    root        15  0.0  0.0      0     0 ?        S    22:32   0:00 [powerd]
    root        19  0.0  0.0      0     0 ?        S<   22:32   0:00 [khubd]
    root        56  0.0  0.0      0     0 ?        S    22:32   0:00 [pdflush]
    root        57  0.0  0.0      0     0 ?        S    22:32   0:00 [pdflush]
    root        59  0.0  0.0      0     0 ?        S<   22:32   0:00 [aio/0]
    root        58  0.0  0.0      0     0 ?        S    22:32   0:00 [kswapd0]
    root       646  0.0  0.0      0     0 ?        S<   22:33   0:00 [kseriod]
    root      1742  0.0  0.0      0     0 ?        S    22:33   0:00 [kjournald]
    root      1880  0.0  0.1   2952   704 ?        S<s  22:33   0:00 /sbin/udevd --d
    root      2950  0.0  0.0      0     0 ?        S    22:33   0:00 [kjournald]
    syslog    3059  0.0  0.1   2376   960 ?        Ss   22:33   0:00 /sbin/syslogd -
    root      3076  0.0  0.1   2136   752 ?        Ss   22:33   0:00 /bin/dd bs 1 if
    klog      3078  0.0  0.2   2608  1368 ?        Ss   22:33   0:00 /sbin/klogd -P
    root      3103  0.0  0.0   1928   392 ?        Ss   22:33   0:00 /sbin/mdadm -F
    daemon    3116  0.0  0.1   2552   560 ?        Ss   22:33   0:00 /usr/sbin/atd
    root      3126  0.0  0.2   3032  1096 ?        Ss   22:33   0:00 /usr/sbin/cron
    root      3147  0.0  0.3   4392  1664 ttyS0    Ss   22:33   0:00 /bin/login -- 
    zoobab    3148  0.1  0.5   5448  2776 ttyS0    S    22:33   0:00 -bash
    root      3175  0.1  0.5   5176  2792 ttyS0    S    22:34   0:00 bash
    root      3282  0.0  0.2   3088  1416 ttyS0    R+   22:40   0:00 ps aux
    root@brol:~# ifconfig
    eth0      Link encap:Ethernet  HWaddr 00:03:BA:27:86:F4  
              inet addr:192.168.42.26  Bcast:192.168.42.255  Mask:255.255.255.0
              UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
              RX packets:0 errors:0 dropped:0 overruns:0 frame:0
              TX packets:0 errors:40 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000 
              RX bytes:0 (0.0 b)  TX bytes:0 (0.0 b)
              Base address:0x100 
    lo        Link encap:Local Loopback  
              inet addr:127.0.0.1  Mask:255.0.0.0
              UP LOOPBACK RUNNING  MTU:16436  Metric:1
              RX packets:52 errors:0 dropped:0 overruns:0 frame:0
              TX packets:52 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:0 
              RX bytes:5338 (5.2 KiB)  TX bytes:5338 (5.2 KiB)
    root@brol:~# dmesg
    [    0.000000] PROMLIB: Sun IEEE Boot Prom 'OBP 4.0.18 2002/05/23 18:22'
    [    0.000000] PROMLIB: Root node compatible: sun4u
    [    0.000000] Linux version 2.6.15-51-sparc64 (buildd@sejong) (gcc version 4.0.3 (Ubuntu 4.0.3-1ubuntu5)) #1 Thu Dec 6 20:26:55 UTC 2007
    [    0.000000] ARCH: SUN4U
    [    0.000000] Ethernet address: 00:03:ba:27:86:f3
    [    0.000000] On node 0 totalpages: 64037
    [    0.000000]   DMA zone: 64037 pages, LIFO batch:15
    [    0.000000]   DMA32 zone: 0 pages, LIFO batch:0
    [    0.000000]   Normal zone: 0 pages, LIFO batch:0
    [    0.000000]   HighMem zone: 0 pages, LIFO batch:0
    [    0.000000] CPU[0]: Caches D[sz(16384):line_sz(32)] I[sz(16384):line_sz(32)] E[sz(524288):line_sz(64)]
    [    0.000000] Built 1 zonelists
    [    0.000000] Kernel command line: root=/dev/hda2 ro quiet splash
    [    0.000000] PID hash table entries: 2048 (order: 11, 65536 bytes)
    [    2.070360] Console: colour dummy device 80x25
    [    2.073255] Dentry cache hash table entries: 65536 (order: 6, 524288 bytes)
    [    2.076518] Inode-cache hash table entries: 32768 (order: 5, 262144 bytes)
    [    2.107459] Memory: 507208k available (2352k kernel code, 712k data, 160k init) [fffff80000000000,00000000dfec8000]
    [    2.185473] Calibrating delay using timer specific routine.. 11.12 BogoMIPS (lpj=22241)
    [    2.185695] Security Framework v1.0.0 initialized
    [    2.185741] SELinux:  Disabled at boot.
    [    2.185812] Mount-cache hash table entries: 512
    [    2.186978] checking if image is initramfs... it is
    [    4.341515] Freeing initrd memory: 6485k freed
    [    4.343495] NET: Registered protocol family 16
    [    4.344929] PCI: Probing for controllers.
    [    4.345740] PCI: Found SABRE, main regs at 000001fe00000000
    [    4.345766] SABRE: Shared PCI config space at 000001fe01000000
    [    4.348672] SABRE: DVMA at 60000000 [20000000]
    [    4.350251] PCI quirk: region 2000-203f claimed by ali7101 ACPI
    [    4.350270] PCI quirk: region 4000-401f claimed by ali7101 SMB
    [    4.354620] PCI: Address space collision on region 6 [000001ff00080000:000001ff000bffff] of device 0000:00:05.0
    [    4.354839] PCI-IRQ: Routing bus[ 0] slot[ 5] to INO[1c]
    [    4.354976] PCI-IRQ: Routing bus[ 0] slot[ a] to INO[24]
    [    4.355087] PCI-IRQ: Routing bus[ 0] slot[ c] to INO[06]
    [    4.355198] PCI-IRQ: Routing bus[ 0] slot[ d] to INO[0c]
    [    4.355215] PCI0(PBMA): Bus running at 33MHz
    [    4.355406] isa0: [dma] [rtc -> (todm5819)] [power] [SUNW,lomh] [serial] [serial] [flashprom]
    [    4.357035] ebus: No EBus's found.
    [    4.989970] power: Control reg at 000001fe02002000 ... powerd running.
    [    4.993333] usbcore: registered new driver usbfs
    [    4.993523] usbcore: registered new driver hub
    [    4.998242] audit: initializing netlink socket (disabled)
    [    4.998284] audit(1257910373.828:1): initialized
    [    4.998495] Total HugeTLB memory allocated, 0
    [    4.999001] VFS: Disk quotas dquot_6.5.1
    [    4.999131] Dquot-cache hash table entries: 1024 (order 0, 8192 bytes)
    [    4.999509] Initializing Cryptographic API
    [    4.999532] io scheduler noop registered
    [    4.999559] io scheduler anticipatory registered
    [    4.999585] io scheduler deadline registered
    [    4.999634] io scheduler cfq registered
    [    4.999658] Activating ISA DMA hang workarounds.
    [   13.462368] Console: switching to mono PROM 80x34
    [   13.534273] Real Time Clock Driver v1.12
    [   13.534334] [drm] Initialized drm 1.0.1 20051102
    [   13.543535] ttyS0 at MMIO 0x1fe020003f8 (irq = 7616992) is a 16550A
    [   13.543805] Console: ttyS0 (SU)
    [   13.676687] ttyS1 at MMIO 0x1fe020002e8 (irq = 7616992) is a 16550A
    [   13.679103] RAMDISK driver initialized: 16 RAM disks of 65536K size 1024 blocksize
    [   13.680105] loop: loaded (max 8 devices)
    [   13.680482] Uniform Multi-Platform E-IDE driver Revision: 7.00alpha2
    [   13.680500] ide: Assuming 33MHz system bus speed for PIO modes; override with idebus=xx
    [   13.681225] usbmon: debugfs is not available
    [   13.681383] usbcore: registered new driver usbhid
    [   13.681397] drivers/usb/input/hid-core.c: v2.6:USB HID core driver
    [   13.681650] mice: PS/2 mouse device common for all mice
    [   13.682307] input: Sparc ISA Speaker as /class/input/input0
    [   13.682541] NET: Registered protocol family 2
    [   13.717633] IP route cache hash table entries: 4096 (order: 2, 32768 bytes)
    [   13.718488] TCP established hash table entries: 16384 (order: 4, 131072 bytes)
    [   13.719139] TCP bind hash table entries: 16384 (order: 4, 131072 bytes)
    [   13.719822] TCP: Hash tables configured (established 16384 bind 16384)
    [   13.719840] TCP reno registered
    [   13.720141] TCP bic registered
    [   13.720196] NET: Registered protocol family 1
    [   13.720227] NET: Registered protocol family 17
    [   13.994426] Capability LSM initialized
    [   15.600583] ALI15X3: IDE controller at PCI slot 0000:00:0d.0
    [   15.600641] ALI15X3: chipset revision 195
    [   15.600672] ALI15X3: 100% native mode on irq 5,7cc
    [   15.600704]     ide0: BM-DMA at 0x1fe02010220-0x1fe02010227, BIOS settings: hda:pio, hdb:pio
    [   15.600762]     ide1: BM-DMA at 0x1fe02010228-0x1fe0201022f, BIOS settings: hdc:pio, hdd:pio
    [   15.600810] Probing IDE interface ide0...
    [   15.889536] hda: ST340016A, ATA DISK drive
    [   16.561701] ide0 at 0x1fe02010200-0x1fe02010207,0x1fe0201021a on irq 5,7cc
    [   16.561828] Probing IDE interface ide1...
    [   16.849515] hdc: ST340016A, ATA DISK drive
    [    0.117640] hdd: CD-224E, ATAPI CD/DVD-ROM drive
    [    0.173644] ide1 at 0x1fe02010210-0x1fe02010217,0x1fe0201020a on irq 5,7cc
    [    0.218411] hda: max request size: 128KiB
    [    0.232077] hda: 78165360 sectors (40020 MB) w/2048KiB Cache, CHS=65535/16/63, UDMA(66)
    [    0.232106] hda: cache flushes not supported
    [    0.232263]  hda: hda1 hda2 hda3 hda4
    [    0.238796] hdc: max request size: 128KiB
    [    0.239308] hdc: 78165360 sectors (40020 MB) w/2048KiB Cache, CHS=65535/16/63, UDMA(66)
    [    0.239334] hdc: cache flushes not supported
    [    0.239448]  hdc: hdc1 hdc2 hdc3 hdc4 hdc8
    [    0.287118] hdd: ATAPI 24X CD-ROM drive, 128kB Cache
    [    0.287147] Uniform CD-ROM driver Revision: 3.20
    [    0.753214] ohci_hcd: 2005 April 22 USB 1.1 'Open' Host Controller (OHCI) Driver (PCI)
    [    0.753323] ohci_hcd 0000:00:0a.0: OHCI Host Controller
    [    0.754435] ohci_hcd 0000:00:0a.0: new USB bus registered, assigned bus number 1
    [    0.754476] ohci_hcd 0000:00:0a.0: irq 14,7e4, io mem 0x1ff01000000
    [    0.773794] hub 1-0:1.0: USB hub found
    [    0.773856] hub 1-0:1.0: 2 ports detected
    [    1.005504] usb 1-1: new low speed USB device using ohci_hcd and address 2
    [    1.183425] input: USB-compliant keyboard as /class/input/input1
    [    1.183478] input: USB HID v1.10 Keyboard [USB-compliant keyboard] on usb-0000:00:0a.0-1
    [    1.214157] input: USB-compliant keyboard as /class/input/input2
    [    1.214281] input: USB HID v1.10 Mouse [USB-compliant keyboard] on usb-0000:00:0a.0-1
    [    1.313625] kjournald starting.  Commit interval 5 seconds
    [    1.313672] EXT3-fs: mounted filesystem with ordered data mode.
    [    7.489090] Linux Tulip driver version 1.1.13-NAPI (December 15, 2004)
    [    7.499670] tulip0: Old style EEPROM with no media selection information.
    [    7.499931] tulip0:  MII transceiver #1 config 1000 status 7809 advertising 01e1.
    [    7.502777] eth0: Davicom DM9102/DM9102A rev 49 at 000001fe02010100, EEPROM not present, 00:03:BA:27:86:F4, IRQ 7616512.
    [    7.513222] tulip1: Old style EEPROM with no media selection information.
    [    7.513492] tulip1:  MII transceiver #1 config 1100 status 782d advertising 01e1.
    [    7.516273] eth1: Davicom DM9102/DM9102A rev 49 at 000001fe02010000, EEPROM not present, 00:03:BA:27:86:F3, IRQ 7615808.
    [    8.611910] Adding 1510088k swap on /dev/hda4.  Priority:-1 extents:1 across:1510088k
    [    8.746139] EXT3 FS on hda2, internal journal
    [    9.208605] md: md driver 0.90.3 MAX_MD_DEVS=256, MD_SB_DISKS=27
    [    9.208625] md: bitmap version 4.39
    [   10.151402] device-mapper: 4.4.0-ioctl (2005-01-12) initialised: dm-devel@redhat.com
    [   11.392181] hdd: packet command error: status=0x51 { DriveReady SeekComplete Error }
    [   11.392207] hdd: packet command error: error=0x54 { AbortedCommand LastFailedSense=0x05 }
    [   11.392226] ide: failed opcode was: unknown
    [   11.392907] cdrom: open failed.
    [   11.926715] kjournald starting.  Commit interval 5 seconds
    [   11.926936] EXT3 FS on hda1, internal journal
    [   11.926955] EXT3-fs: mounted filesystem with ordered data mode.
    [   11.605323] hdd: packet command error: status=0x51 { DriveReady SeekComplete Error }
    [   11.605354] hdd: packet command error: error=0x54 { AbortedCommand LastFailedSense=0x05 }
    [   11.605373] ide: failed opcode was: unknown
    [   11.606761] cdrom: open failed.
    [   11.700819] hdd: packet command error: status=0x51 { DriveReady SeekComplete Error }
    [   11.700849] hdd: packet command error: error=0x54 { AbortedCommand LastFailedSense=0x05 }
    [   11.700867] ide: failed opcode was: unknown
    [   11.702259] cdrom: open failed.
    [    6.437080] NETDEV WATCHDOG: eth0: transmit timed out
    [    6.438634] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   14.437001] NETDEV WATCHDOG: eth0: transmit timed out
    [   14.438545] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    5.257056] NETDEV WATCHDOG: eth0: transmit timed out
    [    5.258604] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   13.256972] NETDEV WATCHDOG: eth0: transmit timed out
    [   13.258516] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    4.077027] NETDEV WATCHDOG: eth0: transmit timed out
    [    4.078575] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   12.076946] NETDEV WATCHDOG: eth0: transmit timed out
    [   12.078495] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    2.896998] NETDEV WATCHDOG: eth0: transmit timed out
    [    2.898543] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   10.896918] NETDEV WATCHDOG: eth0: transmit timed out
    [   10.898464] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    1.716966] NETDEV WATCHDOG: eth0: transmit timed out
    [    1.718511] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    9.716890] NETDEV WATCHDOG: eth0: transmit timed out
    [    9.718438] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    0.536943] NETDEV WATCHDOG: eth0: transmit timed out
    [    0.538493] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    8.536865] NETDEV WATCHDOG: eth0: transmit timed out
    [    8.538406] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   16.536785] NETDEV WATCHDOG: eth0: transmit timed out
    [   16.538333] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    7.356833] NETDEV WATCHDOG: eth0: transmit timed out
    [    7.358376] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   15.356758] NETDEV WATCHDOG: eth0: transmit timed out
    [   15.358307] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    6.176806] NETDEV WATCHDOG: eth0: transmit timed out
    [    6.178352] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   14.176727] NETDEV WATCHDOG: eth0: transmit timed out
    [   14.178272] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    4.996779] NETDEV WATCHDOG: eth0: transmit timed out
    [    4.998319] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   12.996699] NETDEV WATCHDOG: eth0: transmit timed out
    [   12.998242] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    3.816750] NETDEV WATCHDOG: eth0: transmit timed out
    [    3.818287] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   11.816671] NETDEV WATCHDOG: eth0: transmit timed out
    [   11.818213] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    2.636722] NETDEV WATCHDOG: eth0: transmit timed out
    [    2.638259] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   10.636643] NETDEV WATCHDOG: eth0: transmit timed out
    [   10.638184] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    1.456699] NETDEV WATCHDOG: eth0: transmit timed out
    [    1.458250] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    9.456621] NETDEV WATCHDOG: eth0: transmit timed out
    [    9.458172] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    0.276670] NETDEV WATCHDOG: eth0: transmit timed out
    [    0.278218] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    8.276590] NETDEV WATCHDOG: eth0: transmit timed out
    [    8.278133] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   16.276512] NETDEV WATCHDOG: eth0: transmit timed out
    [   16.278059] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    7.096565] NETDEV WATCHDOG: eth0: transmit timed out
    [    7.098114] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   15.096482] NETDEV WATCHDOG: eth0: transmit timed out
    [   15.098024] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    5.916533] NETDEV WATCHDOG: eth0: transmit timed out
    [    5.918075] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   13.916453] NETDEV WATCHDOG: eth0: transmit timed out
    [   13.917994] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    4.736504] NETDEV WATCHDOG: eth0: transmit timed out
    [    4.738041] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   12.736425] NETDEV WATCHDOG: eth0: transmit timed out
    [   12.737962] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    3.556477] NETDEV WATCHDOG: eth0: transmit timed out
    [    3.558017] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   11.556398] NETDEV WATCHDOG: eth0: transmit timed out
    [   11.557937] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    2.376449] NETDEV WATCHDOG: eth0: transmit timed out
    [    2.377987] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   10.376370] NETDEV WATCHDOG: eth0: transmit timed out
    [   10.377908] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    1.196423] NETDEV WATCHDOG: eth0: transmit timed out
    [    1.197965] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    9.196350] NETDEV WATCHDOG: eth0: transmit timed out
    [    9.197900] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    0.016398] NETDEV WATCHDOG: eth0: transmit timed out
    [    0.017948] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    root@brol:~# [   14.439922] eth0: Out-of-sync dirty pointer, 16 vs. 86.
    root@brol:~# 
    root@brol:~# 
    root@brol:~# 
    root@brol:~# ifconfig 
    eth0      Link encap:Ethernet  HWaddr 00:03:BA:27:86:F4  
              inet addr:192.168.42.26  Bcast:192.168.42.255  Mask:255.255.255.0
              UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
              RX packets:32 errors:0 dropped:0 overruns:0 frame:0
              TX packets:0 errors:76 dropped:0 overruns:0 carrier:32
              collisions:0 txqueuelen:1000 
              RX bytes:1920 (1.8 KiB)  TX bytes:0 (0.0 b)
              Base address:0x100 
    lo        Link encap:Local Loopback  
              inet addr:127.0.0.1  Mask:255.0.0.0
              UP LOOPBACK RUNNING  MTU:16436  Metric:1
              RX packets:52 errors:0 dropped:0 overruns:0 frame:0
              TX packets:52 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:0 
              RX bytes:5338 (5.2 KiB)  TX bytes:5338 (5.2 KiB)
    root@brol:~# ifconfig  eth1
    eth1      Link encap:Ethernet  HWaddr 00:03:BA:27:86:F3  
              BROADCAST MULTICAST  MTU:1500  Metric:1
              RX packets:0 errors:0 dropped:0 overruns:0 frame:0
              TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000 
              RX bytes:0 (0.0 b)  TX bytes:0 (0.0 b)
              Interrupt:64 
    root@brol:~# ifconfig  eth1
    [Peth1
    [Peth1
    [Peth1
    [Peth1
    [Peth1
    [Peth1
    [Peth1
    [Peth1
    [Peth1
    [Peth1
    deth1
    heth1
    geth1
    ceth1
    leth1
     eth1
    [Peth1
    [Peth1
    [Peth1
    [Peth1
    ceth1
    leth1
    ienteth1
     eth1
    Internet Systems Consortium DHCP Client V3.0.3
    Copyright 2004-2005 Internet Systems Consortium.
    All rights reserved.
    For info, please visit http://www.isc.org/products/DHCP
    Listening on LPF/eth1/00:03:ba:27:86:f3
    Sending on   LPF/eth1/00:03:ba:27:86:f3
    Sending on   Socket/fallback
    DHCPDISCOVER on eth1 to 255.255.255.255 port 67 interval 3
    DHCPDISCOVER on eth1 to 255.255.255.255 port 67 interval 4
    DHCPDISCOVER on eth1 to 255.255.255.255 port 67 interval 6
    DHCPDISCOVER on eth1 to 255.255.255.255 port 67 interval 8
    root@brol:~# if
    [Kdmesg
    [    0.000000] PROMLIB: Sun IEEE Boot Prom 'OBP 4.0.18 2002/05/23 18:22'
    [    0.000000] PROMLIB: Root node compatible: sun4u
    [    0.000000] Linux version 2.6.15-51-sparc64 (buildd@sejong) (gcc version 4.0.3 (Ubuntu 4.0.3-1ubuntu5)) #1 Thu Dec 6 20:26:55 UTC 2007
    [    0.000000] ARCH: SUN4U
    [    0.000000] Ethernet address: 00:03:ba:27:86:f3
    [    0.000000] On node 0 totalpages: 64037
    [    0.000000]   DMA zone: 64037 pages, LIFO batch:15
    [    0.000000]   DMA32 zone: 0 pages, LIFO batch:0
    [    0.000000]   Normal zone: 0 pages, LIFO batch:0
    [    0.000000]   HighMem zone: 0 pages, LIFO batch:0
    [    0.000000] CPU[0]: Caches D[sz(16384):line_sz(32)] I[sz(16384):line_sz(32)] E[sz(524288):line_sz(64)]
    [    0.000000] Built 1 zonelists
    [    0.000000] Kernel command line: root=/dev/hda2 ro quiet splash
    [    0.000000] PID hash table entries: 2048 (order: 11, 65536 bytes)
    [    2.070360] Console: colour dummy device 80x25
    [    2.073255] Dentry cache hash table entries: 65536 (order: 6, 524288 bytes)
    [    2.076518] Inode-cache hash table entries: 32768 (order: 5, 262144 bytes)
    [    2.107459] Memory: 507208k available (2352k kernel code, 712k data, 160k init) [fffff80000000000,00000000dfec8000]
    [    2.185473] Calibrating delay using timer specific routine.. 11.12 BogoMIPS (lpj=22241)
    [    2.185695] Security Framework v1.0.0 initialized
    [    2.185741] SELinux:  Disabled at boot.
    [    2.185812] Mount-cache hash table entries: 512
    [    2.186978] checking if image is initramfs... it is
    [    4.341515] Freeing initrd memory: 6485k freed
    [    4.343495] NET: Registered protocol family 16
    [    4.344929] PCI: Probing for controllers.
    [    4.345740] PCI: Found SABRE, main regs at 000001fe00000000
    [    4.345766] SABRE: Shared PCI config space at 000001fe01000000
    [    4.348672] SABRE: DVMA at 60000000 [20000000]
    [    4.350251] PCI quirk: region 2000-203f claimed by ali7101 ACPI
    [    4.350270] PCI quirk: region 4000-401f claimed by ali7101 SMB
    [    4.354620] PCI: Address space collision on region 6 [000001ff00080000:000001ff000bffff] of device 0000:00:05.0
    [    4.354839] PCI-IRQ: Routing bus[ 0] slot[ 5] to INO[1c]
    [    4.354976] PCI-IRQ: Routing bus[ 0] slot[ a] to INO[24]
    [    4.355087] PCI-IRQ: Routing bus[ 0] slot[ c] to INO[06]
    [    4.355198] PCI-IRQ: Routing bus[ 0] slot[ d] to INO[0c]
    [    4.355215] PCI0(PBMA): Bus running at 33MHz
    [    4.355406] isa0: [dma] [rtc -> (todm5819)] [power] [SUNW,lomh] [serial] [serial] [flashprom]
    [    4.357035] ebus: No EBus's found.
    [    4.989970] power: Control reg at 000001fe02002000 ... powerd running.
    [    4.993333] usbcore: registered new driver usbfs
    [    4.993523] usbcore: registered new driver hub
    [    4.998242] audit: initializing netlink socket (disabled)
    [    4.998284] audit(1257910373.828:1): initialized
    [    4.998495] Total HugeTLB memory allocated, 0
    [    4.999001] VFS: Disk quotas dquot_6.5.1
    [    4.999131] Dquot-cache hash table entries: 1024 (order 0, 8192 bytes)
    [    4.999509] Initializing Cryptographic API
    [    4.999532] io scheduler noop registered
    [    4.999559] io scheduler anticipatory registered
    [    4.999585] io scheduler deadline registered
    [    4.999634] io scheduler cfq registered
    [    4.999658] Activating ISA DMA hang workarounds.
    [   13.462368] Console: switching to mono PROM 80x34
    [   13.534273] Real Time Clock Driver v1.12
    [   13.534334] [drm] Initialized drm 1.0.1 20051102
    [   13.543535] ttyS0 at MMIO 0x1fe020003f8 (irq = 7616992) is a 16550A
    [   13.543805] Console: ttyS0 (SU)
    [   13.676687] ttyS1 at MMIO 0x1fe020002e8 (irq = 7616992) is a 16550A
    [   13.679103] RAMDISK driver initialized: 16 RAM disks of 65536K size 1024 blocksize
    [   13.680105] loop: loaded (max 8 devices)
    [   13.680482] Uniform Multi-Platform E-IDE driver Revision: 7.00alpha2
    [   13.680500] ide: Assuming 33MHz system bus speed for PIO modes; override with idebus=xx
    [   13.681225] usbmon: debugfs is not available
    [   13.681383] usbcore: registered new driver usbhid
    [   13.681397] drivers/usb/input/hid-core.c: v2.6:USB HID core driver
    [   13.681650] mice: PS/2 mouse device common for all mice
    [   13.682307] input: Sparc ISA Speaker as /class/input/input0
    [   13.682541] NET: Registered protocol family 2
    [   13.717633] IP route cache hash table entries: 4096 (order: 2, 32768 bytes)
    [   13.718488] TCP established hash table entries: 16384 (order: 4, 131072 bytes)
    [   13.719139] TCP bind hash table entries: 16384 (order: 4, 131072 bytes)
    [   13.719822] TCP: Hash tables configured (established 16384 bind 16384)
    [   13.719840] TCP reno registered
    [   13.720141] TCP bic registered
    [   13.720196] NET: Registered protocol family 1
    [   13.720227] NET: Registered protocol family 17
    [   13.994426] Capability LSM initialized
    [   15.600583] ALI15X3: IDE controller at PCI slot 0000:00:0d.0
    [   15.600641] ALI15X3: chipset revision 195
    [   15.600672] ALI15X3: 100% native mode on irq 5,7cc
    [   15.600704]     ide0: BM-DMA at 0x1fe02010220-0x1fe02010227, BIOS settings: hda:pio, hdb:pio
    [   15.600762]     ide1: BM-DMA at 0x1fe02010228-0x1fe0201022f, BIOS settings: hdc:pio, hdd:pio
    [   15.600810] Probing IDE interface ide0...
    [   15.889536] hda: ST340016A, ATA DISK drive
    [   16.561701] ide0 at 0x1fe02010200-0x1fe02010207,0x1fe0201021a on irq 5,7cc
    [   16.561828] Probing IDE interface ide1...
    [   16.849515] hdc: ST340016A, ATA DISK drive
    [    0.117640] hdd: CD-224E, ATAPI CD/DVD-ROM drive
    [    0.173644] ide1 at 0x1fe02010210-0x1fe02010217,0x1fe0201020a on irq 5,7cc
    [    0.218411] hda: max request size: 128KiB
    [    0.232077] hda: 78165360 sectors (40020 MB) w/2048KiB Cache, CHS=65535/16/63, UDMA(66)
    [    0.232106] hda: cache flushes not supported
    [    0.232263]  hda: hda1 hda2 hda3 hda4
    [    0.238796] hdc: max request size: 128KiB
    [    0.239308] hdc: 78165360 sectors (40020 MB) w/2048KiB Cache, CHS=65535/16/63, UDMA(66)
    [    0.239334] hdc: cache flushes not supported
    [    0.239448]  hdc: hdc1 hdc2 hdc3 hdc4 hdc8
    [    0.287118] hdd: ATAPI 24X CD-ROM drive, 128kB Cache
    [    0.287147] Uniform CD-ROM driver Revision: 3.20
    [    0.753214] ohci_hcd: 2005 April 22 USB 1.1 'Open' Host Controller (OHCI) Driver (PCI)
    [    0.753323] ohci_hcd 0000:00:0a.0: OHCI Host Controller
    [    0.754435] ohci_hcd 0000:00:0a.0: new USB bus registered, assigned bus number 1
    [    0.754476] ohci_hcd 0000:00:0a.0: irq 14,7e4, io mem 0x1ff01000000
    [    0.773794] hub 1-0:1.0: USB hub found
    [    0.773856] hub 1-0:1.0: 2 ports detected
    [    1.005504] usb 1-1: new low speed USB device using ohci_hcd and address 2
    [    1.183425] input: USB-compliant keyboard as /class/input/input1
    [    1.183478] input: USB HID v1.10 Keyboard [USB-compliant keyboard] on usb-0000:00:0a.0-1
    [    1.214157] input: USB-compliant keyboard as /class/input/input2
    [    1.214281] input: USB HID v1.10 Mouse [USB-compliant keyboard] on usb-0000:00:0a.0-1
    [    1.313625] kjournald starting.  Commit interval 5 seconds
    [    1.313672] EXT3-fs: mounted filesystem with ordered data mode.
    [    7.489090] Linux Tulip driver version 1.1.13-NAPI (December 15, 2004)
    [    7.499670] tulip0: Old style EEPROM with no media selection information.
    [    7.499931] tulip0:  MII transceiver #1 config 1000 status 7809 advertising 01e1.
    [    7.502777] eth0: Davicom DM9102/DM9102A rev 49 at 000001fe02010100, EEPROM not present, 00:03:BA:27:86:F4, IRQ 7616512.
    [    7.513222] tulip1: Old style EEPROM with no media selection information.
    [    7.513492] tulip1:  MII transceiver #1 config 1100 status 782d advertising 01e1.
    [    7.516273] eth1: Davicom DM9102/DM9102A rev 49 at 000001fe02010000, EEPROM not present, 00:03:BA:27:86:F3, IRQ 7615808.
    [    8.611910] Adding 1510088k swap on /dev/hda4.  Priority:-1 extents:1 across:1510088k
    [    8.746139] EXT3 FS on hda2, internal journal
    [    9.208605] md: md driver 0.90.3 MAX_MD_DEVS=256, MD_SB_DISKS=27
    [    9.208625] md: bitmap version 4.39
    [   10.151402] device-mapper: 4.4.0-ioctl (2005-01-12) initialised: dm-devel@redhat.com
    [   11.392181] hdd: packet command error: status=0x51 { DriveReady SeekComplete Error }
    [   11.392207] hdd: packet command error: error=0x54 { AbortedCommand LastFailedSense=0x05 }
    [   11.392226] ide: failed opcode was: unknown
    [   11.392907] cdrom: open failed.
    [   11.926715] kjournald starting.  Commit interval 5 seconds
    [   11.926936] EXT3 FS on hda1, internal journal
    [   11.926955] EXT3-fs: mounted filesystem with ordered data mode.
    [   11.605323] hdd: packet command error: status=0x51 { DriveReady SeekComplete Error }
    [   11.605354] hdd: packet command error: error=0x54 { AbortedCommand LastFailedSense=0x05 }
    [   11.605373] ide: failed opcode was: unknown
    [   11.606761] cdrom: open failed.
    [   11.700819] hdd: packet command error: status=0x51 { DriveReady SeekComplete Error }
    [   11.700849] hdd: packet command error: error=0x54 { AbortedCommand LastFailedSense=0x05 }
    [   11.700867] ide: failed opcode was: unknown
    [   11.702259] cdrom: open failed.
    [    6.437080] NETDEV WATCHDOG: eth0: transmit timed out
    [    6.438634] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   14.437001] NETDEV WATCHDOG: eth0: transmit timed out
    [   14.438545] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    5.257056] NETDEV WATCHDOG: eth0: transmit timed out
    [    5.258604] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   13.256972] NETDEV WATCHDOG: eth0: transmit timed out
    [   13.258516] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    4.077027] NETDEV WATCHDOG: eth0: transmit timed out
    [    4.078575] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   12.076946] NETDEV WATCHDOG: eth0: transmit timed out
    [   12.078495] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    2.896998] NETDEV WATCHDOG: eth0: transmit timed out
    [    2.898543] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   10.896918] NETDEV WATCHDOG: eth0: transmit timed out
    [   10.898464] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    1.716966] NETDEV WATCHDOG: eth0: transmit timed out
    [    1.718511] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    9.716890] NETDEV WATCHDOG: eth0: transmit timed out
    [    9.718438] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    0.536943] NETDEV WATCHDOG: eth0: transmit timed out
    [    0.538493] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    8.536865] NETDEV WATCHDOG: eth0: transmit timed out
    [    8.538406] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   16.536785] NETDEV WATCHDOG: eth0: transmit timed out
    [   16.538333] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    7.356833] NETDEV WATCHDOG: eth0: transmit timed out
    [    7.358376] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   15.356758] NETDEV WATCHDOG: eth0: transmit timed out
    [   15.358307] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    6.176806] NETDEV WATCHDOG: eth0: transmit timed out
    [    6.178352] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   14.176727] NETDEV WATCHDOG: eth0: transmit timed out
    [   14.178272] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    4.996779] NETDEV WATCHDOG: eth0: transmit timed out
    [    4.998319] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   12.996699] NETDEV WATCHDOG: eth0: transmit timed out
    [   12.998242] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    3.816750] NETDEV WATCHDOG: eth0: transmit timed out
    [    3.818287] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   11.816671] NETDEV WATCHDOG: eth0: transmit timed out
    [   11.818213] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    2.636722] NETDEV WATCHDOG: eth0: transmit timed out
    [    2.638259] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   10.636643] NETDEV WATCHDOG: eth0: transmit timed out
    [   10.638184] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    1.456699] NETDEV WATCHDOG: eth0: transmit timed out
    [    1.458250] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    9.456621] NETDEV WATCHDOG: eth0: transmit timed out
    [    9.458172] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    0.276670] NETDEV WATCHDOG: eth0: transmit timed out
    [    0.278218] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    8.276590] NETDEV WATCHDOG: eth0: transmit timed out
    [    8.278133] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   16.276512] NETDEV WATCHDOG: eth0: transmit timed out
    [   16.278059] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    7.096565] NETDEV WATCHDOG: eth0: transmit timed out
    [    7.098114] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   15.096482] NETDEV WATCHDOG: eth0: transmit timed out
    [   15.098024] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    5.916533] NETDEV WATCHDOG: eth0: transmit timed out
    [    5.918075] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   13.916453] NETDEV WATCHDOG: eth0: transmit timed out
    [   13.917994] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    4.736504] NETDEV WATCHDOG: eth0: transmit timed out
    [    4.738041] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   12.736425] NETDEV WATCHDOG: eth0: transmit timed out
    [   12.737962] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    3.556477] NETDEV WATCHDOG: eth0: transmit timed out
    [    3.558017] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   11.556398] NETDEV WATCHDOG: eth0: transmit timed out
    [   11.557937] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    2.376449] NETDEV WATCHDOG: eth0: transmit timed out
    [    2.377987] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   10.376370] NETDEV WATCHDOG: eth0: transmit timed out
    [   10.377908] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    1.196423] NETDEV WATCHDOG: eth0: transmit timed out
    [    1.197965] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    9.196350] NETDEV WATCHDOG: eth0: transmit timed out
    [    9.197900] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    0.016398] NETDEV WATCHDOG: eth0: transmit timed out
    [    0.017948] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    8.016318] NETDEV WATCHDOG: eth0: transmit timed out
    [    8.017869] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   16.016237] NETDEV WATCHDOG: eth0: transmit timed out
    [   16.017779] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    6.836289] NETDEV WATCHDOG: eth0: transmit timed out
    [    6.837830] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   14.439922] eth0: Out-of-sync dirty pointer, 16 vs. 86.
    root@brol:~# ifconfig eth0 19
    [K0.0.0.1
    root@brol:~# ifconfig eth0 10.0.0.1
    [P 10.0.0.1
    1 10.0.0.1
    root@brol:~# ifconfig eth1 
    root@brol:~# ifconfig eth1 1
    root@brol:~# ifconfig eth1 10
    root@brol:~# ifconfig eth1 10.
    root@brol:~# ifconfig eth1 10.0
    root@brol:~# ifconfig eth1 10.0.
    root@brol:~# ifconfig eth1 10.0.0
    root@brol:~# ifconfig eth1 10.0.0.
    root@brol:~# ifconfig eth1 10.0.0.1
    root@brol:~# ifconfig eth1 192.168.42.27
    root@brol:~# ping 192.168.42.2
    PING 192.168.42.1 (192.168.42.1) 56(84) bytes of data.
    From 192.168.42.27 icmp_seq=1 Destination Host Unreachable
    From 192.168.42.27 icmp_seq=2 Destination Host Unreachable
    From 192.168.42.27 icmp_seq=3 Destination Host Unreachable
    --- 192.168.42.1 ping statistics ---
    5 packets transmitted, 0 received, +3 errors, 100% packet loss, time 4018ms
    , pipe 3
    root@brol:~# dmesg
    [    0.000000] PROMLIB: Sun IEEE Boot Prom 'OBP 4.0.18 2002/05/23 18:22'
    [    0.000000] PROMLIB: Root node compatible: sun4u
    [    0.000000] Linux version 2.6.15-51-sparc64 (buildd@sejong) (gcc version 4.0.3 (Ubuntu 4.0.3-1ubuntu5)) #1 Thu Dec 6 20:26:55 UTC 2007
    [    0.000000] ARCH: SUN4U
    [    0.000000] Ethernet address: 00:03:ba:27:86:f3
    [    0.000000] On node 0 totalpages: 64037
    [    0.000000]   DMA zone: 64037 pages, LIFO batch:15
    [    0.000000]   DMA32 zone: 0 pages, LIFO batch:0
    [    0.000000]   Normal zone: 0 pages, LIFO batch:0
    [    0.000000]   HighMem zone: 0 pages, LIFO batch:0
    [    0.000000] CPU[0]: Caches D[sz(16384):line_sz(32)] I[sz(16384):line_sz(32)] E[sz(524288):line_sz(64)]
    [    0.000000] Built 1 zonelists
    [    0.000000] Kernel command line: root=/dev/hda2 ro quiet splash
    [    0.000000] PID hash table entries: 2048 (order: 11, 65536 bytes)
    [    2.070360] Console: colour dummy device 80x25
    [    2.073255] Dentry cache hash table entries: 65536 (order: 6, 524288 bytes)
    [    2.076518] Inode-cache hash table entries: 32768 (order: 5, 262144 bytes)
    [    2.107459] Memory: 507208k available (2352k kernel code, 712k data, 160k init) [fffff80000000000,00000000dfec8000]
    [    2.185473] Calibrating delay using timer specific routine.. 11.12 BogoMIPS (lpj=22241)
    [    2.185695] Security Framework v1.0.0 initialized
    [    2.185741] SELinux:  Disabled at boot.
    [    2.185812] Mount-cache hash table entries: 512
    [    2.186978] checking if image is initramfs... it is
    [    4.341515] Freeing initrd memory: 6485k freed
    [    4.343495] NET: Registered protocol family 16
    [    4.344929] PCI: Probing for controllers.
    [    4.345740] PCI: Found SABRE, main regs at 000001fe00000000
    [    4.345766] SABRE: Shared PCI config space at 000001fe01000000
    [    4.348672] SABRE: DVMA at 60000000 [20000000]
    [    4.350251] PCI quirk: region 2000-203f claimed by ali7101 ACPI
    [    4.350270] PCI quirk: region 4000-401f claimed by ali7101 SMB
    [    4.354620] PCI: Address space collision on region 6 [000001ff00080000:000001ff000bffff] of device 0000:00:05.0
    [    4.354839] PCI-IRQ: Routing bus[ 0] slot[ 5] to INO[1c]
    [    4.354976] PCI-IRQ: Routing bus[ 0] slot[ a] to INO[24]
    [    4.355087] PCI-IRQ: Routing bus[ 0] slot[ c] to INO[06]
    [    4.355198] PCI-IRQ: Routing bus[ 0] slot[ d] to INO[0c]
    [    4.355215] PCI0(PBMA): Bus running at 33MHz
    [    4.355406] isa0: [dma] [rtc -> (todm5819)] [power] [SUNW,lomh] [serial] [serial] [flashprom]
    [    4.357035] ebus: No EBus's found.
    [    4.989970] power: Control reg at 000001fe02002000 ... powerd running.
    [    4.993333] usbcore: registered new driver usbfs
    [    4.993523] usbcore: registered new driver hub
    [    4.998242] audit: initializing netlink socket (disabled)
    [    4.998284] audit(1257910373.828:1): initialized
    [    4.998495] Total HugeTLB memory allocated, 0
    [    4.999001] VFS: Disk quotas dquot_6.5.1
    [    4.999131] Dquot-cache hash table entries: 1024 (order 0, 8192 bytes)
    [    4.999509] Initializing Cryptographic API
    [    4.999532] io scheduler noop registered
    [    4.999559] io scheduler anticipatory registered
    [    4.999585] io scheduler deadline registered
    [    4.999634] io scheduler cfq registered
    [    4.999658] Activating ISA DMA hang workarounds.
    [   13.462368] Console: switching to mono PROM 80x34
    [   13.534273] Real Time Clock Driver v1.12
    [   13.534334] [drm] Initialized drm 1.0.1 20051102
    [   13.543535] ttyS0 at MMIO 0x1fe020003f8 (irq = 7616992) is a 16550A
    [   13.543805] Console: ttyS0 (SU)
    [   13.676687] ttyS1 at MMIO 0x1fe020002e8 (irq = 7616992) is a 16550A
    [   13.679103] RAMDISK driver initialized: 16 RAM disks of 65536K size 1024 blocksize
    [   13.680105] loop: loaded (max 8 devices)
    [   13.680482] Uniform Multi-Platform E-IDE driver Revision: 7.00alpha2
    [   13.680500] ide: Assuming 33MHz system bus speed for PIO modes; override with idebus=xx
    [   13.681225] usbmon: debugfs is not available
    [   13.681383] usbcore: registered new driver usbhid
    [   13.681397] drivers/usb/input/hid-core.c: v2.6:USB HID core driver
    [   13.681650] mice: PS/2 mouse device common for all mice
    [   13.682307] input: Sparc ISA Speaker as /class/input/input0
    [   13.682541] NET: Registered protocol family 2
    [   13.717633] IP route cache hash table entries: 4096 (order: 2, 32768 bytes)
    [   13.718488] TCP established hash table entries: 16384 (order: 4, 131072 bytes)
    [   13.719139] TCP bind hash table entries: 16384 (order: 4, 131072 bytes)
    [   13.719822] TCP: Hash tables configured (established 16384 bind 16384)
    [   13.719840] TCP reno registered
    [   13.720141] TCP bic registered
    [   13.720196] NET: Registered protocol family 1
    [   13.720227] NET: Registered protocol family 17
    [   13.994426] Capability LSM initialized
    [   15.600583] ALI15X3: IDE controller at PCI slot 0000:00:0d.0
    [   15.600641] ALI15X3: chipset revision 195
    [   15.600672] ALI15X3: 100% native mode on irq 5,7cc
    [   15.600704]     ide0: BM-DMA at 0x1fe02010220-0x1fe02010227, BIOS settings: hda:pio, hdb:pio
    [   15.600762]     ide1: BM-DMA at 0x1fe02010228-0x1fe0201022f, BIOS settings: hdc:pio, hdd:pio
    [   15.600810] Probing IDE interface ide0...
    [   15.889536] hda: ST340016A, ATA DISK drive
    [   16.56170
    1] ide0 at 0x1fe[02010200-0x1fe02H010207,0x1fe0201
    021a on irq 5,7c[c
    [   16.561828J] Probing IDE in
    terface ide1...
    [   16.849515] 7hdc: ST340016A, mATA DISK drive
     [    0.117640] h
    dd: CD-224E, ATA[PI CD/DVD-ROM drmive
    [    0.1736
    44] ide1 at 0x1fe02010210-0x1fe02010217,0x1fe0201020a on irq 5,7cc
    [    0.218411] hda: max request size: 128KiB
    [    0.232077] hda: 78165360 sectors (40020 MB) w/2048KiB Cache, CHS=65535/16/63, UDMA(66)
    [    0.232106] hda: cache flushes not supported
    [    0.232263]  hda: hda1 hda2 hda3 hda4
    [    0.238796] hdc: max request size: 128KiB
    [    0.239308] hdc: 78165360 sectors (40020 MB) w/2048KiB Cache, CHS=65535/16/63, UDMA(66)
    [    0.239334] hdc: cache flushes not supported
    [    0.239448]  hdc: hdc1 hdc2 hdc3 hdc4 hdc8
    [    0.287118] hdd: ATAPI 24X CD-ROM drive, 128kB Cache
    [    0.287147] Uniform CD-ROM driver Revision: 3.20
    [    0.753214] ohci_hcd: 2005 April 22 USB 1.1 'Open' Host Controller (OHCI) Driver (PCI)
    [    0.753323] ohci_hcd 0000:00:0a.0: OHCI Host Controller
    [    0.754435] ohci_hcd 0000:00:0a.0: new USB bus registered, assigned bus number 1
    [    0.754476] ohci_hcd 0000:00:0a.0: irq 14,7e4, io mem 0x1ff01000000
    [    0.773794] hub 1-0:1.0: USB hub found
    [    0.773856] hub 1-0:1.0: 2 ports detected
    [    1.005504] usb 1-1: new low speed USB device using ohci_hcd and address 2
    [    1.183425] input: USB-compliant keyboard as /class/input/input1
    [    1.183478] input: USB HID v1.10 Keyboard [USB-compliant keyboard] on usb-0000:00:0a.0-1
    [    1.214157] input: USB-compliant keyboard as /class/input/input2
    [    1.214281] input: USB HID v1.10 Mouse [USB-compliant keyboard] on usb-0000:00:0a.0-1
    [    1.313625] kjournald starting.  Commit interval 5 seconds
    [    1.313672] EXT3-fs: mounted filesystem with ordered data mode.
    [    7.489090] Linux Tulip driver version 1.1.13-NAPI (December 15, 2004)
    [    7.499670] tulip0: Old style EEPROM with no media selection information.
    [    7.499931] tulip0:  MII transceiver #1 config 1000 status 7809 advertising 01e1.
    [    7.502777] eth0: Davicom DM9102/DM9102A rev 49 at 000001fe02010100, EEPROM not present, 00:03:BA:27:86:F4, IRQ 7616512.
    [    7.513222] tulip1: Old style EEPROM with no media selection information.
    [    7.513492] tulip1:  MII transceiver #1 config 1100 status 782d advertising 01e1.
    [    7.516273] eth1: Davicom DM9102/DM9102A rev 49 at 000001fe02010000, EEPROM not present, 00:03:BA:27:86:F3, IRQ 7615808.
    [    8.611910] Adding 1510088k swap on /dev/hda4.  Priority:-1 extents:1 across:1510088k
    [    8.746139] EXT3 FS on hda2, internal journal
    [    9.208605] md: md driver 0.90.3 MAX_MD_DEVS=256, MD_SB_DISKS=27
    [    9.208625] md: bitmap version 4.39
    [   10.151402] device-mapper: 4.4.0-ioctl (2005-01-12) initialised: dm-devel@redhat.com
    [   11.392181] hdd: packet command error: status=0x51 { DriveReady SeekComplete Error }
    [   11.392207] hdd: packet command error: error=0x54 { AbortedCommand LastFailedSense=0x05 }
    [   11.392226] ide: failed opcode was: unknown
    [   11.392907] cdrom: open failed.
    [   11.926715] kjournald starting.  Commit interval 5 seconds
    [   11.926936] EXT3 FS on hda1, internal journal
    [   11.926955] EXT3-fs: mounted filesystem with ordered data mode.
    [   11.605323] hdd: packet command error: status=0x51 { DriveReady SeekComplete Error }
    [   11.605354] hdd: packet command error: error=0x54 { AbortedCommand LastFailedSense=0x05 }
    [   11.605373] ide: failed opcode was: unknown
    [   11.606761] cdrom: open failed.
    [   11.700819] hdd: packet command error: status=0x51 { DriveReady SeekComplete Error }
    [   11.700849] hdd: packet command error: error=0x54 { AbortedCommand LastFailedSense=0x05 }
    [   11.700867] ide: failed opcode was: unknown
    [   11.702259] cdrom: open failed.
    [    6.437080] NETDEV WATCHDOG: eth0: transmit timed out
    [    6.438634] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   14.437001] NETDEV WATCHDOG: eth0: transmit timed out
    [   14.438545] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    5.257056] NETDEV WATCHDOG: eth0: transmit timed out
    [    5.258604] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   13.256972] NETDEV WATCHDOG: eth0: transmit timed out
    [   13.258516] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    4.077027] NETDEV WATCHDOG: eth0: transmit timed out
    [    4.078575] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   12.076946] NETDEV WATCHDOG: eth0: transmit timed out
    [   12.078495] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    2.896998] NETDEV WATCHDOG: eth0: transmit timed out
    [    2.898543] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   10.896918] NETDEV WATCHDOG: eth0: transmit timed out
    [   10.898464] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    1.716966] NETDEV WATCHDOG: eth0: transmit timed out
    [    1.718511] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    9.716890] NETDEV WATCHDOG: eth0: transmit timed out
    [    9.718438] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    0.536943] NETDEV WATCHDOG: eth0: transmit timed out
    [    0.538493] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    8.536865] NETDEV WATCHDOG: eth0: transmit timed out
    [    8.538406] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   16.536785] NETDEV WATCHDOG: eth0: transmit timed out
    [   16.538333] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    7.356833] NETDEV WATCHDOG: eth0: transmit timed out
    [    7.358376] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   15.356758] NETDEV WATCHDOG: eth0: transmit timed out
    [   15.358307] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    6.176806] NETDEV WATCHDOG: eth0: transmit timed out
    [    6.178352] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   14.176727] NETDEV WATCHDOG: eth0: transmit timed out
    [   14.178272] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    4.996779] NETDEV WATCHDOG: eth0: transmit timed out
    [    4.998319] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   12.996699] NETDEV WATCHDOG: eth0: transmit timed out
    [   12.998242] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    3.816750] NETDEV WATCHDOG: eth0: transmit timed out
    [    3.818287] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   11.816671] NETDEV WATCHDOG: eth0: transmit timed out
    [   11.818213] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    2.636722] NETDEV WATCHDOG: eth0: transmit timed out
    [    2.638259] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   10.636643] NETDEV WATCHDOG: eth0: transmit timed out
    [   10.638184] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    1.456699] NETDEV WATCHDOG: eth0: transmit timed out
    [    1.458250] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    9.456621] NETDEV WATCHDOG: eth0: transmit timed out
    [    9.458172] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    0.276670] NETDEV WATCHDOG: eth0: transmit timed out
    [    0.278218] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    8.276590] NETDEV WATCHDOG: eth0: transmit timed out
    [    8.278133] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   16.276512] NETDEV WATCHDOG: eth0: transmit timed out
    [   16.278059] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    7.096565] NETDEV WATCHDOG: eth0: transmit timed out
    [    7.098114] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   15.096482] NETDEV WATCHDOG: eth0: transmit timed out
    [   15.098024] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    5.916533] NETDEV WATCHDOG: eth0: transmit timed out
    [    5.918075] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   13.916453] NETDEV WATCHDOG: eth0: transmit timed out
    [   13.917994] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    4.736504] NETDEV WATCHDOG: eth0: transmit timed out
    [    4.738041] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   12.736425] NETDEV WATCHDOG: eth0: transmit timed out
    [   12.737962] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    3.556477] NETDEV WATCHDOG: eth0: transmit timed out
    [    3.558017] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   11.556398] NETDEV WATCHDOG: eth0: transmit timed out
    [   11.557937] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    2.376449] NETDEV WATCHDOG: eth0: transmit timed out
    [    2.377987] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   10.376370] NETDEV WATCHDOG: eth0: transmit timed out
    [   10.377908] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    1.196423] NETDEV WATCHDOG: eth0: transmit timed out
    [    1.197965] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    9.196350] NETDEV WATCHDOG: eth0: transmit timed out
    [    9.197900] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    0.016398] NETDEV WATCHDOG: eth0: transmit timed out
    [    0.017948] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    8.016318] NETDEV WATCHDOG: eth0: transmit timed out
    [    8.017869] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   16.016237] NETDEV WATCHDOG: eth0: transmit timed out
    [   16.017779] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    6.836289] NETDEV WATCHDOG: eth0: transmit timed out
    [    6.837830] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   14.439922] eth0: Out-of-sync dirty pointer, 16 vs. 86.
    root@brol:~# 
    dmesg
    ping 192.168.42.1
    PING 192.168.42.1 (192.168.42.1) 56(84) bytes of data.
    --- 192.168.42.1 ping statistics ---
    2 packets transmitted, 0 received, 100% packet loss, time 1014ms
    root@brol:~# route -n
    Kernel IP routing table
    Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
    192.168.42.0    0.0.0.0         255.255.255.0   U     0      0        0 eth1
    10.0.0.0        0.0.0.0         255.0.0.0       U     0      0        0 eth0
    root@brol:~# route -n
    ping 192.168.42.1
    PING 192.168.42.1 (192.168.42.1) 56(84) bytes of data.
    From 192.168.42.27 icmp_seq=1 Destination Host Unreachable
    From 192.168.42.27 icmp_seq=2 Destination Host Unreachable
    From 192.168.42.27 icmp_seq=3 Destination Host Unreachable
    From 192.168.42.27 icmp_seq=5 Destination Host Unreachable
    From 192.168.42.27 icmp_seq=6 Destination Host Unreachable
    From 192.168.42.27 icmp_seq=7 Destination Host Unreachable
    From 192.168.42.27 icmp_seq=9 Destination Host Unreachable
    From 192.168.42.27 icmp_seq=10 Destination Host Unreachable
    From 192.168.42.27 icmp_seq=11 Destination Host Unreachable
    From 192.168.42.27 icmp_seq=13 Destination Host Unreachable
    From 192.168.42.27 icmp_seq=14 Destination Host Unreachable
    From 192.168.42.27 icmp_seq=15 Destination Host Unreachable
    --- 192.168.42.1 ping statistics ---
    15 packets transmitted, 0 received, +12 errors, 100% packet loss, time 14026ms
    , pipe 3
    root@brol:~# cat /proc/version 
    Linux version 2.6.15-51-sparc64 (buildd@sejong) (gcc version 4.0.3 (Ubuntu 4.0.3-1ubuntu5)) #1 Thu Dec 6 20:26:55 UTC 2007
    root@brol:~# dmesg
    [    0.000000] PROMLIB: Sun IEEE Boot Prom 'OBP 4.0.18 2002/05/23 18:22'
    [    0.000000] PROMLIB: Root node compatible: sun4u
    [    0.000000] Linux version 2.6.15-51-sparc64 (buildd@sejong) (gcc version 4.0.3 (Ubuntu 4.0.3-1ubuntu5)) #1 Thu Dec 6 20:26:55 UTC 2007
    [    0.000000] ARCH: SUN4U
    [    0.000000] Ethernet address: 00:03:ba:27:86:f3
    [    0.000000] On node 0 totalpages: 64037
    [    0.000000]   DMA zone: 64037 pages, LIFO batch:15
    [    0.000000]   DMA32 zone: 0 pages, LIFO batch:0
    [    0.000000]   Normal zone: 0 pages, LIFO batch:0
    [    0.000000]   HighMem zone: 0 pages, LIFO batch:0
    [    0.000000] CPU[0]: Caches D[sz(16384):line_sz(32)] I[sz(16384):line_sz(32)] E[sz(524288):line_sz(64)]
    [    0.000000] Built 1 zonelists
    [    0.000000] Kernel command line: root=/dev/hda2 ro quiet splash
    [    0.000000] PID hash table entries: 2048 (order: 11, 65536 bytes)
    [    2.070360] Console: colour dummy device 80x25
    [    2.073255] Dentry cache hash table entries: 65536 (order: 6, 524288 bytes)
    [    2.076518] Inode-cache hash table entries: 32768 (order: 5, 262144 bytes)
    [    2.107459] Memory: 507208k available (2352k kernel code, 712k data, 160k init) [fffff80000000000,00000000dfec8000]
    [    2.185473] Calibrating delay using timer specific routine.. 11.12 BogoMIPS (lpj=22241)
    [    2.185695] Security Framework v1.0.0 initialized
    [    2.185741] SELinux:  Disabled at boot.
    [    2.185812] Mount-cache hash table entries: 512
    [    2.186978] checking if image is initramfs... it is
    [    4.341515] Freeing initrd memory: 6485k freed
    [    4.343495] NET: Registered protocol family 16
    [    4.344929] PCI: Probing for controllers.
    [    4.345740] PCI: Found SABRE, main regs at 000001fe00000000
    [    4.345766] SABRE: Shared PCI config space at 000001fe01000000
    [    4.348672] SABRE: DVMA at 60000000 [20000000]
    [    4.350251] PCI quirk: region 2000-203f claimed by ali7101 ACPI
    [    4.350270] PCI quirk: region 4000-401f claimed by ali7101 SMB
    [    4.354620] PCI: Address space collision on region 6 [000001ff00080000:000001ff000bffff] of device 0000:00:05.0
    [    4.354839] PCI-IRQ: Routing bus[ 0] slot[ 5] to INO[1c]
    [    4.354976] PCI-IRQ: Routing bus[ 0] slot[ a] to INO[24]
    [    4.355087] PCI-IRQ: Routing bus[ 0] slot[ c] to INO[06]
    [    4.355198] PCI-IRQ: Routing bus[ 0] slot[ d] to INO[0c]
    [    4.355215] PCI0(PBMA): Bus running at 33MHz
    [    4.355406] isa0: [dma] [rtc -> (todm5819)] [power] [SUNW,lomh] [serial] [serial] [flashprom]
    [    4.357035] ebus: No EBus's found.
    [    4.989970] power: Control reg at 000001fe02002000 ... powerd running.
    [    4.993333] usbcore: registered new driver usbfs
    [    4.993523] usbcore: registered new driver hub
    [    4.998242] audit: initializing netlink socket (disabled)
    [    4.998284] audit(1257910373.828:1): initialized
    [    4.998495] Total HugeTLB memory allocated, 0
    [    4.999001] VFS: Disk quotas dquot_6.5.1
    [    4.999131] Dquot-cache hash table entries: 1024 (order 0, 8192 bytes)
    [    4.999509] Initializing Cryptographic API
    [    4.999532] io scheduler noop registered
    [    4.999559] io scheduler anticipatory registered
    [    4.999585] io scheduler deadline registered
    [    4.999634] io scheduler cfq registered
    [    4.999658] Activating ISA DMA hang workarounds.
    [   13.462368] Console: switching to mono PROM 80x34
    [   13.534273] Real Time Clock Driver v1.12
    [   13.534334] [drm] Initialized drm 1.0.1 20051102
    [   13.543535] ttyS0 at MMIO 0x1fe020003f8 (irq = 7616992) is a 16550A
    [   13.543805] Console: ttyS0 (SU)
    [   13.676687] ttyS1 at MMIO 0x1fe020002e8 (irq = 7616992) is a 16550A
    [   13.679103] RAMDISK driver initialized: 16 RAM disks of 65536K size 1024 blocksize
    [   13.680105] loop: loaded (max 8 devices)
    [   13.680482] Uniform Multi-Platform E-IDE driver Revision: 7.00alpha2
    [   13.680500] ide: Assuming 33MHz system bus speed for PIO modes; override with idebus=xx
    [   13.681225] usbmon: debugfs is not available
    [   13.681383] usbcore: registered new driver usbhid
    [   13.681397] drivers/usb/input/hid-core.c: v2.6:USB HID core driver
    [   13.681650] mice: PS/2 mouse device common for all mice
    [   13.682307] input: Sparc ISA Speaker as /class/input/input0
    [   13.682541] NET: Registered protocol family 2
    [   13.717633] IP route cache hash table entries: 4096 (order: 2, 32768 bytes)
    [   13.718488] TCP established hash table entries: 16384 (order: 4, 131072 bytes)
    [   13.719139] TCP bind hash table entries: 16384 (order: 4, 131072 bytes)
    [   13.719822] TCP: Hash tables configured (established 16384 bind 16384)
    [   13.719840] TCP reno registered
    [   13.720141] TCP bic registered
    [   13.720196] NET: Registered protocol family 1
    [   13.720227] NET: Registered protocol family 17
    [   13.994426] Capability LSM initialized
    [   15.600583] ALI15X3: IDE controller at PCI slot 0000:00:0d.0
    [   15.600641] ALI15X3: chipset revision 195
    [   15.600672] ALI15X3: 100% native mode on irq 5,7cc
    [   15.600704]     ide0: BM-DMA at 0x1fe02010220-0x1fe02010227, BIOS settings: hda:pio, hdb:pio
    [   15.600762]     ide1: BM-DMA at 0x1fe02010228-0x1fe0201022f, BIOS settings: hdc:pio, hdd:pio
    [   15.600810] Probing IDE interface ide0...
    [   15.889536] hda: ST340016A, ATA DISK drive
    [   16.561701] ide0 at 0x1fe02010200-0x1fe02010207,0x1fe0201021a on irq 5,7cc
    [   16.561828] Probing IDE interface ide1...
    [   16.849515] hdc: ST340016A, ATA DISK drive
    [    0.117640] hdd: CD-224E, ATAPI CD/DVD-ROM drive
    [    0.173644] ide1 at 0x1fe02010210-0x1fe02010217,0x1fe0201020a on irq 5,7cc
    [    0.218411] hda: max request size: 128KiB
    [    0.232077] hda: 78165360 sectors (40020 MB) w/2048KiB Cache, CHS=65535/16/63, UDMA(66)
    [    0.232106] hda: cache flushes not supported
    [    0.232263]  hda: hda1 hda2 hda3 hda4
    [    0.238796] hdc: max request size: 128KiB
    [    0.239308] hdc: 78165360 sectors (40020 MB) w/2048KiB Cache, CHS=65535/16/63, UDMA(66)
    [    0.239334] hdc: cache flushes not supported
    [    0.239448]  hdc: hdc1 hdc2 hdc3 hdc4 hdc8
    [    0.287118] hdd: ATAPI 24X CD-ROM drive, 128kB Cache
    [    0.287147] Uniform CD-ROM driver Revision: 3.20
    [    0.753214] ohci_hcd: 2005 April 22 USB 1.1 'Open' Host Controller (OHCI) Driver (PCI)
    [    0.753323] ohci_hcd 0000:00:0a.0: OHCI Host Controller
    [    0.754435] ohci_hcd 0000:00:0a.0: new USB bus registered, assigned bus number 1
    [    0.754476] ohci_hcd 0000:00:0a.0: irq 14,7e4, io mem 0x1ff01000000
    [    0.773794] hub 1-0:1.0: USB hub found
    [    0.773856] hub 1-0:1.0: 2 ports detected
    [    1.005504] usb 1-1: new low speed USB device using ohci_hcd and address 2
    [    1.183425] input: USB-compliant keyboard as /class/input/input1
    [    1.183478] input: USB HID v1.10 Keyboard [USB-compliant keyboard] on usb-0000:00:0a.0-1
    [    1.214157] input: USB-compliant keyboard as /class/input/input2
    [    1.214281] input: USB HID v1.10 Mouse [USB-compliant keyboard] on usb-0000:00:0a.0-1
    [    1.313625] kjournald starting.  Commit interval 5 seconds
    [    1.313672] EXT3-fs: mounted filesystem with ordered data mode.
    [    7.489090] Linux Tulip driver version 1.1.13-NAPI (December 15, 2004)
    [    7.499670] tulip0: Old style EEPROM with no media selection information.
    [    7.499931] tulip0:  MII transceiver #1 config 1000 status 7809 advertising 01e1.
    [    7.502777] eth0: Davicom DM9102/DM9102A rev 49 at 000001fe02010100, EEPROM not present, 00:03:BA:27:86:F4, IRQ 7616512.
    [    7.513222] tulip1: Old style EEPROM with no media selection information.
    [    7.513492] tulip1:  MII transceiver #1 config 1100 status 782d advertising 01e1.
    [    7.516273] eth1: Davicom DM9102/DM9102A rev 49 at 000001fe02010000, EEPROM not present, 00:03:BA:27:86:F3, IRQ 7615808.
    [    8.611910] Adding 1510088k swap on /dev/hda4.  Priority:-1 extents:1 across:1510088k
    [    8.746139] EXT3 FS on hda2, internal journal
    [    9.208605] md: md driver 0.90.3 MAX_MD_DEVS=256, MD_SB_DISKS=27
    [    9.208625] md: bitmap version 4.39
    [   10.151402] device-mapper: 4.4.0-ioctl (2005-01-12) initialised: dm-devel@redhat.com
    [   11.392181] hdd: packet command error: status=0x51 { DriveReady SeekComplete Error }
    [   11.392207] hdd: packet command error: error=0x54 { AbortedCommand LastFailedSense=0x05 }
    [   11.392226] ide: failed opcode was: unknown
    [   11.392907] cdrom: open failed.
    [   11.926715] kjournald starting.  Commit interval 5 seconds
    [   11.926936] EXT3 FS on hda1, internal journal
    [   11.926955] EXT3-fs: mounted filesystem with ordered data mode.
    [   11.605323] hdd: packet command error: status=0x51 { DriveReady SeekComplete Error }
    [   11.605354] hdd: packet command error: error=0x54 { AbortedCommand LastFailedSense=0x05 }
    [   11.605373] ide: failed opcode was: unknown
    [   11.606761] cdrom: open failed.
    [   11.700819] hdd: packet command error: status=0x51 { DriveReady SeekComplete Error }
    [   11.700849] hdd: packet command error: error=0x54 { AbortedCommand LastFailedSense=0x05 }
    [   11.700867] ide: failed opcode was: unknown
    [   11.702259] cdrom: open failed.
    [    6.437080] NETDEV WATCHDOG: eth0: transmit timed out
    [    6.438634] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   14.437001] NETDEV WATCHDOG: eth0: transmit timed out
    [   14.438545] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    5.257056] NETDEV WATCHDOG: eth0: transmit timed out
    [    5.258604] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   13.256972] NETDEV WATCHDOG: eth0: transmit timed out
    [   13.258516] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    4.077027] NETDEV WATCHDOG: eth0: transmit timed out
    [    4.078575] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   12.076946] NETDEV WATCHDOG: eth0: transmit timed out
    [   12.078495] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    2.896998] NETDEV WATCHDOG: eth0: transmit timed out
    [    2.898543] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   10.896918] NETDEV WATCHDOG: eth0: transmit timed out
    [   10.898464] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    1.716966] NETDEV WATCHDOG: eth0: transmit timed out
    [    1.718511] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    9.716890] NETDEV WATCHDOG: eth0: transmit timed out
    [    9.718438] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    0.536943] NETDEV WATCHDOG: eth0: transmit timed out
    [    0.538493] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    8.536865] NETDEV WATCHDOG: eth0: transmit timed out
    [    8.538406] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   16.536785] NETDEV WATCHDOG: eth0: transmit timed out
    [   16.538333] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    7.356833] NETDEV WATCHDOG: eth0: transmit timed out
    [    7.358376] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   15.356758] NETDEV WATCHDOG: eth0: transmit timed out
    [   15.358307] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    6.176806] NETDEV WATCHDOG: eth0: transmit timed out
    [    6.178352] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   14.176727] NETDEV WATCHDOG: eth0: transmit timed out
    [   14.178272] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    4.996779] NETDEV WATCHDOG: eth0: transmit timed out
    [    4.998319] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   12.996699] NETDEV WATCHDOG: eth0: transmit timed out
    [   12.998242] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    3.816750] NETDEV WATCHDOG: eth0: transmit timed out
    [    3.818287] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   11.816671] NETDEV WATCHDOG: eth0: transmit timed out
    [   11.818213] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    2.636722] NETDEV WATCHDOG: eth0: transmit timed out
    [    2.638259] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   10.636643] NETDEV WATCHDOG: eth0: transmit timed out
    [   10.638184] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    1.456699] NETDEV WATCHDOG: eth0: transmit timed out
    [    1.458250] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    9.456621] NETDEV WATCHDOG: eth0: transmit timed out
    [    9.458172] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    0.276670] NETDEV WATCHDOG: eth0: transmit timed out
    [    0.278218] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    8.276590] NETDEV WATCHDOG: eth0: transmit timed out
    [    8.278133] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   16.276512] NETDEV WATCHDOG: eth0: transmit timed out
    [   16.278059] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    7.096565] NETDEV WATCHDOG: eth0: transmit timed out
    [    7.098114] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   15.096482] NETDEV WATCHDOG: eth0: transmit timed out
    [   15.098024] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    5.916533] NETDEV WATCHDOG: eth0: transmit timed out
    [    5.918075] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   13.916453] NETDEV WATCHDOG: eth0: transmit timed out
    [   13.917994] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    4.736504] NETDEV WATCHDOG: eth0: transmit timed out
    [    4.738041] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   12.736425] NETDEV WATCHDOG: eth0: transmit timed out
    [   12.737962] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    3.556477] NETDEV WATCHDOG: eth0: transmit timed out
    [    3.558017] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   11.556398] NETDEV WATCHDOG: eth0: transmit timed out
    [   11.557937] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    2.376449] NETDEV WATCHDOG: eth0: transmit timed out
    [    2.377987] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   10.376370] NETDEV WATCHDOG: eth0: transmit timed out
    [   10.377908] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    1.196423] NETDEV WATCHDOG: eth0: transmit timed out
    [    1.197965] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    9.196350] NETDEV WATCHDOG: eth0: transmit timed out
    [    9.197900] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    0.016398] NETDEV WATCHDOG: eth0: transmit timed out
    [    0.017948] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    8.016318] NETDEV WATCHDOG: eth0: transmit timed out
    [    8.017869] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   16.016237] NETDEV WATCHDOG: eth0: transmit timed out
    [   16.017779] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    6.836289] NETDEV WATCHDOG: eth0: transmit timed out
    [    6.837830] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   14.439922] eth0: Out-of-sync dirty pointer, 16 vs. 86.
    root@brol:~# dmesg
    [    0.000000] PROMLIB: Sun IEEE Boot Prom 'OBP 4.0.18 2002/05/23 18:22'
    [    0.000000] PROMLIB: Root node compatible: sun4u
    [    0.000000] Linux version 2.6.15-51-sparc64 (buildd@sejong) (gcc version 4.0.3 (Ubuntu 4.0.3-1ubuntu5)) #1 Thu Dec 6 20:26:55 UTC 2007
    [    0.000000] ARCH: SUN4U
    [    0.000000] Ethernet address: 00:03:ba:27:86:f3
    [    0.000000] On node 0 totalpages: 64037
    [    0.000000]   DMA zone: 64037 pages, LIFO batch:15
    [    0.000000]   DMA32 zone: 0 pages, LIFO batch:0
    [    0.000000]   Normal zone: 0 pages, LIFO batch:0
    [    0.000000]   HighMem zone: 0 pages, LIFO batch:0
    [    0.000000] CPU[0]: Caches D[sz(16384):line_sz(32)] I[sz(16384):line_sz(32)] E[sz(524288):line_sz(64)]
    [    0.000000] Built 1 zonelists
    [    0.000000] Kernel command line: root=/dev/hda2 ro quiet splash
    [    0.000000] PID hash table entries: 2048 (order: 11, 65536 bytes)
    [    2.070360] Console: colour dummy device 80x25
    [    2.073255] Dentry cache hash table entries: 65536 (order: 6, 524288 bytes)
    [    2.076518] Inode-cache hash table entries: 32768 (order: 5, 262144 bytes)
    [    2.107459] Memory: 507208k available (2352k kernel code, 712k data, 160k init) [fffff80000000000,00000000dfec8000]
    [    2.185473] Calibrating delay using timer specific routine.. 11.12 BogoMIPS (lpj=22241)
    [    2.185695] Security Framework v1.0.0 initialized
    [    2.185741] SELinux:  Disabled at boot.
    [    2.185812] Mount-cache hash table entries: 512
    [    2.186978] checking if image is initramfs... it is
    [    4.341515] Freeing initrd memory: 6485k freed
    [    4.343495] NET: Registered protocol family 16
    [    4.344929] PCI: Probing for controllers.
    [    4.345740] PCI: Found SABRE, main regs at 000001fe00000000
    [    4.345766] SABRE: Shared PCI config space at 000001fe01000000
    [    4.348672] SABRE: DVMA at 60000000 [20000000]
    [    4.350251] PCI quirk: region 2000-203f claimed by ali7101 ACPI
    [    4.350270] PCI quirk: region 4000-401f claimed by ali7101 SMB
    [    4.354620] PCI: Address space collision on region 6 [000001ff00080000:000001ff000bffff] of device 0000:00:05.0
    [    4.354839] PCI-IRQ: Routing bus[ 0] slot[ 5] to INO[1c]
    [    4.354976] PCI-IRQ: Routing bus[ 0] slot[ a] to INO[24]
    [    4.355087] PCI-IRQ: Routing bus[ 0] slot[ c] to INO[06]
    [    4.355198] PCI-IRQ: Routing bus[ 0] slot[ d] to INO[0c]
    [    4.355215] PCI0(PBMA): Bus running at 33MHz
    [    4.355406] isa0: [dma] [rtc -> (todm5819)] [power] [SUNW,lomh] [serial] [serial] [flashprom]
    [    4.357035] ebus: No EBus's found.
    [    4.989970] power: Control reg at 000001fe02002000 ... powerd running.
    [    4.993333] usbcore: registered new driver usbfs
    [    4.993523] usbcore: registered new driver hub
    [    4.998242] audit: initializing netlink socket (disabled)
    [    4.998284] audit(1257910373.828:1): initialized
    [    4.998495] Total HugeTLB memory allocated, 0
    [    4.999001] VFS: Disk quotas dquot_6.5.1
    [    4.999131] Dquot-cache hash table entries: 1024 (order 0, 8192 bytes)
    [    4.999509] Initializing Cryptographic API
    [    4.999532] io scheduler noop registered
    [    4.999559] io scheduler anticipatory registered
    [    4.999585] io scheduler deadline registered
    [    4.999634] io scheduler cfq registered
    [    4.999658] Activating ISA DMA hang workarounds.
    [   13.462368] Console: switching to mono PROM 80x34
    [   13.534273] Real Time Clock Driver v1.12
    [   13.534334] [drm] Initialized drm 1.0.1 20051102
    [   13.543535] ttyS0 at MMIO 0x1fe020003f8 (irq = 7616992) is a 16550A
    [   13.543805] Console: ttyS0 (SU)
    [   13.676687] ttyS1 at MMIO 0x1fe020002e8 (irq = 7616992) is a 16550A
    [   13.679103] RAMDISK driver initialized: 16 RAM disks of 65536K size 1024 blocksize
    [   13.680105] loop: loaded (max 8 devices)
    [   13.680482] Uniform Multi-Platform E-IDE driver Revision: 7.00alpha2
    [   13.680500] ide: Assuming 33MHz system bus speed for PIO modes; override with idebus=xx
    [   13.681225] usbmon: debugfs is not available
    [   13.681383] usbcore: registered new driver usbhid
    [   13.681397] drivers/usb/input/hid-core.c: v2.6:USB HID core driver
    [   13.681650] mice: PS/2 mouse device common for all mice
    [   13.682307] input: Sparc ISA Speaker as /class/input/input0
    [   13.682541] NET: Registered protocol family 2
    [   13.717633] IP route cache hash table entries: 4096 (order: 2, 32768 bytes)
    [   13.718488] TCP established hash table entries: 16384 (order: 4, 131072 bytes)
    [   13.719139] TCP bind hash table entries: 16384 (order: 4, 131072 bytes)
    [   13.719822] TCP: Hash tables configured (established 16384 bind 16384)
    [   13.719840] TCP reno registered
    [   13.720141] TCP bic registered
    [   13.720196] NET: Registered protocol family 1
    [   13.720227] NET: Registered protocol family 17
    [   13.994426] Capability LSM initialized
    [   15.600583] ALI15X3: IDE controller at PCI slot 0000:00:0d.0
    [   15.600641] ALI15X3: chipset revision 195
    [   15.600672] ALI15X3: 100% native mode on irq 5,7cc
    [   15.600704]     ide0: BM-DMA at 0x1fe02010220-0x1fe02010227, BIOS settings: hda:pio, hdb:pio
    [   15.600762]     ide1: BM-DMA at 0x1fe02010228-0x1fe0201022f, BIOS settings: hdc:pio, hdd:pio
    [   15.600810] Probing IDE interface ide0...
    [   15.889536] hda: ST340016A, ATA DISK drive
    [   16.561701] ide0 at 0x1fe02010200-0x1fe02010207,0x1fe0201021a on irq 5,7cc
    [   16.561828] Probing IDE interface ide1...
    [   16.849515] hdc: ST340016A, ATA DISK drive
    [    0.117640] hdd: CD-224E, ATAPI CD/DVD-ROM drive
    [    0.173644] ide1 at 0x1fe02010210-0x1fe02010217,0x1fe0201020a on irq 5,7cc
    [    0.218411] hda: max request size: 128KiB
    [    0.232077] hda: 78165360 sectors (40020 MB) w/2048KiB Cache, CHS=65535/16/63, UDMA(66)
    [    0.232106] hda: cache flushes not supported
    [    0.232263]  hda: hda1 hda2 hda3 hda4
    [    0.238796] hdc: max request size: 128KiB
    [    0.239308] hdc: 78165360 sectors (40020 MB) w/2048KiB Cache, CHS=65535/16/63, UDMA(66)
    [    0.239334] hdc: cache flushes not supported
    [    0.239448]  hdc: hdc1 hdc2 hdc3 hdc4 hdc8
    [    0.287118] hdd: ATAPI 24X CD-ROM drive, 128kB Cache
    [    0.287147] Uniform CD-ROM driver Revision: 3.20
    [    0.753214] ohci_hcd: 2005 April 22 USB 1.1 'Open' Host Controller (OHCI) Driver (PCI)
    [    0.753323] ohci_hcd 0000:00:0a.0: OHCI Host Controller
    [    0.754435] ohci_hcd 0000:00:0a.0: new USB bus registered, assigned bus number 1
    [    0.754476] ohci_hcd 0000:00:0a.0: irq 14,7e4, io mem 0x1ff01000000
    [    0.773794] hub 1-0:1.0: USB hub found
    [    0.773856] hub 1-0:1.0: 2 ports detected
    [    1.005504] usb 1-1: new low speed USB device using ohci_hcd and address 2
    [    1.183425] input: USB-compliant keyboard as /class/input/input1
    [    1.183478] input: USB HID v1.10 Keyboard [USB-compliant keyboard] on usb-0000:00:0a.0-1
    [    1.214157] input: USB-compliant keyboard as /class/input/input2
    [    1.214281] input: USB HID v1.10 Mouse [USB-compliant keyboard] on usb-0000:00:0a.0-1
    [    1.313625] kjournald starting.  Commit interval 5 seconds
    [    1.313672] EXT3-fs: mounted filesystem with ordered data mode.
    [    7.489090] Linux Tulip driver version 1.1.13-NAPI (December 15, 2004)
    [    7.499670] tulip0: Old style EEPROM with no media selection information.
    [    7.499931] tulip0:  MII transceiver #1 config 1000 status 7809 advertising 01e1.
    [    7.502777] eth0: Davicom DM9102/DM9102A rev 49 at 000001fe02010100, EEPROM not present, 00:03:BA:27:86:F4, IRQ 7616512.
    [    7.513222] tulip1: Old style EEPROM with no media selection information.
    [    7.513492] tulip1:  MII transceiver #1 config 1100 status 782d advertising 01e1.
    [    7.516273] eth1: Davicom DM9102/DM9102A rev 49 at 000001fe02010000, EEPROM not present, 00:03:BA:27:86:F3, IRQ 7615808.
    [    8.611910] Adding 1510088k swap on /dev/hda4.  Priority:-1 extents:1 across:1510088k
    [    8.746139] EXT3 FS on hda2, internal journal
    [    9.208605] md: md driver 0.90.3 MAX_MD_DEVS=256, MD_SB_DISKS=27
    [    9.208625] md: bitmap version 4.39
    [   10.151402] device-mapper: 4.4.0-ioctl (2005-01-12) initialised: dm-devel@redhat.com
    [   11.392181] hdd: packet command error: status=0x51 { DriveReady SeekComplete Error }
    [   11.392207] hdd: packet command error: error=0x54 { AbortedCommand LastFailedSense=0x05 }
    [   11.392226] ide: failed opcode was: unknown
    [   11.392907] cdrom: open failed.
    [   11.926715] kjournald starting.  Commit interval 5 seconds
    [   11.926936] EXT3 FS on hda1, internal journal
    [   11.926955] EXT3-fs: mounted filesystem with ordered data mode.
    [   11.605323] hdd: packet command error: status=0x51 { DriveReady SeekComplete Error }
    [   11.605354] hdd: packet command error: error=0x54 { AbortedCommand LastFailedSense=0x05 }
    [   11.605373] ide: failed opcode was: unknown
    [   11.606761] cdrom: open failed.
    [   11.700819] hdd: packet command error: status=0x51 { DriveReady SeekComplete Error }
    [   11.700849] hdd: packet command error: error=0x54 { AbortedCommand LastFailedSense=0x05 }
    [   11.700867] ide: failed opcode was: unknown
    [   11.702259] cdrom: open failed.
    [    6.437080] NETDEV WATCHDOG: eth0: transmit timed out
    [    6.438634] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   14.437001] NETDEV WATCHDOG: eth0: transmit timed out
    [   14.438545] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    5.257056] NETDEV WATCHDOG: eth0: transmit timed out
    [    5.258604] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   13.256972] NETDEV WATCHDOG: eth0: transmit timed out
    [   13.258516] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    4.077027] NETDEV WATCHDOG: eth0: transmit timed out
    [    4.078575] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   12.076946] NETDEV WATCHDOG: eth0: transmit timed out
    [   12.078495] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    2.896998] NETDEV WATCHDOG: eth0: transmit timed out
    [    2.898543] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   10.896918] NETDEV WATCHDOG: eth0: transmit timed out
    [   10.898464] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    1.716966] NETDEV WATCHDOG: eth0: transmit timed out
    [    1.718511] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    9.716890] NETDEV WATCHDOG: eth0: transmit timed out
    [    9.718438] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    0.536943] NETDEV WATCHDOG: eth0: transmit timed out
    [    0.538493] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    8.536865] NETDEV WATCHDOG: eth0: transmit timed out
    [    8.538406] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   16.536785] NETDEV WATCHDOG: eth0: transmit timed out
    [   16.538333] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    7.356833] NETDEV WATCHDOG: eth0: transmit timed out
    [    7.358376] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   15.356758] NETDEV WATCHDOG: eth0: transmit timed out
    [   15.358307] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    6.176806] NETDEV WATCHDOG: eth0: transmit timed out
    [    6.178352] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   14.176727] NETDEV WATCHDOG: eth0: transmit timed out
    [   14.178272] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    4.996779] NETDEV WATCHDOG: eth0: transmit timed out
    [    4.998319] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   12.996699] NETDEV WATCHDOG: eth0: transmit timed out
    [   12.998242] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    3.816750] NETDEV WATCHDOG: eth0: transmit timed out
    [    3.818287] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   11.816671] NETDEV WATCHDOG: eth0: transmit timed out
    [   11.818213] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    2.636722] NETDEV WATCHDOG: eth0: transmit timed out
    [    2.638259] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   10.636643] NETDEV WATCHDOG: eth0: transmit timed out
    [   10.638184] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    1.456699] NETDEV WATCHDOG: eth0: transmit timed out
    [    1.458250] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    9.456621] NETDEV WATCHDOG: eth0: transmit timed out
    [    9.458172] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    0.276670] NETDEV WATCHDOG: eth0: transmit timed out
    [    0.278218] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    8.276590] NETDEV WATCHDOG: eth0: transmit timed out
    [    8.278133] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   16.276512] NETDEV WATCHDOG: eth0: transmit timed out
    [   16.278059] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    7.096565] NETDEV WATCHDOG: eth0: transmit timed out
    [    7.098114] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   15.096482] NETDEV WATCHDOG: eth0: transmit timed out
    [   15.098024] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    5.916533] NETDEV WATCHDOG: eth0: transmit timed out
    [    5.918075] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   13.916453] NETDEV WATCHDOG: eth0: transmit timed out
    [   13.917994] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    4.736504] NETDEV WATCHDOG: eth0: transmit timed out
    [    4.738041] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   12.736425] NETDEV WATCHDOG: eth0: transmit timed out
    [   12.737962] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    3.556477] NETDEV WATCHDOG: eth0: transmit timed out
    [    3.558017] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   11.556398] NETDEV WATCHDOG: eth0: transmit timed out
    [   11.557937] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    2.376449] NETDEV WATCHDOG: eth0: transmit timed out
    [    2.377987] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   10.376370] NETDEV WATCHDOG: eth0: transmit timed out
    [   10.377908] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    1.196423] NETDEV WATCHDOG: eth0: transmit timed out
    [    1.197965] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    9.196350] NETDEV WATCHDOG: eth0: transmit timed out
    [    9.197900] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    0.016398] NETDEV WATCHDOG: eth0: transmit timed out
    [    0.017948] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    8.016318] NETDEV WATCHDOG: eth0: transmit timed out
    [    8.017869] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   16.016237] NETDEV WATCHDOG: eth0: transmit timed out
    [   16.017779] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    6.836289] NETDEV WATCHDOG: eth0: transmit timed out
    [    6.837830] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   14.439922] eth0: Out-of-sync dirty pointer, 16 vs. 86.
    root@brol:~# lspci
    0000:00:00.0 Host bridge: Sun Microsystems Computer Corp. Ultra IIe
    0000:00:03.0 Non-VGA unclassified device: ALi Corporation M7101 Power Management Controller [PMU]
    0000:00:05.0 Ethernet controller: Davicom Semiconductor, Inc. 21x4x DEC-Tulip compatible 10/100 Ethernet (rev 31)
    0000:00:07.0 ISA bridge: ALi Corporation M1533 PCI to ISA Bridge [Aladdin IV]
    0000:00:0a.0 USB Controller: ALi Corporation USB 1.1 Controller (rev 03)
    0000:00:0c.0 Ethernet controller: Davicom Semiconductor, Inc. 21x4x DEC-Tulip compatible 10/100 Ethernet (rev 31)
    0000:00:0d.0 IDE interface: ALi Corporation M5229 IDE (rev c3)
    root@brol:~# lspi
    [Kci -v
    0000:00:00.0 Host bridge: Sun Microsystems Computer Corp. Ultra IIe
    	Flags: bus master, 66MHz, medium devsel, latency 40
    0000:00:03.0 Non-VGA unclassified device: ALi Corporation M7101 Power Management Controller [PMU]
    	Flags: medium devsel
    0000:00:05.0 Ethernet controller: Davicom Semiconductor, Inc. 21x4x DEC-Tulip compatible 10/100 Ethernet (rev 31)
    	Flags: bus master, medium devsel, latency 160, IRQ 7616512
    	I/O ports at 2010100 [size=256]
    	Memory at 000001ff00002000 (32-bit, non-prefetchable) [size=256]
    	Expansion ROM at 0000000000100000 [disabled] [size=256K]
    	Capabilities: [50] Power Management version 2
    0000:00:07.0 ISA bridge: ALi Corporation M1533 PCI to ISA Bridge [Aladdin IV]
    	Subsystem: ALi Corporation ALI M1533 Aladdin IV ISA Bridge
    	Flags: bus master, medium devsel, latency 0
    	Capabilities: [a0] Power Management version 1
    0000:00:0a.0 USB Controller: ALi Corporation USB 1.1 Controller (rev 03) (prog-if 10 [OHCI])
    	Flags: bus master, medium devsel, latency 32, IRQ 7616768
    	Memory at 000001ff01000000 (32-bit, non-prefetchable) [size=4K]
    	Capabilities: [60] Power Management version 2
    0000:00:0c.0 Ethernet controller: Davicom Semiconductor, Inc. 21x4x DEC-Tulip compatible 10/100 Ethernet (rev 31)
    	Flags: bus master, medium devsel, latency 160, IRQ 7615808
    	I/O ports at 2010000 [size=256]
    	[virtual] Memory at 000001ff00000000 (32-bit, non-prefetchable) [size=256]
    	Expansion ROM at 0000000000040000 [disabled] [size=256K]
    	Capabilities: [50] Power Management version 2
    0000:00:0d.0 IDE interface: ALi Corporation M5229 IDE (rev c3) (prog-if ff)
    	Flags: bus master, medium devsel, latency 16, IRQ 7616000
    	I/O ports at 2010200 [size=8]
    	I/O ports at 2010218 [size=4]
    	I/O ports at 2010210 [size=8]
    	I/O ports at 2010208 [size=4]
    	I/O ports at 2010220 [size=16]
    	Capabilities: [60] Power Management version 2
    root@brol:~# lspci -vv
    0000:00:00.0 Host bridge: Sun Microsystems Computer Corp. Ultra IIe
    	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr+ Stepping- SERR+ FastB2B-
    	Status: Cap- 66MHz+ UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort+ >SERR- <PERR-
    	Latency: 40
    0000:00:03.0 Non-VGA unclassified device: ALi Corporation M7101 Power Management Controller [PMU]
    	Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B-
    	Status: Cap- 66MHz- UDF- FastB2B- ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR-
    0000:00:05.0 Ethernet controller: Davicom Semiconductor, Inc. 21x4x DEC-Tulip compatible 10/100 Ethernet (rev 31)
    	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr+ Stepping- SERR+ FastB2B-
    	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR-
    	Latency: 160 (5000ns min, 10000ns max)
    	Interrupt: pin A routed to IRQ 7616512
    	Region 0: I/O ports at 2010100 [size=256]
    	Region 1: Memory at 000001ff00002000 (32-bit, non-prefetchable) [size=256]
    	Expansion ROM at 0000000000100000 [disabled] [size=256K]
    	Capabilities: [50] Power Management version 2
    		Flags: PMEClk- DSI+ D1- D2- AuxCurrent=220mA PME(D0-,D1-,D2-,D3hot+,D3cold+)
    		Status: D0 PME-Enable- DSel=0 DScale=0 PME-
    0000:00:07.0 ISA bridge: ALi Corporation M1533 PCI to ISA Bridge [Aladdin IV]
    	Subsystem: ALi Corporation ALI M1533 Aladdin IV ISA Bridge
    	Control: I/O+ Mem+ BusMaster+ SpecCycle+ MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B-
    	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR-
    	Latency: 0
    	Capabilities: [a0] Power Management version 1
    		Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0-,D1-,D2-,D3hot-,D3cold-)
    		Status: D0 PME-Enable- DSel=0 DScale=0 PME-
    0000:00:0a.0 USB Controller: ALi Corporation USB 1.1 Controller (rev 03) (prog-if 10 [OHCI])
    	Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B-
    	Status: Cap+ 66MHz- UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR-
    	Latency: 32 (20000ns max)
    	Interrupt: pin A routed to IRQ 7616768
    	Region 0: Memory at 000001ff01000000 (32-bit, non-prefetchable) [size=4K]
    	Capabilities: [60] Power Management version 2
    		Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0-,D1-,D2-,D3hot-,D3cold-)
    		Status: D0 PME-Enable- DSel=0 DScale=0 PME-
    0000:00:0c.0 Ethernet controller: Davicom Semiconductor, Inc. 21x4x DEC-Tulip compatible 10/100 Ethernet (rev 31)
    	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr+ Stepping- SERR+ FastB2B-
    	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR-
    	Latency: 160 (5000ns min, 10000ns max)
    	Interrupt: pin A routed to IRQ 7615808
    	Region 0: I/O ports at 2010000 [size=256]
    	Region 1: [virtual] Memory at 000001ff00000000 (32-bit, non-prefetchable) [size=256]
    	Expansion ROM at 0000000000040000 [disabled] [size=256K]
    	Capabilities: [50] Power Management version 2
    		Flags: PMEClk- DSI+ D1- D2- AuxCurrent=220mA PME(D0-,D1-,D2-,D3hot+,D3cold+)
    		Status: D0 PME-Enable- DSel=0 DScale=0 PME-
    0000:00:0d.0 IDE interface: ALi Corporation M5229 IDE (rev c3) (prog-if ff)
    	Control: I/O+ Mem- BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B-
    	Status: Cap+ 66MHz- UDF- FastB2B+ ParErr- DEVSEL=medium >TAbort- <TAbort- <MAbort- >SERR- <PERR-
    	Latency: 16 (500ns min, 1000ns max)
    	Interrupt: pin A routed to IRQ 7616000
    	Region 0: I/O ports at 2010200 [size=8]
    	Region 1: I/O ports at 2010218 [size=4]
    	Region 2: I/O ports at 2010210 [size=8]
    	Region 3: I/O ports at 2010208 [size=4]
    	Region 4: I/O ports at 2010220 [size=16]
    	Capabilities: [60] Power Management version 2
    		Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0-,D1-,D2-,D3hot-,D3cold-)
    		Status: D0 PME-Enable- DSel=0 DScale=0 PME-
    root@brol:~# ps a
    [Kls
    [mroot@brol:~# ifconfig
    eth0      Link encap:Ethernet  HWaddr 00:03:BA:27:86:F4  
              inet addr:10.0.0.1  Bcast:10.255.255.255  Mask:255.0.0.0
              UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
              RX packets:32 errors:0 dropped:0 overruns:0 frame:0
              TX packets:0 errors:76 dropped:0 overruns:0 carrier:32
              collisions:0 txqueuelen:1000 
              RX bytes:1920 (1.8 KiB)  TX bytes:0 (0.0 b)
              Base address:0x100 
    eth1      Link encap:Ethernet  HWaddr 00:03:BA:27:86:F3  
              inet addr:192.168.42.27  Bcast:192.168.42.255  Mask:255.255.255.0
              UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
              RX packets:0 errors:0 dropped:0 overruns:0 frame:0
              TX packets:0 errors:25 dropped:0 overruns:0 carrier:25
              collisions:0 txqueuelen:1000 
              RX bytes:0 (0.0 b)  TX bytes:0 (0.0 b)
              Interrupt:64 
    lo        Link encap:Local Loopback  
              inet addr:127.0.0.1  Mask:255.0.0.0
              UP LOOPBACK RUNNING  MTU:16436  Metric:1
              RX packets:71 errors:0 dropped:0 overruns:0 frame:0
              TX packets:71 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:0 
              RX bytes:7466 (7.2 KiB)  TX bytes:7466 (7.2 KiB)
    root@brol:~# ping udev.org
    root@brol:~# 
    [Jroot@brol:~# ls
    [mroot@brol:~# ps
      PID TTY          TIME CMD
     3147 ttyS0    00:00:00 login
     3175 ttyS0    00:00:00 bash
     3315 ttyS0    00:00:00 ps
    root@brol:~# ps aux
    USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
    root         1  1.2  0.1   1872   752 ?        S    22:32   0:11 init [2]      
    root         2  0.0  0.0      0     0 ?        SN   22:32   0:00 [ksoftirqd/0]
    root         3  0.0  0.0      0     0 ?        S<   22:32   0:00 [events/0]
    root         4  0.0  0.0      0     0 ?        S<   22:32   0:00 [khelper]
    root         5  0.0  0.0      0     0 ?        S<   22:32   0:00 [kthread]
    root        16  0.0  0.0      0     0 ?        S<   22:32   0:00 [kblockd/0]
    root        15  0.0  0.0      0     0 ?        S    22:32   0:00 [powerd]
    root        19  0.0  0.0      0     0 ?        S<   22:32   0:00 [khubd]
    root        56  0.0  0.0      0     0 ?        S    22:32   0:00 [pdflush]
    root        57  0.0  0.0      0     0 ?        S    22:32   0:00 [pdflush]
    root        59  0.0  0.0      0     0 ?        S<   22:32   0:00 [aio/0]
    root        58  0.0  0.0      0     0 ?        S    22:32   0:00 [kswapd0]
    root       646  0.0  0.0      0     0 ?        S<   22:33   0:00 [kseriod]
    root      1742  0.0  0.0      0     0 ?        S    22:33   0:00 [kjournald]
    root      1880  0.0  0.1   2952   704 ?        S<s  22:33   0:00 /sbin/udevd --d
    root      2950  0.0  0.0      0     0 ?        S    22:33   0:00 [kjournald]
    syslog    3059  0.0  0.1   2376   960 ?        Ss   22:33   0:00 /sbin/syslogd -
    root      3076  0.0  0.1   2136   752 ?        Ss   22:33   0:00 /bin/dd bs 1 if
    klog      3078  0.0  0.2   2608  1368 ?        Ss   22:33   0:00 /sbin/klogd -P
    root      3103  0.0  0.0   1928   392 ?        Ss   22:33   0:00 /sbin/mdadm -F
    daemon    3116  0.0  0.1   2552   560 ?        Ss   22:33   0:00 /usr/sbin/atd
    root      3126  0.0  0.2   3032  1096 ?        Ss   22:33   0:00 /usr/sbin/cron
    root      3147  0.0  0.3   4392  1664 ttyS0    Ss   22:33   0:00 /bin/login -- 
    zoobab    3148  0.0  0.5   5448  2776 ttyS0    S    22:33   0:00 -bash
    root      3175  0.0  0.5   5176  2792 ttyS0    S    22:34   0:00 bash
    root      3316  0.0  0.2   3088  1416 ttyS0    R+   22:48   0:00 ps aux
    root@brol:~# rmmod tupi
    [Klip
    root@brol:~# rmmod tulip
    [Kdmfe
    ERROR: Module dmfe does not exist in /proc/modules
    root@brol:~# modprp
    [Krobe dmfe
    FATAL: Module dmfe not found.
    root@brol:~# modprobe dmfe
    FATAL: Module dmfe not found.
    root@brol:~# dmesg
    [    0.000000] PROMLIB: Sun IEEE Boot Prom 'OBP 4.0.18 2002/05/23 18:22'
    [    0.000000] PROMLIB: Root node compatible: sun4u
    [    0.000000] Linux version 2.6.15-51-sparc64 (buildd@sejong) (gcc version 4.0.3 (Ubuntu 4.0.3-1ubuntu5)) #1 Thu Dec 6 20:26:55 UTC 2007
    [    0.000000] ARCH: SUN4U
    [    0.000000] Ethernet address: 00:03:ba:27:86:f3
    [    0.000000] On node 0 totalpages: 64037
    [    0.000000]   DMA zone: 64037 pages, LIFO batch:15
    [    0.000000]   DMA32 zone: 0 pages, LIFO batch:0
    [    0.000000]   Normal zone: 0 pages, LIFO batch:0
    [    0.000000]   HighMem zone: 0 pages, LIFO batch:0
    [    0.000000] CPU[0]: Caches D[sz(16384):line_sz(32)] I[sz(16384):line_sz(32)] E[sz(524288):line_sz(64)]
    [    0.000000] Built 1 zonelists
    [    0.000000] Kernel command line: root=/dev/hda2 ro quiet splash
    [    0.000000] PID hash table entries: 2048 (order: 11, 65536 bytes)
    [    2.070360] Console: colour dummy device 80x25
    [    2.073255] Dentry cache hash table entries: 65536 (order: 6, 524288 bytes)
    [    2.076518] Inode-cache hash table entries: 32768 (order: 5, 262144 bytes)
    [    2.107459] Memory: 507208k available (2352k kernel code, 712k data, 160k init) [fffff80000000000,00000000dfec8000]
    [    2.185473] Calibrating delay using timer specific routine.. 11.12 BogoMIPS (lpj=22241)
    [    2.185695] Security Framework v1.0.0 initialized
    [    2.185741] SELinux:  Disabled at boot.
    [    2.185812] Mount-cache hash table entries: 512
    [    2.186978] checking if image is initramfs... it is
    [    4.341515] Freeing initrd memory: 6485k freed
    [    4.343495] NET: Registered protocol family 16
    [    4.344929] PCI: Probing for controllers.
    [    4.345740] PCI: Found SABRE, main regs at 000001fe00000000
    [    4.345766] SABRE: Shared PCI config space at 000001fe01000000
    [    4.348672] SABRE: DVMA at 60000000 [20000000]
    [    4.350251] PCI quirk: region 2000-203f claimed by ali7101 ACPI
    [    4.350270] PCI quirk: region 4000-401f claimed by ali7101 SMB
    [    4.354620] PCI: Address space collision on region 6 [000001ff00080000:000001ff000bffff] of device 0000:00:05.0
    [    4.354839] PCI-IRQ: Routing bus[ 0] slot[ 5] to INO[1c]
    [    4.354976] PCI-IRQ: Routing bus[ 0] slot[ a] to INO[24]
    [    4.355087] PCI-IRQ: Routing bus[ 0] slot[ c] to INO[06]
    [    4.355198] PCI-IRQ: Routing bus[ 0] slot[ d] to INO[0c]
    [    4.355215] PCI0(PBMA): Bus running at 33MHz
    [    4.355406] isa0: [dma] [rtc -> (todm5819)] [power] [SUNW,lomh] [serial] [serial] [flashprom]
    [    4.357035] ebus: No EBus's found.
    [    4.989970] power: Control reg at 000001fe02002000 ... powerd running.
    [    4.993333] usbcore: registered new driver usbfs
    [    4.993523] usbcore: registered new driver hub
    [    4.998242] audit: initializing netlink socket (disabled)
    [    4.998284] audit(1257910373.828:1): initialized
    [    4.998495] Total HugeTLB memory allocated, 0
    [    4.999001] VFS: Disk quotas dquot_6.5.1
    [    4.999131] Dquot-cache hash table entries: 1024 (order 0, 8192 bytes)
    [    4.999509] Initializing Cryptographic API
    [    4.999532] io scheduler noop registered
    [    4.999559] io scheduler anticipatory registered
    [    4.999585] io scheduler deadline registered
    [    4.999634] io scheduler cfq registered
    [    4.999658] Activating ISA DMA hang workarounds.
    [   13.462368] Console: switching to mono PROM 80x34
    [   13.534273] Real Time Clock Driver v1.12
    [   13.534334] [drm] Initialized drm 1.0.1 20051102
    [   13.543535] ttyS0 at MMIO 0x1fe020003f8 (irq = 7616992) is a 16550A
    [   13.543805] Console: ttyS0 (SU)
    [   13.676687] ttyS1 at MMIO 0x1fe020002e8 (irq = 7616992) is a 16550A
    [   13.679103] RAMDISK driver initialized: 16 RAM disks of 65536K size 1024 blocksize
    [   13.680105] loop: loaded (max 8 devices)
    [   13.680482] Uniform Multi-Platform E-IDE driver Revision: 7.00alpha2
    [   13.680500] ide: Assuming 33MHz system bus speed for PIO modes; override with idebus=xx
    [   13.681225] usbmon: debugfs is not available
    [   13.681383] usbcore: registered new driver usbhid
    [   13.681397] drivers/usb/input/hid-core.c: v2.6:USB HID core driver
    [   13.681650] mice: PS/2 mouse device common for all mice
    [   13.682307] input: Sparc ISA Speaker as /class/input/input0
    [   13.682541] NET: Registered protocol family 2
    [   13.717633] IP route cache hash table entries: 4096 (order: 2, 32768 bytes)
    [   13.718488] TCP established hash table entries: 16384 (order: 4, 131072 bytes)
    [   13.719139] TCP bind hash table entries: 16384 (order: 4, 131072 bytes)
    [   13.719822] TCP: Hash tables configured (established 16384 bind 16384)
    [   13.719840] TCP reno registered
    [   13.720141] TCP bic registered
    [   13.720196] NET: Registered protocol family 1
    [   13.720227] NET: Registered protocol family 17
    [   13.994426] Capability LSM initialized
    [   15.600583] ALI15X3: IDE controller at PCI slot 0000:00:0d.0
    [   15.600641] ALI15X3: chipset revision 195
    [   15.600672] ALI15X3: 100% native mode on irq 5,7cc
    [   15.600704]     ide0: BM-DMA at 0x1fe02010220-0x1fe02010227, BIOS settings: hda:pio, hdb:pio
    [   15.600762]     ide1: BM-DMA at 0x1fe02010228-0x1fe0201022f, BIOS settings: hdc:pio, hdd:pio
    [   15.600810] Probing IDE interface ide0...
    [   15.889536] hda: ST340016A, ATA DISK drive
    [   16.561701] ide0 at 0x1fe02010200-0x1fe02010207,0x1fe0201021a on irq 5,7cc
    [   16.561828] Probing IDE interface ide1...
    [   16.849515] hdc: ST340016A, ATA DISK drive
    [    0.117640] hdd: CD-224E, ATAPI CD/DVD-ROM drive
    [    0.173644] ide1 at 0x1fe02010210-0x1fe02010217,0x1fe0201020a on irq 5,7cc
    [    0.218411] hda: max request size: 128KiB
    [    0.232077] hda: 78165360 sectors (40020 MB) w/2048KiB Cache, CHS=65535/16/63, UDMA(66)
    [    0.232106] hda: cache flushes not supported
    [    0.232263]  hda: hda1 hda2 hda3 hda4
    [    0.238796] hdc: max request size: 128KiB
    [    0.239308] hdc: 78165360 sectors (40020 MB) w/2048KiB Cache, CHS=65535/16/63, UDMA(66)
    [    0.239334] hdc: cache flushes not supported
    [    0.239448]  hdc: hdc1 hdc2 hdc3 hdc4 hdc8
    [    0.287118] hdd: ATAPI 24X CD-ROM drive, 128kB Cache
    [    0.287147] Uniform CD-ROM driver Revision: 3.20
    [    0.753214] ohci_hcd: 2005 April 22 USB 1.1 'Open' Host Controller (OHCI) Driver (PCI)
    [    0.753323] ohci_hcd 0000:00:0a.0: OHCI Host Controller
    [    0.754435] ohci_hcd 0000:00:0a.0: new USB bus registered, assigned bus number 1
    [    0.754476] ohci_hcd 0000:00:0a.0: irq 14,7e4, io mem 0x1ff01000000
    [    0.773794] hub 1-0:1.0: USB hub found
    [    0.773856] hub 1-0:1.0: 2 ports detected
    [    1.005504] usb 1-1: new low speed USB device using ohci_hcd and address 2
    [    1.183425] input: USB-compliant keyboard as /class/input/input1
    [    1.183478] input: USB HID v1.10 Keyboard [USB-compliant keyboard] on usb-0000:00:0a.0-1
    [    1.214157] input: USB-compliant keyboard as /class/input/input2
    [    1.214281] input: USB HID v1.10 Mouse [USB-compliant keyboard] on usb-0000:00:0a.0-1
    [    1.313625] kjournald starting.  Commit interval 5 seconds
    [    1.313672] EXT3-fs: mounted filesystem with ordered data mode.
    [    7.489090] Linux Tulip driver version 1.1.13-NAPI (December 15, 2004)
    [    7.499670] tulip0: Old style EEPROM with no media selection information.
    [    7.499931] tulip0:  MII transceiver #1 config 1000 status 7809 advertising 01e1.
    [    7.502777] eth0: Davicom DM9102/DM9102A rev 49 at 000001fe02010100, EEPROM not present, 00:03:BA:27:86:F4, IRQ 7616512.
    [    7.513222] tulip1: Old style EEPROM with no media selection information.
    [    7.513492] tulip1:  MII transceiver #1 config 1100 status 782d advertising 01e1.
    [    7.516273] eth1: Davicom DM9102/DM9102A rev 49 at 000001fe02010000, EEPROM not present, 00:03:BA:27:86:F3, IRQ 7615808.
    [    8.611910] Adding 1510088k swap on /dev/hda4.  Priority:-1 extents:1 across:1510088k
    [    8.746139] EXT3 FS on hda2, internal journal
    [    9.208605] md: md driver 0.90.3 MAX_MD_DEVS=256, MD_SB_DISKS=27
    [    9.208625] md: bitmap version 4.39
    [   10.151402] device-mapper: 4.4.0-ioctl (2005-01-12) initialised: dm-devel@redhat.com
    [   11.392181] hdd: packet command error: status=0x51 { DriveReady SeekComplete Error }
    [   11.392207] hdd: packet command error: error=0x54 { AbortedCommand LastFailedSense=0x05 }
    [   11.392226] ide: failed opcode was: unknown
    [   11.392907] cdrom: open failed.
    [   11.926715] kjournald starting.  Commit interval 5 seconds
    [   11.926936] EXT3 FS on hda1, internal journal
    [   11.926955] EXT3-fs: mounted filesystem with ordered data mode.
    [   11.605323] hdd: packet command error: status=0x51 { DriveReady SeekComplete Error }
    [   11.605354] hdd: packet command error: error=0x54 { AbortedCommand LastFailedSense=0x05 }
    [   11.605373] ide: failed opcode was: unknown
    [   11.606761] cdrom: open failed.
    [   11.700819] hdd: packet command error: status=0x51 { DriveReady SeekComplete Error }
    [   11.700849] hdd: packet command error: error=0x54 { AbortedCommand LastFailedSense=0x05 }
    [   11.700867] ide: failed opcode was: unknown
    [   11.702259] cdrom: open failed.
    [    6.437080] NETDEV WATCHDOG: eth0: transmit timed out
    [    6.438634] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   14.437001] NETDEV WATCHDOG: eth0: transmit timed out
    [   14.438545] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    5.257056] NETDEV WATCHDOG: eth0: transmit timed out
    [    5.258604] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   13.256972] NETDEV WATCHDOG: eth0: transmit timed out
    [   13.258516] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    4.077027] NETDEV WATCHDOG: eth0: transmit timed out
    [    4.078575] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   12.076946] NETDEV WATCHDOG: eth0: transmit timed out
    [   12.078495] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    2.896998] NETDEV WATCHDOG: eth0: transmit timed out
    [    2.898543] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   10.896918] NETDEV WATCHDOG: eth0: transmit timed out
    [   10.898464] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    1.716966] NETDEV WATCHDOG: eth0: transmit timed out
    [    1.718511] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    9.716890] NETDEV WATCHDOG: eth0: transmit timed out
    [    9.718438] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    0.536943] NETDEV WATCHDOG: eth0: transmit timed out
    [    0.538493] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    8.536865] NETDEV WATCHDOG: eth0: transmit timed out
    [    8.538406] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   16.536785] NETDEV WATCHDOG: eth0: transmit timed out
    [   16.538333] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    7.356833] NETDEV WATCHDOG: eth0: transmit timed out
    [    7.358376] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   15.356758] NETDEV WATCHDOG: eth0: transmit timed out
    [   15.358307] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    6.176806] NETDEV WATCHDOG: eth0: transmit timed out
    [    6.178352] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   14.176727] NETDEV WATCHDOG: eth0: transmit timed out
    [   14.178272] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    4.996779] NETDEV WATCHDOG: eth0: transmit timed out
    [    4.998319] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   12.996699] NETDEV WATCHDOG: eth0: transmit timed out
    [   12.998242] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    3.816750] NETDEV WATCHDOG: eth0: transmit timed out
    [    3.818287] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   11.816671] NETDEV WATCHDOG: eth0: transmit timed out
    [   11.818213] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    2.636722] NETDEV WATCHDOG: eth0: transmit timed out
    [    2.638259] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   10.636643] NETDEV WATCHDOG: eth0: transmit timed out
    [   10.638184] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    1.456699] NETDEV WATCHDOG: eth0: transmit timed out
    [    1.458250] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    9.456621] NETDEV WATCHDOG: eth0: transmit timed out
    [    9.458172] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    0.276670] NETDEV WATCHDOG: eth0: transmit timed out
    [    0.278218] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    8.276590] NETDEV WATCHDOG: eth0: transmit timed out
    [    8.278133] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   16.276512] NETDEV WATCHDOG: eth0: transmit timed out
    [   16.278059] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    7.096565] NETDEV WATCHDOG: eth0: transmit timed out
    [    7.098114] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   15.096482] NETDEV WATCHDOG: eth0: transmit timed out
    [   15.098024] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    5.916533] NETDEV WATCHDOG: eth0: transmit timed out
    [    5.918075] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   13.916453] NETDEV WATCHDOG: eth0: transmit timed out
    [   13.917994] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    4.736504] NETDEV WATCHDOG: eth0: transmit timed out
    [    4.738041] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   12.736425] NETDEV WATCHDOG: eth0: transmit timed out
    [   12.737962] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    3.556477] NETDEV WATCHDOG: eth0: transmit timed out
    [    3.558017] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   11.556398] NETDEV WATCHDOG: eth0: transmit timed out
    [   11.557937] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    2.376449] NETDEV WATCHDOG: eth0: transmit timed out
    [    2.377987] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   10.376370] NETDEV WATCHDOG: eth0: transmit timed out
    [   10.377908] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    1.196423] NETDEV WATCHDOG: eth0: transmit timed out
    [    1.197965] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    9.196350] NETDEV WATCHDOG: eth0: transmit timed out
    [    9.197900] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    0.016398] NETDEV WATCHDOG: eth0: transmit timed out
    [    0.017948] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    8.016318] NETDEV WATCHDOG: eth0: transmit timed out
    [    8.017869] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   16.016237] NETDEV WATCHDOG: eth0: transmit timed out
    [   16.017779] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    6.836289] NETDEV WATCHDOG: eth0: transmit timed out
    [    6.837830] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   14.439922] eth0: Out-of-sync dirty pointer, 16 vs. 86.
    [   12.014181] 0000:00:0c.0: tulip_stop_rxtx() failed (CSR5 0xfc040002 CSR6 0x20e0000)
    root@brol:~# dmesg
    modprobe dmfe
    lsmod
    Module                  Size  Used by
    isofs                  32904  0 
    udf                   116168  0 
    dm_mod                 61584  0 
    md_mod                 79912  0 
    evdev                  15040  0 
    ext3                  154768  2 
    jbd                    60968  1 ext3
    ide_generic             1792  0 
    ohci_hcd               20548  0 
    ide_cd                 36360  0 
    cdrom                  43048  1 ide_cd
    ide_disk               18752  4 
    generic                 6276  0 
    alim15x3               13728  0 [permanent]
    capability              6088  0 
    commoncap               8768  1 capability
    root@brol:~# ls
    [mroot@brol:~# ifconjf
    cd /li
    root@brol:/lib# ls
    [01;34mdhcp3-client
    [0m                          
    [01;36mlibnsl.so.1
    [01;34mevms
    [0m                                  
    [0mlibnss_compat-2.3.6.so
    [01;34mfirmware
    [0m                              
    [01;36mlibnss_compat.so.2
    [01;34minit
    [0m                                  
    [0mlibnss_dns-2.3.6.so
    [01;34miptables
    [0m                              
    [01;36mlibnss_dns.so.2
    [01;32mklibc-J989uCjNG9NlBocFqA2e0KZLqTs.so
    [0m  
    [0mlibnss_files-2.3.6.so
    [01;32mld-2.3.6.so
    [0m                           
    [01;36mlibnss_files.so.2
    [01;36mld-linux.so.2
    [0m                         
    [0mlibnss_hesiod-2.3.6.so
    [01;36mlibacl.so.1
    [0m                           
    [01;36mlibnss_hesiod.so.2
    [0mlibacl.so.1.1.0
    [0m                       
    [0mlibnss_nis-2.3.6.so
    [0mlibanl-2.3.6.so
    [0m                       
    [0mlibnss_nisplus-2.3.6.so
    [01;36mlibanl.so.1
    [0m                           
    [01;36mlibnss_nisplus.so.2
    [01;36mlibatm.so.1
    [0m                           
    [01;36mlibnss_nis.so.2
    [0mlibatm.so.1.0.0
    [0m                       
    [01;36mlibpamc.so.0
    [01;36mlibattr.so.1
    [0m                          
    [0mlibpamc.so.0.79
    [0mlibattr.so.1.1.0
    [0m                      
    [01;36mlibpam_misc.so.0
    [01;36mlibblkid.so.1
    [0m                         
    [0mlibpam_misc.so.0.79
    [0mlibblkid.so.1.0
    [0m                       
    [01;36mlibpam.so.0
    [0mlibBrokenLocale-2.3.6.so
    [0m              
    [0mlibpam.so.0.79
    [01;36mlibBrokenLocale.so.1
    [0m                  
    [01;36mlibparted-1.6.so.13
    [01;36mlibbz2.so.1
    [0m                           
    [0mlibparted-1.6.so.13.11.1
    [01;36mlibbz2.so.1.0
    [0m                         
    [0mlibpcprofile.so
    [0mlibbz2.so.1.0.3
    [0m                       
    [01;36mlibpopt.so.0
    [01;32mlibc-2.3.6.so
    [0m                         
    [0mlibpopt.so.0.0.0
    [01;36mlibcap.so.1
    [0m                           
    [0mlibproc-3.2.6.so
    [0mlibcap.so.1.10
    [0m                        
    [0mlibpthread-2.3.6.so
    [01;36mlibcfont.so.0
    [0m                         
    [01;36mlibpthread.so.0
    [0mlibcfont.so.0.0.0
    [0m                     
    [01;36mlibreadline.so.5
    [0mlibcidn-2.3.6.so
    [0m                      
    [0mlibreadline.so.5.1
    [01;36mlibcidn.so.1
    [0m                          
    [0mlibresolv-2.3.6.so
    [01;36mlibcom_err.so.2
    [0m                       
    [01;36mlibresolv.so.2
    [0mlibcom_err.so.2.1
    [0m                     
    [0mlibrt-2.3.6.so
    [01;36mlibconsole.so.0
    [0m                       
    [01;36mlibrt.so.1
    [0mlibconsole.so.0.0.0
    [0m                   
    [0mlibSegFault.so
    [0mlibcrypt-2.3.6.so
    [0m                     
    [0mlibselinux.so.1
    [01;36mlibcrypt.so.1
    [0m                         
    [0mlibsepol.so.1
    [01;36mlibc.so.6
    [0m                             
    [01;36mlibslang.so.2
    [01;36mlibctutils.so.0
    [0m                       
    [0mlibslang.so.2.0.5
    [0mlibctutils.so.0.0.0
    [0m                   
    [01;36mlibss.so.2
    [0mlibdevmapper.so.1.02
    [0m                  
    [0mlibss.so.2.0
    [0mlibdl-2.3.6.so
    [0m                        
    [01;36mlibsysfs.so.2
    [01;36mlibdl.so.2
    [0m                            
    [0mlibsysfs.so.2.0.0
    [01;36mlibe2p.so.2
    [0m                           
    [0mlibthread_db-1.0.so
    [0mlibe2p.so.2.3
    [0m                         
    [01;36mlibthread_db.so.1
    [01;36mlibevms-2.5.so.0
    [0m                      
    [01;36mlibusb-0.1.so.4
    [0mlibevms-2.5.so.0.4
    [0m                    
    [0mlibusb-
    root@brol:/lib# cd modules/
    root@brol:/lib/modules# ls
    [01;34m2.6.15-51-sparc64
    [mroot@brol:/lib/modules# cd 2.6.15-51-sparc64/
    root@brol:/lib/modules/2.6.15-51-sparc64# ls
    [01;34minitrd
    [0m          
    [0mmodules.dep
    [0m          
    [0mmodules.ofmap
    [0m     
    [0mmodules.usbmap
    [01;34mkernel
    [0m          
    [0mmodules.ieee1394map
    [0m  
    [0mmodules.pcimap
    [0m    
    [01;34mupdates
    [0mmodules.alias
    [0m   
    [0mmodules.inputmap
    [0m     
    [0mmodules.seriomap
    [0mmodules.ccwmap
    [0m  
    [0mmodules.isapnpmap
    [0m    
    [0mmodules.symbols
    [mroot@brol:/lib/modules/2.6.15-51-sparc64# cd kernel/
    root@brol:/lib/modules/2.6.15-51-sparc64/kernel# ls
    [01;34march
    [0m  
    [01;34mcluster
    [0m  
    [01;34mcrypto
    [0m  
    [01;34mdrivers
    [0m  
    [01;34mfs
    [0m  
    [01;34mlib
    [0m  
    [01;34mnet
    [0m  
    [01;34msecurity
    [0m  
    [01;34msound
    [mroot@brol:/lib/modules/2.6.15-51-sparc64/kernel# date
    Tue Nov 10 22:50:54 EST 2009
    root@brol:/lib/modules/2.6.15-51-sparc64/kernel# ls
    [01;34march
    [0m  
    [01;34mcluster
    [0m  
    [01;34mcrypto
    [0m  
    [01;34mdrivers
    [0m  
    [01;34mfs
    [0m  
    [01;34mlib
    [0m  
    [01;34mnet
    [0m  
    [01;34msecurity
    [0m  
    [01;34msound
    [mroot@brol:/lib/modules/2.6.15-51-sparc64/kernel# ls
    [01;34march
    [0m  
    [01;34mcluster
    [0m  
    [01;34mcrypto
    [0m  
    [01;34mdrivers
    [0m  
    [01;34mfs
    [0m  
    [01;34mlib
    [0m  
    [01;34mnet
    [0m  
    [01;34msecurity
    [0m  
    [01;34msound
    [mroot@brol:/lib/modules/2.6.15-51-sparc64/kernel# cd 
    [Kcd net/
    root@brol:/lib/modules/2.6.15-51-sparc64/kernel/net# ls
    [01;34m802
    [0m    
    [01;34mappletalk
    [0m  
    [01;34mdccp
    [0m    
    [01;34mieee80211
    [0m         
    [01;34mipv4
    [0m  
    [01;34mipx
    [0m  
    [01;34mllc
    [0m        
    [01;34mrxrpc
    [0m  
    [01;34msunrpc
    [01;34m8021q
    [0m  
    [01;34mbridge
    [0m     
    [01;34mdecnet
    [0m  
    [01;34mieee80211_1_1_13
    [0m  
    [01;34mipv6
    [0m  
    [01;34mkey
    [0m  
    [01;34mnetfilter
    [0m  
    [01;34msched
    [0m  
    [01;34mxfrm
    [mroot@brol:/lib/modules/2.6.15-51-sparc64/kernel/net# cd ..
    root@brol:/lib/modules/2.6.15-51-sparc64/kernel# ls
    [01;34march
    [0m  
    [01;34mcluster
    [0m  
    [01;34mcrypto
    [0m  
    [01;34mdrivers
    [0m  
    [01;34mfs
    [0m  
    [01;34mlib
    [0m  
    [01;34mnet
    [0m  
    [01;34msecurity
    [0m  
    [01;34msound
    [mroot@brol:/lib/modules/2.6.15-51-sparc64/kernel# cd ..
    root@brol:/lib/modules/2.6.15-51-sparc64# ls
    [01;34minitrd
    [0m          
    [0mmodules.dep
    [0m          
    [0mmodules.ofmap
    [0m     
    [0mmodules.usbmap
    [01;34mkernel
    [0m          
    [0mmodules.ieee1394map
    [0m  
    [0mmodules.pcimap
    [0m    
    [01;34mupdates
    [0mmodules.alias
    [0m   
    [0mmodules.inputmap
    [0m     
    [0mmodules.seriomap
    [0mmodules.ccwmap
    [0m  
    [0mmodules.isapnpmap
    [0m    
    [0mmodules.symbols
    [mroot@brol:/lib/modules/2.6.15-51-sparc64# find ./
    ./modules.pcimap
    ./kernel
    ./kernel/security
    ./kernel/security/capability.ko
    ./kernel/security/commoncap.ko
    ./kernel/security/realcap.ko
    ./kernel/security/root_plug.ko
    ./kernel/security/seclvl.ko
    ./kernel/arch
    ./kernel/arch/sparc64
    ./kernel/arch/sparc64/solaris
    ./kernel/arch/sparc64/solaris/solaris.ko
    ./kernel/cluster
    ./kernel/cluster/cman
    ./kernel/cluster/cman/cman.ko
    ./kernel/cluster/dlm
    ./kernel/cluster/dlm/dlm.ko
    ./kernel/crypto
    ./kernel/crypto/anubis.ko
    ./kernel/crypto/aes.ko
    ./kernel/crypto/blowfish.ko
    ./kernel/crypto/arc4.ko
    ./kernel/crypto/crypto_null.ko
    ./kernel/crypto/cast5.ko
    ./kernel/crypto/cast6.ko
    ./kernel/crypto/crc32c.ko
    ./kernel/crypto/michael_mic.ko
    ./kernel/crypto/deflate.ko
    ./kernel/crypto/khazad.ko
    ./kernel/crypto/md4.ko
    ./kernel/crypto/serpent.ko
    ./kernel/crypto/sha1.ko
    ./kernel/crypto/sha256.ko
    ./kernel/crypto/sha512.ko
    ./kernel/crypto/tea.ko
    ./kernel/crypto/tgr192.ko
    ./kernel/crypto/twofish.ko
    ./kernel/crypto/wp512.ko
    ./kernel/drivers
    ./kernel/drivers/connector
    ./kernel/drivers/connector/cn.ko
    ./kernel/drivers/block
    ./kernel/drivers/block/cloop.ko
    ./kernel/drivers/block/aoe
    ./kernel/drivers/block/aoe/aoe.ko
    ./kernel/drivers/block/pktcdvd.ko
    ./kernel/drivers/block/gnbd.ko
    ./kernel/drivers/block/nbd.ko
    ./kernel/drivers/block/sx8.ko
    ./kernel/drivers/cdrom
    ./kernel/drivers/cdrom/cdrom.ko
    ./kernel/drivers/char
    ./kernel/drivers/char/generic_serial.ko
    ./kernel/drivers/char/applicom.ko
    ./kernel/drivers/char/cyclades.ko
    ./kernel/drivers/char/drm
    ./kernel/drivers/char/drm/radeon.ko
    ./kernel/drivers/char/drm/mga.ko
    ./kernel/drivers/char/drm/r128.ko
    ./kernel/drivers/char/drm/savage.ko
    ./kernel/drivers/char/drm/tdfx.ko
    ./kernel/drivers/char/drm/via.ko
    ./kernel/drivers/char/dtlk.ko
    ./kernel/drivers/char/ecc.ko
    ./kernel/drivers/char/epca.ko
    ./kernel/drivers/char/ip2main.ko
    ./kernel/drivers/char/ip2.ko
    ./kernel/drivers/char/istallion.ko
    ./kernel/drivers/char/ipmi
    ./kernel/drivers/char/ipmi/ipmi_msghandler.ko
    ./kernel/drivers/char/ipmi/ipmi_devintf.ko
    ./kernel/drivers/char/ipmi/ipmi_watchdog.ko
    ./kernel/drivers/char/ipmi/ipmi_
    root@brol:/lib/modules/2.6.15-51-sparc64# find ./ | grep dmfe
    root@brol:/lib/modules/2.6.15-51-sparc64# find ./ | grep dmfe
    [Ktulip
    ./kernel/drivers/net/tulip
    ./kernel/drivers/net/tulip/winbond-840.ko
    ./kernel/drivers/net/tulip/tulip.ko
    ./kernel/drivers/net/tulip/uli526x.ko
    root@brol:/lib/modules/2.6.15-51-sparc64# cd kernel/drivers/net/
    root@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net# cd tulip/
    root@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# ls
    [0mtulip.ko
    [0m  
    [0muli526x.ko
    [0m  
    [0mwinbond-840.ko
    [mroot@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# modprobe tuli 
    root@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# i
    lsmod
    Module                  Size  Used by
    tulip                  56840  0 
    isofs                  32904  0 
    udf                   116168  0 
    dm_mod                 61584  0 
    md_mod                 79912  0 
    evdev                  15040  0 
    ext3                  154768  2 
    jbd                    60968  1 ext3
    ide_generic             1792  0 
    ohci_hcd               20548  0 
    ide_cd                 36360  0 
    cdrom                  43048  1 ide_cd
    ide_disk               18752  4 
    generic                 6276  0 
    alim15x3               13728  0 [permanent]
    capability              6088  0 
    commoncap               8768  1 capability
    root@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# ifconfig
    eth0      Link encap:Ethernet  HWaddr 00:03:BA:27:86:F4  
              inet addr:192.168.42.26  Bcast:192.168.42.255  Mask:255.255.255.0
              UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
              RX packets:3 errors:0 dropped:1 overruns:0 frame:128
              TX packets:0 errors:4 dropped:0 overruns:0 carrier:4
              collisions:0 txqueuelen:1000 
              RX bytes:255 (255.0 b)  TX bytes:0 (0.0 b)
              Base address:0x100 
    lo        Link encap:Local Loopback  
              inet addr:127.0.0.1  Mask:255.0.0.0
              UP LOOPBACK RUNNING  MTU:16436  Metric:1
              RX packets:72 errors:0 dropped:0 overruns:0 frame:0
              TX packets:72 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:0 
              RX bytes:7548 (7.3 KiB)  TX bytes:7548 (7.3 KiB)
    root@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# ping 1301.0
    [K.104. 
    PING 130.104.1.1 (130.104.1.1) 56(84) bytes of data.
    64 bytes from 130.104.1.1: icmp_seq=1 ttl=243 time=13.1 ms
    64 bytes from 130.104.1.1: icmp_seq=2 ttl=243 time=12.7 ms
    64 bytes from 130.104.1.1: icmp_seq=3 ttl=243 time=12.6 ms
    --- 130.104.1.1 ping statistics ---
    3 packets transmitted, 3 received, 0% packet loss, time 2006ms
    rtt min/avg/max/mdev = 12.679/12.876/13.179/0.217 ms
    root@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# apt-get updat 
    0% [Working][   17.027887] Unable to handle kernel paging request in mna handler<1> at virtual address 00020030daa9a04c
    [   17.152796] current->{active_,}mm->context = 0000000000000f21
    [    0.048505] current->{active_,}mm->pgd = fffff800ddab4000
                
    E: Method http has died unexpectedly!
    E: Method http has died unexpectedly!
    root@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# dmesg
    rts detected
    [    1.005504] usb 1-1: new low speed USB device using ohci_hcd and address 2
    [    1.183425] input: USB-compliant keyboard as /class/input/input1
    [    1.183478] input: USB HID v1.10 Keyboard [USB-compliant keyboard] on usb-0000:00:0a.0-1
    [    1.214157] input: USB-compliant keyboard as /class/input/input2
    [    1.214281] input: USB HID v1.10 Mouse [USB-compliant keyboard] on usb-0000:00:0a.0-1
    [    1.313625] kjournald starting.  Commit interval 5 seconds
    [    1.313672] EXT3-fs: mounted filesystem with ordered data mode.
    [    7.489090] Linux Tulip driver version 1.1.13-NAPI (December 15, 2004)
    [    7.499670] tulip0: Old style EEPROM with no media selection information.
    [    7.499931] tulip0:  MII transceiver #1 config 1000 status 7809 advertising 01e1.
    [    7.502777] eth0: Davicom DM9102/DM9102A rev 49 at 000001fe02010100, EEPROM not present, 00:03:BA:27:86:F4, IRQ 7616512.
    [    7.513222] tulip1: Old style EEPROM with no media selection information.
    [    7.513492] tulip1:  MII transceiver #1 config 1100 status 782d advertising 01e1.
    [    7.516273] eth1: Davicom DM9102/DM9102A rev 49 at 000001fe02010000, EEPROM not present, 00:03:BA:27:86:F3, IRQ 7615808.
    [    8.611910] Adding 1510088k swap on /dev/hda4.  Priority:-1 extents:1 across:1510088k
    [    8.746139] EXT3 FS on hda2, internal journal
    [    9.208605] md: md driver 0.90.3 MAX_MD_DEVS=256, MD_SB_DISKS=27
    [    9.208625] md: bitmap version 4.39
    [   10.151402] device-mapper: 4.4.0-ioctl (2005-01-12) initialised: dm-devel@redhat.com
    [   11.392181] hdd: packet command error: status=0x51 { DriveReady SeekComplete Error }
    [   11.392207] hdd: packet command error: error=0x54 { AbortedCommand LastFailedSense=0x05 }
    [   11.392226] ide: failed opcode was: unknown
    [   11.392907] cdrom: open failed.
    [   11.926715] kjournald starting.  Commit interval 5 seconds
    [   11.926936] EXT3 FS on hda1, internal journal
    [   11.926955] EXT3-fs: mounted filesystem with ordered data mode.
    [   11.605323] hdd: packet command error: status=0x51 { DriveReady SeekComplete Error }
    [   11.605354] hdd: packet command error: error=0x54 { AbortedCommand LastFailedSense=0x05 }
    [   11.605373] ide: failed opcode was: unknown
    [   11.606761] cdrom: open failed.
    [   11.700819] hdd: packet command error: status=0x51 { DriveReady SeekComplete Error }
    [   11.700849] hdd: packet command error: error=0x54 { AbortedCommand LastFailedSense=0x05 }
    [   11.700867] ide: failed opcode was: unknown
    [   11.702259] cdrom: open failed.
    [    6.437080] NETDEV WATCHDOG: eth0: transmit timed out
    [    6.438634] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   14.437001] NETDEV WATCHDOG: eth0: transmit timed out
    [   14.438545] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    5.257056] NETDEV WATCHDOG: eth0: transmit timed out
    [    5.258604] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   13.256972] NETDEV WATCHDOG: eth0: transmit timed out
    [   13.258516] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    4.077027] NETDEV WATCHDOG: eth0: transmit timed out
    [    4.078575] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   12.076946] NETDEV WATCHDOG: eth0: transmit timed out
    [   12.078495] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    2.896998] NETDEV WATCHDOG: eth0: transmit timed out
    [    2.898543] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   10.896918] NETDEV WATCHDOG: eth0: transmit timed out
    [   10.898464] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    1.716966] NETDEV WATCHDOG: eth0: transmit timed out
    [    1.718511] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    9.716890] NETDEV WATCHDOG: eth0: transmit timed out
    [    9.718438] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    0.536943] NETDEV WATCHDOG: eth0: transmit timed out
    [    0.538493] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    8.536865] NETDEV WATCHDOG: eth0: transmit timed out
    [    8.538406] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   16.536785] NETDEV WATCHDOG: eth0: transmit timed out
    [   16.538333] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    7.356833] NETDEV WATCHDOG: eth0: transmit timed out
    [    7.358376] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   15.356758] NETDEV WATCHDOG: eth0: transmit timed out
    [   15.358307] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    6.176806] NETDEV WATCHDOG: eth0: transmit timed out
    [    6.178352] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   14.176727] NETDEV WATCHDOG: eth0: transmit timed out
    [   14.178272] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    4.996779] NETDEV WATCHDOG: eth0: transmit timed out
    [    4.998319] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   12.996699] NETDEV WATCHDOG: eth0: transmit timed out
    [   12.998242] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    3.816750] NETDEV WATCHDOG: eth0: transmit timed out
    [    3.818287] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   11.816671] NETDEV WATCHDOG: eth0: transmit timed out
    [   11.818213] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    2.636722] NETDEV WATCHDOG: eth0: transmit timed out
    [    2.638259] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   10.636643] NETDEV WATCHDOG: eth0: transmit timed out
    [   10.638184] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    1.456699] NETDEV WATCHDOG: eth0: transmit timed out
    [    1.458250] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    9.456621] NETDEV WATCHDOG: eth0: transmit timed out
    [    9.458172] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    0.276670] NETDEV WATCHDOG: eth0: transmit timed out
    [    0.278218] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    8.276590] NETDEV WATCHDOG: eth0: transmit timed out
    [    8.278133] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   16.276512] NETDEV WATCHDOG: eth0: transmit timed out
    [   16.278059] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    7.096565] NETDEV WATCHDOG: eth0: transmit timed out
    [    7.098114] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   15.096482] NETDEV WATCHDOG: eth0: transmit timed out
    [   15.098024] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    5.916533] NETDEV WATCHDOG: eth0: transmit timed out
    [    5.918075] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   13.916453] NETDEV WATCHDOG: eth0: transmit timed out
    [   13.917994] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    4.736504] NETDEV WATCHDOG: eth0: transmit timed out
    [    4.738041] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   12.736425] NETDEV WATCHDOG: eth0: transmit timed out
    [   12.737962] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    3.556477] NETDEV WATCHDOG: eth0: transmit timed out
    [    3.558017] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   11.556398] NETDEV WATCHDOG: eth0: transmit timed out
    [   11.557937] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    2.376449] NETDEV WATCHDOG: eth0: transmit timed out
    [    2.377987] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   10.376370] NETDEV WATCHDOG: eth0: transmit timed out
    [   10.377908] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    1.196423] NETDEV WATCHDOG: eth0: transmit timed out
    [    1.197965] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    9.196350] NETDEV WATCHDOG: eth0: transmit timed out
    [    9.197900] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    0.016398] NETDEV WATCHDOG: eth0: transmit timed out
    [    0.017948] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    8.016318] NETDEV WATCHDOG: eth0: transmit timed out
    [    8.017869] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   16.016237] NETDEV WATCHDOG: eth0: transmit timed out
    [   16.017779] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [    6.836289] NETDEV WATCHDOG: eth0: transmit timed out
    [    6.837830] 0000:00:05.0: tulip_stop_rxtx() failed (CSR5 0xfc540400 CSR6 0x20e0000)
    [   14.439922] eth0: Out-of-sync dirty pointer, 16 vs. 86.
    [   12.014181] 0000:00:0c.0: tulip_stop_rxtx() failed (CSR5 0xfc040002 CSR6 0x20e0000)
    [   10.454604] Linux Tulip driver version 1.1.13-NAPI (December 15, 2004)
    [   10.465202] tulip0: Old style EEPROM with no media selection information.
    [   10.465464] tulip0:  MII transceiver #1 config 3100 status 7829 advertising 01e1.
    [   10.468311] eth0: Davicom DM9102/DM9102A rev 49 at 000001fe02010100, EEPROM not present, 00:03:BA:27:86:F4, IRQ 7616512.
    [   10.478774] tulip1: Old style EEPROM with no media selection information.
    [   10.479034] tulip1:  MII transceiver #1 config 3100 status 7809 advertising 01e1.
    [   10.481825] eth1: Davicom DM9102/DM9102A rev 49 at 000001fe02010000, EEPROM not present, 00:03:BA:27:86:F3, IRQ 7615808.
    [   12.163375] spitfire_data_access_exception: SFSR[0000000000801009] SFAR[fffffa2786f40030], going.
    [   12.163403]               \|/ ____ \|/
    [   12.163410]               "@'/ .. \`@"
    [   12.163417]               /_| \__/ |_\
    [   12.163423]                  \__U_/
    [   12.163438] ntpdate(3388): Dax [#1]
    [   12.163455] TSTATE: 0000000011009603 TPC: 000000000047d684 TNPC: 000000000047d688 Y: 00000000    Not tainted
    [   12.163492] TPC: <put_page+0x4/0xe0>
    [   12.163513] g0: fffff800ddb1b740 g1: fffff800df5fe640 g2: fffff800df5fe640 g3: 00000000005dc8e0
    [   12.163535] g4: fffff800c0e13c00 g5: 0000000000000018 g6: fffff800ddb18000 g7: 0000000000000728
    [   12.163553] o0: 0000000000000000 o1: 0000000000000004 o2: fffff800df5fe02a o3: 0000000000000000
    [   12.163574] o4: 0000000000000080 o5: 0000000000000080 sp: fffff800ddb1aef1 ret_pc: 000000000042260c
    [   12.163604] RPC: <kernel_unaligned_trap+0x10c/0x4e0>
    [   12.163620] l0: fffff800ddb1b898 l1: 0000000000000001 l2: 0000000000000080 l3: 0000000000000001
    [   12.163641] l4: 0000000000000004 l5: 0000000000000080 l6: fffff800df5fe02a l7: 00000000f7dd6000
    [   12.163664] i0: 0003ba2786f40030 i1: 00000000c200a00c i2: fffff800c0e13c00 i3: 0000000081627e9d
    [   12.163684] i4: 0000000000000053 i5: 0000000000000000 i6: fffff800ddb1afb1 i7: 00000000005e13e8
    [   12.163709] I7: <skb_release_data+0x88/0xc0>
    [   12.163720] Caller[00000000005e13e8]: skb_release_data+0x88/0xc0
    [   12.163738] Caller[00000000005e17a4]: kfree_skbmem+0x4/0xa0
    [   12.163755] Caller[000000000062bf30]: udp_recvmsg+0x270/0x320
    [   12.163783] Caller[00000000005dcdb4]: sock_common_recvmsg+0x34/0x60
    [   12.163801] Caller[00000000005da2cc]: sock_recvmsg+0xcc/0x100
    [   12.163828] Caller[00000000005dba88]: sys_recvfrom+0x68/0xe0
    [   12.163848] Caller[0000000000406ad4]: linux_sparc_syscall32+0x34/0x40
    [   12.163877] Caller[00000000f7dbd2c8]: 0xf7dbd2c8
    [   12.163898] Instruction DUMP: c27621b8  01000000  9de3bf40 <c25e0000> 07000010  82084003  2ac04016  f05e2010  c25e0000 
    [   17.027887] Unable to handle kernel paging request in mna handler<1> at virtual address 00020030daa9a04c
    [   17.152796] current->{active_,}mm->context = 0000000000000f21
    [    0.048505] current->{active_,}mm->pgd = fffff800ddab4000
    [    0.119461]               \|/ ____ \|/
    [    0.119468]               "@'/ .. \`@"
    [    0.119475]               /_| \__/ |_\
    [    0.119481]                  \__U_/
    [    0.119495] http(3395): Oops [#2]
    [    0.119511] TSTATE: 0000000011009607 TPC: 000000000047d684 TNPC: 000000000047d688 Y: 00000000    Not tainted
    [    0.119547] TPC: <put_page+0x4/0xe0>
    [    0.119566] g0: fffff800ddb3b740 g1: fffff800de66d640 g2: fffff800de66d640 g3: 00000000005dc8e0
    [    0.119588] g4: fffff800dec92800 g5: 0000000000000018 g6: fffff800ddb38000 g7: 0000000000000728
    [    0.119606] o0: 0000000000000000 o1: 0000000000000004 o2: fffff800de66d02a o3: 0000000000000000
    [    0.119627] o4: 0000000000000080 o5: 0000000000000080 sp: fffff800ddb3aef1 ret_pc: 000000000042260c
    [    0.119658] RPC: <kernel_unaligned_trap+0x10c/0x4e0>
    [    0.119673] l0: fffff800ddb3b898 l1: 0000000000000001 l2: 0000000000000080 l3: 0000000000000001
    [    0.119694] l4: 0000000000000004 l5: 0000000000000080 l6: fffff800de66d02a l7: 00000000f7a42000
    [    0.119717] i0: 00020030daa9a04c i1: 00000000c200a00c i2: fffff800dec92800 i3: 0000000081627e9d
    [    0.119737] i4: 00000000000000b5 i5: 0000000000000000 i6: fffff800ddb3afb1 i7: 00000000005e13e8
    [    0.119760] I7: <skb_release_data+0x88/0xc0>
    [    0.119771] Caller[00000000005e13e8]: skb_release_data+0x88/0xc0
    [    0.119789] Caller[00000000005e17a4]: kfree_skbmem+0x4/0xa0
    [    0.119805] Caller[000000000062bf30]: udp_recvmsg+0x270/0x320
    [    0.119833] Caller[00000000005dcdb4]: sock_common_recvmsg+0x34/0x60
    [    0.119850] Caller[00000000005da2cc]: sock_recvmsg+0xcc/0x100
    [    0.119877] Caller[00000000005dba88]: sys_recvfrom+0x68/0xe0
    [    0.119896] Caller[0000000000406ad4]: linux_sparc_syscall32+0x34/0x40
    [    0.119925] Caller[00000000f7a292c8]: 0xf7a292c8
    [    0.119944] Instruction DUMP: c27621b8  01000000  9de3bf40 <c25e0000> 07000010  82084003  2ac04016  f05e2010  c25e0000 
    [    0.120658] spitfire_data_access_exception: SFSR[0000000000801009] SFAR[000000a82a1a0000], going.
    [    0.120676]               \|/ ____ \|/
    [    0.120683]               "@'/ .. \`@"
    [    0.120690]               /_| \__/ |_\
    [    0.120696]                  \__U_/
    [    0.120709] http(3394): Dax [#3]
    [    0.120724] TSTATE: 0000000811009607 TPC: 000000000047d684 TNPC: 000000000047d688 Y: 00000000    Not tainted
    [    0.120748] TPC: <put_page+0x4/0xe0>
    [    0.120769] g0: fffff800ddb17740 g1: fffff800de66ce40 g2: fffff800de66ce40 g3: 00000000005dc8e0
    [    0.120790] g4: fffff800dec92400 g5: 0000000000000018 g6: fffff800ddb14000 g7: 0000000000000728
    [    0.120809] o0: 0000000000000000 o1: 0000000000000004 o2: fffff800de66c82a o3: 0000000000000000
    [    0.120829] o4: 0000000000000080 o5: 0000000000000080 sp: fffff800ddb16ef1 ret_pc: 000000000042260c
    [    0.120852] RPC: <kernel_unaligned_trap+0x10c/0x4e0>
    [    0.120867] l0: fffff800ddb17898 l1: 0000000000000001 l2: 0000000000000080 l3: 0000000000000001
    [    0.120887] l4: 0000000000000004 l5: 0000000000000080 l6: fffff800de66c82a l7: 00000000f79e2000
    [    0.120910] i0: 86f4c0a82a1a0000 i1: 00000000c200a00c i2: fffff800dec92400 i3: 0000000081627e9d
    [    0.120930] i4: 0000000000000055 i5: 0000000000000000 i6: fffff800ddb16fb1 i7: 00000000005e13e8
    [    0.120950] I7: <skb_release_data+0x88/0xc0>
    [    0.120960] Caller[00000000005e13e8]: skb_release_data+0x88/0xc0
    [    0.120977] Caller[00000000005e17a4]: kfree_skbmem+0x4/0xa0
    [    0.120993] Caller[000000000062bf30]: udp_recvmsg+0x270/0x320
    [    0.121015] Caller[00000000005dcdb4]: sock_common_recvmsg+0x34/0x60
    [    0.121033] Caller[00000000005da2cc]: sock_recvmsg+0xcc/0x100
    [    0.121055] Caller[00000000005dba88]: sys_recvfrom+0x68/0xe0
    [    0.121074] Caller[0000000000406ad4]: linux_sparc_syscall32+0x34/0x40
    [    0.121098] Caller[00000000f79c92c8]: 0xf79c92c8
    [    0.121113] Instruction DUMP: c27621b8  01000000  9de3bf40 <c25e0000> 07000010  82084003  2ac04016  f05e2010  c25e0000 
    root@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# 
    [Jroot@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# ls
    [0mtulip.ko
    [0m  
    [0muli526x.ko
    [0m  
    [0mwinbond-840.ko
    [mroot@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# top
    top - 22:54:15 up 21 min,  1 user,  load average: 0.00, 0.00, 0.00
    Tasks:
      26 
    total,
       1 
    running,
      25 
    sleeping,
       0 
    stopped,
       0 
    zombie
    Cpu(s):
      0.8% 
      1.6% 
      0.0% 
     97.0% 
      0.6% 
      0.0% 
      0.0% 
    Mem: 
       514472k 
    total,
        42352k 
    used,
       472120k 
    free,
         5192k 
    buffers
    Swap:
      1510088k 
    total,
            0k 
    used,
      1510088k 
    free,
        19768k 
    cached
    [6;1H
    [7m  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND            
     3398 root      15   0  3040 1352 1080 R  2.0  0.3   0:00.01 top                
        1 root      16   0  1872  752  664 S  0.0  0.1   0:11.51 init               
        2 root      34  19     0    0    0 S  0.0  0.0   0:00.00 ksoftirqd/0        
        3 root      10  -5     0    0    0 S  0.0  0.0   0:00.24 events/0           
        4 root      10  -5     0    0    0 S  0.0  0.0   0:00.04 khelper            
        5 root      10  -5     0    0    0 S  0.0  0.0   0:00.00 kthread            
       16 root      10  -5     0    0    0 S  0.0  0.0   0:00.00 kblockd/0          
       15 root      25   0     0    0    0 S  0.0  0.0   0:00.00 powerd             
       19 root      10  -5     0    0    0 S  0.0  0.0   0:00.00 khubd              
       56 root      20   0     0    0    0 S  0.0  0.0   0:00.00 pdflush            
       57 root      15   0     0    0    0 S  0.0  0.0   0:00.00 pdflush            
       59 root      11  -5     0    0    0 S  0.0  0.0   0:00.00 aio/0              
       58 root      25   0     0    0    0 S  0.0  0.0   0:00.00 kswapd0            
      646 root      10  -5     0    0    0 S  0.0  0.0   0:00.00 kseriod            
     1742 root      15   0     0    0    0 S  0.0  0.0   0:00.00 kjournald          
     1880 root      14  -4  2952  704  448 S  0.0  0.1   0:00.32 udevd              
     2950 root      15   0     0    0    0 S  0.0  0.0   0:00.00 kjournald          
    [6;1H
    top - 22:54:18 up 21 min,  1 user,  load average: 0.00, 0.00, 0.00
    Tasks:
      26 
    total,
       1 
    running,
      25 
    sleeping,
       0 
    stopped,
       0 
    zombie
    Cpu(s):
      0.0% 
      0.3% 
      0.0% 
     99.7% 
      0.0% 
      0.0% 
      0.0% 
    Mem: 
       514472k 
    total,
        42352k 
    used,
       472120k 
    free,
         5192k 
    buffers
    Swap:
      1510088k 
    total,
            0k 
    used,
      1510088k 
    free,
        19768k 
    cached
    [6;1H
    [7m  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND            
        1 root      16   0  1872  752  664 S  0.0  0.1   0:11.51 init               
        2 root      34  19     0    0    0 S  0.0  0.0   0:00.00 ksoftirqd/0        
        3 root      10  -5     0    0    0 S  0.0  0.0   0:00.24 events/0           
        4 root      10  -5     0    0    0 S  0.0  0.0   0:00.04 khelper            
        5 root      10  -5     0    0    0 S  0.0  0.0   0:00.00 kthread            
       16 root      10  -5     0    0    0 S  0.0  0.0   0:00.00 kblockd/0          
       15 root      25   0     0    0    0 S  0.0  0.0   0:00.00 powerd             
       19 root      10  -5     0    0    0 S  0.0  0.0   0:00.00 khubd              
       56 root      20   0     0    0    0 S  0.0  0.0   0:00.00 pdflush            
       57 root      15   0     0    0    0 S  0.0  0.0   0:00.00 pdflush            
       59 root      11  -5     0    0    0 S  0.0  0.0   0:00.00 aio/0              
       58 root      25   0     0    0    0 S  0.0  0.0   0:00.00 kswapd0            
      646 root      10  -5     0    0    0 S  0.0  0.0   0:00.00 kseriod            
     1742 root      15   0     0    0    0 S  0.0  0.0   0:00.00 kjournald          
     1880 root      14  -4  2952  704  448 S  0.0  0.1   0:00.32 udevd              
     2950 root      15   0     0    0    0 S  0.0  0.0   0:00.00 kjournald          
     3059 syslog    16   0  2376  960  768 S  0.0  0.2   0:00.03 syslogd            
    [6;1H
    top - 22:54:21 up 21 min,  1 user,  load average: 0.00, 0.00, 0.00
    Tasks:
      26 
    total,
       1 
    running,
      25 
    sleeping,
       0 
    stopped,
       0 
    zombie
    Cpu(s):
      0.0% 
      0.0% 
      0.0% 
     100.0% 
      0.0% 
      0.0% 
      0.0% 
    Mem: 
       514472k 
    total,
        42352k 
    used,
       472120k 
    free,
         5208k 
    buffers
    Swap:
      1510088k 
    total,
            0k 
    used,
      1510088k 
    free,
        19768k 
    cached
    [6;1H
    [7m  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND            
     3398 root      15   0  3048 1456 1168 R  0.3  0.3   0:00.02 top                
        1 root      16   0  1872  752  664 S  0.0  0.1   0:11.51 init               
        2 root      34  19     0    0    0 S  0.0  0.0   0:00.00 ksoftirqd/0        
        3 root      10  -5     0    0    0 S  0.0  0.0   0:00.24 events/0           
        4 root      10  -5     0    0    0 S  0.0  0.0   0:00.04 khelper            
        5 root      10  -5     0    0    0 S  0.0  0.0   0:00.00 kthread            
       16 root      10  -5     0    0    0 S  0.0  0.0   0:00.00 kblockd/0          
       15 root      25   0     0    0    0 S  0.0  0.0   0:00.00 powerd             
       19 root      10  -5     0    0    0 S  0.0  0.0   0:00.00 khubd              
       56 root      20   0     0    0    0 S  0.0  0.0   0:00.00 pdflush            
       57 root      15   0     0    0    0 S  0.0  0.0   0:00.00 pdflush            
       59 root      11  -5     0    0    0 S  0.0  0.0   0:00.00 aio/0              
       58 root      25   0     0    0    0 S  0.0  0.0   0:00.00 kswapd0            
      646 root      10  -5     0    0    0 S  0.0  0.0   0:00.00 kseriod            
     1742 root      15   0     0    0    0 S  0.0  0.0   0:00.00 kjournald          
     1880 root      14  -4  2952  704  448 S  0.0  0.1   0:00.32 udevd              
     2950 root      15   0     0    0    0 S  0.0  0.0   0:00.00 kjournald          
    [6;1H
    top - 22:54:24 up 21 min,  1 user,  load average: 0.00, 0.00, 0.00
    Tasks:
      26 
    total,
       1 
    running,
      25 
    sleeping,
       0 
    stopped,
       0 
    zombie
    Cpu(s):
      0.0% 
      0.0% 
      0.0% 
     100.0% 
      0.0% 
      0.0% 
      0.0% 
    Mem: 
       514472k 
    total,
        42352k 
    used,
       472120k 
    free,
         5208k 
    buffers
    Swap:
      1510088k 
    total,
            0k 
    used,
      1510088k 
    free,
        19768k 
    cached
    [6;1H
    [7m  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND            
     3398 root      15   0  3048 1456 1168 R  0.3  0.3   0:00.03 top                
    [6;1H
    top - 22:54:27 up 21 min,  1 user,  load average: 0.00, 0.00, 0.00
    Tasks:
      26 
    total,
       1 
    running,
      25 
    sleeping,
       0 
    stopped,
       0 
    zombie
    Cpu(s):
      0.0% 
      0.3% 
      0.0% 
     99.7% 
      0.0% 
      0.0% 
      0.0% 
    Mem: 
       514472k 
    total,
        42352k 
    used,
       472120k 
    free,
         5208k 
    buffers
    Swap:
      1510088k 
    total,
            0k 
    used,
      1510088k 
    free,
        19768k 
    cached
    [6;1H
    [7m  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND            
        1 root      16   0  1872  752  664 S  0.0  0.1   0:11.51 init               
        2 root      34  19     0    0    0 S  0.0  0.0   0:00.00 ksoftirqd/0        
        3 root      10  -5     0    0    0 S  0.0  0.0   0:00.24 events/0           
        4 root      10  -5     0    0    0 S  0.0  0.0   0:00.04 khelper            
        5 root      10  -5     0    0    0 S  0.0  0.0   0:00.00 kthread            
       16 root      10  -5     0    0    0 S  0.0  0.0   0:00.00 kblockd/0          
       15 root      25   0     0    0    0 S  0.0  0.0   0:00.00 powerd             
       19 root      10  -5     0    0    0 S  0.0  0.0   0:00.00 khubd              
       56 root      20   0     0    0    0 S  0.0  0.0   0:00.00 pdflush            
       57 root      15   0     0    0    0 S  0.0  0.0   0:00.00 pdflush            
       59 root      11  -5     0    0    0 S  0.0  0.0   0:00.00 aio/0              
       58 root      25   0     0    0    0 S  0.0  0.0   0:00.00 kswapd0            
      646 root      10  -5     0    0    0 S  0.0  0.0   0:00.00 kseriod            
     1742 root      15   0     0    0    0 S  0.0  0.0   0:00.00 kjournald          
     1880 root      14  -4  2952  704  448 S  0.0  0.1   0:00.32 udevd              
     2950 root      15   0     0    0    0 S  0.0  0.0   0:00.00 kjournald          
     3059 syslog    16   0  2376  960  768 S  0.0  0.2   0:00.03 syslogd            
    [6;1H
    top - 22:54:30 up 21 min,  1 user,  load average: 0.00, 0.00, 0.00
    Tasks:
      26 
    total,
       1 
    running,
      25 
    sleeping,
       0 
    stopped,
       0 
    zombie
    Cpu(s):
      0.0% 
      0.0% 
      0.0% 
     100.0% 
      0.0% 
      0.0% 
      0.0% 
    Mem: 
       514472k 
    total,
        42352k 
    used,
       472120k 
    free,
         5208k 
    buffers
    Swap:
      1510088k 
    total,
            0k 
    used,
      1510088k 
    free,
        19768k 
    cached
    [6;1H
    [7m  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND            
    [6;1H
    top - 22:54:33 up 21 min,  1 user,  load average: 0.00, 0.00, 0.00
    Tasks:
      26 
    total,
       1 
    running,
      25 
    sleeping,
       0 
    stopped,
       0 
    zombie
    Cpu(s):
      0.0% 
      0.0% 
      0.0% 
     100.0% 
      0.0% 
      0.0% 
      0.0% 
    Mem: 
       514472k 
    total,
        42352k 
    used,
       472120k 
    free,
         5208k 
    buffers
    Swap:
      1510088k 
    total,
            0k 
    used,
      1510088k 
    free,
        19768k 
    cached
    [6;1H
    [7m  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND            
    [6;1H
    top - 22:54:36 up 21 min,  1 user,  load average: 0.00, 0.00, 0.00
    Tasks:
      26 
    total,
       1 
    running,
      25 
    sleeping,
       0 
    stopped,
       0 
    zombie
    Cpu(s):
      0.0% 
      0.0% 
      0.0% 
     100.0% 
      0.0% 
      0.0% 
      0.0% 
    Mem: 
       514472k 
    total,
        42352k 
    used,
       472120k 
    free,
         5208k 
    buffers
    Swap:
      1510088k 
    total,
            0k 
    used,
      1510088k 
    free,
        19768k 
    cached
    [6;1H
    [7m  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND            
     3398 root      16   0  3048 1456 1168 R  0.3  0.3   0:00.04 top                
        1 root      16   0  1872  752  664 S  0.0  0.1   0:11.51 init               
        2 root      34  19     0    0    0 S  0.0  0.0   0:00.00 ksoftirqd/0        
        3 root      10  -5     0    0    0 S  0.0  0.0   0:00.24 events/0           
        4 root      10  -5     0    0    0 S  0.0  0.0   0:00.04 khelper            
        5 root      10  -5     
    [25;1H
    root@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# ls
    [0mtulip.ko
    [0m  
    [0muli526x.ko
    [0m  
    [0mwinbond-840.ko
    [mroot@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# vi /etc/ap
    t/s 
    rces.list
    [?1h
    [1;24r
    [24;1H"/etc/apt/sources.list" 39L, 1993C
    [1;1H#
    # deb cdrom:[Ubuntu-Server 6.06.2 _Dapper Drake_ - Release sparc (20080110.1)]/  
    [3;1Hdapper main restricted
    #deb cdrom:[Ubuntu-Server 6.06.2 _Dapper Drake_ - Release sparc (20080110.1)]/ dd
    [7;1Happer main restricted
    deb http://us.archive.ubuntu.com/ubuntu/ dapper main restricted
    deb-src http://us.archive.ubuntu.com/ubuntu/ dapper main restricted
    ## Major bug fix updates produced after the final release of the
    ## distribution.
    deb http://us.archive.ubuntu.com/ubuntu/ dapper-updates main restricted
    deb-src http://us.archive.ubuntu.com/ubuntu/ dapper-updates main restricted
    ## Uncomment the following two lines to add software from the 'universe'
    ## repository.
    ## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu
    ## team, and may not be under a free licence. Please satisfy yourself as to
    ## your rights to use the software. Also, please note that software in
    ## universe WILL NOT receive any review or updates from the Ubuntu security
    ## team.
    [24;63H1,1
    [11CTop
    [1;1H
    [24;63H2
    [2;1H
     deb cdrom:[Ubuntu-Server 6.06.2 _Dapper Drake_ - Release sparc (20080110.1)]/ dd
    [3;1Happer main restricted
    [3;22H
    [2;1H
    [24;63H3,0-1
    [4;1H
    [24;63H4
    [5;1H
    [24;63H5,1  
    [6;1H
    deb cdrom:[Ubuntu-Server 6.06.2 _Dapper Drake_ - Release sparc (20080110.1)]/ daa
    [7;1Hpper main restricted
    [7;21H
    [6;1H
    [24;1H
    [24;1H:w
    "/etc/apt/sources.list" 39L, 1991C written
    [20C5,1
    [11CTop
    [24;63H
    [24;63H5,1
    [11CTop
    [6;1H
    [24;1H
    [24;1H:q
    [?1l
    [24;1H
    [24;1Hroot@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# apt-hget
    root@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# apt-get updat 
    0% [Working][    2.409629] Unable to handle kernel NULL pointer dereference
    [    2.488963] tsk->{mm,active_mm}->context = 0000000000000f43
    [    2.562262] tsk->{mm,active_mm}->pgd = fffff800ddb28000
                
    E: Method http has died unexpectedly!
    E: Method http has died unexpectedly!
    root@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# apt-get update
    0% [Working][    5.372448] Unable to handle kernel NULL pointer dereference
                
    Ig[    5.451654] tsk->{mm,active_mm}->context = 0000000000000f53
    n cdrom://Ubuntu[    5.541607] tsk->{mm,active_mm}->pgd = fffff800ddae4000
    -Server 6.06.2 _[    5.628244] Unable to handle kernel paging request in mna handlerDapper Drake_ - <1> at virtual address 200040800003ba27
    Release sparc (2[    5.785216] current->{active_,}mm->context = 0000000000000f55
    0080110.1) dappe[    5.877522] current->{active_,}mm->pgd = fffff800ddb32000
    r Release.gpg
                
    14% [Connecting to us.archive.ubuntu.com] [Connecting to security.ubuntu.com]
                                                                                 
    E: Method http has died unexpectedly!
    E: Method http has died unexpectedly!
    root@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# apt-get update
    0% [Working]
                
    Ig[    8.329886] Unable to handle kernel paging request in mna handlern cdrom://Ubuntu<1> at virtual address c0a82a010003ba27
    -Server 6.06.2 _[    8.486795] current->{active_,}mm->context = 0000000000000f61
    Dapper Drake_ - [    8.579088] current->{active_,}mm->pgd = fffff800ddaae000
    Release sparc (20080110.1) dapper Release.gpg
                
    14% [Connecting to us.archive.ubuntu.com]
                                             
    E: Method http has died unexpectedly!
    root@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# apt-get update
    0% [Working]
                
    Ig[   10.291412] Unable to handle kernel NULL pointer dereference
    n cdrom://Ubuntu[   10.381851] tsk->{mm,active_mm}->context = 0000000000000f6d
    -Server 6.06.2 _[   10.471850] tsk->{mm,active_mm}->pgd = fffff800ddbf0000
    Dapper Drake_ - [   10.558273] Unable to handle kernel paging request in mna handlerRelease sparc (2<1> at virtual address 200040800003ba27
    0080110.1) dappe[   10.715476] current->{active_,}mm->context = 0000000000000f6b
    r Release.gpg
    [   10.807786] current->{active_,}mm->pgd = fffff800ddae4000
                
    14% [Connecting to us.archive.ubuntu.com] [Connecting to security.ubuntu.com]
                                                                                 
    E: Method http has died unexpectedly!
    E: Method http has died unexpectedly!
    root@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# apt-get update
    0% [Working]
                
    Ig[   12.795053] Unable to handle kernel paging request in mna handlern cdrom://Ubuntu<1> at virtual address c0a82a010003ba27
    -Server 6.06.2 _[   12.943950] current->{active_,}mm->context = 0000000000000f79
    Dapper Drake_ - [   13.036247] current->{active_,}mm->pgd = fffff800ddaae000
    Release sparc (2[   13.124534] Fixing recursive fault but reboot is needed!
    0080110.1) dapper Release.gpg
                
    14% [Connecting to us.archive.ubuntu.com] [Connecting to security.ubuntu.com]
                                                                                 
    root@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# apt-get update
    0% [Working][    9.493501] Unable to handle kernel NULL pointer dereference
                
    Ig[    9.572782] tsk->{mm,active_mm}->context = 0000000000000f83
    n cdrom://Ubuntu[    9.662722] tsk->{mm,active_mm}->pgd = fffff800de6c0000
    -Server 6.06.2 _[    9.749171] Unable to handle kernel paging request in mna handlerDapper Drake_ - <1> at virtual address 200040800003ba27
    Release sparc (2[    9.906334] current->{active_,}mm->context = 0000000000000f85
    0080110.1) dappe[    9.998638] current->{active_,}mm->pgd = fffff800ddb02000
    r Release.gpg
                
    14% [Connecting to us.archive.ubuntu.com] [Connecting to security.ubuntu.com]
                                                                                 
    E: Method http has died unexpectedly!
    E: Method http has died unexpectedly!
    root@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# vi /+
    [K/etc/ap
    t/s 
    urces.list
    [?1h
    [1;24r
    [24;1H"/etc/apt/sources.list" 39L, 1991C
    [1;1H#
     deb cdrom:[Ubuntu-Server 6.06.2 _Dapper Drake_ - Release sparc (20080110.1)]/ dd
    [3;1Happer main restricted
    deb cdrom:[Ubuntu-Server 6.06.2 _Dapper Drake_ - Release sparc (20080110.1)]/ daa
    [7;1Hpper main restricted
    deb http://us.archive.ubuntu.com/ubuntu/ dapper main restricted
    deb-src http://us.archive.ubuntu.com/ubuntu/ dapper main restricted
    ## Major bug fix updates produced after the final release of the
    ## distribution.
    deb http://us.archive.ubuntu.com/ubuntu/ dapper-updates main restricted
    deb-src http://us.archive.ubuntu.com/ubuntu/ dapper-updates main restricted
    ## Uncomment the following two lines to add software from the 'universe'
    ## repository.
    ## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu
    ## team, and may not be under a free licence. Please satisfy yourself as to
    ## your rights to use the software. Also, please note that software in
    ## universe WILL NOT receive any review or updates from the Ubuntu security
    ## team.
    [24;63H1,1
    [11CTop
    [1;1H
    [24;63H2
    [2;1H
    [24;63H3,0-1
    [4;1H
    [24;63H4
    [5;1H
    [24;63H5,1  
    [6;1H
    [24;63H6,0-1
    [8;1H
    [24;63H7,1  
    [9;1H
    [24;63H8
    [10;1H
    [24;63H9,0-1
    [11;1H
    [24;63H10,1 
    [12;1H
    [24;64H1
    [13;1H
    [24;64H2
    [14;1H
    [24;64H3
    [15;1H
    [24;64H4,0-1
    [16;1H
    [24;64H5,1  
    [17;1H
    [24;64H4,0-1
    [16;1H
    [24;64H3,1  
    [15;1H
    [24;64H2
    [14;1H
    [14;23r
    [23;1H
    [1;24r
    [23;1H# deb http://us.archive.ubuntu.com/ubuntu/ dapper universe
    [24;1H
    [24;63H12,1
    [10CTop
    [14;1H
    [14;23r
    [23;1H
    [1;24r
    [23;1H# deb-src http://us.archive.ubuntu.com/ubuntu/ dapper universe
    [24;63H
    [24;63H12,0-1
    [8CTop
    [14;1H
    [24;64H3,1  
    [15;1H
    [24;64H4
    [16;1H
    [24;64H5
    [17;1H
    [24;64H6
    [18;1H
    [24;64H7
    [19;1H
    [24;64H8
    [20;1H
    [24;64H9
    [21;1H
    [24;63H20
    [22;1H
    [24;64H1
    [23;1H
    [1;23r
    [23;1H
    [1;24r
    [24;63H
    [24;63H22,0-1
    [9C6%
    [23;1H
    [1;23r
    [23;1H
    [1;24r
    [22;1H## Uncomment the following two lines to add software from the 'backports'
    ## repository.
    [24;63H
    [24;63H23,1
    [10C13%
    [22;1H
    [24;64H4
    [23;1H
    [1;23r
    [23;1H
    [1;24r
    [23;1H## N.B. software from this repository may not have been tested as
    [24;63H
    [24;63H25,1
    [10C20%
    [23;1H
    [24;64H4
    [22;1H
    [10;23r
    [10;1H
    [1;24r
    [10;1Hdeb-src http://us.archive.ubuntu.com/ubuntu/ dapper-updates main restricted
    [24;63H
    [24;63H12,1
    [10C18%
    [10;1H
    [10;23r
    [10;1H
    [1;24r
    [10;1Hdeb http://us.archive.ubuntu.com/ubuntu/ dapper-updates main restricted
    [24;63H
    [24;63H12,1
    [10C17%
    [10;1H
    [24;1H
    [1m-- INSERT --
    [24;63H
    [24;63H12,1
    [10C17%
    [10;1H
    [24;1H
    [10;1H
    [24;63H12,1
    [10C17%
    [10;1H
    [24;1H
    [1m-- INSERT --
    [24;63H
    [24;63H12,1
    [10C17%
    [10;1H#deb http://us.archive.ubuntu.com/ubuntu/ dapper-updates main restricted
    [24;66H2
    [10;2H
    [24;64H3
    [11;2H
    [24;66H1
    [11;1H#deb-src http://us.archive.ubuntu.com/ubuntu/ dapper-updates main restricted
    [24;66H2
    [11;2H
    [24;64H4,1
    [12;1H
    [24;64H5,2
    [13;2H
    [24;64H6
    [14;2H
    [24;64H7
    [15;2H
    [24;64H8
    [16;2H
    [24;64H9
    [17;2H
    [24;63H20
    [18;2H
    [24;64H1
    [19;2H
    [24;64H2
    [20;2H
    [24;64H3
    [21;2H
    [24;64H4,1
    [22;1H
    [24;64H5,2
    [23;2H
    [1;23r
    [23;1H
    [1;24r
    [23;1H## repository.
    [24;63H
    [24;63H26,2
    [10C23%
    [23;2H
    [1;23r
    [23;1H
    [1;24r
    [22;1H## N.B. software from this repository may not have been tested as
    ## extensively as that contained in the main release, although it includes
    [24;63H
    [24;63H27,2
    [10C31%
    [22;2H
    [24;64H8
    [23;2H
    [1;23r
    [23;1H
    [1;24r
    [23;1H## newer versions of some applications which may provide useful features.
    [24;63H
    [24;63H29,2
    [10C37%
    [23;2H
    [1;23r
    [23;1H
    [1;24r
    [23;1H## Also, please note that software in backports WILL NOT receive any review
    [24;63H
    [24;63H30,2
    [10C43%
    [23;2H
    [1;23r
    [23;1H
    [1;24r
    [23;1H## or updates from the Ubuntu security team.
    [24;63H
    [24;63H31,2
    [10C50%
    [23;2H
    [1;23r
    [23;1H
    [1;24r
    [22;1Hdeb http://us.archive.ubuntu.com/ubuntu/ dapper-backports main restricted univerr
    [23;1Hse multiverse
    [24;63H
    [24;63H32,2
    [10C58%
    [22;2H
    [1;23r
    [23;1H
    [1;24r
    [22;1H# deb-src http://us.archive.ubuntu.com/ubuntu/ dapper-backports main restricted  
    [23;1Huniverse multiverse
    [24;63H
    [24;63H33,2
    [10C66%
    [22;2H
    [1;23r
    [23;1H
    [1;24r
    [24;63H
    [24;63H34,1
    [10C72%
    [23;1H
    [1;23r
    [23;1H
    [1;24r
    [24;63H
    [24;63H35,1
    [10C77%
    [23;1H
    [1;23r
    [23;1H
    [1;24r
    [23;1Hdeb http://security.ubuntu.com/ubuntu dapper-security main restricted
    [24;63H
    [24;63H36,2
    [10C83%
    [23;2H
    [1;23r
    [23;1H
    [1;24r
    [23;1Hdeb-src http://security.ubuntu.com/ubuntu dapper-security main restricted
    [24;63H
    [24;63H37,2
    [10C88%
    [23;2H
    [1;23r
    [23;1H
    [1;24r
    [23;1H# deb http://security.ubuntu.com/ubuntu dapper-security universe
    [24;63H
    [24;63H38,2
    [10C94%
    [23;2H
    [1;23r
    [23;1H
    [1;24r
    [23;1H# deb-src http://security.ubuntu.com/ubuntu dapper-security universe
    [24;63H
    [24;63H39,2
    [10CBot
    [23;2H
    [24;64H8
    [22;2H
    [24;64H7
    [21;2H
    [24;64H6
    [20;2H
    [24;64H5,1
    [19;1H
    [24;64H4
    [18;1H
    [24;64H3,2
    [16;2H
    [24;64H2
    [14;2H
    [24;64H1
    [13;2H
    [24;64H2
    [14;2H
    [24;66H1
    [14;1H#deb http://us.archive.ubuntu.com/ubuntu/ dapper-backports main restricted univee
    [15;1Hrse multiverse
    [24;66H2
    [14;2H
    [24;64H3
    [16;2H
    [24;64H4,1
    [18;1H
    [24;64H5
    [19;1H
    [24;64H6,2
    [20;2H
    [24;66H1
    [20;1H#deb http://security.ubuntu.com/ubuntu dapper-security main restricted
    [24;64H7,2
    [21;2H
    [24;66H1
    [21;1H#deb-src http://security.ubuntu.com/ubuntu dapper-security main restricted
    [24;64H8,2
    [22;2H
    [24;64H9
    [23;2H
    [24;1H
    [24;63H39,1
    [10CBot
    [23;1H
    [24;63H
    [24;1H:w
    "/etc/apt/sources.list" 39L, 1996C written
    [20C39,1
    [10CBot
    [24;63H
    [24;63H39,1
    [10CBot
    [23;1H
    [24;1H
    [24;1H:q
    [?1l
    [24;1H
    [24;1Hroot@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# vi /etc/apt/so
    ources.list
    root@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# apt-get update
    0% [Working]
                
    Ig[   14.268383] Unable to handle kernel paging request in mna handlern cdrom://Ubuntu<1> at virtual address c0a82a010003ba27
    -Server 6.06.2 _[   14.425169] current->{active_,}mm->context = 0000000000000fa5
    Dapper Drake_ - [   14.517463] current->{active_,}mm->pgd = fffff800c0cf2000
    Release sparc (20080110.1) dapper Release.gpg
                
    25% [Connecting to us.archive.ubuntu.com]
                                             
    E: Method http has died unexpectedly!
    root@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# apt-get update
    0% [Working]
                
    Ig[   11.649122] Unable to handle kernel NULL pointer dereference
    n cdrom://Ubuntu[   11.738432] tsk->{mm,active_mm}->context = 0000000000000faf
    -Server 6.06.2 _[   11.828414] tsk->{mm,active_mm}->pgd = fffff800ddad6000
    Dapper Drake_ - Release sparc (20080110.1) dapper Release.gpg
                
    25% [Connecting to us.archive.ubuntu.com]
                                             
    E: Method http has died unexpectedly!
    root@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# apt-get update
    0% [Working]
                
    Ig[   14.142832] Unable to handle kernel paging request in mna handlern cdrom://Ubuntu<1> at virtual address 200040800003ba27
    -Server 6.06.2 _[   14.293236] current->{active_,}mm->context = 0000000000000fb9
    Dapper Drake_ - [   14.385548] current->{active_,}mm->pgd = fffff800de6a6000
    Release sparc (20080110.1) dapper Release.gpg
                
    25% [Working]
                 
    E: Method http has died unexpectedly!
    root@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# apt)
    [K-cache sea 
    rch kernel
    alsa-base - ALSA driver configuration files
    autofs - kernel-based automounter for Linux
    binutils-static - statically linked binutils tools
    debianutils - Miscellaneous utilities specific to Debian
    dmsetup - The Linux Kernel Device Mapper userspace library
    libdevmapper1.02 - The Linux Kernel Device Mapper userspace library
    ethtool - Display or change ethernet card settings
    evms-cli - Enterprise Volume Management System (CLI)
    evms-ncurses - Enterprise Volume Management System (ncurses UI)
    evms - Enterprise Volume Management System (core)
    git-core - content addressable filesystem
    ifenslave-2.6 - Attach and detach slave interfaces to a bonding device
    initramfs-tools - tools for generating an initramfs
    inputattach - utility to attach serial devices to the input subsystem
    iproute - Professional tools to control the networking in Linux kernels
    ipsec-tools - IPsec tools for Linux
    iptables - Linux kernel 2.4+ iptables administration tools
    keepalived - Failover and monitoring daemon for LVS clusters
    linux-backports-modules-2.6.15-51-sparc64-smp - Ubuntu supplied Linux modules for version 2.6.15 on 64-bit UltraSPARC SMP
    linux-backports-modules-2.6.15-51-sparc64 - Ubuntu supplied Linux modules for version 2.6.15 on 64-bit UltraSPARC
    linux-kernel-headers - Linux Kernel Headers for development
    linux-headers-sparc64-smp - Linux kernel headers on UltraSparc (SMP)
    linux-image-sparc64-smp - Linux kernel image on UltraSparc (SMP)
    linux-image-sparc64 - Linux kernel image on UltraSparc
    linux-sparc64-smp - Complete Linux kernel on UltraSparc (SMP)
    linux-sparc64 - Complete Linux kernel on sparc64.
    linux-headers-2.6.15-51-sparc64-smp - Header files for Linux kernel 2.6.15 on multiprocessor 64-bit SPARC
    linux-headers-2.6.15-51 - Header files related to Linux kernel version 2.6.15
    linux-image-2.6.15-51-sparc64-smp - Linux kernel binary image for SMP UltraSPARC (sparc64) systems
    linux-image-2.6.15-51-sparc64 - Linux kernel binary image for UltraSPARC (sparc64) systems
    lm-sensors - utilities to read temperature/voltage/fan sensors
    sensord - hardware sensor information logging daemon
    lsb-core - Linux Standard Base 3.1 core support package
    lsb-cxx - Linux Standard Base 3.1 C++ support package
    lvm-common - The Logical Volume Manager for Linux (common files)
    lvm2 - The Linux Logical Volume Manager
    libaio-dev - kernel aio access library - development files
    libaio1 - kernel aio access library
    libcap1 - support for getting/setting POSIX.1e capabilities
    libselinux1 - SELinux shared libraries
    libsepol1 - Security Enhanced Linux policy library for changing policy binaries
    libusb-0.1-4 - userspace USB programming library
    module-init-tools - tools for managing Linux kernel modules
    net-tools - The NET-3 networking toolkit
    nfs-kernel-server - Kernel NFS server support
    pcmciautils - PCMCIA utilities for Linux 2.6
    perl-suid - Runs setuid Perl scripts
    procps - /proc file system utilities
    quagga - unoff. s
    root@brol:/lib/modules/2.6.15-51-sparc64/kernel/drivers/net/tulip# ap
    [Khalt
    Broadca * Stopping deferred execution scheduler...       
    [80G 
    [74G[ ok ]
     * Stopping periodic command scheduler...       
    [80G 
    [74G[ ok ]
     * Stopping rsync daemon: rsync       
    [80G 
    [74G[ ok ]
     * Stopping RAID monitoring services...       
    [80G 
    [74G[ ok ]
     * Shutting down ALSA...       
    [80G 
    [74G[ ok ]
     * Stopping kernel log...       
    [80G 
    [74G[ ok ]
     * Stopping system log...       
    [80G 
    [74G[ ok ]
     * Terminating any remaining processes...       
    [80G 
    [74G[ ok ]
     * Unmounting remote filesystems...       
    [80G 
    [74G[ ok ]
     * Deconfiguring network interfaces...       
    [80G [    0.949997] Unable to handle kernel NULL pointer dereference
    [    1.024363] tsk->{mm,active_mm}->context = 00000000000010fb
    [    1.097622] tsk->{mm,active_mm}->pgd = fffff800de6a6000
    [74G[ ok ]
     * Unmounting local filesystems...       
    [80G 
    [74G[ ok ]
     * Deactivating swap...       
    [80G 
    [74G[ ok ]
     * Shutting down LVM Volume Groups...        
    [80G 
    [74G[ ok ]
     * Will now halt
