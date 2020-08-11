

# About


A multimedia player found in the "throwaway" bin at [HSBXL](http://www.hsbxl.be). While the device looks fully functional, it is the posterchild of the ["throwaway culture"](https://www.theguardian.com/world/2018/mar/15/can-we-fix-it-the-repair-cafes-waging-war-on-throwaway-culture). 

The device is based around the SoC Realtek RTD1073.

# Pictures


[[=image apacer-al670-all.jpg]]
[[=image apacer-al670-serialconsole.jpg size="medium"]]
[[=image apacer-al670-back.jpg size="medium"]]

# Cpuinfo



    # cat /proc/cpuinfo 
    system type             : Realtek Venus
    processor               : 0
    cpu model               : MIPS 24K V7.8
    BogoMIPS                : 269.51
    wait instruction        : yes
    microsecond timers      : yes
    tlb_entries             : 32
    extra interrupt vector  : yes
    hardware watchpoint     : yes
    ASEs implemented        : mips16
    VCED exceptions         : not available
    VCEI exceptions         : not available


# Ram



    /etc # cat /proc/meminfo 
    MemTotal:       119808 kB
    MemFree:         36740 kB
    Buffers:            60 kB
    Cached:           5460 kB
    SwapCached:          0 kB
    Active:           4640 kB
    Inactive:         2216 kB
    HighTotal:           0 kB
    HighFree:            0 kB
    LowTotal:       119808 kB
    LowFree:         36740 kB
    SwapTotal:          32 kB
    SwapFree:           32 kB
    Dirty:               0 kB
    Writeback:           0 kB
    Mapped:           4744 kB
    Slab:             5412 kB
    CommitLimit:     59936 kB
    Committed_AS:     5348 kB
    PageTables:        356 kB
    VmallocTotal:  1048548 kB
    VmallocUsed:       532 kB
    VmallocChunk:  1047932 kB


# Flash



    # df -h
    Filesystem                Size      Used Available Use% Mounted on
    /dev/root                73.6M     73.6M         0 100% /
    /dev/mtdblock/2          40.0M      1.3M     38.7M   3% /usr/local/etc
    /dev/rd/0                40.0k     40.0k         0 100% /mnt/rd


# Serial console


Next to the CPU, there is a 4 pins holes, so I soldered 4 pins header, and got a serial console (at the usual speed of 115200 bps):


    / # watchdog test pid 202, threshold: 50
    / # 
    / # 
    / # 
    / # 
    / # reboot
    / # umount: Cannot remount /dev/rd/0 read-only
    umount: Cosave exit: isCheckpointed 1
    uldn't umount /mnt/rd: Inappropriate ioctl for device
    umount: Cannot remount none read-only
    umount: Couldn't umount /tmp: No such file or directory
    umount: none busy - remounted read-only
    The system is going down NOW !!
    Sending SIGTERM to all processes.
    pli initialization...
    clear pli setting....
    ***128MB version...
       Memory address 0x40000000
    ************* PAY ATTENTION *************
    Not support mntent, use sync() instead...
    *****************************************
    Sending SIGKILLclear pli setting....
    Please stand by while rebooting the system.
    Restarting system.
    REALTEK ROM Monitor, Revision 0000.0202.0016.
    Copyright (c) Realtek Semiconductor Corp. - All Rights Reserved.
    For a list of available commands, type 'help'.
    Compilation time /version=      Jan 15 2010  17:08:36  /0000.0202.0016
    MAC address =                   00.0a.d8.01.da.6d
    Processor Company ID/options =  0x01 (MIPS Technologies, Inc.) / 0x00
    Processor ID/revision =         0x93 / 0x78
    Endianness =                    Little
    Flash memory size =             256 MByte
    SDRAM size =                    128 MByte
    First free SDRAM address =      0x800fd000
    Press 'ESC' to Monitor mode
    Linux Kernel:
    	FW Image from 0xa2020000, to 0x80100000, size=0x456086 
    Audio FW:
    	FW Image from 0xa2480000, to 0x81b00000, size=0x1b3d98 
    Video FW:
    	FW Image from 0xa2640000, to 0x81d80000, size=0x213070 
    PAL logo
    5280Go 5280Go BoagrdBonding  0x00000o002
     0x80100000 rootfstype=yaffs2 root=31:01 mtdparts=rtk_nand:132608k,75392k(/),40960k(/usr/local/etc),13184k 
    Reset Ethernet Mac.
    Address = 0x80100000
    Realtek LINUX (DC ALIAS) started...
    Venus setting:
    	ROSs have 2621440 bytes RAM.
    	System CPU has 2 UARTs.
    	System CPU uses external timer interrupt.
    	Bootloader version: 0000.0202.0016. This version string is of new format.
    [31;5mError! Unknown SB2_CHIP_INFO. Linux is too old?
    	Ethernet Mac address: 00.0A.D8.01.DA.6D
    	Model Config length=0
    Config serial console: console=ttyS0,115200n8r
    prom_flashsize = 0x10000000
    Linux version 2.6.12.6-VENUS (root@Fedora8) (gcc version 3.4.4 mipssde-6.03.01-20051114) #2 Tue Dec 29 01:48:51 CST 2009
    audio addr: 1b00000 
    CPU revision is: 00019378
    Determined physical RAM map:
     memory: 00100000 @ 00000000 (usable)
     memory: 004f4000 @ 00100000 (reserved)
     memory: 0150c000 @ 005f4000 (usable)
     memory: 00500000 @ 01b00000 (reserved)
     memory: 06000000 @ 02000000 (usable)
      show info: max_low_pfn:32768
      show info: min_low_pfn:1524
    Built 1 zonelists
    Kernel command line: rootfstype=yaffs2 root=31:01 mtdparts=rtk_nand:132608k,75392k(/),40960k(/usr/local/etc),13184k console=ttyS0,115200n8r ip=192.168.0.9::192.168.0.254:255.0.0.0:::
    Primary instruction cache 32kB, physically tagged, 4-way, linesize 32 bytes.
    Primary data cache 32kB, 4-way, linesize 32 bytes.
    Synthesized TLB refill handler (20 instructions).
    Synthesized TLB load handler fastpath (32 instructions).
    Synthesized TLB store handler fastpath (32 instructions).
    Synthesized TLB modify handler fastpath (31 instructions).
    Cache parity protection disabled
    PID hash table entries: 256 (order: 8, 4096 bytes)
    Estimate value: CPU frequency 405.02 MHz
    Using 27.000 MHz high precision timer.
    Console: colour dummy device 80x25
    Dentry cache hash table entries: 8192 (order: 3, 32768 bytes)
    Inode-cache hash table entries: 4096 (order: 2, 16384 bytes)
    Memory: 118704k/120880k available (3484k kernel code, 2112k reserved, 811k data, 144k init, 0k highmem)
    Warning! Unknown board id.
    ==================== Warning! The calculated loops_per_jiffy is not similar to the default one. ====================
    Mount-cache hash table entries: 512
    Checking for 'wait' instruction...  available.
    ========== board id: 202 ==========
    [INFO] neptune mode...
    boot_param value: a0002800 
    mode: 14991360 
    size: 35391013 
    color1: 0x5200322 
    color2: 0x140e683 
    color3: 0x44424500 
    color4: 0x28045830 
    NET: Registered protocol family 16
    SCSI subsystem initialized
    usbcore: registered new driver usbfs
    usbcore: registered new driver hub
    se init module major number = 254
    size of RPC_POLL_Dev 52 and RPC_INTR_Dev 52...
    [user land] CmdBuf virt addr = 8072c000/a072c000, phy addr=0072c000
       Hello, Realtek TLB Mapper
    squashfs: version 3.1 (2006/08/19) Phillip Lougher
    devfs: 2004-01-31 Richard Gooch (rgooch@atnf.csiro.au)
    devfs: boot_options: 0x1
    JFFS2 version 2.2. (C) 2001-2003 Red Hat, Inc.
    YAFFS Driver Rev:268981 (2009-09-21)
    YAFFS Driver is successfully installing.
    Initializing Cryptographic API
    Generic RTC Driver v1.07
    Serial: 8250
    [Audio Firmware Version] 283447
    [Binary src compiled at] Dec  1 2009 15:32:36
    /16550 driver $Revision: 1.90 $ 4 ports, IRQ sharing enabled
    ttyS0 at MMIO 0x0 (irq = 3) is a 16550A
    ttyS1 at MMIO 0x0 (irq = 3) is a 16550A
    io scheduler noop registered
    RAMDISK driver initialized: 1 RAM disks of 128K size 1024 blocksize
    loop: loaded (max 8 devices)
    this  MARS eth RX_OFFSET = 0x0
    8139cplus: 10/100 PCI Ethernet driver v1.2 (Mar 22, 2004)
    MAC address = 0x00.0A.D8.01.DA.6D 
    eth0: RTL-8139C+ at 0xb8016000, 00:0a:d8:01:da:6d, IRQ 2
    PPP generic driver version 2.4.2
    cp_hotplug 
    PPP Deflate Compression module registered
    PPP BSD Compression module registered
    NET: Registered protocol family 24
    VenusSFC MTD init
    serial flash inaccessible
    physmap flash device: 10000000 at fd00000
    Realtek NAND Flash Driver Rev:268236 (2009-09-17)
    One HY27UF082G2B chip has 1 die(s) on board
    nand part=HY27UF082G2B, id=adda1095, device_size=268435456, chip_size=268435456, num_chips=1, isLastPage=0
    [rtk_nand_scan_bbt] have created bbt B0, just loads it !!
    [dump_BBT] Nand BBT Content
    Congratulation!! No BBs in this Nand.
    4 cmdlinepart partitions found on MTD device rtk_nand
    RTK: using dynamic nand partition
    Creating 4 MTD partitions on "rtk_nand":
    0x00000000-0x08180000 : "Partition_000"
    0x08180000-0x0cb20000 : "/"
    0x0cb20000-0x0f320000 : "/usr/local/etc"
    0x0f320000-0x10000000 : "Partition_003"
    0x00000000-0x10000000 : "disc"
    Realtek Nand Flash Driver is successfully installing.
    Initializing USB Mass Storage driver...
    usbcore: registered new driver usb-storage
    USB Mass Storage support registered.
    i2c /dev entries driver
    [I2C0] i2c speed changed to 100 KHz
    I2C0 Bus Status Check.... OK
    =========================
    = VER : 2.0a               
    =========================
    = PHY : 0               
    = MODE: MARS               
    = SPD : 100               
    = SAR : 0x024 (7 bits) 
    = TX FIFO DEPTH : 8     
    = RX FIFO DEPTH : 8     
    = FIFO THRESHOLD: 4     
    = BUS JAM RECORVER : ON  
    = NON STOP WRITE : ON  
    = SP PROTECT : ON  
    =========================
    FATAL : I2C 1 pins have been occupied by PCI
    Trying to free free IRQ3
    NET: Registered protocol family 2
    IP: routing cache hash table of 1024 buckets, 8Kbytes
    TCP established hash table entries: 8192 (order: 4, 65536 bytes)
    TCP bind hash table entries: 8192 (order: 3, 32768 bytes)
    TCP: Hash tables configured (established 8192 bind 8192)
    NET: Registered protocol family 1
    NET: Registered protocol family 17
    NET: Registered protocol family 5
    Realtek Venus Power Management, (c) 2006 Realtek Semiconductor Corp.
    cp_open 
    alloc rings cp->rxdesc_buf =0xa1009000 , cp->ring_dma=0x1009000
    init_hw 
    init_hw finished 
    IP-Config: Complete:
          device=eth0, addr=192.168.0.9, mask=255.0.0.0, gw=192.168.0.254RTK rtc cannot work.
         host=192.168.0.9, domain=, nis-domain=(none),
         bootserver=255.255.255.255, rootserver=255.255.255.255, rootpath=
    yaffs: dev is 32505857 name is "mtdblock1"
    yaffs: Attempting MTD mount on 31.1, "mtdblock1"
    force MTDBLOCK1_CHECKPOINT
    save exit: isCheckpointed 0
    VFS: Mounted root (yaffs2 filesystem) readonly.
    Mounted devfs on /dev
    Freeing prom memory: 0kb freed
    Reclaim bootloader memory from 80020000 to 80100000
    Freeing unused kernel memory: 144k freed
    Welcome to Realtek Linux
    Please press Enter to activate this console. ------flush priority: 10 
    flush_page_cache: do flush...
    ------flush priority: 10 
    flush_page_cache: do flush...
    ------flush priority: 10 
    flush_page_cache: do flush...
    ------flush priority: 10 
    flush_page_cache: do flush...
    yaffs: dev is 32505858 name is "mtdblock2"
    yaffs: Attempting MTD mount on 31.2, "mtdblock2"
    yaffs: auto selecting yaffs2
    yaffs: restored from checkpoint
    ------flush priority: 10 
    flush_page_cache: do flush...
    Starting INET services....
    libata version 1.12 loaded.
    sata driver initial...2009/11/23 11:00
    ata_device_add(4865)probe begin
    scsi0 : SATA_DRV
    sata dma reset
    Running dvdplayer with RootApp
    RootApp AVHDD version...
    set corepath: /tmp/hdd/volumes/HDD1/ 
    enter 2nd case...
    ================================================
    ================================================
    root execute DvdPlayer...
    ================================================
    ================================================
    IN : /tmp/ramfs/smb
    CMD: mkdir -p /tmp/netb/smb 
    In my system...
    CMD: mkdir -p /tmp/smb 
    In my system...
    CMD: ifconfig > /tmp/netb/samba_my_ip 
    In my system...
    Warning!! the Mask is 255.0.0.0.
    file system 2, sector 4294966272
    mount to /tmp/hdd/volumes/HDD1
    file system 4, sector 262144
    mount to na
    file system 3, sector 262144
    mount to /tmp/hdd/root
    DB FILENAME = /tmp/ramfs/Setup 
    [DataObject.cpp 387]DB Develop Version same . Don't be upgrade. 
    [DataObject.cpp 426]DB Version same . Don't be upgrade. 
     m_BookMark_Size=4096 m_Signature_Size=16 
    GrandMa Ver: BY2***128MB version...
    3_2.7.0323.AP2P
    (User Input)Pip   Memory address 0x40000000
    e Created.
    (Internal Event)Pipe Created.
    pli initialization...
    513 loadThemeSetting resource.cpp
    No THEMESET_INI exists
    try_to_free_pages: free 772 
    1. start remap DVR zone...
    save exit: isCheckpointed 1
    sata1: reset phy again!
    sata phy reset
    fastmode is 100...
    map_done is 1569...
    map_fail is 0...
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    try_to_free_pages: free 28 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 2...
    map_fail is 0...
    try_to_free_pages: free 164 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 18...
    map_fail is 0...
    Video DebugMem Physical Address = 0x58600
    VIDEO_RPC_SetDebugMemory Called!try_to_free_pages: free 51 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 5...
    map_fail is 0...
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 25...
    map_fail is 0...
    -------------------
    Audio Version = 283447
    Common Version = 280972
    Build Date = Dec  1 2009
    Build Time = 15:32:36
    Note = 
    -------------------
    [Video Firmware Version]   284003
    [Video Binary  Built on]   Dec  4 2009 16:02:40
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    VBM: configured to SD!
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    Error in threshotry_to_free_pages: free 0 
    ld value: 0...
    1. start remap DVR zone...
    WatchDog does nofastmode is 100...
    t receive signalmap_done is 0...
     for 2 seconds, map_fail is 0...
    value: 0 
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    board = 14 !, if -1, this board has illegal ID
    file is (AC3,DTS,WMA) (1,0,0)
    Do you have key?(0 = no!) AC3 = 0, DTS = 0, WMA = 0
    Bonding option process  0x00000009 to AUDIO_UNKNOWN_TYPE !!!
    ClassifyBonding  DD   0x00000002
    board = 14 !, if -1, this board has illegal ID
    file is (AC3,DTS,WMA) (1,0,0)
    Do you have key?(0 = no!) AC3 = 0, DTS = 0, WMA = 0
    Bonding option process  0x0000000a to passThrough !!!
    ClassifyBonding  DD   0x00000002
    board = 14 !, if -1, this board has illegal ID
    file is (AC3,DTS,WMA) (0,1,0)
    Do you have key?(0 = no!) AC3 = 0, DTS = 0, WMA = 0
    Bonding option process  0x0000000b to passThrough !!!
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    board = 14 !, if -1, this board has illegal ID
    file is (AC3,DTS,WMA) (0,1,0)
    Do you have key?(0 = no!) AC3 = 0, DTS = 0, WMA = 0
    Bonding option process  0x0000001b to passThrough !!!
    ClassifyBonding  DD   0x00000002
    board = 14 !, if -1, this board has illegal ID
    file is (AC3,DTS,WMA) (0,1,0)
    Do you have key?(0 = no!) AC3 = 0, DTS = 0, WMA = 0
    Bonding option process  0x0000001c to passThrough !!!
    ClassifyBonding  DD   0x00000002
    board = 14 !, if -1, this board has illegal ID
    file is (AC3,DTS,WMA) (0,1,0)
    Do you have key?(0 = no!) AC3 = 0, DTS = 0, WMA = 0
    Bonding option process  0x0000001d to passThrough !!!
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    board = 14 !, if -1, this board has illegal ID
    file is (AC3,DTS,WMA) (0,0,1)
    Do you have key?(0 = no!) AC3 = 0, DTS = 0, WMA = 0
    Bonding option process  0x00000023 to AUDIO_UNKNOWN_TYPE !!!
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    ClassifyBonding  DD   0x00000002
    High =  0x00000000, Low =  0x03c1b1fe
    The following Format is supported:
    MPEG
    LPCM
    VORBIS
    WMA Pro
    MP4 LC-AAC
    MP4 HE-AAC
    RAW AAC
    ADPCM
    FLAC
    A Law PCM
    u Law PCM
    [VIDEO Capability]HighWord  0xffffffff, LowWord  0xffffffff
    [HDMI]: Set AVMute
    HDMI_gen_audio_infoframe
    try_to_free_pages: free 218 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 26...
    map_fail is 0...
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    req: 168000, get: 200000 
    reclaim size: 80000 
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    [Util.cpp 1313] try_to_free_pages: free 0 
    videoVersion = 21. start remap DVR zone...
    84003
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    req: aa000, get: 100000 
    reclaim size: 40000 HDMI_gen_audio_infoframe
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    req: 2e000, get: 40000 
    reclaim size: 10000 
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    req: 66000, get: 80000 
    reclaim size: 10000 
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    req: 66000, get: 80000 
    reclaim size: 10000 
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    ~~SetVideoStandard 25 1
    try_to_free_pages: free 103 
    1. start remap DVR zone...
    WARNING[4]:TVE i-underflow @ line 0
    fastmode is 100...
    map_done is 8...
    map_fail is 0...
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    req: b0000, get: 100000 
    reclaim size: 40000 
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 1...
    map_fail is 0...
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    req: 50000, get: 80000 
    reclaim size: 20000 
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    IN : /tmp/ramfs/usb/livepause
    IN : /tmp/ramfs/usb
    OUT : /tmp/ramfs/usb/livepause
    IN : /tmp/ramfs/usb/rec
    Activate
    m_browserDevice: 3
    2331 SetCurrentBrowserTypeChoice GNewBrowserMenu.cpp 3
    try_to_free_pages: free 183 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 43...
    map_fail is 0...
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    req: 1c2000, get: 200000 
    reclaim size: 20000 
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    [GBrowserAP.cpp:533]:GiveUpFocus()- %%%%%% - !!
    DG_DrawBitmapCommon: Invalid destination rectangle!
    DG_DrawBitmapCommon: Invalid destination rectangle!
    IN : /tmp/net
    Create /tmp/net Ok!!!
    In my system...
    In my system...
    [usb_param] setting for mars
    Setting for MARS-B
    [usb_param] set port two for host!
    [usb1_param] usbphy reg 32, set sh = 0x5, get sh = 0x5, 4bit
    [usb1_param] usbphy reg 35, set src = 0x7, get src = 0x7, 3bit
    [usb1_param] usbphy reg 36, set senh = 0xd, get senh = 0xd, 4bit
    [usb1_param] usbphy reg 32, set sen = 0x8, get sen = 0x8, 4bit
    [usb1_param] usbphy reg 33, set dr = 0x0, get dr = 0x0, 3bit
    [usb2_param] usbphy reg 32, set sh = 0x5, get sh = 0x5, 4bit
    [usb2_param] usbphy reg 35, set src = 0x7, get src = 0x7, 3bit
    [usb2_param] usbphy reg 36, set senh = 0xd, get senh = 0xd, 4bit
    [usb2_param] usbphy reg 32, set sen = 0x8, get sen = 0x8, 4bit
    [usb2_param] usbphy reg 33, set dr = 0x0, get dr = 0x0, 3bit
    ehci_hcd ehci_hcd: EHCI Host Controller
    sata1: reset phy again!
    sata phy reset
    ehci_hcd ehci_hcd: new USB bus registered, assigned bus number 1
    ehci_hcd ehci_hcd: irq 2, io mem 0xb8013000
    ehci_hcd ehci_hcd: park 0
    ehci_hcd ehci_hcd: USB 0.0 initialized, EHCI 1.00, driver 10 Dec 2004
    hub 1-0:1.0: USB hub found
    hub 1-0:1.0: 2 ports detected
    hub : individual port power switching
    hub : individual port over-current protection
    0 usb block device found
    No Recording Partition Available !!!!!!
    No Timeshift Partition Available !!!!!!
    0 usb block device found
    No Recording Partition Available !!!!!!
    No Timeshift Partition Available !!!!!!
    [cfyeh] set PPE = 0
    [usb_param] setting for mars
    Setting for MARS-B
    [usb_param] set port two for host!
    [usb1_param] usbphy reg 32, set sh = 0x5, get sh = 0x5, 4bit
    [usb1_param] usbphy reg 35, set src = 0x7, get src = 0x7, 3bit
    [usb1_param] usbphy reg 36, set senh = 0xd, get senh = 0xd, 4bit
    [usb1_param] usbphy reg 32, set sen = 0x8, get sen = 0x8, 4bit
    [usb1_param] usbphy reg 33, set dr = 0x0, get dr = 0x0, 3bit
    [usb2_param] usbphy reg 32, set sh = 0x5, get sh = 0x5, 4bit
    [usb2_param] usbphy reg 35, set src = 0x7, get src = 0x7, 3bit
    [usb2_param] usbphy reg 36, set senh = 0xd, get senh = 0xd, 4bit
    [usb2_param] usbphy reg 32, set sen = 0x8, get sen = 0x8, 4bit
    [usb2_param] usbphy reg 33, set dr = 0x0, get dr = 0x0, 3bit
    ohci_hcd ohci_hcd: OHCI Host Controller
    ohci_hcd ohci_hcd: new USB bus registered, assigned bus number 2
    ohci_hcd ohci_hcd: irq 2, io mem 0xb8013400
    hub 2-0:1.0: USB hub found
    hub 2-0:1.0: 2 ports detected
    hub : no power switching (usb 1.0)
    Error in threshohub : no over-current protection
    ld value: 0...
    WatchDog does not receive signal for 2 seconds, value: 0 
    0 usb block device found
    No Recording Partition Available !!!!!!
    No Timeshift Partition Available !!!!!!
    0 usb block device found
    No Recording Partition Available !!!!!!
    No Timeshift Partition Available !!!!!!
    In my system...
    This is the current time: PowerUP_Done!!!
    In my system...
    In my system...
    In my system...
    In my system...
    [HDMI]: MARS HDMI is running...
    [HDMI]: Disable HDCP
    [HDMI]: Show Aksv========================================ST
    [HDMI]: HDMI Device Private Key does not exist!!!! 2
    ReadAksv() fails
    [HDMI]: Show Aksv========================================SP
    [HDMI]: Hotplug Change !!! -1 -> 0
    save exit: isCheckpointed 1
    watchdog test pid 202, threshold: 50
    sata1: reset phy extra!
    sata phy reset
    watchdog test pid 202, threshold: 50
    watchdog test pid 202, threshold: 50
    sata1: reset phy extra!
    sata phy reset
    watchdog test pid 202, threshold: 50
    watchdog test pid 202, threshold: 50
    watchdog test pid 202, threshold: 50
    sata1: reset phy extra!
    sata phy reset
    watchdog test pid 202, threshold: 50
    watchdog test pid 202, threshold: 50
    watchdog test pid 202, threshold: 50
    sata1: phy reset timeout!
    sata1: no device found (phy stat 00000000)
    sata1: ata_bus_probe failed
    scsi1 : SATA_DRV
    sata dma reset
    watchdog test pid 202, threshold: 50
    sata2: reset phy again!
    sata phy reset
    watchdog test pid 202, threshold: 50
    sata2: reset phy again!
    sata phy reset
    watchdog test pid 202, threshold: 50
    watchdog test pid 202, threshold: 50
    sata2: phy reset timeout!
    sata2: no device found (phy stat 00000000)
    sata2: ata_bus_probe failed
    BusyBox v1.1.3 (2009.12.25-16:48+0000) Built-in shell (ash)
    Enter 'help' for a list of built-in commands.
    watchdog test pid 202, threshold: 50
    / # 
    / # ps
      PID  Uid     VmSize Stat Command
        1 root        428 S   init       
        2 root            SWN [ksoftirqd/0]
        3 root            SW< [events/0]
        4 root            SW< [khelper]
        5 root            SW< [kthread]
        6 root            SW< [kblockd/0]
        7 root            SW  [khubd]
        8 root            SW  [pdflush]
        9 root            SW  [pdflush]
       11 root            SW< [aio/0]
       10 root            SW  [kswapd0]
       12 root            SW< [cifsoplockd]
       13 root            SW< [cifsdnotifyd]
       14 root            SW  [eth0]
       15 root            SW  [mtdblockd]
       27 root        536 S   -sh 
       28 root        432 S   init       
       31 root        432 S   init       
       34 root        432 S   init       
      179 root        432 S   inetd 
      183 root            SW< [sata_eh/0]
      188 root            SW  [scsi_eh_0]
      196 root            SW  [scsi_eh_1]
      198 root        168 S   ./RootApp DvdPlayer 
      199 root        168 S   ./RootApp DvdPlayer 
      202 root       3580 R   DvdPlayer 
      203 root        168 S   ./RootApp DvdPlayer 
      210 root       3580 S   DvdPlayer 
      211 root       3580 S   DvdPlayer 
      213 root       3580 S   DvdPlayer 
      215 root       3580 S   DvdPlayer 
      216 root       3580 S   DvdPlayer 
      217 root       3580 S   DvdPlayer 
      218 root       3580 S   DvdPlayer 
      219 root       3580 S   DvdPlayer 
      220 root       3580 S   DvdPlayer 
      221 root       3580 S   DvdPlayer 
      222 root       3580 S   DvdPlayer 
      223 root       3580 S   DvdPlayer 
      244 root       3580 S   DvdPlayer 
      247 root       3580 S   DvdPlayer 
      248 root       3580 S   DvdPlayer 
      249 root       3580 S   DvdPlayer 
      250 root       3580 S   DvdPlayer 
      304 root       3580 S   DvdPlayer 
      317 root        392 R   ps 
    / # watchdog test pid 202, threshold: 50
    / # ifconfiwatchdog test pid 202, threshold: 50
    eth0      Link encap:Ethernet  HWaddr 00:0A:D8:01:DA:6D  
              UP BROADCAST MULTICAST  MTU:1500  Metric:1
              RX packets:0 errors:0 dropped:0 overruns:0 frame:0
              TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000 
              RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
              Interrupt:2 Base address:0x6000 
    lo        Link encap:Local Loopback  
              inet addr:127.0.0.1  Mask:255.0.0.0
              UP LOOPBACK RUNNING  MTU:16436  Metric:1
              RX packets:0 errors:0 dropped:0 overruns:0 frame:0
              TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:0 
              RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
    / # dwatchdog test pid 202, threshold: 50
    mesg
    5, rootpath=
    yaffs: dev is 32505857 name is "mtdblock1"
    yaffs: Attempting MTD mount on 31.1, "mtdblock1"
    force MTDBLOCK1_CHECKPOINT
    save exit: isCheckpointed 0
    VFS: Mounted root (yaffs2 filesystem) readonly.
    Mounted devfs on /dev
    Freeing prom memory: 0kb freed
    Reclaim bootloader memory from 80020000 to 80100000
    Freeing unused kernel memory: 144k freed
    ------flush priority: 10 
    flush_page_cache: do flush...
    ------flush priority: 10 
    flush_page_cache: do flush...
    ------flush priority: 10 
    flush_page_cache: do flush...
    ------flush priority: 10 
    flush_page_cache: do flush...
    yaffs: dev is 32505858 name is "mtdblock2"
    yaffs: Attempting MTD mount on 31.2, "mtdblock2"
    yaffs: auto selecting yaffs2
    yaffs: restored from checkpoint
    ------flush priority: 10 
    flush_page_cache: do flush...
    libata version 1.12 loaded.
    sata driver initial...2009/11/23 11:00
    ata_device_add(4865)probe begin
    scsi0 : SATA_DRV
    sata dma reset
    set corepath: /tmp/hdd/volumes/HDD1/ 
    ***128MB version...
       Memory address 0x40000000
    try_to_free_pages: free 772 
    1. start remap DVR zone...
    save exit: isCheckpointed 1
    sata1: reset phy again!
    sata phy reset
    fastmode is 100...
    map_done is 1569...
    map_fail is 0...
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    try_to_free_pages: free 28 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 2...
    map_fail is 0...
    try_to_free_pages: free 164 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 18...
    map_fail is 0...
    try_to_free_pages: free 51 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 5...
    map_fail is 0...
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 25...
    map_fail is 0...
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    try_to_free_pages: free 218 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 26...
    map_fail is 0...
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    req: 168000, get: 200000 
    reclaim size: 80000 
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    req: aa000, get: 100000 
    reclaim size: 40000 
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    req: 2e000, get: 40000 
    reclaim size: 10000 
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    req: 66000, get: 80000 
    reclaim size: 10000 
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    req: 66000, get: 80000 
    reclaim size: 10000 
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    try_to_free_pages: free 103 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 8...
    map_fail is 0...
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    req: b0000, get: 100000 
    reclaim size: 40000 
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 1...
    map_fail is 0...
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    req: 50000, get: 80000 
    reclaim size: 20000 
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    try_to_free_pages: free 183 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 43...
    map_fail is 0...
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    req: 1c2000, get: 200000 
    reclaim size: 20000 
    =*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
    try_to_free_pages: free 0 
    1. start remap DVR zone...
    fastmode is 100...
    map_done is 0...
    map_fail is 0...
    [usb_param] setting for mars
    Setting for MARS-B
    [usb_param] set port two for host!
    [usb1_param] usbphy reg 32, set sh = 0x5, get sh = 0x5, 4bit
    [usb1_param] usbphy reg 35, set src = 0x7, get src = 0x7, 3bit
    [usb1_param] usbphy reg 36, set senh = 0xd, get senh = 0xd, 4bit
    [usb1_param] usbphy reg 32, set sen = 0x8, get sen = 0x8, 4bit
    [usb1_param] usbphy reg 33, set dr = 0x0, get dr = 0x0, 3bit
    [usb2_param] usbphy reg 32, set sh = 0x5, get sh = 0x5, 4bit
    [usb2_param] usbphy reg 35, set src = 0x7, get src = 0x7, 3bit
    [usb2_param] usbphy reg 36, set senh = 0xd, get senh = 0xd, 4bit
    [usb2_param] usbphy reg 32, set sen = 0x8, get sen = 0x8, 4bit
    [usb2_param] usbphy reg 33, set dr = 0x0, get dr = 0x0, 3bit
    ehci_hcd ehci_hcd: EHCI Host Controller
    sata1: reset phy again!
    sata phy reset
    ehci_hcd ehci_hcd: new USB bus registered, assigned bus number 1
    ehci_hcd ehci_hcd: irq 2, io mem 0xb8013000
    ehci_hcd ehci_hcd: park 0
    ehci_hcd ehci_hcd: USB 0.0 initialized, EHCI 1.00, driver 10 Dec 2004
    hub 1-0:1.0: USB hub found
    hub 1-0:1.0: 2 ports detected
    hub : individual port power switching
    hub : individual port over-current protection
    [cfyeh] set PPE = 0
    ohci_hcd: 2004 Nov 08 USB 1.1 'Open' Host Controller (OHCI) Driver (PCI)
    [usb_param] setting for mars
    Setting for MARS-B
    [usb_param] set port two for host!
    [usb1_param] usbphy reg 32, set sh = 0x5, get sh = 0x5, 4bit
    [usb1_param] usbphy reg 35, set src = 0x7, get src = 0x7, 3bit
    [usb1_param] usbphy reg 36, set senh = 0xd, get senh = 0xd, 4bit
    [usb1_param] usbphy reg 32, set sen = 0x8, get sen = 0x8, 4bit
    [usb1_param] usbphy reg 33, set dr = 0x0, get dr = 0x0, 3bit
    [usb2_param] usbphy reg 32, set sh = 0x5, get sh = 0x5, 4bit
    [usb2_param] usbphy reg 35, set src = 0x7, get src = 0x7, 3bit
    [usb2_param] usbphy reg 36, set senh = 0xd, get senh = 0xd, 4bit
    [usb2_param] usbphy reg 32, set sen = 0x8, get sen = 0x8, 4bit
    [usb2_param] usbphy reg 33, set dr = 0x0, get dr = 0x0, 3bit
    ohci_hcd ohci_hcd: OHCI Host Controller
    ohci_hcd ohci_hcd: new USB bus registered, assigned bus number 2
    ohci_hcd ohci_hcd: irq 2, io mem 0xb8013400
    hub 2-0:1.0: USB hub found
    hub 2-0:1.0: 2 ports detected
    hub : no power switching (usb 1.0)
    hub : no over-current protection
    This is the current time: PowerUP_Done!!!
    save exit: isCheckpointed 1
    sata1: reset phy extra!
    sata phy reset
    sata1: reset phy extra!
    sata phy reset
    sata1: reset phy extra!
    sata phy reset
    sata1: phy reset timeout!
    sata1: no device found (phy stat 00000000)
    sata1: ata_bus_probe failed
    scsi1 : SATA_DRV
    sata dma reset
    sata2: reset phy again!
    sata phy reset
    sata2: reset phy again!
    sata phy reset
    sata2: phy reset timeout!
    sata2: no device found (phy stat 00000000)
    sata2: ata_bus_probe failed
    / # watchdog test pid 202, threshold: 50
    / # ls
    ls      lsmod 
    / # ls
    watchdog test pid 202, threshold: 50
    -sh: lsu: not found
    / # 
    / # watchdog test pid 202, threshold: 50
    / # lsmowatchdog test pid 202, threshold: 50
    Module                  Size  Used by    Not tainted
    ohci_hcd               25200  0 
    ehci_hcd               45792  0 
    sata_mars              26464  0 
    libata                 60816  1 sata_mars
    / # watchdog test pid 202, threshold: 50
    / # ps
      PID  Uid     VmSize Stat Command
        1 root        428 S   init       
        2 root            SWN [ksoftirqd/0]
        3 root            SW< [events/0]
        4 root            SW< [khelper]
        5 root            SW< [kthread]
        6 root            SW< [kblockd/0]
        7 root            SW  [khubd]
        8 root            SW  [pdflush]
        9 root            SW  [pdflush]
       11 root            SW< [aio/0]
       10 root            SW  [kswapd0]
       12 root            SW< [cifsoplockd]
       13 root            SW< [cifsdnotifyd]
       14 root            SW  [eth0]
       15 root            SW  [mtdblockd]
       27 root        588 S   -sh 
       28 root        432 S   init       
       31 root        432 S   init       
       34 root        432 S   init       
      179 root        432 S   inetd 
      183 root            SW< [sata_eh/0]
      188 root            SW  [scsi_eh_0]
      196 root            SW  [scsi_eh_1]
      198 root        168 S   ./RootApp DvdPlayer 
      199 root        168 S   ./RootApp DvdPlayer 
      202 root       3580 S < DvdPlayer 
      203 root        168 S   ./RootApp DvdPlayer 
      210 root       3580 S   DvdPlayer 
      211 root       3580 S   DvdPlayer 
      213 root       3580 S   DvdPlayer 
      215 root       3580 S   DvdPlayer 
      216 root       3580 S   DvdPlayer 
      217 root       3580 S   DvdPlayer 
      218 root       3580 S   DvdPlayer 
      219 root       3580 S   DvdPlayer 
      220 root       3580 S   DvdPlayer 
      221 root       3580 S   DvdPlayer 
      222 root       3580 S   DvdPlayer 
      223 root       3580 S   DvdPlayer 
      244 root       3580 S   DvdPlayer 
      247 root       3580 S   DvdPlayer 
      248 root       3580 S   DvdPlayer 
      249 root       3580 S   DvdPlayer 
      250 root       3580 S   DvdPlayer 
      304 root       3580 S   DvdPlayer 
      321 root        392 R   ps 
    / # watchdog test pid 202, threshold: 50
    Test.fat    etc         lost+found  sbin        tmp_orig    vmlinux
    bin         lib         mnt         sys         usr
    dev         linuxrc     proc        tmp         var
    / # watchdog test pid 202, threshold: 50
    / # 
    / # cd biwatchdog test pid 202, threshold: 50
    / # cd bin/
    /bin # ls
    addgroup     delgroup     hostname     more         rm           true
    adduser      deluser      ip           mount        rmdir        umount
    ash          df           ipcalc       mv           sed          uname
    busybox      dmesg        kill         netstat      sh           usleep
    cat          echo         ln           nice         sleep        vi
    chmod        egrep        login        pidof        stty
    chown        false        ls           ping         sync
    cp           fgrep        mkdir        ps           tar
    date         getopt       mknod        pwd          top
    dd           grep         mktemp       replaceFile  touch
    /bin # ls watchdog test pid 202, threshold: 50
    .            date         getopt       mknod        pwd          top
    ..           dd           grep         mktemp       replaceFile  touch
    addgroup     delgroup     hostname     more         rm           true
    adduser      deluser      ip           mount        rmdir        umount
    ash          df           ipcalc       mv           sed          uname
    busybox      dmesg        kill         netstat      sh           usleep
    cat          echo         ln           nice         sleep        vi
    chmod        egrep        login        pidof        stty
    chown        false        ls           ping         sync
    cp           fgrep        mkdir        ps           tar
    /bin # ls -lawatchdog test pid 202, threshold: 50
    watchdog test pid 202, threshold: 50
    /bin # 
    /bin # watchdog test pid 202, threshold: 50
    /bin # 
    /bin # ls -watchdog test pid 202, threshold: 50
    drwxr-xr-x    1 500      500          2.0k Feb  6  2010 .
    drwxr-xr-x    1 root     root         2.0k Mar 22  2010 ..
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 addgroup -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 adduser -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 ash -> busybox
    -rwxr-xr-x    1 500      500       1017.7k Feb  8  2010 busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 cat -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 chmod -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 chown -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 cp -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 date -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 dd -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 delgroup -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 deluser -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 df -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 dmesg -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 echo -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 egrep -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 false -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 fgrep -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 getopt -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 grep -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 hostname -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 ip -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 ipcalc -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 kill -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 ln -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 login -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 ls -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 mkdir -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 mknod -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 mktemp -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 more -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 mount -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 mv -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 netstat -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 nice -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 pidof -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 ping -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 ps -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 pwd -> busybox
    -rwx------    1 500      500          9.4k Dec 28  2009 replaceFile
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 rm -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 rmdir -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 sed -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 sh -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 sleep -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 stty -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 sync -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 tar -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 top -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 touch -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 true -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 umount -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 uname -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 usleep -> busybox
    lrwxrwxrwx    1 500      500             7 Mar 22  2010 vi -> busybox
    /bin # cdwatchdog test pid 202, threshold: 50
    / # ls
    Test.fat    etc         lost+found  sbin        tmp_orig    vmlinux
    bin         lib         mnt         sys         usr
    dev         linuxrc     proc        tmp         var
    / # cwatchdog test pid 202, threshold: 50
    d watchdog test pid 202, threshold: 50
    / # ls
    Test.fat    etc         lost+found  sbin        tmp_orig    vmlinux
    bin         lib         mnt         sys         usr
    dev         linuxrc     proc        tmp         var
    / # pwatchdog test pid 202, threshold: 50
      PID  Uid     VmSize Stat Command
        1 root        428 S   init       
        2 root            SWN [ksoftirqd/0]
        3 root            SW< [events/0]
        4 root            SW< [khelper]
        5 root            SW< [kthread]
        6 root            SW< [kblockd/0]
        7 root            SW  [khubd]
        8 root            SW  [pdflush]
        9 root            SW  [pdflush]
       11 root            SW< [aio/0]
       10 root            SW  [kswapd0]
       12 root            SW< [cifsoplockd]
       13 root            SW< [cifsdnotifyd]
       14 root            SW  [eth0]
       15 root            SW  [mtdblockd]
       27 root        624 S   -sh 
       28 root        432 S   init       
       31 root        432 S   init       
       34 root        432 S   init       
      179 root        432 S   inetd 
      183 root            SW< [sata_eh/0]
      188 root            SW  [scsi_eh_0]
      196 root            SW  [scsi_eh_1]
      198 root        168 S   ./RootApp DvdPlayer 
      199 root        168 S   ./RootApp DvdPlayer 
      202 root       3580 S < DvdPlayer 
      203 root        168 S   ./RootApp DvdPlayer 
      210 root       3580 S   DvdPlayer 
      211 root       3580 S   DvdPlayer 
      213 root       3580 S   DvdPlayer 
      215 root       3580 S   DvdPlayer 
      216 root       3580 S   DvdPlayer 
      217 root       3580 S   DvdPlayer 
      218 root       3580 S   DvdPlayer 
      219 root       3580 S   DvdPlayer 
      220 root       3580 S   DvdPlayer 
      221 root       3580 S   DvdPlayer 
      222 root       3580 S   DvdPlayer 
      223 root       3580 S   DvdPlayer 
      244 root       3580 S   DvdPlayer 
      247 root       3580 S   DvdPlayer 
      248 root       3580 S   DvdPlayer 
      249 root       3580 S   DvdPlayer 
      250 root       3580 S   DvdPlayer 
      304 root       3580 S   DvdPlayer 
      328 root        392 R   ps 
    / # df
    Filesystem           1k-blocks      Used Available Use% Mounted on
    /dev/root                75392     75392         0 100% /
    /dev/mtdblock/2          40960      1312     39648   3% /usr/local/etc
    /dev/rd/0                   40        40         0 100% /mnt/rd
    / # 
    / # df
    [Jwatchdog test pid 202, threshold: 50
    / # f -lha
    -sh: f: not found
    / # watchdog test pid 202, threshold: 50
    df -lha
    df: illegal option -- l
    BusyBox v1.1.3 (2009.12.25-16:48+0000) multi-call binary
    Usage: df [-hmk] [FILESYSTEM ...]
    Print the filesystem space used and space available.
    Options:
    	-h	print sizes in human readable format (e.g., 1K 243M 2G )
    	-m	print sizes in megabytes
    	-k	print sizes in kilobytes(default)
    / # watchdog test pid 202, threshold: 50
    df -h
    Filesystem                Size      Used Available Use% Mounted on
    /dev/root                73.6M     73.6M         0 100% /
    /dev/mtdblock/2          40.0M      1.3M     38.7M   3% /usr/local/etc
    /dev/rd/0                40.0k     40.0k         0 100% /mnt/rd
    / # watchdog test pid 202, threshold: 50
    / # 
    / # watchdog test pid 202, threshold: 50
    / # 
    / # 
    / # 
    / # 
    / # watchdog test pid 202, threshold: 50
    / # 
    / # 
    / # 
    / # 
    / # watchdog test pid 202, threshold: 50
    Test.fat    etc         lost+found  sbin        tmp_orig    vmlinux
    bin         lib         mnt         sys         usr
    dev         linuxrc     proc        tmp         var
    / # ps
      PID  Uid     VmSize Stat Command
        1 root        428 S   init       
        2 root            SWN [ksoftirqd/0]
        3 root            SW< [events/0]
        4 root            SW< [khelper]
        5 root            SW< [kthread]
        6 root            SW< [kblockd/0]
        7 root            SW  [khubd]
        8 root            SW  [pdflush]
        9 root            SW  [pdflush]
       11 root            SW< [aio/0]
       10 root            SW  [kswapd0]
       12 root            SW< [cifsoplockd]
       13 root            SW< [cifsdnotifyd]
       14 root            SW  [eth0]
       15 root            SW  [mtdblockd]
       27 root        628 S   -sh 
       28 root        432 S   init       
       31 root        432 S   init       
       34 root        432 S   init       
      179 root        432 S   inetd 
      183 root            SW< [sata_eh/0]
      188 root            SW  [scsi_eh_0]
      196 root            SW  [scsi_eh_1]
      198 root        168 S   ./RootApp DvdPlayer 
      199 root        168 S   ./RootApp DvdPlayer 
      202 root       3580 S < DvdPlayer 
      203 root        168 S   ./RootApp DvdPlayer 
      210 root       3580 S   DvdPlayer 
      211 root       3580 S   DvdPlayer 
      213 root       3580 S   DvdPlayer 
      215 root       3580 S   DvdPlayer 
      216 root       3580 S   DvdPlayer 
      217 root       3580 S   DvdPlayer 
      218 root       3580 S   DvdPlayer 
      219 root       3580 S   DvdPlayer 
      220 root       3580 S   DvdPlayer 
      221 root       3580 S   DvdPlayer 
      222 root       3580 S   DvdPlayer 
      223 root       3580 S   DvdPlayer 
      244 root       3580 S   DvdPlayer 
      247 root       3580 S   DvdPlayer 
      248 root       3580 S   DvdPlayer 
      249 root       3580 S   DvdPlayer 
      250 root       3580 S   DvdPlayer 
      304 root       3580 S   DvdPlayer 
      333 root        392 R   ps 
    / # watchdog test pid 202, threshold: 50
    / # 
    / # lswatchdog test pid 202, threshold: 50
    / # watchdog test pid 202, threshold: 50
    lspci
    -sh: lspci: not found
    / # ls
    Test.fat    etc         lost+found  sbin        tmp_orig    vmlinux
    bin         lib         mnt         sys         usr
    dev         linuxrc     proc        tmp         var
    / # watchdog test pid 202, threshold: 50
    / # cd et
    / # cd etc/
    /etc # lwatchdog test pid 202, threshold: 50
    dvdplayer           ld.so.cache         reexec_init
    fstab               ld.so.conf          resolv.conf
    group               mtab                services
    hostname            passwd              sysconfig
    hosts               passwd-             system_svn_version
    httpd.conf          ppp                 udhcpc.script
    inetd.conf          ppscdn_config.ini
    init.d              profile
    /etc # cat watchdog test pid 202, threshold: 50
    hosts
    127.0.0.1	localhost
    /etc # ls
    dvdplayer           ld.so.cache         reexec_init
    fstab               ld.so.conf          resolv.conf
    group               mtab                services
    hostname            passwd              sysconfig
    hosts               passwd-             system_svn_version
    httpd.conf          ppp                 udhcpc.script
    inetd.conf          ppscdn_config.ini
    init.d              profile
    /etc # watchdog test pid 202, threshold: 50
    watchdog test pid 202, threshold: 50
    /etc # 
    /etc # ps
      PID  Uid     VmSize Stat Command
        1 root        428 S   init       
        2 root            SWN [ksoftirqd/0]
        3 root            SW< [events/0]
        4 root            SW< [khelper]
        5 root            SW< [kthread]
        6 root            SW< [kblockd/0]
        7 root            SW  [khubd]
        8 root            SW  [pdflush]
        9 root            SW  [pdflush]
       11 root            SW< [aio/0]
       10 root            SW  [kswapd0]
       12 root            SW< [cifsoplockd]
       13 root            SW< [cifsdnotifyd]
       14 root            SW  [eth0]
       15 root            SW  [mtdblockd]
       27 root        628 S   -sh 
       28 root        432 S   init       
       31 root        432 S   init       
       34 root        432 S   init       
      179 root        432 S   inetd 
      183 root            SW< [sata_eh/0]
      188 root            SW  [scsi_eh_0]
      196 root            SW  [scsi_eh_1]
      198 root        168 S   ./RootApp DvdPlayer 
      199 root        168 S   ./RootApp DvdPlayer 
      202 root       3580 S < DvdPlayer 
      203 root        168 S   ./RootApp DvdPlayer 
      210 root       3580 S   DvdPlayer 
      211 root       3580 S   DvdPlayer 
      213 root       3580 S   DvdPlayer 
      215 root       3580 S   DvdPlayer 
      216 root       3580 S   DvdPlayer 
      217 root       3580 S   DvdPlayer 
      218 root       3580 S   DvdPlayer 
      219 root       3580 S   DvdPlayer 
      220 root       3580 S   DvdPlayer 
      221 root       3580 S   DvdPlayer 
      222 root       3580 S   DvdPlayer 
      223 root       3580 S   DvdPlayer 
      244 root       3580 S   DvdPlayer 
      247 root       3580 S   DvdPlayer 
      248 root       3580 S   DvdPlayer 
      249 root       3580 S   DvdPlayer 
      250 root       3580 S   DvdPlayer 
      304 root       3580 S   DvdPlayer 
      338 root        392 R   ps 
    /etc # watchdog test pid 202, threshold: 50
    watchdog test pid 202, threshold: 50
    watchdog test pid 202, threshold: 50
    watchdog test pid 202, threshold: 50
    /etc # watchdog test pid 202, threshold: 50
    watchdog test pid 202, threshold: 50


# Links


* <http://rtd1073.wikia.com/wiki/DvdPlayer>  
* <https://www.ixbt.com/multimedia/iconbit-hds6l-hds7l/6l/07-big.jpg>  
* <http://www.hwp.ru/Multimedia/Iconbit.hds7l/images/Iconbit_HDs7l_7.jpg>  
* <https://sourceforge.net/p/smartmontools/mailman/message/31066827/>  
* <https://github.com/xtreamerdev/venus_ir_wo>  
* <https://github.com/xtreamerdev/linux-xtr>  