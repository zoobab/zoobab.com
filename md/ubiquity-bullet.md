# Images


[[=image <<http://www.digdice.com/wp-content/uploads/2009/01/ubiquiti-bullet-2-and-bullet-5-back.jpg>  >  ]]
[[=image <<http://www.digdice.com/wp-content/uploads/2009/01/ubiquiti-bullet-2-and-bullet-5.jpg>  >  ]]

http://www.digdice.com/wp-content/uploads/2009/01/ubiquiti-bullet-2-and-bullet-5.jpg
http://www.digdice.com/wp-content/uploads/2009/01/ubiquiti-bullet-2-and-bullet-5-back.jpg

# Dmesg



    zoobab@warsaw /home/zoobab [1]$ telnet 192.168.0.42
    Trying 192.168.0.42...                             
    Connected to 192.168.0.42.                         
    Escape character is '^]'.                          
     === IMPORTANT ============================        
      Use 'passwd' to set your login password          
      this will disable telnet and enable SSH          
     ------------------------------------------        
    
    
    BusyBox v1.11.2 (2009-01-05 06:34:55 CET) built-in shell (ash)
    Enter 'help' for a list of built-in commands.                 
    
      _______                     ________        __
     |       |.-----.-----.-----.|  |  |  |.----.|  |_
     |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
     |_______||   __|_____|__|__||________||__|  |____|
              |__| W I R E L E S S   F R E E D O M     
     KAMIKAZE (8.09, r14127) ----------------------------
      * 10 oz Vodka       Shake well with ice and strain 
      * 10 oz Triple sec  mixture into 10 shot glasses.  
      * 10 oz lime juice  Salute!                        
     --------------------------------------------------- 
    root@wifi-momo:/# dmesg                              
    Linux version 2.6.26.5 (nbd@baustelle) (gcc version 4.1.2) #13 Wed Jan 21 02:13:07 CET 2009
    CPU revision is: 00019064 (MIPS 4KEc)                                                      
    Determined physical RAM map:                                                               
     memory: 01000000 @ 00000000 (usable)                                                      
    Entering add_active_range(0, 0, 4096) 0 entries of 256 used                                
    Initrd not found or empty - disabling initrd                                               
    Zone PFN ranges:                                                                           
      Normal          0 ->     4096                                                            
    Movable zone start PFN for each node                                                       
    early_node_map[1] active PFN ranges                                                        
        0:        0 ->     4096                                                                
    On node 0 totalpages: 4096                                                                 
      Normal zone: 32 pages used for memmap                                                    
      Normal zone: 0 pages reserved                                                            
      Normal zone: 4064 pages, LIFO batch:0                                                    
      Movable zone: 0 pages used for memmap                                                    
    Built 1 zonelists in Zone order, mobility grouping off.  Total pages: 4064                                                                     
    Kernel command line: console=ttyS0,9600 rootfstype=squashfs,jffs2 init=/etc/preinit                                                            
    Primary instruction cache 16kB, VIPT, 4-way, linesize 16 bytes.                                                                                
    Primary data cache 16kB, 4-way, VIPT, no aliases, linesize 16 bytes                                                                            
    PID hash table entries: 64 (order: 6, 256 bytes)                                                                                               
    console [ttyS0] enabled                                                                                                                        
    Dentry cache hash table entries: 2048 (order: 1, 8192 bytes)                                                                                   
    Inode-cache hash table entries: 1024 (order: 0, 4096 bytes)                                                                                    
    Memory: 13564k/16384k available (1876k kernel code, 2820k reserved, 310k data, 124k init, 0k highmem)                                          
    SLUB: Genslabs=6, HWalign=32, Order=0-3, MinObjects=0, CPUs=1, Nodes=1                                                                         
    Calibrating delay loop... 183.50 BogoMIPS (lpj=917504)                                                                                         
    Mount-cache hash table entries: 512                                                                                                            
    net_namespace: 644 bytes                                                                                                                       
    NET: Registered protocol family 16                                                                                                             
    Radio config found at offset 0xf8(0x1f8)                                                                                                       
    Switched to high resolution mode on CPU 0                                                                                                      
    NET: Registered protocol family 2                                                                                                              
    IP route cache hash table entries: 1024 (order: 0, 4096 bytes)                                                                                 
    TCP established hash table entries: 512 (order: 0, 4096 bytes)                                                                                 
    TCP bind hash table entries: 512 (order: -1, 2048 bytes)                                                                                       
    TCP: Hash tables configured (established 512 bind 512)                                                                                         
    TCP reno registered                                                                                                                            
    NET: Registered protocol family 1                                                                                                              
    ar531x: Registering GPIODEV device                                                                                                             
    squashfs: version 3.0 (2006/03/15) Phillip Lougher                                                                                             
    Registering mini_fo version $Id$                                                                                                               
    JFFS2 version 2.2. (NAND) (SUMMARY)  © 2001-2006 Red Hat, Inc.                                                                                 
    msgmni has been set to 26                                                                                                                      
    io scheduler noop registered                                                                                                                   
    io scheduler deadline registered (default)                                                                                                     
    gpiodev: gpio device registered with major 254                                                                                                 
    gpiodev: gpio platform device registered with access mask FFFFFFFF                                                                             
    Serial: 8250/16550 driver $Revision: 1.90 $ 1 ports, IRQ sharing disabled                                                                      
    serial8250: ttyS0 at MMIO 0xb1100003 (irq = 37) is a 16550A                                                                                    
    eth0: Atheros AR231x: 00:15:6d:ae:05:92, irq 4                                                                                                 
    ar2313_eth_mii: probed                                                                                                                         
    eth0: attached PHY driver [Generic PHY] (mii_bus:phy_addr=0:01)                                                                                
    cmdlinepart partition parsing not available                                                                                                    
    Searching for RedBoot partition table in spiflash at offset 0x3d0000                                                                           
    Searching for RedBoot partition table in spiflash at offset 0x3e0000                                                                           
    7 RedBoot partitions found on MTD device spiflash                                                                                              
    Creating 7 MTD partitions on "spiflash":                                                                                                       
    0x00000000-0x00030000 : "RedBoot"                                                                                                              
    0x00030000-0x000f0000 : "kernel"                                                                                                               
    0x000f0000-0x003c0000 : "rootfs"                                                                                                               
    mtd: partition "rootfs" set to be root filesystem                                                                                              
    mtd: partition "rootfs_data" created automatically, ofs=270000, len=150000
    0x00270000-0x003c0000 : "rootfs_data"
    0x003c0000-0x003e0000 : "cfg"
    0x003e0000-0x003ef000 : "FIS directory"
    0x003ef000-0x003f0000 : "RedBoot config"
    0x003f0000-0x00400000 : "boardconfig"
    Registered led device: gpio1
    Registered led device: gpio2
    Registered led device: gpio3
    Registered led device: gpio4
    Registered led device: wlan
    TCP vegas registered
    NET: Registered protocol family 17
    802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
    All bugs added by David S. Miller <davem@redhat.com>
    VFS: Mounted root (squashfs filesystem) readonly.
    Freeing unused kernel memory: 124k freed
    Please be patient, while OpenWrt loads ...
    Algorithmics/MIPS FPU Emulator v1.5
    mini_fo: using base directory: /
    mini_fo: using storage directory: /jffs
    PPP generic driver version 2.4.2
    ip_tables: (C) 2000-2006 Netfilter Core Team
    nf_conntrack version 0.5.0 (1024 buckets, 4096 max)
    wlan: trunk
    ath_hal: module license 'Proprietary' taints kernel.
    ath_hal: 2008-10-02 (AR5212, AR5312, RF5111, RF5112, RF2316, RF2317, REGOPS_FUNC, TX_DESC_SWAP, DFS, XR)
    ath_rate_minstrel: Minstrel automatic rate control algorithm 1.2 (trunk)
    ath_rate_minstrel: look around rate set to 10%
    ath_rate_minstrel: EWMA rolloff level set to 75%
    ath_rate_minstrel: max segment size in the mrr set to 6000 us
    wlan: mac acl policy registered
    ath_ahb: trunk
    Atheros HAL provided by OpenWrt, DD-WRT and MakSat Technologies
    wifi0: 11b rates: 1Mbps 2Mbps 5.5Mbps 11Mbps
    wifi0: 11g rates: 1Mbps 2Mbps 5.5Mbps 11Mbps 6Mbps 9Mbps 12Mbps 18Mbps 24Mbps 36Mbps 48Mbps 54Mbps
    wifi0: turboG rates: 6Mbps 12Mbps 18Mbps 24Mbps 36Mbps 48Mbps 54Mbps
    wifi0: H/W encryption support: WEP AES AES_CCM TKIP
    ath_ahb: wifi0: Atheros 2317 WiSoC REV1: mem=0xb0000000, irq=3
    eth0: Configuring MAC for full duplex
    root@wifi-momo:/#


# Cpuinfo



    root@wifi-momo:~# cat /proc/cpuinfo
    system type             : Atheros AR2317
    processor               : 0
    cpu model               : MIPS 4KEc V6.4
    BogoMIPS                : 183.50
    wait instruction        : yes
    microsecond timers      : yes
    tlb_entries             : 16
    extra interrupt vector  : yes
    hardware watchpoint     : no
    ASEs implemented        :
    shadow register sets    : 1
    core                    : 0
    VCED exceptions         : not available
    VCEI exceptions         : not available


# Df



    root@wifi-momo:~# df
    Filesystem           1k-blocks      Used Available Use% Mounted on
    rootfs                    1536      1536         0 100% /
    /dev/root                 1536      1536         0 100% /rom
    tmpfs                     6844        36      6808   1% /tmp
    tmpfs                      512         0       512   0% /dev
    /dev/mtdblock3            1344       212      1132  16% /jffs
    mini_fo:/jffs             1536      1536         0 100% /
    root@wifi-momo:~# df -h
    Filesystem                Size      Used Available Use% Mounted on
    rootfs                    1.5M      1.5M         0 100% /
    /dev/root                 1.5M      1.5M         0 100% /rom
    tmpfs                     6.7M     36.0k      6.6M   1% /tmp
    tmpfs                   512.0k         0    512.0k   0% /dev
    /dev/mtdblock3            1.3M    212.0k      1.1M  16% /jffs
    mini_fo:/jffs             1.5M      1.5M         0 100% /
    root@wifi-momo:~#


# Top



    Mem: 10608K used, 3080K free, 0K shrd, 1152K buff, 3848K cached
    CPU:   0% usr  16% sys   0% nice  83% idle   0% io   0% irq   0% softirq
    Load average: 0.00 0.07 0.05
