# Pictures


[[=image netgear-wndr3800-back.jpg size="small"]]
[[=image netgear-wndr3800-front.jpg size="small"]]

# Screenlog



    U-Boot 1.1.4 (May 27 2011 - 14:58:01)
    DNI HW ID: 29763654 flash 16MB RAM 128MB (ar7100) U-boot dni25 V0.1
    DRAM:  b8050000: 0xc0140180
    128 MB
    Top of RAM usable for U-Boot at: 88000000
    Reserving 265k for U-Boot at: 87fbc000
    Reserving 192k for malloc() at: 87f8c000
    Reserving 44 Bytes for Board Info at: 87f8bfd4
    Reserving 36 Bytes for Global Data at: 87f8bfb0
    Reserving 128k for boot params() at: 87f6bfb0
    Stack Pointer at: 87f6bf98
    Now running in RAM - U-Boot at: 87fbc000
    id read 0x100000ff
    flash size 16MB, sector count = 256
    Flash: 16 MB
    *** Warning - bad CRC, using default environment
    In:    serial
    Out:   serial
    Err:   serial
    Net:   ag7100_enet_initialize...
    CHH:mac: 0 if: 2
    CHH:mac:verify: 0 if: 00000002
    : cfg1 0xf cfg2 0x7014
    in rtl8366s_phy_setup mac=-1476803788
    after rtl8366s_initChip ret=0
    eth0: 20:4e:7f:5a:cd:30
    eth0 up
    CHH:mac: 1 if: 1
    CHH:mac:verify: 1 if: 00000001
    : cfg1 0xf cfg2 0x7014
    in rtl8366s_phy_setup mac=-1476803308
    eth1: 20:4e:7f:5a:cd:31
    eth1 up
    eth0, eth1
    Trying eth0
    : unit 0 phy is up...RGMii 1000Mbps full duplex
    #259:ag7100_set_mac_from_link
    : pll reg 0x18050010: 0x11110000  
    : cfg_1: 0x1ff0000
    : cfg_2: 0x3ff
    : cfg_3: 0x8001ff
    : cfg_4: 0xffff
    : cfg_5: 0xfffef
    : done cfg2 0x7215 ifctl 0x40605060 miictrl 0x22 
     Client starts...[Listening] for ADVERTISE...TTT
    Retry count exceeded; boot the image as usual
     nmrp server is stopped or failed !
    Hit any key to stop autoboot:  1 
       Verifying Checksum ... OK
    ### SQUASHFS loading 'image/uImage' to 0x80800000
    ### SQUASHFS load complete: 846065 bytes loaded to 0x80800000
    ## Booting image at 80800000 ...
       Image Name:   MIPS OpenWrt Linux-2.6.32.10
       Created:      2011-08-22  10:56:45 UTC
       Image Type:   MIPS Linux Kernel Image (lzma compressed)
       Data Size:    846001 Bytes = 826.2 kB
       Load Address: 80060000
       Entry Point:  80060000
       Verifying Checksum ... OK
       Uncompressing Kernel Image ... OK
    No initrd
    ## Transferring control to Linux (at address 80060000) ...
    ## Giving linux memsize in bytes, 134217728
    Starting kernel ...
    Linux version 2.6.32.10 (tatha@localhost.localdomain) (gcc version 4.3.3 (GCC) ) #1 Mon Aug 22 16:26:31 IST 2011
    flash_size passed from bootloader = 16
    bootconsole [early0] enabled
    CPU revision is: 00019374 (MIPS 24Kc)
    Atheros AR7161 rev 2, CPU:680.000 MHz, AHB:170.000 MHz, DDR:340.000 MHz
    Determined physical RAM map:
     memory: 08000000 @ 00000000 (usable)
    Initrd not found or empty - disabling initrd
    Zone PFN ranges:
      Normal   0x00000000 -> 0x00008000
    Movable zone start PFN for each node
    early_node_map[1] active PFN ranges
        0: 0x00000000 -> 0x00008000
    Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 32512
    Kernel command line: console=ttyS0,115200 root=/dev/mtdblock3 rootfstype=squashfs init=/etc/preinit
    PID hash table entries: 512 (order: -1, 2048 bytes)
    Dentry cache hash table entries: 16384 (order: 4, 65536 bytes)
    Inode-cache hash table entries: 8192 (order: 3, 32768 bytes)
    Primary instruction cache 64kB, VIPT, 4-way, linesize 32 bytes.
    Primary data cache 32kB, 4-way, VIPT, cache aliases, linesize 32 bytes
    Writing ErrCtl register=00000000
    Readback ErrCtl register=00000000
    Memory: 126776k/131072k available (2013k kernel code, 4132k reserved, 377k data, 136k init, 0k highmem)
    SLUB: Genslabs=7, HWalign=32, Order=0-3, MinObjects=0, CPUs=1, Nodes=1
    Hierarchical RCU implementation.
    NR_IRQS:56
    Calibrating delay loop... 452.19 BogoMIPS (lpj=2260992)
    Mount-cache hash table entries: 512
    NET: Registered protocol family 16
    MIPS: machine is NETGEAR WNDR3800
    registering PCI controller with io_map_base unset
    bio: create slab <bio-0> at 0
    pci 0000:00:00.0: PME# supported from D0 D1 D2 D3hot
    pci 0000:00:00.0: PME# disabled
    PCI: fixup device 0000:00:11.0
    pci 0000:00:11.0: PME# supported from D0 D3hot
    pci 0000:00:11.0: PME# disabled
    PCI: fixup device 0000:00:12.0
    pci 0000:00:12.0: PME# supported from D0 D3hot
    pci 0000:00:12.0: PME# disabled
    PCI: mapping irq 48 to pin1@0000:00:11.0
    PCI: mapping irq 49 to pin1@0000:00:12.0
    Switching to clocksource MIPS
    NET: Registered protocol family 2
    IP route cache hash table entries: 1024 (order: 0, 4096 bytes)
    TCP established hash table entries: 4096 (order: 3, 32768 bytes)
    TCP bind hash table entries: 4096 (order: 2, 16384 bytes)
    TCP: Hash tables configured (established 4096 bind 4096)
    TCP reno registered
    NET: Registered protocol family 1
    squashfs: version 4.0 (2009/01/31) Phillip Lougher
    Registering mini_fo version $Id$
    JFFS2 version 2.2. (NAND) (SUMMARY)  
     2001-2006 Red Hat, Inc.
    yaffs Aug 22 2011 16:22:17 Installing. 
    msgmni has been set to 247
    io scheduler noop registered
    io scheduler deadline registered (default)
    Serial: 8250/16550 driver, 1 ports, IRQ sharing disabled
    serial8250.0: ttyS0 at MMIO 0x18020000 (irq = 11) is a 16550A
    console [ttyS0] enabled, bootconsole disabled
    console [ttyS0] enabled, bootconsole disabled
    Atheros AR71xx SPI Controller driver version 0.2.4
    m25p80 spi0.0: mx25l12805d (16384 Kbytes)
    Searching for RedBoot partition table in spi0.0 at offset 0xfe0000
    Searching for RedBoot partition table in spi0.0 at offset 0xff0000
    No RedBoot partition table detected in spi0.0
    Creating 10 MTD partitions on "spi0.0":
    0x000000000000-0x000000050000 : "uboot"
    0x000000050000-0x000000070000 : "env"
    0x000000070000-0x000000eb0000 : "kernel"
    0x000000170000-0x000000eb0000 : "rootfs"
    mtd: partition "rootfs" set to be root filesystem
    mtd: partition "rootfs_data" created automatically, ofs=450000, len=A60000 
    0x000000450000-0x000000eb0000 : "rootfs_data"
    0x000000eb0000-0x000000ec0000 : "config"
    0x000000ec0000-0x000000ed0000 : "config_bak"
    0x000000ed0000-0x000000ee0000 : "pot"
    0x000000ee0000-0x000000ef0000 : "traffic_meter"
    0x000000ef0000-0x000000f10000 : "language"
    0x000000ff0000-0x000001000000 : "caldata"
    Realtek RTL8366S ethernet switch driver version 0.2.1
    rtl8366s rtl8366s: using GPIO pins 5 (SDA) and 7 (SCK)
    rtl8366s rtl8366s: RTL8366 ver. 1 chip found
    rtl8366-rtl: probed
    eth0: Atheros AG71xx at 0xb9000000, irq 4
    eth1: Atheros AG71xx at 0xba000000, irq 5
    Atheros AR71xx hardware watchdog driver version 0.1.0
    TCP westwood registered
    NET: Registered protocol family 17
    802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
    All bugs added by David S. Miller <davem@redhat.com>
    VFS: Mounted root (squashfs filesystem) readonly on device 31:3.
    Freeing unused kernel memory: 136k freed
    Please be patient, while OpenWrt loads ...
    udev: starting version 142
    gpio-buttons driver version 0.1.2
    input: gpio-buttons as /devices/platform/gpio-buttons/input/input0
    pio-buttons drivnput: gpio-butto: gpio-butto gpio-buttogpio-buttopio-buttoio-buttoo-butto-buttoButton Hotplug driver version 0.3.1
    buttodriver version 0eth0: link up (1000Mbps/Full duplex)
    uttodriver version 0th0: link up (10- preinit -
    ttodriver version 0t
    todriver version 0t
    odriver version 
    driver version 
    river version 
    iver version 
    Registered led device: wndr3800:green:power
    Registered led device: wndr3800:orange:power
    ver version 
    gistered led devegistRegistered led device: wndr3800:green:wps
    ered led
    :pver version 
    gisRegistered led device: wndr3800:orange:wps
    tered led devRegistered led device: wndr3800:green:wan
     led
    :pver version 
    gisndr3800tegistered led devd
    :pver version 
    gisnd
    :pver version 
    gisnd:pver version 
    gisndPress the [f] key and hit [enter] to enter failsafe mode
    pver version 
    gisnd the [f] key and hit [emode
    pver version 
    [emode
    pver version
    pver version
    - regular preinit -
     regular preinit 
    regular preinit egular preinit gular preinit ular preinit lar preinit ar preinit r preinit  preinit preinit reinit einit init nit it t  switching to jffs2
    witching to jffs2
    mini_fo: using base directory: /
    mini_fo: using storage directory: /overlay
    itttyS0: 9 input overrun(s)
    ching to jff
    ing base directodirectory: /over overrun(s)
    ching to 
    ctory: /over overrun(s
    hing to 
    ctorying to 
    ctoryng to 
    ctoryg to 
    ctory to 
    ctoryto 
    ctoryo 
    ctory 
    ctory
    ctoryctoryCollected errors:
     * opkg_conf_init: Could not create lock file /var/lock/opkg.lock: No such file or directory.
    ollected erro
    Could not create lock 
    : No such file or dire
    ould not create 
    dire
    ould not create 
    ould not cre
    ould not 
    ould not 
    ould not 
    ould not 
    uld not 
    ld not 
    d not 
     not 
    not 
    - init -
     init -
    eth0: link down
    init -
    nit -
    it -
    Please press Enter to activate this console. t -
    BusyBox v1.15.3 (2011-08-22 15:59:17 IST) built-in shell (ash)
    Enter 'help' for a list of built-in commands.
    press Enter to activat
    (2011-08-22 15:59:17 IS
    Enter 'help' for a li
      _______                     ________        __
     |       |.-----.-----.-----.|  |  |  |.----.|  |_
     |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
     |_______||   __|_____|__|__||________||__|  |____|
              |__| W I R E L E S S   F R E E D O M
     Backfire (10.03, unknown) --------------------------
      * 1/3 shot Kahlua    In a shot glass, layer Kahlua 
      * 1/3 shot Bailey's  on the bottom, then Bailey's, 
      * 1/3 shot Vodka     then Vodka.
     ---------------------------------------------------
    root@(none):/# 
    root@(none):/# itching to jff
    ing base directodirectory: /over overrun(s)
    /bin/ash: syntax error: unexpected "("
    root@(none):/# 
    root@(none):/# ching to 
    ctory: /over overrun(s
    hing to 
    ctorying to 
    ctoryng to
    ctoryg to 
    ctory to 
    ctoryto 
    ctoryo 
    ctory 
    ctory
    ctoryctoryollected erro
    ld not create lock 
    : No such file or dire
    ould not create 
    dire
    ould not create
    ould not cre
    ould not 
    ould not 
    ould not 
    ould not 
    uld not 
    ld not
    d not 
     not 
    not 
     init -
    /bin/ash: syntax error: unexpected "("
    root@(none):/# 
    root@(none):/# init -
        |__| W I
     O M
     Backfire (10.03
    -------------
      * 1/3  glass, layer Kahlua 
    on the bottom, then Ba
    odka     then Vodka.
    ----------------------
    root@(none):/# itchingBusyBox v1.15.3 (2011-08-22 15:59:17 IST) multi-call binary
    Usage: init 
    Init is the parent of all processes
    directory: /over overr
    error: unexpected "("
    none):/# ching to 
     to 
    ctorying to 
    ctor
    ory to 
    ctoryto 
    ctory
    ryollected erro
    lsuch file or dire
    ould
    ot create
    ould
    ould not 
    ould not 
    d not 
     not 
    not 
    /ash: syntax error: une:/# 
    root@(none):/# i
     Backfire (10.03
     glass, layer Kahlua 
    odka     then Vodka.
    root@(none):/# itc1-08-22 15:59:17 IST) 
    ge: init 
    Init is t
    directory: /over
     "("
    none):/# ching 
    ctor
    ory to 
    ctoryto Cou
    lsuch file or 
    ould
    ould not 
     not 
    not 
    /ash: s
    root@(none):/# i
    lass, layer Kahlua 
    root@(none):/# i
    ge: init 
    Init
    y: /over
     "("
    none
    ctoryto Cou
    ould
    ould not 
    (none):/# i
    root@(none
    Init
    y: /over
    ryto Cou
    (none):/# i
    root@(none
    ipv6: Unknown symbol xfrm_inner_extract_output
    ipv6: Unknown symbol __ipv6_addr_type
    ipv6: Unknown symbol xfrm_user_policy
    ipv6: Unknown symbol xfrm_lookup
    ipv6: Unknown symbol __xfrm_lookup
    ipv6: Unknown symbol __xfrm_decode_session
    ipv6: Unknown symbol xfrm_state_check_expire
    ipv6: Unknown symbol __xfrm_policy_check
    ipv6: Unknown symbol __xfrm_state_destroy
    ipv6: Unknown symbol inet6_lookup
    ipv6: Unknown symbol xfrm_policy_unregister_afinfo
    ipv6: Unknown symbol secure_tcpv6_sequence_number
    ipv6: Unknown symbol ipv6_skip_exthdr
    ipv6: Unknown symbol flow_cache_genid
    ipv6: Unknown symbol __secpath_destroy
    ipv6: Unknown symbol inet6_hash_connect
    ipv6: Unknown symbol __xfrm_route_forward
    ipv6: Unknown symbol xfrm_input
    ipv6: Unknown symbol ipv6_ext_hdr
    ipv6: Unknown symbol __inet6_lookup_established
    ipv6: Unknown symbol __inet6_hash
    ipv6: Unknown symbol xfrm_state_unregister_afinfo
    ipv6: Unknown symbol xfrm_dst_ifdown
    ipv6: Unknown symbol xfrm_bundle_ok
    ipv6: Unknown symbol xfrm_state_lookup_byaddr
    ipv6: Unknown symbol inet6_lookup_listener
    ipv6: Unknown symbol xfrm_policy_register_afinfo
    ipv6: Unknown symbol xfrm_output
    ipv6: Unknown symbol xfrm_state_register_afinfo
    ipv6: Unknown symbol secpath_dup
    ttyS0: 2 input overrun(s)
    ipv6: Unknown symbol xfrm_inner_extract_output
    ipv6: Unknown symbol __ipv6_addr_type
    ipv6: Unknown symbol xfrm_user_policy
    ipv6: Unknown symbol xfrm_lookup
    ipv6: Unknown symbol __xfrm_lookup
    ipv6: Unknown symbol __xfrm_decode_session
    ipv6: Unknown symbol xfrm_state_check_expire
    ipv6: Unknown symbol __xfrm_policy_check
    ipv6: Unknown symbol __xfrm_state_destroy
    ipv6: Unknown symbol inet6_lookup
    ipv6: Unknown symbol xfrm_policy_unregister_afinfo
    ipv6: Unknown symbol secure_tcpv6_sequence_number
    ipv6: Unknown symbol ipv6_skip_exthdr
    ipv6: Unknown symbol flow_cache_genid
    ipv6: Unknown symbol __secpath_destroy
    ipv6: Unknown symbol inet6_hash_connect
    ipv6: Unknown symbol __xfrm_route_forward
    ipv6: Unknown symbol xfrm_input
    ipv6: Unknown symbol ipv6_ext_hdr
    ipv6: Unknown symbol __inet6_lookup_established
    ipv6: Unknown symbol __inet6_hash
    ipv6: Unknown symbol xfrm_state_unregister_afinfo
    ipv6: Unknown symbol xfrm_dst_ifdown
    ipv6: Unknown symbol xfrm_bundle_ok
    ipv6: Unknown symbol xfrm_state_lookup_byaddr
    ipv6: Unknown symbol inet6_lookup_listener
    ipv6: Unknown symbol xfrm_policy_register_afinfo
    ipv6: Unknown symbol xfrm_output
    ipv6: Unknown symbol xfrm_state_register_afinfo
    ipv6: Unknown symbol secpath_dup
    eth0: link up (1000Mbps/Full duplex)
    device eth0 entered promiscuous mode
    br-lan: port 1(eth0) entering forwarding state
    ipv6: Unknown symbol xfrm_inner_extract_output
    ipv6: Unknown symbol __ipv6_addr_type
    ipv6: Unknown symbol xfrm_user_policy
    ipv6: Unknown symbol xfrm_lookup
    ipv6: Unknown symbol __xfrm_lookup
    ipv6: Unknown symbol __xfrm_decode_session
    ipv6: Unknown symbol xfrm_state_check_expire
    ipv6: Unknown symbol __xfrm_policy_check
    ipv6: Unknown symbol __xfrm_state_destroy
    ipv6: Unknown symbol inet6_lookup
    ipv6: Unknown symbol xfrm_policy_unregister_afinfo
    ipv6: Unknown symbol secure_tcpv6_sequence_number
    ipv6: Unknown symbol ipv6_skip_exthdr
    ipv6: Unknown symbol flow_cache_genid
    ipv6: Unknown symbol __secpath_destroy
    ipv6: Unknown symbol inet6_hash_connect
    ipv6: Unknown symbol __xfrm_route_forward
    ipv6: Unknown symbol xfrm_input
    ipv6: Unknown symbol ipv6_ext_hdr
    ipv6: Unknown symbol __inet6_lookup_established
    ipv6: Unknown symbol __inet6_hash
    ipv6: Unknown symbol xfrm_state_unregister_afinfo
    ipv6: Unknown symbol xfrm_dst_ifdown
    ipv6: Unknown symbol xfrm_bundle_ok
    ipv6: Unknown symbol xfrm_state_lookup_byaddr
    ipv6: Unknown symbol inet6_lookup_listener
    ipv6: Unknown symbol xfrm_policy_register_afinfo
    ipv6: Unknown symbol xfrm_output
    ipv6: Unknown symbol xfrm_state_register_afinfo
    ipv6: Unknown symbol secpath_dup
    ipv6: Unknown symbol xfrm_inner_extract_output
    ipv6: Unknown symbol __ipv6_addr_type
    ipv6: Unknown symbol xfrm_user_policy
    ipv6: Unknown symbol xfrm_lookup
    ipv6: Unknown symbol __xfrm_lookup
    ipv6: Unknown symbol __xfrm_decode_session
    ipv6: Unknown symbol xfrm_state_check_expire
    ipv6: Unknown symbol __xfrm_policy_check
    ipv6: Unknown symbol __xfrm_state_destroy
    ipv6: Unknown symbol inet6_lookup
    ipv6: Unknown symbol xfrm_policy_unregister_afinfo
    ipv6: Unknown symbol secure_tcpv6_sequence_number
    ipv6: Unknown symbol ipv6_skip_exthdr
    ipv6: Unknown symbol flow_cache_genid
    ipv6: Unknown symbol __secpath_destroy
    ipv6: Unknown symbol inet6_hash_connect
    ipv6: Unknown symbol __xfrm_route_forward
    ipv6: Unknown symbol xfrm_input
    ipv6: Unknown symbol ipv6_ext_hdr
    ipv6: Unknown symbol __inet6_lookup_established
    ipv6: Unknown symbol __inet6_hash
    ipv6: Unknown symbol xfrm_state_unregister_afinfo
    ipv6: Unknown symbol xfrm_dst_ifdown
    ipv6: Unknown symbol xfrm_bundle_ok
    ipv6: Unknown symbol xfrm_state_lookup_byaddr
    ipv6: Unknown symbol inet6_lookup_listener
    ipv6: Unknown symbol xfrm_policy_register_afinfo
    ipv6: Unknown symbol xfrm_output
    ipv6: Unknown symbol xfrm_state_register_afinfo
    ipv6: Unknown symbol secpath_dup
    Generic kernel compatibility enabled based on linux-next next-20100113
    cfg80211: Calling CRDA to update world regulatory domain
    ipv6: Unknown symbol xfrm_inner_extract_output
    ipv6: Unknown symbol __ipv6_addr_type
    ipv6: Unknown symbol xfrm_user_policy
    ipv6: Unknown symbol xfrm_lookup
    ipv6: Unknown symbol __xfrm_lookup
    ipv6: Unknown symbol __xfrm_decode_session
    ipv6: Unknown symbol xfrm_state_check_expire
    ipv6: Unknown symbol __xfrm_policy_check
    ipv6: Unknown symbol __xfrm_state_destroy
    ipv6: Unknown symbol inet6_lookup
    ipv6: Unknown symbol xfrm_policy_unregister_afinfo
    ipv6: Unknown symbol secure_tcpv6_sequence_number
    ipv6: Unknown symbol ipv6_skip_exthdr
    ipv6: Unknown symbol flow_cache_genid
    ipv6: Unknown symbol __secpath_destroy
    ipv6: Unknown symbol inet6_hash_connect
    ipv6: Unknown symbol __xfrm_route_forward
    ipv6: Unknown symbol xfrm_input
    ipv6: Unknown symbol ipv6_ext_hdr
    ipv6: Unknown symbol __inet6_lookup_established
    ipv6: Unknown symbol __inet6_hash
    ipv6: Unknown symbol xfrm_state_unregister_afinfo
    ipv6: Unknown symbol xfrm_dst_ifdown
    ipv6: Unknown symbol xfrm_bundle_ok
    ipv6: Unknown symbol xfrm_state_lookup_byaddr
    ipv6: Unknown symbol inet6_lookup_listener
    ipv6: Unknown symbol xfrm_policy_register_afinfo
    ipv6: Unknown symbol xfrm_output
    ipv6: Unknown symbol xfrm_state_register_afinfo
    ipv6: Unknown symbol secpath_dup
    cfg80211: World regulatory domain updated:
        (start_freq - end_freq @ bandwidth), (max_antenna_gain, max_eirp)
        (2402000 KHz - 2472000 KHz @ 40000 KHz), (300 mBi, 2000 mBm)
        (2457000 KHz - 2482000 KHz @ 20000 KHz), (300 mBi, 2000 mBm)
        (2474000 KHz - 2494000 KHz @ 20000 KHz), (300 mBi, 2000 mBm)
        (5170000 KHz - 5250000 KHz @ 40000 KHz), (300 mBi, 2000 mBm)
        (5735000 KHz - 5835000 KHz @ 40000 KHz), (300 mBi, 2000 mBm)
    SCSI subsystem initialized
    usbcore: registered new interface driver usbfs
    usbcore: registered new interface driver hub
    usbcore: registered new device driver usb
    PCI: Enabling device 0000:00:11.0 (0000 -> 0002)
    Registered led device: ath9k-phy0::radio
    Registered led device: ath9k-phy0::assoc
    Registered led device: ath9k-phy0::tx
    Registered led device: ath9k-phy0::rx
    phy0: Atheros AR9280 Rev:2 mem=0xb0000000, irq=48
    PCI: Enabling device 0000:00:12.0 (0000 -> 0002)
    cfg80211: Calling CRDA for country: US
    ipv6: Unknown symbol xfrm_inner_extract_output
    ipv6: Unknown symbol __ipv6_addr_type
    ipv6: Unknown symbol xfrm_user_policy
    ipv6: Unknown symbol xfrm_lookup
    ipv6: Unknown symbol __xfrm_lookup
    ipv6: Unknown symbol __xfrm_decode_session
    ipv6: Unknown symbol xfrm_state_check_expire
    ipv6: Unknown symbol __xfrm_policy_check
    ipv6: Unknown symbol __xfrm_state_destroy
    ipv6: Unknown symbol inet6_lookup
    ipv6: Unknown symbol xfrm_policy_unregister_afinfo
    ipv6: Unknown symbol secure_tcpv6_sequence_number
    ipv6: Unknown symbol ipv6_skip_exthdr
    ipv6: Unknown symbol flow_cache_genid
    ipv6: Unknown symbol __secpath_destroy
    ipv6: Unknown symbol inet6_hash_connect
    ipv6: Unknown symbol __xfrm_route_forward
    ipv6: Unknown symbol xfrm_input
    ipv6: Unknown symbol ipv6_ext_hdr
    ipv6: Unknown symbol __inet6_lookup_established
    ipv6: Unknown symbol __inet6_hash
    ipv6: Unknown symbol xfrm_state_unregister_afinfo
    ipv6: Unknown symbol xfrm_dst_ifdown
    ipv6: Unknown symbol xfrm_bundle_ok
    ipv6: Unknown symbol xfrm_state_lookup_byaddr
    ipv6: Unknown symbol inet6_lookup_listener
    ipv6: Unknown symbol xfrm_policy_register_afinfo
    ipv6: Unknown symbol xfrm_output
    ipv6: Unknown symbol xfrm_state_register_afinfo
    ipv6: Unknown symbol secpath_dup
    Registered led device: ath9k-phy1::radio
    Registered led device: ath9k-phy1::assoc
    Registered led device: ath9k-phy1::tx
    Registered led device: ath9k-phy1::rx
    phy1: Atheros AR9280 Rev:2 mem=0xb0010000, irq=49
    cfg80211: Calling CRDA for country: US
    cfg80211: Current regulatory domain intersected: 
        (start_freq - end_freq @ bandwidth), (max_antenna_gain, max_eirp)
        (2402000 KHz - 2472000 KHz @ 40000 KHz), (300 mBi, 2000 mBm)
        (2457000 KHz - 2472000 KHz @ 15000 KHz), (300 mBi, 2000 mBm)
        (5170000 KHz - 5250000 KHz @ 40000 KHz), (300 mBi, 1700 mBm)
        (5735000 KHz - 5835000 KHz @ 40000 KHz), (300 mBi, 2000 mBm)
    ipv6: Unknown symbol xfrm_inner_extract_output
    ipv6: Unknown symbol __ipv6_addr_type
    ipv6: Unknown symbol xfrm_user_policy
    ipv6: Unknown symbol xfrm_lookup
    ipv6: Unknown symbol __xfrm_lookup
    ipv6: Unknown symbol __xfrm_decode_session
    ipv6: Unknown symbol xfrm_state_check_expire
    ipv6: Unknown symbol __xfrm_policy_check
    ipv6: Unknown symbol __xfrm_state_destroy
    ipv6: Unknown symbol inet6_lookup
    ipv6: Unknown symbol xfrm_policy_unregister_afinfo
    ipv6: Unknown symbol secure_tcpv6_sequence_number
    ipv6: Unknown symbol ipv6_skip_exthdr
    ipv6: Unknown symbol flow_cache_genid
    ipv6: Unknown symbol __secpath_destroy
    ipv6: Unknown symbol inet6_hash_connect
    ipv6: Unknown symbol __xfrm_route_forward
    ipv6: Unknown symbol xfrm_input
    ipv6: Unknown symbol ipv6_ext_hdr
    ipv6: Unknown symbol __inet6_lookup_established
    ipv6: Unknown symbol __inet6_hash
    ipv6: Unknown symbol xfrm_state_unregister_afinfo
    ipv6: Unknown symbol xfrm_dst_ifdown
    ipv6: Unknown symbol xfrm_bundle_ok
    ipv6: Unknown symbol xfrm_state_lookup_byaddr
    ipv6: Unknown symbol inet6_lookup_listener
    ipv6: Unknown symbol xfrm_policy_register_afinfo
    ipv6: Unknown symbol xfrm_output
    ipv6: Unknown symbol xfrm_state_register_afinfo
    ipv6: Unknown symbol secpath_dup
    NTFS driver 2.1.29 [Flags: R/O MODULE].
    cfg80211: Current regulatory domain intersected: 
        (start_freq - end_freq @ bandwidth), (max_antenna_gain, max_eirp)
        (2402000 KHz - 2472000 KHz @ 40000 KHz), (300 mBi, 2000 mBm)
        (2457000 KHz - 2472000 KHz @ 15000 KHz), (300 mBi, 2000 mBm)
        (5170000 KHz - 5250000 KHz @ 40000 KHz), (300 mBi, 1700 mBm)
        (5735000 KHz - 5835000 KHz @ 40000 KHz), (300 mBi, 2000 mBm)
    PPP generic driver version 2.4.2
    ip_tables: (C) 2000-2006 Netfilter Core Team
    NET: Registered protocol family 24
    ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
    ar71xx-ehci ar71xx-ehci: Atheros AR71xx built-in EHCI controller
    ar71xx-ehci ar71xx-ehci: new USB bus registered, assigned bus number 1
    ar71xx-ehci ar71xx-ehci: irq 3, io mem 0x1b000000
    ar71xx-ehci ar71xx-ehci: USB 2.0 started, EHCI 1.00
    usb usb1: configuration #1 chosen from 1 choice
    hub 1-0:1.0: USB hub found
    hub 1-0:1.0: 2 ports detected
    nf_conntrack version 0.5.0 (1985 buckets, 7940 max)
    ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
    ar71xx-ohci ar71xx-ohci: Atheros AR71xx built-in OHCI controller
    ar71xx-ohci ar71xx-ohci: new USB bus registered, assigned bus number 2
    ar71xx-ohci ar71xx-ohci: irq 14, io mem 0x1c000000
    usb usb2: configuration #1 chosen from 1 choice
    hub 2-0:1.0: USB hub found
    hub 2-0:1.0: 2 ports detected
    Initializing USB Mass Storage driver...
    usbcore: registered new interface driver usb-storage
    USB Mass Storage support registered.
