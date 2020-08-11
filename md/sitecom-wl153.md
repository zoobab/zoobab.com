# Pictures


# Serial Port


RX GND TX VCC

Only connecting RX GND TX was enough to get the serial access.

# Log



    =~=~=~=~=~=~=~=~=~=~=~= PuTTY log 2009.12.06 18:36:12 =~=~=~=~=~=~=~=~=~=~=~=
    +Ethernet eth0: MAC address 00:50:fc:02:03:04
    IP: 192.168.12.142/255.255.240.0, Gateway: 192.168.12.14
    Default server: 0.0.0.0
    
    RedBoot(tm) bootstrap and debug environment [ROM]
    Non-certified release, version v2_0 - built 21:05:24, Oct 17 2005
    
    Platform: PC (I386) 
    Copyright (C) 2000, 2001, 2002, Red Hat, Inc.R1
    
    RAM: 0x00000000-0x000f0000, 0x00070470-0x000a0000 available
    linux -b 0x400000 -l 0x0009be0c -s 0x00142a3d -c "console=ttyS0,38400"
    == Executing boot script in 1.000 seconds - enter ^C to abort
    RedBoot> IP: 192.168.12.142/255.255.240.0, Gateway: 192.168.12.14
    Default server: 192.168.12.148
    RedBoot> 
    mem_size: 1000000
    initrd e9d000 len 142a3d
    Linux version 2.4.25-386 (root@Fedora) (gcc version 3.3.1) #1445 Tue Jul 25 15:19:38 CST 2006
    BIOS-provided physical RAM map:
     BIOS-e801: 0000000000000000 - 000000000009f000 (usable)
     BIOS-e801: 0000000000100000 - 0000000001000000 (usable)
    16MB LOWMEM available.
    On node 0 totalpages: 4096
    zone(0): 4096 pages.
    zone(1): 0 pages.
    zone(2): 0 pages.
    DMI not present.
    Kernel command line: console=ttyS0,38400
    No local APIC present or hardware disabled
    Initializing CPU#0
    Calibrating delay loop... 50.79 BogoMIPS
    Memory: 13060k/16384k available (950k kernel code, 2936k reserved, 221k data, 84k init, 0k highmem)
    Checking if this processor honours the WP bit even in supervisor mode... Ok.
    Dentry cache hash table entries: 2048 (order: 2, 16384 bytes)
    Inode cache hash table entries: 1024 (order: 1, 8192 bytes)
    Mount cache hash table entries: 512 (order: 0, 4096 bytes)
    Buffer cache hash table entries: 1024 (order: 0, 4096 bytes)
    Page-cache hash table entries: 4096 (order: 2, 16384 bytes)
    CPU: Cyrix Cx486SLC
    Checking 'hlt' instruction... OK.
    Checking for popad bug... OK.
    POSIX conformance testing by UNIFIX
    mtrr: v1.40 (20010327) Richard Gooch (rgooch@atnf.csiro.au)
    mtrr: detected mtrr type: none
    PCI: Using configuration type 1
    PCI: Probing PCI hardware
    PCI: Probing PCI hardware (bus 00)
    Linux NET4.0 for Linux 2.4
    Based upon Swansea University Computer Society NET3.039
    Initializing RT netlink socket
    LED & GPIO & LAN Status Driver LED_VERSION 
    IA-32 Microcode Update Driver: v1.13 <tigran@veritas.com>
    Starting kswapd
    pty: 256 Unix98 ptys configured
    Serial driver version 5.05c (2001-07-08) with MANY_PORTS SHARE_IRQ SERIAL_PCI enabled
    ttyS00 at 0x03f8 (irq = 4) is a 16550A
    HDLC line discipline: version $Revision: 3.7 $, maxframe=4096
    N_HDLC line discipline registered.
    RAMDISK driver initialized: 16 RAM disks of 4096K size 1024 blocksize
    loop: loaded (max 8 devices)
    r6040: RDC R6040 net driver, version 0.8 (28March2005)
    r6040: RDC R6040 net driver, version 0.8 (28March2005)
    r6040: RDC R6040 net driver, version 0.8 (28March2005)
    PPP generic driver version 2.4.2
    PPP Deflate Compression module registered
    PPP BSD Compression module registered
    MX29LV320B flash device: 200000 at ffe00000
     Amd/Fujitsu Extended Query Table v1.0 at 0x0040
    number of CFI chips: 1
    cfi_cmdset_0002: Disabling fast programming due to code brokenness.
    Creating 1 MTD partitions on "MX29LV320B flash device":
    0x00000000-0x001f0000 : "Flash Disk 1"
    MX29LV320B flash device initialized
    NET4: Linux TCP/IP 1.0 for NET4.0
    IP Protocols: ICMP, UDP, TCP
    IP: routing cache hash table of 512 buckets, 4Kbytes
    TCP: Hash tables configured (established 1024 bind 2048)
    ip_conntrack version 2.1 (128 buckets, 1024 max) - 336 bytes per conntrack
    ip_tables: (C) 2000-2002 Netfilter core team
    ipt_recent v0.2.3: Stephen Frost <sfrost@snowman.net>.  http://snowman.net/projects/ipt_recent/
    ipt_time loading
    NET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
    NET4: Ethernet Bridge 008 for NET4.0
    aaaaaaaaaaa
    bbbbbbbbbbb
    RAMDISK: Compressed image found at block 0
    Uncompressing....... <5>done 
    Freeing initrd memory: 1290k freed
    VFS: Mounted root (ext2 filesystem).
    dddddddddd
    Freeing unused kernel memory: 84k freed
    run_init_process:/sbin/init, env PATH=/bin:/usr/bin:/sbin
    insmod: islpc
    
    Please press Enter to activate this console. Sat Jan  1 00:00:00 UTC 2000
     R6040 phyAddr=5, Link at Full duplex
     R6040 phyAddr=4, Link at Full duplex
    killall: pptp.sh: no process killed
    
    killall: pppoe.sh: no process killed
    Initialize WLAN interface
    Using /bin/rt61ap.o
    *RT61*<7>===> RT61_init_one
    *RT61*<7>Driver version-1.0.6.0
    *RT61*<7>ra0: at 0xd5000000, VA 0xc1a52000, IRQ 12. 
    *RT61*<7><=== RT61_init_one
    *RT61*<7>===> NICLoadFirmware
    *RT61*<7>NICLoadFirmware: CRC ok, ver=1.0
    *RT61*<7><=== NICLoadFirmware (src=/etc/Wireless/RT61AP/RT2661.bin, status=0)
    *RT61*<7>--> RTMPAllocAdapterBlock
    *RT61*<7><-- RTMPAllocAdapterBlock
    *RT61*<7>--> RTMPAllocDMAMemory
    *RT61*<7>TxRing[0]: total 96 entry allocated
    *RT61*<7>TxRing[1]: total 96 entry allocated
    *RT61*<7>TxRing[2]: total 96 entry allocated
    *RT61*<7>TxRing[3]: total 96 entry allocated
    *RT61*<7>TxRing[4]: total 96 entry allocated
    *RT61*<7>MGMT Ring: total 32 entry allocated
    *RT61*<7>Rx Ring: total 96 entry allocated
    *RT61*<7><-- RTMPAllocDMAMemory
    *RT61*<7><--> NICInitTxRxRingAndBacklogQueue
    *RT61*<7>--> MLME Initialize
    *RT61*<7><-- MLME Initialize
    *RT61*<7>--> PortCfgInit
    *RT61*<7><-- PortCfgInit
    *RT61*<7>--> NICInitializeAdapter
    *RT61*<7>--> NICInitializeAsic
    *RT61*<7>BBP version = 48
    *RT61*<7><-- NICInitializeAsic
    *RT61*<7><-- NICInitializeAdapter
    *RT61*<7>CountryRegion=5
    *RT61*<7>SSID[0]=Sitecom
    *RT61*<7>PhyMode=1
    *RT61*<7>I/F(ra0) TxRate=(16,00,00,00,00,00,00,00,00,00,00,00)
    *RT61*<7>Channel=1
    *RT61*<7>BasicRate=3
    *RT61*<7>BeaconPeriod=100
    *RT61*<7>DtimPeriod=3
    *RT61*<7>TxPower=100
    *RT61*<7>BGProtection=2
    *RT61*<7>OLBCDetection=0
    *RT61*<7>TxAntenna=-1
    *RT61*<7>RxAntenna=
    *RT61*<7>TxPreamble=0
    *RT61*<7>RTSThreshold=2347
    *RT61*<7>FragThreshold=2346
    *RT61*<7>TxBurst=0
    *RT61*<7>PktAggregate=1
    *RT61*<7>TurboRate=1
    *RT61*<7>I/F(ra0) WmmCapable=1
    *RT61*<7>I/F(ra0) NoForwarding=0
    *RT61*<7>NoForwardingBTNBSSID=0
    *RT61*<7>I/F(ra0) HideSSID=0
    *RT61*<7>ShortSlot=1
    *RT61*<7>AutoChannelAtBootup=0
    *RT61*<7>IEEE8021X=0
    *RT61*<7>IEEE80211H=0
    *RT61*<7>CSPeriod=10
    *RT61*<7>I/F(ra0) AuthMode=2
    *RT61*<7>I/F(ra0) EncrypType=0
    *RT61*<7>ReKeyMethod=2
    *RT61*<7>PMKCachePeriod=60000
    *RT61*<7>I/F(ra0) DefaultKeyID(0~3)=0
    *RT61*<7>I/F(ra0) Key1Str=1674ae0cb1814e95bcfc44263d and type=Hex
    *RT61*<7>I/F(ra0) Key2Str=00000000000000000000000000 and type=Hex
    *RT61*<7>I/F(ra0) Key3Str=00000000000000000000000000 and type=Hex
    *RT61*<7>I/F(ra0) Key4Str=00000000000000000000000000 and type=Hex
    *RT61*<7>HSCounter=0
    *RT61*<7>AccessPolicy0=0
    *RT61*<7>WDS-Enable mode=0
    *RT61*<7>WDS-AP(00) (0)-00:00:00:00:00:00
    *RT61*<7>WDS-AP(01) (0)-00:00:00:00:00:00
    *RT61*<7>WDS-AP(02) (0)-00:00:00:00:00:00
    *RT61*<7>WDS-AP(03) (0)-00:00:00:00:00:00
    *RT61*<7>--> NICReadEEPROMParameters
    *RT61*<7>MBSSID[0] MAC=00:0c:f6:23:9f:53
    *RT61*<7>E2PROM: Version = 1, FAE release #0
    *RT61*<7>E2PROM: G Tssi[-4 .. +4] = 255 255 255 255 - 255 -255 255 255 255, step=255, tuning=0
    *RT61*<7>E2PROM: A Tssi[-4 .. +4] = 255 255 255 255 - 255 -255 255 255 255, step=255, tuning=0
    *RT61*<7>E2PROM: RF freq offset=0x1c, RF programming seq=0
    *RT61*<7>TxPowerDelta Config (Delta=0, Sign=0, Enable=0)
    *RT61*<7><-- NICReadEEPROMParameters
    *RT61*<7>country code=5/0, RFIC=1, PHY mode=1, support 14 channels
    *RT61*<7>channel #1
    *RT61*<7>channel #2
    *RT61*<7>channel #3
    *RT61*<7>channel #4
    *RT61*<7>channel #5
    *RT61*<7>channel #6
    *RT61*<7>channel #7
    *RT61*<7>channel #8
    *RT61*<7>channel #9
    *RT61*<7>channel #10
    *RT61*<7>channel #11
    *RT61*<7>channel #12
    *RT61*<7>channel #13
    *RT61*<7>channel #14
    *RT61*<7>IF(ra0) RTMPSetPhyMode(=1)
    *RT61*<7>I/F(ra0) TxRate=(16,00,00,00,00,00,00,00,00,00,00,00)
    *RT61*<7>--> NICInitAsicFromEEPROM
    *RT61*<7>RFIC=4, LED mode=0
    *RT61*<7><-- NICInitAsicFromEEPROM
    *RT61*<7>Register WDS(virtual) interface(ra1)-00:00:00:00:00:00
    *RT61*<7>Register WDS(virtual) interface(ra2)-00:00:00:00:00:00
    *RT61*<7>Register WDS(virtual) interface(ra3)-00:00:00:00:00:00
    *RT61*<7>Register WDS(virtual) interface(ra4)-00:00:00:00:00:00
    *RT61*<7>---> ApInitialize
    *RT61*<7><--- ApInitialize
    *RT61*<7>---> ApStartUp
    *RT61*<7>IF(ra0) CapabilityInfo=11, WepStatus=0
    *RT61*<7>IF(ra0)-AP AuthMode=2, disable Pairwise Key Table
    *RT61*<7>AsicRemoveSharedKeyEntry: #0 
    *RT61*<7>AsicRemoveSharedKeyEntry: #1 
    *RT61*<7>AsicRemoveSharedKeyEntry: #2 
    *RT61*<7>AsicRemoveSharedKeyEntry: #3 
    *RT61*<7>AsicAddSharedKeyEntry(BssIndex=0): wep128 key #0
    *RT61*<7>     Key =16:74:ae:0c:b1:81:4e:95:bc:fc:44:26:3d:00:00:00:
    *RT61*<7>AsicAddSharedKeyEntry(BssIndex=0): wep128 key #1
    *RT61*<7>     Key =00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:
    *RT61*<7>AsicAddSharedKeyEntry(BssIndex=0): wep128 key #2
    *RT61*<7>RSSI=-121, CCA=0, --R17= 0x3f, R62=4 
    *RT61*<7>     Key =00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:
    *RT61*<7>AsicAddSharedKeyEntry(BssIndex=0): wep128 key #3
    *RT61*<7>     Key =00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:
    *RT61*<7>AsicSetEdcaParm
    *RT61*<7>AP [Cnt#0]: AIFSN CWmin CWmax TXOP(us)  ACM
    *RT61*<7>    AC_BE     0     0     0        0     0
    *RT61*<7>    AC_BK     0     0     0        0     0
    *RT61*<7>    AC_VI     0     0     0        0     0
    *RT61*<7>    AC_VO     0     0     0        0     0
    *RT61*<7>STA        : AIFSN CWmin CWmax TXOP(us)  ACM
    *RT61*<7>    AC_BE     0     0   0       0     0
    *RT61*<7>    AC_BK     0     0   0       0     0
    *RT61*<7>    AC_VI     0     0     0       0     0
    *RT61*<7>    AC_VO     0     0     0        0     0
    *RT61*<7>AsicSwitchChannel(RF=4, Pwr=5) to #1, R1=0x95002ccc, R2=0x95004786, R3=0x95068a55, R4=0x950dca0b
    *RT61*<7>UpdateBasicRateBitmap::(BasicRateBitMap=3)(82,84,0b,16,00,00,00,00,00,00,00,00)
    *RT61*<7>IF(ra0) MlmeUpdateTxRates (MaxDesire=11 Mbps, MaxSupport=11 Mbps, MaxTxRate=11 Mbps, Rate Switching =0)
    *RT61*<7> MlmeUpdateTxRates (RtsRate=11 Mbps, MlmeRate=1 Mbps, BasicRateBitmap=0x0003)
    *RT61*<7>MakeBssBeacon(ra0)(FrameLen=80,TimIELocateInBeacon=80,CapInfoLocateInBeacon=34)
    *RT61*<7>SW interrupt MCU (cmd=0x60, token=0xff, arg1,arg0=0x00,0x00)
    *RT61*<7>--->AsicEnableBssSync(INFRA mode)
    *RT61*<7>--->Disable TSF synchronization
    *RT61*<7>LOG#0 00:0c:f6:23:9f:53 restart access point
    *RT61*<7><--- ApStartUp (sec_csr4=0x0)
    *RT61*<7>==> Set_Debug_Proc *******************
    Setup BRIDGE interface
    
    SIOCGIFFLAGS: No such device
    bridge br0 doesn't exist; can't delete it
    Setup bridge...
    device eth0 entered promiscuous mode
     R6040 phyAddr=5, Link at Full duplex
    SIOCDELRT: No such process
    
    device ra0 entered promiscuous mode
    ra0: attempt to add interface with same source address.
    SIOCDELRT: No such process
    
    br0: port 2(ra0) entering listening state
    br0: port 1(eth0) entering listening state
    SIOCDELRT: No such process
    
    SIOCDELRT: No such process
    Static DHCP Leases disable!
    SIOCDELRT: No such process
    udhcpd (v0.9.9-pre) started
    max_leases value (254) not sane, setting to 101 instead
    Setup WAN interface
    br0: port 2(ra0) entering learning state
    br0: port 1(eth0) entering learning state
    ********** run Diagd **********
    
    setting: port: 31727 
    running in daemon mode
    ********** run GaTest **********
    
    rm: cannot remove `/tmp/agentenabledflag': No such file or directory
    udhcp client (v0.9.9-pre) started
    into eth1.deconfig
    -sh: /etc/stupid-ftpd/ftpd: not found
    [?3l[2J[20;1H-------------------------------------------------------------------------------[21;1H[7m[21;1H<TAB> Select                     <ESC> Exit                     <Enter> Enter[0m[4;10HPlease enter your Name and Password[8;2H[7mUser Name[0m[8;14H:br0: port 2(ra0) entering forwarding state
    br0: topology change detected, propagating
    br0: port 1(eth0) entering forwarding state
    br0: topology change detected, propagating


# Links


* <http://oldwiki.openwrt.org/OpenWrtDocs>  (2f)Hardware(2f)Sitecom(2f)WL(2d)153.html
* <http://sites.google.com/site/bifferboard/openwrt-svn>  
* <http://www.ivankuten.com/system-on-chip-soc/rdc-r8610/>  
* <http://nuwiki.openwrt.org/oldwiki/rdcport>  