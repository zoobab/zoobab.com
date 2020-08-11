# Platform


It is based on a Infineon Danube SoC.

# Pictures


[[module FlickrGallery photosetId="72157626447041830"]]

# OpenWRT


iThe ARV4510 seems to be supported by OpenWRT, but there seems to be a need to flash the bootloader with uBoot.

# Screenlog



    # ls
    antispam  dev       home      mnt       proc      sys       var
    bin       etc       lib       opt       sbin      tmp
    # reboot
    # The system is going down NOW !!
    Sending SIGTERM to all processes.
    Sending SIGKILL to all processes.
    Please stand by while rebooting the system.
    ROM VER: 1.0.3
    CFG 01
    Read EEPROMX
       _                              
      | |__   _____      ____ _ _ __  
      | '_ \ / _ \ \ /\ / / _` | '_ \ 
      | |_) |  __/\ V  V / (_| | | | |
      |_.__/ \___| \_/\_/ \__,_|_| |_|
    Portions Copyright (c) 2005-2007 bewan systems
       www.bewan.com
    Parameters:
      Product         : A50801
      Product family  : A50800
      Flash size      : 1000000
      DRAM size       : 2000000
      Ethernet        : MII
      LAN MAC address : 00:0c:c3:71:38:5d
      WAN MAC address : 00:0c:c3:71:38:5d
      Dual bank boot  : yes
      Reset           : no
      Pairing         : no
      Serial number   : 970000074199973
      WEP key         : 9AYRGS2YA4TNR
      Loader version  : 8029
      Capabilities    : 80000000
    Found valid bootable partition 0:
      Copyright (c) 2006-2007 BeWAN Systems
      Arcadyan ARV4510PW-A-LF-L3 - OOL
      A50802
      2007-07-02-12:27:05
      A50802-ool13-6548.bin
    Found valid bootable partition 1:
      Copyright (c) 2006-2007 BeWAN Systems
      Arcadyan ARV4510PW-A-LF-L3 Generic
      A50801
      2007-10-05-17:54:27
      A50801-gen7-8029.bin
    Booting from partition 1 in flash.
    Loading: Linux Kernel Image
    Load address = 80000000
    Uncompressing Linux...................
    done, booting the kernel.
    start addr = 802B1000
    memsize=31
    TODO: chip version
    Linux version 2.6.16bewan (build@megabob) (gcc version 3.3.4) #1 Fri Oct 5 17:41:51 CEST 2007
    Reserving memory for CP1 @0xa1f00000
    memsize=31
    CPU revision is: 00019641
    PCI: Probing PCI hardware on host bus 0.
    Board with an external oscillator
    Determined physical RAM map:
     memory: 01f00000 @ 00000000 (usable)
    User-defined physical RAM map:
     memory: 01f00000 @ 00000000 (usable)
    Built 1 zonelists
    Kernel command line: nofpu console=ttyS0,115200n1 bewan_boot=flash1 bewan_fs_addr=0x8e9000 bewan_fs_size=0x717000 mem=31M 
    Primary instruction cache 16kB, physically tagged, 4-way, linesize 32 bytes.
    Primary data cache 16kB, 4-way, linesize 32 bytes.
    Synthesized TLB refill handler (20 instructions).
    Synthesized TLB load handler fastpath (32 instructions).
    Synthesized TLB store handler fastpath (32 instructions).
    Synthesized TLB modify handler fastpath (31 instructions).
    Cache parity protection disabled
    PID hash table entries: 128 (order: 7, 2048 bytes)
    mips_hpt_frequency:166666667
    r4k_offset: 00196e6a(1666666)
    Using 166.667 MHz high precision timer.
    Dentry cache hash table entries: 4096 (order: 2, 16384 bytes)
    Inode-cache hash table entries: 2048 (order: 1, 8192 bytes)
    Memory: 27912k/31744k available (2293k kernel code, 3832k reserved, 459k data, 152k init, 0k highmem)
    Mount-cache hash table entries: 512
    Checking for 'wait' instruction...  available.
    NET: Registered protocol family 16
    DANUBE MIPS24KEc MPS mailbox driver, Version 1.1.0
    (c) Copyright 2006, Infineon Technologies AG
    IFX_MPS: using proc fs
    squashfs: version 3.0 (2006/03/15) Phillip Lougher
    Squashfs 2.2 with LZMA support
    devfs: 2004-01-31 Richard Gooch (rgooch@atnf.csiro.au)
    devfs: boot_options: 0x1
    Initializing Cryptographic API
    io scheduler noop registered (default)
    Danube MEI version:1.00.09
    Danube MEI MIB version:0.90.04
    Danube Port Settings
    Danube Port Initialization
    cgu: misc_register on minor = 63
    gptu: totally 6 16-bit timers/counters
    gptu: misc_register on minor 62
    gptu: succeeded to request irq 118
    gptu: succeeded to request irq 119
    gptu: succeeded to request irq 120
    gptu: succeeded to request irq 121
    gptu: succeeded to request irq 122
    gptu: succeeded to request irq 123
    ttyS0 at MMIO 0xbe100c00 (irq = 9) is a DANUBEASC
    ttyS1 at MMIO 0xbe100400 (irq = 2) is a DANUBEASC
    RAMDISK driver initialized: 16 RAM disks of 8192K size 1024 blocksize
    loop: loaded (max 8 devices)
    PPP generic driver version 2.4.2
    NET: Registered protocol family 24
    danube ETOP driver loaded!
    ppe: ATM init succeeded (firmware version 1.1.0.2.1.13
    Danube IAD flash device: 0x1000000 at 0xb0000000
    Danube IAD FLASH: Found 1 x16 devices at 0x0 in 16-bit bank
     Intel/Sharp Extended Query Table at 0x0031
    cfi_cmdset_0001: Erase suspend on write enabled
    Creating 5 MTD partitions on "Danube IAD FLASH":
    0x00000000-0x01000000 : "Flash"
    0x00000000-0x00020000 : "Loader"
    0x00020000-0x00040000 : "Config"
    0x00820000-0x01000000 : "Firmware"
    0x00040000-0x00820000 : "OldFirmware"
    bootpart=2
    Creating 1 MTD partitions on "Danube IAD FLASH":
    0x008e9000-0x01000000 : "romFS"
    rootdev = 31,5
    LED and Buttons driver: v2.6.0
    NET: Registered protocol family 2
    IP route cache hash table entries: 256 (order: -2, 1024 bytes)
    TCP established hash table entries: 1024 (order: 0, 4096 bytes)
    TCP bind hash table entries: 1024 (order: 0, 4096 bytes)
    TCP: Hash tables configured (established 1024 bind 1024)
    TCP reno registered
    ip_conntrack version 2.4 (248 buckets, 1984 max) - 212 bytes per conntrack
    ip_tables: (C) 2000-2006 Netfilter Core Team
    arp_tables: (C) 2002 David S. Miller
    TCP bic registered
    Initializing IPsec netlink socket
    NET: Registered protocol family 1
    NET: Registered protocol family 17
    NET: Registered protocol family 15
    Ebtables v2.0 registered
    802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
    All bugs added by David S. Miller <davem@redhat.com>
    Ethernet Multiplexer Support v1.0 Christophe Piel (c) 2006 BeWAN systems
    VFS: Mounted root (squashfs filesystem) readonly.
    Mounted devfs on /dev
    Freeing unused kernel memory
    DS max rate = 0 kbps
    US max rate = 0 kbps
    DS payload rate = 0 kbps
    US payload rate = 0 kbps
    Local CRC = 0
    Remote CRC = 0
    init started:  BusyBox v1.00 (2007.10.05-15:44+0000) multi-call binary
    Starting pid 120, console /dev/tts/0: '/etc/rc'
    Algorithmics/MIPS FPU Emulator v1.5
    Software Watchdog Timer: 0.05, timer margin: 120 sec.
    Mon Jan  1 00:00:00 UTC 2007
     _                              
    | |__   _____      ____ _ _ __  
    | '_ \ / _ \ \ /\ / / _` | '_ \ 
    | |_) |  __/\ V  V / (_| | | | |
    |_.__/ \___| \_/\_/ \__,_|_| |_|
    IFX TAPI, version 3.5.2.5, (c) 2007 Infineon Technologies
    IFX VMMC device driver, version 1.1.6.5, (c) 2007 Infineon Technologies AG
    <6>usbcore: registered new driver usbfs
    usbcore: registered new driver hub
    usbcore: registered new driver usblp
    drivers/usb/class/usblp.c: v0.13: USB Printer Device Class driver
    SCSI subsystem initialized
    Initializing USB Mass Storage driver...
    usbcore: registered new driver usb-storage
    USB Mass Storage support registered.
    PCI: Enabling device 0000:00:0f.2 (0000 -> 0002)
    plat_dev_init(810a6400)
    ehci_hcd 0000:00:0f.2: EHCI Host Controller
    ehci_hcd 0000:00:0f.2: new USB bus registered, assigned bus number 1
    ehci_hcd 0000:00:0f.2: irq 26, io mem 0x18010000
    ehci_hcd 0000:00:0f.2: USB 2.0 started, EHCI 1.00, driver 10 Dec 2004
    usb usb1: configuration #1 chosen from 1 choice
    hub 1-0:1.0: USB hub found
    hub 1-0:1.0: 4 ports detected
    USB Universal Host Controller Interface driver v2.3
    PCI: Enabling device 0000:00:0f.0 (0000 -> 0001)
    plat_dev_init(810a6c00)
    uhci_hcd 0000:00:0f.0: UHCI Host Controller
    uhci_hcd 0000:00:0f.0: new USB bus registered, assigned bus number 2
    uhci_hcd 0000:00:0f.0: irq 26, io base 0x1ae00000
    usb 1-1: new high speed USB device using ehci_hcd and address 2
    usb usb2: configuration #1 chosen from 1 choice
    hub 2-0:1.0: USB hub found
    hub 2-0:1.0: 2 ports detected
    usb 1-1: configuration #1 chosen from 1 choice
    scsi0 : SCSI emulation for USB Mass Storage devices
    PCI: Enabling device 0000:00:0f.1 (0000 -> 0001)
    plat_dev_init(810a6800)
    uhci_hcd 0000:00:0f.1: UHCI Host Controller
    uhci_hcd 0000:00:0f.1: new USB bus registered, assigned bus number 3
    uhci_hcd 0000:00:0f.1: irq 26, io base 0x1ae00020
    usb usb3: configuration #1 chosen from 1 choice
    hub 3-0:1.0: USB hub found
    hub 3-0:1.0: 2 ports detected
    x10: X10 DEV module v2.1.3 (wsh@sprintmail.com)
    x10: $Id: dev.c,v 1.22 2005/03/27 04:39:26 root Exp root $
    x10: X10 driver successfully loaded
    Linux video capture interface: v1.00
    pwc: Philips webcam module version 10.0.12-rc1 loaded.
    pwc: Supports Philips PCA645/646, PCVC675/680/690, PCVC720[40]/730/740/750 & PCVC830/840.
    pwc: Also supports the Askey VC010, various Logitech Quickcams, Samsung MPC-C10 and MPC-C30,
    pwc: the Creative WebCam 5 & Pro Ex, SOTEC Afina Eye and Visionite VCS-UC300 and VCS-UM100.
    usbcore: registered new driver Philips webcam
    usbcore: registered new driver quickcam
      Vendor: Generic   Model: USB Flash Drive   Rev: 1.00
      Type:   Direct-Access                      ANSI SCSI revision: 02
    SCSI device sda: 2072064 512-byte hdwr sectors (1061 MB)
    sda: Write Protect is off
    sda: assuming drive cache: write through
    SCSI device sda: 2072064 512-byte hdwr sectors (1061 MB)
    sda: Write Protect is off
    sda: assuming drive cache: write through
     /dev/scsi/host0/bus0/target0/lun0: p1
    sd 0:0:0:0: Attached scsi removable disk sda
    /etc/init.d/syslog start
    /etc/init.d/dsl start
    modprobe: module ctlmeth not found.
    modprobe: failed to load module ctlmeth
    /etc/init.d/interface start LANEthernetInterface 1
    /etc/init.d/switch stop 1
    /etc/init.d/phy stop 1 1
    using the specified MII index 19.
    power down...
    /etc/init.d/phy stop 1 2
    using the specified MII index 18.
    power down...
    /etc/init.d/phy stop 1 3
    using the specified MII index 17.
    power down...
    /etc/init.d/phy stop 1 4
    using the specified MII index 16.
    power down...
    /etc/init.d/wifi nothing 1
    /etc/init.d/wifi nothing 2
    modprobe: module ctlmatm not found.
    modprobe: failed to load module ctlmatm
    /etc/init.d/interface start ATMEthernetInterface 1
    /etc/init.d/atm start 1
    /bin/atmcfg atm1 -flowset 15 0 0 3 0 0 0 1
    /bin/atmcfg atm1 -vccopen 8 35 15 llc pppoe
    /etc/init.d/interface nothing ATMEthernetInterface 2
    /etc/init.d/interface nothing ATMEthernetInterface 3
    /etc/init.d/interface nothing ATMEthernetInterface 4
    /etc/init.d/interface nothing ATMEthernetInterface 5
    /etc/init.d/autodslam start auto-stop
    /etc/init.d/lan start 1
    /etc/init.d/lanif start 1 all
    date: 13, month: 7, hour: 58, minute: 4
    /etc/init.d/lanintf start lan1 eth0
    device eth0 entered promiscuous mode
    /etc/init.d/lanintf nothing lan1 ath0
    /etc/init.d/lanip start 1
    /etc/config.default/ip-up-dhcp lan1 192.168.1.1
    lan1: port 1(eth0) entering listening state
    /etc/init.d/host start
    /etc/init.d/igmp start
    /etc/init.d/ipsec restart all
    /etc/init.d/landhcp start 1
    /etc/init.d/racoon stop
    /etc/init.d/lanacl start 1
    /etc/init.d/passthrough nothing 1
    /etc/init.d/lan nothing 2
    /etc/init.d/lan nothing 3
    /etc/init.d/lan nothing 4
    /etc/init.d/lan nothing 5
    /etc/init.d/users start
    /etc/init.d/unix start
    /etc/init.d/unixusers start 1
    /etc/init.d/unixusers start 2
    /etc/init.d/samba start
    /etc/init.d/pureftpd start
    /etc/init.d/unixadmin start
    /etc/init.d/time start
    /etc/init.d/mdns start
    /etc/init.d/rmthttp start
    /etc/init.d/wan start 1
    /etc/init.d/interface start WANConnectionDevice 1
    /etc/init.d/wannet start 1
    /etc/init.d/wanbr nothing 1
    /etc/init.d/wanip nothing 1
    /etc/init.d/wanppp start 1
    /etc/init.d/firewall start 1
    /etc/init.d/ports start 1
    /etc/init.d/wan nothing 2
    /etc/init.d/wan nothing 3
    /etc/init.d/wan nothing 4
    /etc/init.d/wan nothing 5
    /etc/init.d/qos start all
    /etc/init.d/dhcp start all
    /etc/init.d/dhcpd start all
    /etc/init.d/dhcrelay start all
    /etc/init.d/hbrdhcp start all
    /etc/init.d/dnsmasq start all
    /etc/init.d/pppd start all
    /etc/init.d/dhclient start all
    /etc/init.d/hostapd nothing all
    /etc/init.d/wsccmd nothing all
    /etc/init.d/wpa_supplicant nothing all
    /etc/init.d/pptp stop
    /etc/init.d/openl2tp stop
    /etc/init.d/ipsec restart all
    /etc/init.d/racoon stop
    lan1: port 1(eth0) entering learning state
    /etc/init.d/fwrules nothing
    /etc/init.d/iptables start
    /etc/init.d/ebtables nothing
    /etc/init.d/routes start
    /etc/init.d/upnp start
    /etc/init.d/dyndns nothing
    /etc/init.d/phy start 1 1
    using the specified MII index 19.
    resetting the transceiver...
    restarting autonegotiation...
    /etc/init.d/phy start 1 2
    using the specified MII index 18.
    resetting the transceiver...
    restarting autonegotiation...
    /etc/init.d/phy start 1 3
    using the specified MII index 17.
    resetting the transceiver...
    restarting autonegotiation...
    /etc/init.d/phy start 1 4
    using the specified MII index 16.
    resetting the transceiver...
    restarting autonegotiation...
    modprobe: module fuse not found.
    modprobe: failed to load module fuse
    /etc/init.d/inittab
    rc completed
    Starting pid 969, console /dev/tts/0: '/bin/sh'
    # Starting pid 970, console /dev/null: '/sbin/syslogd'
    Starting pid 971, console /dev/null: '/sbin/klogd'
    Starting pid 972, console /dev/null: '/bin/dhcpd'
    Starting pid 973, console /dev/null: '/bin/dnsmasq'
    Starting pid 974, console /dev/null: '/sbin/igmpproxyd'
    Starting pid 975, console /dev/null: '/bin/mDNSResponderPosix'
    Starting pid 976, console /dev/null: '/bin/pppd'
    Starting pid 977, console /dev/console: '/bin/resetd'
    Starting pid 979, console /dev/console: '/bin/wdgd'
    Starting pid 978, console /dev/null: '/bin/upnpd'
    Software Watchdog Timer: set margin to 40 sec.
    /etc/init.d/upgd nothing
    /etc/init.d/inetd start
    /etc/init.d/http start
    /etc/init.d/htpwd start
    /etc/init.d/tr069 nothing
    /etc/init.d/usbdevices
    /etc/init.d/printer start
    /etc/init.d/voip-asterisk nothing
    /etc/init.d/bluetooth nothing
    /etc/init.d/host start
    lan1: topology change detected, propagating
    lan1: port 1(eth0) entering forwarding state
    /etc/init.d/userscreatedir start
    /etc/init.d/usersdir start 1
    /etc/init.d/usersdir start 2
    /etc/init.d/sambaserver refresh
    /etc/init.d/pureftpdserver start
    /etc/init.d/obexpush nothing4
    /etc/init.d/upnpav nothing
    /etc/init.d/web nothing
    /etc/init.d/webcam start
    /etc/init.d/inittab
    Reloading /etc/inittab
    Starting pid 1316, console /dev/console: '/bin/thttpd'
    Starting pid 1317, console /dev/null: '/bin/vidcat'
    # ls
    antispam  dev       home      mnt       proc      sys       var
    bin       etc       lib       opt       sbin      tmp
    # cat /et	
    # cd /etc
    # lks
    -sh: lks: not found
    # ls
    asterisk          dsskey.bin        lighttpd          rc
    asterisk.default  file              motd              rc2
    bluetooth         flash             p3scan            release
    chatscripts       fstab             passwd            resolv.conf
    codepages         group             ppp               services
    config            hosts             ppp.default       version
    config.default    inetd.conf        pptpd
    dhclient-script   init.d            pptpd.default
    dhcpd-up          inittab           ramfs.img
    # cd /lib
    # ls
    asterisk              libm-0.9.27.so        libsamba.so.0
    configlib.so          libm.so.0             libssl.so
    iptables              libmagic.so           libssl.so.0
    ld-uClibc-0.9.27.so   libmagic.so.1         libssl.so.0.9.8
    ld-uClibc.so.0        libmagic.so.1.0.0     libuClibc-0.9.27.so
    libadm6996.so         libnetlink.so         libusb-0.1.10a.so
    libc.so.0             libnsl-0.9.27.so      libusb.so
    libcrypt-0.9.27.so    libnsl.so.0           libusb.so.0
    libcrypt.so.0         libplat.so            libutil-0.9.27.so
    libcrypto.so          libpng.so             libutil.so.0
    libcrypto.so.0        libpng.so.0           libz.so
    libcrypto.so.0.9.8    libpng.so.0.1.2.8     libz.so.1
    libdhcp.so            libpthread-0.9.27.so  libz.so.1.2.3
    libdl-0.9.27.so       libpthread.so.0       mod_auth.so
    libdl.so.0            libresolv-0.9.27.so   mod_cgi.so
    libiputil.so          libresolv.so.0        mod_dirlisting.so
    libiw.so.27           librt-0.9.27.so       mod_indexfile.so
    libjpeg.so            librt.so.0            mod_staticfile.so
    libjpeg.so.62         libsamba-0.1.0.so     modules
    libjpeg.so.62.0.0     libsamba.so           rp-pppoe.so
    # cd 
    cd asterisk
    # ls
    modules
    # cd mi
    odules
    # ls
    app_dial.so         chan_mgcp_ua.so     format_g723.so      format_wav.so
    app_echo.so         chan_phone_tapi.so  format_g726.so      format_wav_gsm.so
    app_playback.so     chan_sip.so         format_g729.so      func_callerid.so
    app_system.so       codec_alaw.so       format_gsm.so       pbx_config.so
    app_while.so        codec_gsm.so        format_pcm.so       res_features.so
    chan_local.so       codec_ulaw.so       format_pcm_alaw.so  res_indications.so
    # cd .
    cd ../
    # ls
    modules
    # cd ..
    # ls
    asterisk              libm-0.9.27.so        libsamba.so.0
    configlib.so          libm.so.0             libssl.so
    iptables              libmagic.so           libssl.so.0
    ld-uClibc-0.9.27.so   libmagic.so.1         libssl.so.0.9.8
    ld-uClibc.so.0        libmagic.so.1.0.0     libuClibc-0.9.27.so
    libadm6996.so         libnetlink.so         libusb-0.1.10a.so
    libc.so.0             libnsl-0.9.27.so      libusb.so
    libcrypt-0.9.27.so    libnsl.so.0           libusb.so.0
    libcrypt.so.0         libplat.so            libutil-0.9.27.so
    libcrypto.so          libpng.so             libutil.so.0
    libcrypto.so.0        libpng.so.0           libz.so
    libcrypto.so.0.9.8    libpng.so.0.1.2.8     libz.so.1
    libdhcp.so            libpthread-0.9.27.so  libz.so.1.2.3
    libdl-0.9.27.so       libpthread.so.0       mod_auth.so
    libdl.so.0            libresolv-0.9.27.so   mod_cgi.so
    libiputil.so          libresolv.so.0        mod_dirlisting.so
    libiw.so.27           librt-0.9.27.so       mod_indexfile.so
    libjpeg.so            librt.so.0            mod_staticfile.so
    libjpeg.so.62         libsamba-0.1.0.so     modules
    libjpeg.so.62.0.0     libsamba.so           rp-pppoe.so
    # cd //
    # ls
    antispam  dev       home      mnt       proc      sys       var
    bin       etc       lib       opt       sbin      tmp
    # cd home
    # ls
    # ps
      PID  Uid     VmSize Stat Command
        1 root        360 S   init       
        2 root            SW< [ksoftirqd/0]
        3 root            SW< [events/0]
        4 root            SW< [khelper]
        5 root            SW< [kthread]
        6 root            SW< [kblockd/0]
       39 root            SW  [pdflush]
       40 root            SW  [pdflush]
       42 root            SW< [aio/0]
       41 root            SW  [kswapd0]
       47 root            SW  [kmibpoll]
       48 root            SW  [dsl/0]
       80 root            SW< [eth_leds]
       95 root            SW  [mtdblockd]
      210 root            SW< [khubd]
      318 root            SW< [scsi_eh_0]
      319 root            SW< [usb-storage]
      508 root        316 S   /sbin/danube_autoboot_daemon /sbin/modemhwe.bin all 
      969 root        360 S   -sh 
      970 root        328 S   /sbin/syslogd -n -S -C 64 
      971 root        308 S   /sbin/klogd -n 
      972 root        436 S   /bin/dhcpd -q -d -f -cf /etc/config/dhcpd.conf -lf /v
      973 root        320 S   /bin/dnsmasq -f -r /var/etc/config/resolv.conf -l /va
      974 root        364 S   /sbin/igmpproxyd -D -l3 -c /var/etc/config/igmpproxy.
      975 root        388 S   /bin/mDNSResponderPosix -f /etc/config/mdns/services.
      976 root        584 S   /bin/pppd file /etc/ppp/options.wan1 wan1 
      977 root        280 S   /bin/resetd 
      978 root        680 S   /bin/upnpd lan1 ppp1 
      979 root        156 S   /bin/wdgd 
      991 root        680 S   /bin/upnpd lan1 ppp1 
      992 root        680 S   /bin/upnpd lan1 ppp1 
      993 root        680 S   /bin/upnpd lan1 ppp1 
      994 root        680 S   /bin/upnpd lan1 ppp1 
      995 root        680 S   /bin/upnpd lan1 ppp1 
      996 root        680 S   /bin/upnpd lan1 ppp1 
      997 root        680 S   /bin/upnpd lan1 ppp1 
      998 root        680 S   /bin/upnpd lan1 ppp1 
      999 root        680 S   /bin/upnpd lan1 ppp1 
     1316 root        356 S   /bin/thttpd -p 8080 -d /etc/config.default/html -i /v
     1317 root        336 S   /bin/vidcat -d /dev/v4l/video0 -o /var/home/www/webca
     1329 root        348 R   ps 
    # Process '-/bin/sh' (pid 969) exited.  Scheduling it for restart.
    usb 1-1: USB disconnect, address 2
    /etc/init.d/pureftpdserver stop
    /etc/init.d/obexpush stop
    /etc/init.d/upnpav stop
    /etc/init.d/web stop
    /etc/init.d/inittab
    Reloading /etc/inittab
    /etc/init.d/userscreatedir start
    /etc/init.d/usersdir start 1
    /etc/init.d/usersdir start 2
    /etc/init.d/sambaserver refresh
    /etc/init.d/pureftpdserver start
    /etc/init.d/obexpush nothing4
    /etc/init.d/upnpav nothing
    /etc/init.d/web nothing
    /etc/init.d/inittab
    Reloading /etc/inittab


# Links


* <http://koti.kapsi.fi/jvaarani/homebox/>  
* <http://code.google.com/p/quickanddirty/wiki/WippiesHomeBox>  