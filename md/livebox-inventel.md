# Serial port


screen -L /dev/ttyUSB0 115200 8N1


    56+678ESA: 00:16:ae:93:86:28
    WEP KEY : C48B121F07ED2224BAB6D3475C
    Auto-negotiation timed-out
    10 MB Half-Duplex (assumed)
    Ethernet eth0: MAC address 00:16:ae:93:86:28
    IP: 10.7.58.112, Default server: 0.0.0.0
    Hardware version 0x10 BLUE5G.9 WITHOUT_OPTION
    Factory Settings Recovery Switch OFF High
    Register : 17
    RedBoot(tm) bootstrap and debug environment [ROM]
    Non-certified release, version release-wanadoo-fr - built 16:25:10, Jun 20 2006
    Platform: Blue_5g (MIPS32 4Kc) 
    Copyright (C) 2000, 2001, 2002, Red Hat, Inc.
    RAM: 0x80000000-0x81000000, [0x80445fb0-0x80fe2000] available
    FLASH: 0xbe400000 - 0xbec00000, 128 blocks of 0x00010000 bytes each.
    == Executing boot script in 0.200 seconds - enter ^C twice to abort
    RedBoot> fis load -b 0x80010000 -m cramfs -f Image user_fs
    Partition is : 0xbe430000 - 0x390000 
    mlen : 0x337034 
    begin_tag : 0xbe767000, end : 0xbe767034
    Verif OK 
    Looking for Image in cramfs user_fs partition
    cramfs_load : b 0x80010000, c 0xBE430000, s 0x00390000, f Image
    unable to find magic
    Found a valid SQUASHFS superblock on user_fs.
    	Inodes are compressed
    	Data is compressed
    	Fragments are compressed
    	Check data is not present in the filesystem
    	Fragments are  present in the filesystem
    	Always_use_fragments option is not specified
    	Duplicates are  removed
    	Filesystem size 3370576 bytes
    	Block size 65536
    	Number of fragments 28
    	Number of inodes 658
    	Number of uids 1
    	Number of gids 0
    Scanning existing filesystem...
    Read existing filesystem, 657 inodes scanned
    Return with root_try==0
    RedBoot> exec -c "boot_loader=RedBoot root=1F01 mem=16M" 0x80010000
    root_try == 0 : leave boot cmd alone
    Now booting linux kernel:
     Base address 0x8000fc00 Entry 0x80010000
     Cmdline : boot_loader=RedBoot root=1F01 mem=16M hwversion=BLUE5G.9-WITHOUT_OPTION redbootversion="release-wanadoo-fr-Jun 20 2006-16:25:10"
    Linux version 2.6.12.6 (bellonia@cplx207.edegem.eu.thmulti.com) (gcc version 3.4.2) #1 Fri Mar 14 19:07:34 CET 2008
    C0 config : 2147516544x 
    CPU revision is: 00029107
    mpi: No Card is in the PCMCIA slot
    Determined physical RAM map:
     memory: 00fa0000 @ 00000000 (usable)
     memory: 00060000 @ 00fa0000 (reserved)
    On node 0 totalpages: 4000
      DMA zone: 4000 pages, LIFO batch:1
      Normal zone: 0 pages, LIFO batch:1
      HighMem zone: 0 pages, LIFO batch:1
    Built 1 zonelists
    Kernel command line: boot_loader=RedBoot root=1F01 hwversion=BLUE5G.9-WITHOUT_OPTION redbootversion="release-wanadoo-fr-Jun 20 2006-16:25:10"
    brcm mips: enabling icache and dcache...
    Primary instruction cache 16kB, physically tagged, 2-way, linesize 16 bytes.
    Primary data cache 8kB, 2-way, linesize 16 bytes.
    Synthesized TLB refill handler (19 instructions).
    Synthesized TLB load handler fastpath (31 instructions).
    Synthesized TLB store handler fastpath (31 instructions).
    Synthesized TLB modify handler fastpath (30 instructions).
    PID hash table entries: 64 (order: 6, 1024 bytes)
    Using 128.000 MHz high precision timer.
    Dentry cache hash table entries: 4096 (order: 2, 16384 bytes)
    Inode-cache hash table entries: 2048 (order: 1, 8192 bytes)
    Memory: 13148k/16000k available (1831k kernel code, 2832k reserved, 236k data, 336k init, 0k highmem)
    Calibrating delay loop... (HZ=200) 255.59 BogoMIPS (lpj=638976)
    Mount-cache hash table entries: 512
    Checking for 'wait' instruction...  unavailable.
    NET: Registered protocol family 16
    Squashfs 2.2 (released 2005/07/03) (C) 2002-2005 Phillip Lougher
    devfs: 2004-01-31 Richard Gooch (rgooch@atnf.csiro.au)
    devfs: boot_options: 0x1
    JFFS2 version 2.2. (C) 2001-2003 Red Hat, Inc.
    io scheduler noop registered
    lo:register_netdevice:2847
    PPP generic driver version 2.4.2
    NET: Registered protocol family 24
    initialize redboot parser
    Found: AMD AM29LV640MB
    Inventel Blue5G Flash: Found 1 x16 devices at 0x0 in 16-bit bank
    number of JEDEC chips: 1
    cfi_cmdset_0002: Disabling erase-suspend-program due to code brokenness.
    parse_redboot_partitions
    Searching for RedBoot partition table in Inventel Blue5G Flash at offset 0x7f0000
    6 RedBoot partitions found on MTD device Inventel Blue5G Flash
    Creating 6 MTD partitions on "Inventel Blue5G Flash":
    0x00000000-0x00030000 : "RedBoot"
    0x00030000-0x003c0000 : "user_fs"
    0x003c0000-0x00750000 : "user_2_fs"
    0x00750000-0x007f0000 : "jffs_system"
    0x007f0000-0x007ff000 : "FIS directory"
    0x007ff000-0x00800000 : "RedBoot config"
    bcm963xx_serial driver v2.0
    u32 classifier
    NET: Registered protocol family 2
    IP: routing cache hash table of 512 buckets, 4Kbytes
    TCP established hash table entries: 1024 (order: 1, 8192 bytes)
    TCP bind hash table entries: 1024 (order: 0, 4096 bytes)
    TCP: Hash tables configured (established 1024 bind 1024)
    ip_conntrack version 2.1 (125 buckets, 1000 max) - 212 bytes per conntrack
    ip_tables: (C) 2000-2002 Netfilter core team
    NET: Registered protocol family 1
    NET: Registered protocol family 17
    Ebtables v2.0 registered
    NET: Registered protocol family 8
    NET: Registered protocol family 20
    VFS: Mounted root (squashfs filesystem) readonly.
    Mounted devfs on /dev
    Freeing unused kernel memory: 336k freed
    init started:  BusyBox v1.1.3 (2008.03.14-18:14+0000) multi-call binary
    init started:  BusyBox v1.1.3 (2008.03.14-18:14+0000) multi-call binary
    Starting pid 15, console /dev/tts/0: '/etc_ro_fs/init.d/sysinit'
    Algorithmics/MIPS FPU Emulator v1.5
    SYSINIT
    INVENTEL version : v5.10.7-mobistar-be
    Mounting proc filesystem ...
    Mounting tmpfs filesystem ...
    > NORMAL BOOT <
    + [ -f /etc_ro_fs/autoconf.conf ]
    + . /etc_ro_fs/autoconf.conf
    + CONFIG_TARGET_NAME=Mobistar
    + CONFIG_GENERATION_5G=y
    + CONFIG_GATEWAY_RESIDENTIAL=y
    + CONFIG_BCM_VARIANT=6348
    + CONFIG_LINUX_2_6=y
    + CONFIG_LB2_NONE=y
    + CONFIG_RELEASE=y
    + CONFIG_STRIP_LIBS=y
    + CONFIG_DEFAULT_KERNEL_CONFIG_FILE=Config-LiveBox1-5G
    + CONFIG_DEFAULT_BUSYBOX_CONFIG_FILE=Config-Wanadoo-Release
    + CONFIG_ROOT_SQUASHFS=y
    + CONFIG_ROOT_SPLIT=y
    + CONFIG_RELEASE_BASE_DIR_HOME=y
    + CONFIG_GENERATE_PROGKIT=y
    + CONFIG_GENERATE_PROGKIT_PATH=redboot_6348_sdram_128mbit_flash_64mbit_20060620_rom_5G7G_release_wanadoo_fr
    + CONFIG_GENERATE_WEBUPDATE=y
    + CONFIG_GENERATE_WEBUPDATE_COMPLETEUPGRADECLONE=y
    + CONFIG_GENERATE_WEBUPDATE_PARTIALUPGRADECLONE=y
    + CONFIG_DEFAULT_UPDATE_DIRECTORY=inventel/blue_5g/mobistar/release-e
    + CONFIG_DEFAULT_UPDATE_DIRECTORY_FORCE=y
    + CONFIG_DEFAULT_UPDATE_MACHINE=developers.inventel.com
    + CONFIG_DEFAULT_UPDATE_USERNAME=inventel
    + CONFIG_DEFAULT_UPDATE_PASSWORD=inventel
    + CONFIG_UPDATE_ALERT=y
    + CONFIG_UPDATE_AUTOUPDATE_DELAY=10
    + CONFIG_UPDATE_AUTOUPDATE_ON_FIRST_PPP=y
    + CONFIG_AUTOUPDATE_NONE=y
    + CONFIG_VERSION_NAME_MAJOR=5.10
    + CONFIG_VERSION_NAME_MINOR_TYPE=.
    + CONFIG_VERSION_NAME_MINOR=7
    + CONFIG_VERSION_NAME_SUFFIX=-mobistar-be
    + CONFIG_VERSION_FQN=v5.10.7-mobistar-be
    + CONFIG_HW_VERSION=1.0
    + CONFIG_INCLUDE_PUBKEY=y
    + CONFIG_PUBKEY_FILENAME=release-wanadoo-fr
    + CONFIG_ADDRESS_192_168=y
    + CONFIG_ADDRESS_IP_0=192.168.1.1
    + CONFIG_ADDRESS_NETMASK_0=255.255.255.0
    + CONFIG_ADDRESS_BROADCAST_0=192.168.1.255
    + ADVANCE_MEMORY_CONFIGURATION=y
    + CONFIG_FLASH_64MBIT=y
    + CONFIG_SDRAM_128MBIT=y
    + CONFIG_PAIRABLE_TIMEOUT=600
    + CONFIG_STACK_BLUEZ=y
    + CONFIG_BLUEZ_RFCOMM=y
    + CONFIG_BLUEZ_SDPD=y
    + CONFIG_BLUEZ_PAN=y
    + CONFIG_BLUEZ_OBEX=y
    + CONFIG_BT_WATCHDOG=y
    + CONFIG_BLUETOOTH=y
    + CONFIG_BTNAME_HOSTNAME=y
    + CONFIG_BLUETOOTH_ALTERNATE=y
    + CONFIG_BLUETOOTH_ALTERNATE_VERSION=0x34313832
    + CONFIG_DECT_DISABLE_UPDATE=y
    + CONFIG_BLUEZ_TEST=y
    + CONFIG_DEVGATEWAY=y
    + CONFIG_INCLUDE_FRENCH_MOBISTAR=y
    + CONFIG_INCLUDE_ENGLISH_MOBISTAR=y
    + CONFIG_INCLUDE_DUTCH_MOBISTAR=y
    + CONFIG_DEFAULT_ENGLISH_MOBISTAR=y
    + CONFIG_ADSL=y
    + CONFIG_ADSL_RTC=y
    + CONFIG_ADSL_A2pBT009c1=y
    + CONFIG_ADSL_PPP_NAME=ppp_name
    + CONFIG_ADSL_PPP_PASS=ppp_pass
    + CONFIG_ADSLCTL=y
    + CONFIG_ADSL_MOD_AUTO=y
    + CONFIG_PPPOE_PASSTHRU=y
    + CONFIG_ADSL_BRIDAGE_MOBISTAR=y
    + CONFIG_ADSL_DEFAULT_BRIDAGE_PROFILE=0
    + CONFIG_ADSL_VP=8
    + CONFIG_ADSL_VC=35
    + CONFIG_ADSL_PROTOCOL=pppoe
    + CONFIG_ADSL_ENCAPS=LLCMUX
    + CONFIG_ADSL_MAX_CONNECT_TIME=0
    + CONFIG_BCM_USB=y
    + CONFIG_BCM_USB_PRODUCT_NAME=Inventel Gateway
    + CONFIG_WIRELESS_LAN=y
    + CONFIG_WIRELESS_LAN_WEPONLY_HANDLED_BY_NAS=y
    + CONFIG_WIFI_BLUETOOTH_COEXISTENCE=y
    + CONFIG_WIRELESS_BCMTOOLS=y
    + CONFIG_UPNP=y
    + CONFIG_EBTABLES=y
    + CONFIG_IPROUTE2=y
    + CONFIG_IPROUTE2_IP=y
    + CONFIG_IPROUTE2_TC=y
    + CONFIG_REMOTE_MGT=y
    + CONFIG_COUNTRY_BELGIUM=y
    + CONFIG_COUNTRY_FORCE=y
    + CONFIG_WIFI_SECURITY_WPA_ONLY=y
    + CONFIG_DEFINITIVE_PASSWORD=y
    + CONFIG_WANADOO_SERVER_KIT_DB=y
    + CONFIG_WANADOO_DB_UPDATE_DELAY=5
    + CONFIG_FT_SERVER_KIT_URL=http://suivilb.wanadoo.fr/servlets/maj
    + CONFIG_FT_SERVER_KIT_COUNTRY_CODE=1091
    + CONFIG_FT_UPDATE_SOLUTION=y
    + CONFIG_FEATURE_UPDATE_FT=y
    + CONFIG_SUPPORT_FIRMWARE_PUSH=y
    + CONFIG_GENERIC_SPI=y
    + CONFIG_WEB=y
    + CONFIG_WEB_LEFT_MENU_STYLE=y
    + CONFIG_WEB_LOGIN=admin
    + CONFIG_WEB_PASSWORD=admin
    + CONFIG_WEB_MOBISTAR=y
    + CONFIG_UPNP_MOBISTAR=y
    + CONFIG_VOIP=y
    + CONFIG_VOIP_RADVISION=y
    + CONFIG_VOIP_RADVISION_MOBISTAR=y
    + [ ! -f /etc_ro_fs/autoconf.conf ]
    + [ -z y ]
    + grep user.*_fs
    + cut -f1 -d:
    + cat /proc/mtd
    + mtdlist=mtd1
    mtd2
    + [ -h /dev/root ]
    + ls -al /dev/root
    + sed s/.* -> mtdblock/mtd/
    + mtdroot=mtd1
    + echo mtd1 mtd2
    + sed s/mtd1//
    + mtdlist= mtd2
    + echo mtd2
    + sed s/mtd//
    + mtdlist=2
    + echo 2
    + echo Try to mount /dev/mtdblock2 on /usr
    Try to mount /dev/mtdblock2 on /usr
    + flash_verify /dev/mtd2 0x29032005
    Magic: 29032005
    /dev/mtd2: opening...
    /dev/mtd2: reading signature...
    Signature (48 bytes):
        94 00 03 02 00 14 c8 e6 ba 36 82 81 2d 20 2d c2 
        80 84 13 ff 8e e8 ab 8d fe 20 00 14 ef f4 07 b9 
        fc a5 3f 00 5b 1e 0c 10 a7 8f 59 44 9d f3 d0 1d 
    /dev/mtd2: hashing...
    /dev/mtd2: importing public key...
    /dev/mtd2: verifying hash...
    /dev/mtd2: verification OK
    + mount -t squashfs /dev/mtdblock2 /usr
    + result=0
    + [ ! 0 -eq 0 ]
    + rm -f /var/run/rescue_boot
    + break
    + [ ! -e /etc/rc.d ]
    + rm -f /tmp/touch.test
    + find /lib/modules// -name prod_test*
    + insmod /lib/modules//2.6.12.6/extra/prod_test.ko
    prod_test: module license 'Proprietary' taints kernel.
    insmod: cannot insert `/lib/modules//2.6.12.6/extra/prod_test.ko': Success (1): Success
    + [ 1 = 0 ]
    + [ -n mtd0 ]
    + cat /proc/mtd
    dev:    size   erasesize  name
    mtd0: 00030000 00010000 "RedBoot"
    mtd1: 00390000 00010000 "user_fs"
    mtd2: 00390000 00010000 "user_2_fs"
    mtd3: 000a0000 00010000 "jffs_system"
    mtd4: 0000f000 00010000 "FIS directory"
    mtd5: 00001000 00010000 "RedBoot config"
    + cat /proc/mtd
    + grep jffs_system
    + sed -n s/\(mtd\)\(.*\):\(.\)*/\2/p
    + mount -t jffs2 -o rw /dev/mtdblock3 /mnt/jffs2/jffs2_3
    + rm -f /tmp/touch.test
    + touch /tmp/touch.test
    + [ ! -e /tmp/touch.test ]
    + rm -f /tmp/touch.test
    + [ -e /tmp/touch.test ]
    + [ ! -f /mnt/jffs2/jffs2_3/etc/issue ]
    + [ ! -f /mnt/jffs2/jffs2_3/etc/finished ]
    + cat+ grep version
     /etc/issue.bluedsl
    + x=INVENTEL version : v5.10.7-mobistar-be
    + cat /etc_ro_fs/issue.bluedsl
    + grep version
    + y=INVENTEL version : v5.10.7-mobistar-be
    + [ INVENTEL version : v5.10.7-mobistar-be = INVENTEL version : v5.10.7-mobistar-be ]
    + echo Up to date version INVENTEL version : v5.10.7-mobistar-be
    Up to date version INVENTEL version : v5.10.7-mobistar-be
    + [ -f /usr/etc_ro_fs/init.d/usrboot ]
    + /usr/etc_ro_fs/init.d/usrboot
    + rm -f /var/run/rescue_boot
    + [ ! -f /usr/etc/finished ]
    + cat /usr/etc/issue.bluedsl
    + grep version
    + x=INVENTEL version : v5.10.7-mobistar-be
    + cat /usr/etc_ro_fs/issue.bluedsl
    + grep version
    + y=INVENTEL version : v5.10.7-mobistar-be
    + [ INVENTEL version : v5.10.7-mobistar-be = INVENTEL version : v5.10.7-mobistar-be ]
    + echo /usr up to date version INVENTEL version : v5.10.7-mobistar-be
    /usr up to date version INVENTEL version : v5.10.7-mobistar-be
    + exit 0
    + exit 0
    Starting pid 99, console /dev/tts/0: '/etc_ro_fs/init.d/rc.sysinit'
    Mounting other filesystems ...
    cp: /etc/crontab_root: No such file or directory
    + echo Switching to RUNLEVEL 1 ...
    Switching to RUNLEVEL 1 ...
    + runlevel_manage 1
    + local previous
    + runlevel=1
    + [ -f /var/run/runlevel ]
    + previous=N
    + [ 1 = N ]
    + local scriptlist directorylist
    + directorylist=/etc/rc1.d/:/usr/etc/rc1.d/
    + OLDIFS= 	
    + IFS=: 	
    + scriptlist=
    + find /etc/rc1.d/ -name K*
    + sed s,/etc/rc1.d/,,
    + scriptlist= 
    + find /usr/etc/rc1.d/ -name K*
    + sed s,/usr/etc/rc1.d/,,
    + scriptlist=  
    + sort -u
    + scriptlist=
    + echo 1
    + echo 108
    + scriptlist=
    + sed s,/etc/rc1.d/,,
    + find /etc/rc1.d/ -name S*
    + scriptlist=S20network
    S25update_ft
    S10adsl
    S26pair
    S25wireless
    S22backlight
    S05hardware
    S22http_server
    S99printkoff
    S25dhcp_dns_server 
    + find /usr/etc/rc1.d/ -name S*
    + sed s,/usr/etc/rc1.d/,,
    + scriptlist=S22upnp
    S28krtp
    S85voip
    S27bluetooth
    S90post_webupgrade S20network
    S25update_ft
    S10adsl
    S26pair
    S25wireless
    S22backlight
    S05hardware
    S22http_server
    S99printkoff
    S25dhcp_dns_server 
    + echo S22upnp
    + echo S28krtp
    + echo S85voip
    + echo S27bluetooth
    + sort -u
    + echo S90post_webupgrade
    + echo S20network
    + echo S25update_ft
    + echo S10adsl
    + echo S26pair
    + echo S25wireless
    + echo S22backlight
    + echo S05hardware
    + echo S22http_server
    + echo S99printkoff
    + echo S25dhcp_dns_server
    + scriptlist=S05hardware
    S10adsl
    S20network
    S22backlight
    S22http_server
    S22upnp
    S25dhcp_dns_server
    S25update_ft
    S25wireless
    S26pair
    S27bluetooth
    S28krtp
    S85voip
    S90post_webupgrade
    S99printkoff
    + [ -f /etc/rc1.d/S05hardware ]
    + realscript=/etc/rc1.d/S05hardware
    + [ 1 != N ]
    + number=05hardware
    + echo 05hardware
    + cut -c 1-2
    + number=05
    + echo 05
    + suffix=hardware
    + stop=/etc/rc1.d/K[0-9][0-9]hardware
    + echo /etc/rc1.d/
    + sed s,rc1,rcN,
    + previous_start=/etc/rcN.d/S[0-9][0-9]hardware
    + [ -f /etc/rcN.d/S[0-9][0-9]hardware ]
    + sh /etc/rc1.d/S05hardware start
    Starting core drivers...
    Watchdog init Build:  Mar 14 2008  19:16:23
    irq register OK
    SPI driver Mar 14 2008 19:16:22
       usage: insmod spi.o [debug=1] [tty_low_latency=1]
    Broadcom BCM6348B0 Ethernet Network Device v0.3 Mar 14 2008 19:05:21
    Config Internal PHY Through MDIO
    BCM63xx_ENET: Auto-negotiation timed-out
    BCM63xx_ENET: 10 MB Half-Duplex (assumed)
    eth0:register_netdevice:2847
    eth0: MAC Address: 00:07:3A:FF:FF:FF
    Broadcom BCM6348B0 Ethernet Network Device v0.3 Mar 14 2008 19:05:21
    Config External PHY Through MDIO
    BCM63xx_ENET: Auto-negotiation timed-out
    BCM63xx_ENET: 10 MB Half-Duplex (assumed)
    eth1:register_netdevice:2847
    eth1: MAC Address: 00:07:3A:FF:FF:FF
    USB MAC ADDRESS belongs to 00:16:AE:93:86:2D
    USB HOST MAC ADDRESS belongs to 00:16:AE:93:86:2B
    Broadcom BCM6348B0 USB Network Device v0.4 Mar 14 2008 19:05:23
    usb0: MAC Address: 00 16 AE 93 86 2D
    usb0: Host MAC Address: 00 16 AE 93 86 2B
    usb0:register_netdevice:2847
    Switch module creating proc entry
    dummy0:register_netdevice:2847
    dummy1:register_netdevice:2847
    + break
    + [ -f /etc/rc1.d/S10adsl ]
    + realscript=/etc/rc1.d/S10adsl
    + [ 1 != N ]
    + number=10adsl
    + echo 10adsl
    + cut -c 1-2
    + number=10
    + echo 10
    + suffix=adsl
    + stop=/etc/rc1.d/K[0-9][0-9]adsl
    + echo /etc/rc1.d/
    + sed s,rc1,rcN,
    + previous_start=/etc/rcN.d/S[0-9][0-9]adsl
    + [ -f /etc/rcN.d/S[0-9][0-9]adsl ]
    + sh /etc/rc1.d/S10adsl start
    Loading ADSL & ATM kernel modules...
    Starting ADSL daemon...
    + break
    + [ -f /etc/rc1.d/S20network ]
    + realscript=/etc/rc1.d/S20network
    + [ 1 != N ]
    + number=20network
    + echo 20network
    + cut -c 1-2
    + number=20
    + echo 20
    + suffix=network
    + stop=/etc/rc1.d/K[0-9][0-9]network
    + sed s,rc1,rcN,
    + echo /etc/rc1.d/
    + previous_start=/etc/rcN.d/S[0-9][0-9]network
    + [ -f /etc/rcN.d/S[0-9][0-9]network ]
    + sh /etc/rc1.d/S20network start
    BcmAdsl_Initialize=0xC00DE0C8, g_pFnNotifyCallback=0xC00F3034
    pSdramPHY=0xA0FFFFF8, 0x9FCF2278 0xDEADDEAD
    AdslCoreHwReset: AdslOemDataAddr = 0xA0FFDE10
    AdslCoreEcUpdTmr: timeMs=-275140 ecUpdMask=0x40000
    Local network configuration ...
    Ethernet network configuration ...
    Hostname configuration : Mobistar-8628
    br0:register_netdevice:2847
    device dummy1 entered promiscuous mode
    device usb0 entered promiscuous mode
    device eth0 entered promiscuous mode
    device eth1 entered promiscuous mode
    br0: port 4(eth1) entering learning state
    br0: port 3(eth0) entering learning state
    br0: port 2(usb0) entering learning state
    + break
    + [ -f /etc/rc1.d/S22backlight ]
    + realscript=/etc/rc1.d/S22backlight
    + [ 1 != N ]
    + number=22backlight
    + echo 22backlight
    + cut -c 1-2
    + number=22
    + echo 22
    + suffix=backlight
    + stop=/etc/rc1.d/K[0-9][0-9]backlight
    + echo /etc/rc1.d/+ sed s,rc1,rcN,
    + previous_start=/etc/rcN.d/S[0-9][0-9]backlight
    + [ -f /etc/rcN.d/S[0-9][0-9]backlight ]
    + sh /etc/rc1.d/S22backlight start
    Update Backlight state
    Advanced
    Device open failed: Address family not supported by protocol
    + break
    + [ -f /etc/rc1.d/S22http_server ]
    + realscript=/etc/rc1.d/S22http_server
    + [ 1 != N ]
    + number=22http_server
    br0: topology change detected, propagating
    br0: port 4(eth1) entering forwarding state
    br0: topology change detected, propagating
    br0: port 3(eth0) entering forwarding state
    br0: topology change detected, propagating
    br0: port 2(usb0) entering forwarding state
    + echo 22http_server
    + cut -c 1-2
    + number=22
    + echo 22
    + suffix=http_server
    + stop=/etc/rc1.d/K[0-9][0-9]http_server
    + echo /etc/rc1.d/
    + sed s,rc1,rcN,
    + previous_start=/etc/rcN.d/S[0-9][0-9]http_server
    + [ -f /etc/rcN.d/S[0-9][0-9]http_server ]
    + sh /etc/rc1.d/S22http_server start
    Websrv start ...
    + break
    + [ -f /etc/rc1.d/S22upnp ]
    + [ -f /usr/etc/rc1.d/S22upnp ]
    + realscript=/usr/etc/rc1.d/S22upnp
    + [ 1 != N ]
    + number=22upnp
    + cut -c 1-2
    + echo 22upnp
    + number=22
    + echo 22
    + suffix=upnp
    + stop=/usr/etc/rc1.d/K[0-9][0-9]upnp
    + echo /usr/etc/rc1.d/
    + sed s,rc1,rcN,
    + previous_start=/usr/etc/rcN.d/S[0-9][0-9]upnp
    + [ -f /usr/etc/rcN.d/S[0-9][0-9]upnp ]
    + sh /usr/etc/rc1.d/S22upnp start
    No ADSL, default: abc0
    Upnp init ...
    MyConfig in /usr/etc/upnp.conf:
    	Debug=0
    	descDocName: gatedesc.xml
    	xmlPath: /usr/etc/linuxigd
    	g_iptables: iptables
    	g_forwardChainName: upnp
    	g_preroutingChainName: upnp
    	g_upstreamBitrate: 0
    	g_downstreamBitrate: 0
     TGU: IpAddress: 192.168.1.1
    + break
    + [ -f /etc/rc1.d/S25dhcp_dns_server ]
    + realscript=/etc/rc1.d/S25dhcp_dns_server
    + [ 1 != N ]
    + number=25dhcp_dns_server
    + echo 25dhcp_dns_server
    + cut -c 1-2
    + number=25
    + echo 25
    + suffix=dhcp_dns_server
    + stop=/etc/rc1.d/K[0-9][0-9]dhcp_dns_server
    + echo /etc/rc1.d/
    + sed s,rc1,rcN,
     INFO : IGD root device successfully registered.
    + previous_start=/etc/rcN.d/S[0-9][0-9]dhcp_dns_server
    + [ -f /etc/rcN.d/S[0-9][0-9]dhcp_dns_server ]
    + sh /etc/rc1.d/S25dhcp_dns_server start
    dnsmasq configured as dhcp server
    dnsmasq start ( DNS / DHCP server ) ...
    dnsmasq -o -r/etc/resolv.dnsmasq -z --dhcp-range=192.168.1.9,192.168.1.200,24h --dhcp-leasefile=/etc/dhcp.leases
    [p2] iface->name: br0
    [p2] iface->name: lo
    + break
    + [ -f /etc/rc1.d/S25update_ft ]
    + realscript=/etc/rc1.d/S25update_ft
    + [ 1 != N ]
    + number=25update_ft
    + echo 25update_ft
    + cut -c 1-2
    + number=25
    + echo 25
    + suffix=update_ft
    + stop=/etc/rc1.d/K[0-9][0-9]update_ft
    + echo /etc/rc1.d/
    + sed s,rc1,rcN,
    + previous_start=/etc/rcN.d/S[0-9][0-9]update_ft
    + [ -f /etc/rcN.d/S[0-9][0-9]update_ft ]
    + sh /etc/rc1.d/S25update_ft start
    France Telecom Firmware Update Client v1.12
    Copyright Inventel 2005-2006
    + break
    + [ -f /etc/rc1.d/S25wireless ]
    + realscript=/etc/rc1.d/S25wireless
    + [ 1 != N ]
    + number=25wireless
    + echo 25wireless
    + cut -c 1-2
    + number=25
    + echo 25
    + suffix=wireless
    + stop=/etc/rc1.d/K[0-9][0-9]wireless
    + echo /etc/rc1.d/
    + sed s,rc1,rcN,
    + previous_start=/etc/rcN.d/S[0-9][0-9]wireless
    + [ -f /etc/rcN.d/S[0-9][0-9]wireless ]
    + sh /etc/rc1.d/S25wireless start
     INFO : Advertisements Sent.  Listening for requests ... 
    PCI: Setting latency timer of device 0000:00:01.0 to 64
    PCI: Enabling device 0000:00:01.0 (0004 -> 0006)
    wl0:register_netdevice:2847
    wl0: Broadcom BCM4318 802.11 Wireless Controller 3.131.35.0.cpe0.0
    [p2] wl_event, bssid idx: 0
    [p2] wl_event, dev: 00000000
    [p2] dev == NULL, using wl->dev
    [p2] wl_event, dev->name: wl0
    [p2] wlc_sendup_event, bssid:0
    device wl0 entered promiscuous mode
    [p2] wl_event, bssid idx: 0
    [p2] wl_event, dev: 00000000
    [p2] dev == NULL, using wl->dev
    [p2] wl_event, dev->name: wl0
    [p2] wlc_sendup_event, bssid:0
    br0: port 5(wl0) entering learning state
    + break
    + [ -f /etc/rc1.d/S26pair ]
    + realscript=/etc/rc1.d/S26pair
    + [ 1 != N ]
    + number=26pair
    + echo 26pair
    + cut -c 1-2
    + number=26
    + echo 26
    + suffix=pair
    + stop=/etc/rc1.d/K[0-9][0-9]pair
    + echo /etc/rc1.d/
    + sed s,rc1,rcN,
    + previous_start=/etc/rcN.d/S[0-9][0-9]pair
    + [ -f /etc/rcN.d/S[0-9][0-9]pair ]
    + sh /etc/rc1.d/S26pair start
    Bad run level ...
    Starting pairing manager
    + break
    + [ -f /etc/rc1.d/S27bluetooth ]
    + [ -f /usr/etc/rc1.d/S27bluetooth ]
    + realscript=/usr/etc/rc1.d/S27bluetooth
    + [ 1 != N ]
    + number=27bluetooth
    + echo 27bluetooth
    br0: topology change detected, propagating
    br0: port 5(wl0) entering forwarding state
    + cut -c 1-2
    + number=27
    + echo 27
    + suffix=bluetooth
    + stop=/usr/etc/rc1.d/K[0-9][0-9]bluetooth
    + echo /usr/etc/rc1.d/
    + sed s,rc1,rcN,
    Update Backlight state
    + previous_start=/usr/etc/rcN.d/S[0-9][0-9]bluetooth
    + [ -f /usr/etc/rcN.d/S[0-9][0-9]bluetooth ]
    + sh /usr/etc/rc1.d/S27bluetooth start
    Param: 
    Advanced
    Device open failed: Address family not supported by protocol
    s_backlight : 1
    Function cleanup_link_keys
    R0=00:0B:6B:A0:DF:C1
    wifi_nb : 1
    0 link keys removed
    /sbin/iwpriv wl0 del_mac ff:ff:ff:ff:ff:ff
    R0=00:0B:6B:A0:DF:C1
    /sbin/iwpriv wl0 add_mac 00:0B:6B:A0:DF:C1
    /sbin/iwpriv wl0 maccmd 1
    Bluetooth configuration ...
    Bluetooth: Core ver 2.7
    NET: Registered protocol family 31
    Bluetooth: HCI device and connection manager initialized
    Bluetooth: HCI socket layer initialized
    Bluetooth: L2CAP ver 2.7
    Bluetooth: L2CAP socket layer initialized
    Bluetooth: RFCOMM ver 1.5
    Bluetooth: RFCOMM socket layer initialized
    Bluetooth: BNEP (Ethernet Emulation) ver 1.2
    Bluetooth: HCI UART driver ver 2.1
    Bluetooth: HCI H4 protocol initialized
    Bluetooth: HCI BCSP protocol initialized
    Bluetooth: SCO (Voice Link) ver 0.4
    Bluetooth: SCO socket layer initialized
    ttySPI, 391Khz
    SPI: use CS0 on hardware that way have CS0 and CS2 linked, GPIOmode_grp1 configured to use PC-Card
    ttySPI, 391Khz
    ttySPI, 781Khz
    ttySPI, 781Khz
    ttySPI, 781Khz
    Hardware version: 0x31303032 - Software version: 0x34313832
    < HCI Command: ogf 0x3f, ocf 0x0002, plen 6
      2A 86 93 AE 16 00 
    > HCI Event: 0x0e plen 4
      03 02 FC 00 
    Configuring BT name
    Connecting Daemons ...
    Launching sdp and rfcomm services ...
    Dial-Up Networking service registered
    restart pairingd
    pairingd : SIGTERM received
    Configuring AFH
    < HCI Command: ogf 0x03, ocf 0x003f, plen 10
      00 00 00 FE FF FF FF FF FF FF 
    > HCI Event: 0x0e plen 4
      03 3F 0C 00 
    Testing and configuring WIFI coexistence
    [p2] wl_event, bssid idx: 0
    [p2] wl_event, dev: 00000000
    [p2] dev == NULL, using wl->dev
    [p2] wl_event, dev->name: wl0
    [p2] wlc_sendup_event, bssid:0
    [p2] wl_event, bssid idx: 0
    [p2] wl_event, dev: 00000000
    [p2] dev == NULL, using wl->dev
    [p2] wl_event, dev->name: wl0
    [p2] wlc_sendup_event, bssid:0
    < HCI Command: ogf 0x3f, ocf 0x0107, plen 5
      00 00 00 00 00 
    > HCI Event: 0x0e plen 4
      03 07 FD 01 
    coexistence not supported
    [p2] wl_event, bssid idx: 0
    [p2] wl_event, dev: 00000000
    [p2] dev == NULL, using wl->dev
    [p2] wl_event, dev->name: wl0
    [p2] wlc_sendup_event, bssid:0
    [p2] wl_event, bssid idx: 0
    [p2] wl_event, dev: 00000000
    [p2] dev == NULL, using wl->dev
    [p2] wl_event, dev->name: wl0
    [p2] wlc_sendup_event, bssid:0
    < HCI Command: ogf 0x3f, ocf 0x0107, plen 5
      FF FF 00 00 00 
    > HCI Event: 0x0e plen 4
      03 07 FD 01 
    + break
    + [ -f /etc/rc1.d/S28krtp ]
    + [ -f /usr/etc/rc1.d/S28krtp ]
    + realscript=/usr/etc/rc1.d/S28krtp
    + [ 1 != N ]
    + number=28krtp
    + echo 28krtp
    + cut -c 1-2
    + number=28
    + echo 28
    + suffix=krtp
    + stop=/usr/etc/rc1.d/K[0-9][0-9]krtp
    + echo /usr/etc/rc1.d/
    + sed s,rc1,rcN,
    + previous_start=/usr/etc/rcN.d/S[0-9][0-9]krtp
    + [ -f /usr/etc/rcN.d/S[0-9][0-9]krtp ]
    + sh /usr/etc/rc1.d/S28krtp start
    krtp start ...
    krtp ver 2.8 softdsp-vad-multiline-wb (Mar 14 2008 19:16:47)
    Copyright (C) 2004 Inventel Systemes
    Written 2004 by David Libault <david.libault@inventel.fr>
    Written 2004 by Bruce Forgues <bruce.forgues@inventel.fr>
    Written 2004 by Eric Humbert  <eric.humbert@inventel.fr>
    + break
    + [ -f /etc/rc1.d/S85voip ]
    + [ -f /usr/etc/rc1.d/S85voip ]
    + realscript=/usr/etc/rc1.d/S85voip
    + [ 1 != N ]
    + number=85voip
    + echo 85voip
    + cut -c 1-2
    + number=85
    + echo 85
    + suffix=voip
    + stop=/usr/etc/rc1.d/K[0-9][0-9]voip
    + echo /usr/etc/rc1.d/
    + sed s,rc1,rcN,
    + previous_start=/usr/etc/rcN.d/S[0-9][0-9]voip
    + [ -f /usr/etc/rcN.d/S[0-9][0-9]voip ]
    + sh /usr/etc/rc1.d/S85voip start
    iptables: No chain/target/match by that name
    iptables: No chain/target/match by that name
    iptables: No chain/target/match by that name
    voip start...
    + break
    + [ -f /etc/rc1.d/S90post_webupgrade ]
    + [ -f /usr/etc/rc1.d/S90post_webupgrade ]
    + realscript=/usr/etc/rc1.d/S90post_webupgrade
    + [ 1 != N ]
    + number=90post_webupgrade
    + echo 90post_webupgrade
    + cut -c 1-2
    + number=90
    + echo 90
    + suffix=post_webupgrade
    + stop=/usr/etc/rc1.d/K[0-9][0-9]post_webupgrade
    + echo /usr/etc/rc1.d/
    + sed s,rc1,rcN,
    + previous_start=/usr/etc/rcN.d/S[0-9][0-9]post_webupgrade
    + [ -f /usr/etc/rcN.d/S[0-9][0-9]post_webupgrade ]
    + sh /usr/etc/rc1.d/S90post_webupgrade start
    [post_webupgrade] Detected 'start' from rc script during a normal boot. I will not start services now
    + break
    + [ -f /etc/rc1.d/S99printkoff ]
    + realscript=/etc/rc1.d/S99printkoff
    + [ 1 != N ]
    + number=99printkoff
    + echo 99printkoff
    + cut -c 1-2
    + number=99
    + echo 99
    + suffix=printkoff
    + stop=/etc/rc1.d/K[0-9][0-9]printkoff
    + echo /etc/rc1.d/
    + sed s,rc1,rcN,
    + previous_start=/etc/rcN.d/S[0-9][0-9]printkoff
    + [ -f /etc/rcN.d/S[0-9][0-9]printkoff ]
    + sh /etc/rc1.d/S99printkoff start
    Setting printk off
    + break
    + rm -f /var/run/rc.pid
    + rm -f /var/run/runlevel_in_progress
    + rm -f /var/run/init_in_progress_stage
    + echo 1
    Sysinit done
    Please press Enter to activate this console. 
    Starting pid 824, console /dev/tts/0: '/bin/login'
    Mobistar-8628 login: root
    Password: 
    Login incorrect
    Mobistar-8628 login: 
    Login timed out after 60 seconds.
    Please press Enter to activate this console. 
    Starting pid 825, console /dev/tts/0: '/bin/login'
    Mobistar-8628 login: root
    Password: 
    Login incorrect
    Mobistar-8628 login: 
    Login timed out after 60 seconds.
    Please press Enter to activate this console. a
    Starting pid 826, console /dev/tts/0: '/bin/login'
    Mobistar-8628 login: admin
    Password: 
    Login incorrect
    Mobistar-8628 login: root
    Password: 
    Login incorrect
    Mobistar-8628 login: admin
    Password: 
    Login incorrect
    Jan  1 00:05:35 login[826]: invalid password for `UNKNOWN' on `tts/0'
    Please press Enter to activate this console. 	
    Starting pid 827, console /dev/tts/0: '/bin/login'
    Mobistar-8628 login: root
    Password: 
    Login incorrect
    Mobistar-8628 login: admin
    Password: 
    Login incorrect
    Mobistar-8628 login: 
    Login timed out after 60 seconds.
    Please press Enter to activate this console. 
    Starting pid 828, console /dev/tts/0: '/bin/login'
    Mobistar-8628 login:
