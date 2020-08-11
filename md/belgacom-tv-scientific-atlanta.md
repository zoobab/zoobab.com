

# About


Scientific-Atlanta Model IPP330HD

[[=image belgacom-tv-scientific-atlanta-IPP330HD.jpg]]

# Nmap



    root@buzek /home/zoobab [4]# nmap -O 10.20.30.140
    
    Starting Nmap 5.21 ( http://nmap.org ) at 2012-01-08 17:13 CET
    Nmap scan report for 10.20.30.140
    Host is up (0.00081s latency).
    Not shown: 997 closed ports
    PORT     STATE SERVICE
    22/tcp   open  ssh
    80/tcp   open  http
    9001/tcp open  tor-orport
    MAC Address: 00:1E:6B:6C:FF:27 (Scientific Atlanta, A Cisco Company)
    Device type: general purpose
    Running: Linux 2.6.X
    OS details: Linux 2.6.9 - 2.6.28
    Network Distance: 1 hop


# Dropbear



    root@buzek /home/zoobab [6]# telnet 10.20.30.140 22
    Trying 10.20.30.140...
    Connected to 10.20.30.140.
    Escape character is '^]'.
    SSH-2.0-dropbear_0.46


# Http


On port 80, there is a login/password box with "Operational Diagnostics Login". No idea what to put there.

# Serial


Croatian hackers found the [serial port pinout](http://213.202.123.24/forum/topic/digitalna-televizija/kako-iskoristiti-stari-maxtv-stb/69014.aspx?jumpto=1285045&sort=asc&view=flat&page=26):

[[=image belgacom-tv-scientific-atlanta-IPP330HD-serial-port-pinout.jpg]]

Here is the output in 115200:


    DxosPda serial#afa2fcedc0bcf7f32f972ae535a509e1 subid 0xc4
    xenv cs2 ok
    power supply: ok
    dram0 ok (7)
    dram1 ok (8)
    zboot ok
    ����������������������������������������


It has switched to another speed of 38400:


    **********************************
    * FocusBoot start ...
    * Build Date: Nov 12 2007
    * Build Version: 1.4.0.1
    * Started at 0x94400000.
    * Configurations (chip revision: 4):
    *    Use 8KB DRAM as stack.
    *    Support XLoad format.
    **********************************
    Boot from flash (0x48000000) mapped to 0xac000000.
    Found XENV block at 0xac000000.
    CPU clock frequency: 301.50MHz.
    System clock frequency: 201.00MHz.
    DRAM0 dunit_cfg/delay0_ctrl (0xf34111ba/0x00098888).
    DRAM1 dunit_cfg/delay0_ctrl (0xf34111ba/0x000b9897).
    Board ID.: "Scientific-Atlanta"
    Chip Revision: 0x8634:0x82 .. Mismatched.
    Setting up H/W from XENV block at 0xac000000.
      Setting <SYSCLK premux> to 0x00000603.
      Setting <SYSCLK avclk_mux> to 0x00000000.
      Setting <SYSCLK hostclk_mux> to 0x00000100.
      Setting <IRQ rise edge trigger lo> to 0xff284a00.
      Setting <IRQ fall edge trigger lo> to 0x0000c000.
      Setting <IRQ rise edge trigger hi> to 0x000001ff.
      Setting <IRQ fall edge trigger hi> to 0x00000000.
      Setting <IRQ GPIO map> to 0x0d0c0800.
      Setting <PB default timing> to 0x10101010.
      Setting <PB timing0> to 0x10101010.
      Setting <PB Use timing0> to 0x000001f4.
      Setting <PB timing1> to 0x00110101.
      Setting <PB Use timing1> to 0x000003f3.
      PB cs config: 0x000c10c0 (use 0x000c10c0)
      Enabled Devices: 0x000202fa
        BM/IDE Ethernet IR FIP I2CM I2CS USB SCARD
      Smartcard pin assignments:
        OFF pin = 0
        5V pin = 1
        CMD pin = 2
      Setting up Clean Divider 2 to 96000000Hz.
      Setting up Clean Divider 4 to 33333333Hz.
      GPIO dir/data = 0x00020000/0x00000000
      UART0 GPIO mode/dir/data = 0x6e/0x00/0x00
      UART1 GPIO mode/dir/data = 0x00/0x00/0x00
    XENV block processing completed.
    Found existing memcfg: DRAM0(0x08000000), DRAM1(0x08000000)
    Serial Init Done
    *****************************************
    Configuring Flash Sizes...
    Boot Flash Size is 2M
    App Flash Size is 64M
    Total Flash Size: 0x4200000
    *****************************************
    Configuring the Boot Flash
    Flash device is the Spansion S29GL...
    *****************************************
    Configuring the Application Flash
    Flash device is the Spansion S29GL...
    Configuring 64M Flash part
    *****************************************
    Flash Init Done
    Front Panel Init Done
    ********* STAGE *1* BOOTLOADER ************
    * Build Date: Nov 12 2007
    * Build Version: 1.4.0.1
    ********************************************
    SOC Mac Address:00:1e:6b:6c:ff:27
    hpnaSelect value = 0
    ********************************************************
    *       --------> No HPNA Device present <--------     *
    ********************************************************
    Boot Delay: 2009ms
    ____________Starting DHCP Process__________
    ____________STATE_DHCP_DISCOVER____________
    Time since initial DHCP Discover: 0 seconds
    VCI:SAIPP430MC
    ____________STATE_DHCP_OFFER_______________
    DHCP Discover Retransmission Delay: 5013ms
    ____________STATE_DHCP_DISCOVER____________
    Time since initial DHCP Discover: 13 seconds
    VCI:SAIPP430MC
    ____________STATE_DHCP_OFFER_______________
    DHCP Discover Retransmission Delay: 8521ms
    ____________STATE_DHCP_DISCOVER____________
    Time since initial DHCP Discover: 29 seconds
    VCI:SAIPP430MC
    ____________STATE_DHCP_OFFER_______________
    MyIp:10.20.30.140
    ServerIp:10.20.30.1
    NetMask:255.0.0.0
    Filename: 
    ____________STATE_DHCP_REQUEST_____________
    VCI:SAIPP430MC
    ____________STATE_DHCP_DONE________________
    ....Starting CVT Download
    Unable to locate, or use the MCast Info from Option-67...looking for Bootp Filename
    Unable to locate MCast Info from Bootp Filename
    No update data found in CVT
    Downloaded Checksum: 496c62d3d2331046bef989ace7abfc69
    Calculated Checksum: 496c62d3d2331046bef989ace7abfc69
    load_xload(): Calling doxrpc on c040000 [xload.c:27]
    load_xload(): Doing memcpy from 0xac040000 to 0xb1800000, size 0x32d64
     [xload.c:33]
    load_xload(): Setting dest_addr to load_addr
     [xload.c:37]
    Image signature is valid
    Stage 2 is valid. Commencing hyper-jump [0x93000000]
    Turning on the HD LED
    ..Serial Init Done
    *****************************************
    Configuring Flash Sizes...
    Boot Flash Size is 2M
    Device Info
    0x1 0x227e 0x2223 0x2201
    App Flash Size is 64M
    Total Flash Size: 0x4200000
    *****************************************
    Configuring the Boot Flash
    Flash device is the Spansion S29GL...
    *****************************************
    Configuring the Application Flash
    Flash device is the Spansion S29GL...
    Configuring 64M Flash part
    *****************************************
    Flash Init Done
    48 bit address supported
    Max Native Address: 312581807
        Setting drive 0 for Ultra DMA Mode 5.
    ************ STAGE 2 BOOTLOADER ************
    * Build Type: TEST
    * Build Date: Jan 15 2008
    * Build Version: 4.4.0.7
    ********************************************
    _______________Initializating FIP and Ethernet_______________
    Init Stage 2 Bootloader...
    Found entry in the hwApproximation_Table for this VCI, SAIPP430MC
    LED display init completed 
    Stage 2 Bootloader was launched by the ConFocus Bootloader
    Read Mac Address from RO Memory
    Initializing the Ethernet
    _______________Launching Splash Screen_______________________
    Initializing SCART
    Unable to configure the RF Interface, status: 0x2
    ROMFS found at 0xac07e850, Volume name = SADefault.2.1.4.4.0.7.TEST
    Splash Screen ROMFS Container found in flash.
    file[0]: 30_1_vsyncparam.zbf
    file extension: zbf
    Found a ZBF file
    There is an image associated with index 1
    Found 7 file(s) to be processed in ROMFS.
    Processing 30_1_vsyncparam.zbf (start: 0xac07fd90, size: 0x00001403)
      Checking zboot file signature .. OK.
      Decompressing to 0x10001000 .. OK (32192/0x7dc0).
      Load time total 10/34 msec.
    Processing 30_9_vsyncparam.zbf (start: 0xac07e950, size: 0x00001407)
      Checking zboot file signature .. Invalid image index...
    Processing 31_1_bitmap.zbf (start: 0xac0811c0, size: 0x00008755)
      Checking zboot file signature .. OK.
      Decompressing to 0x178addc4 .. OK (1385020/0x15223c).
      Load time total 10/276 msec.
    Processing 31_9_bitmap.zbf (start: 0xac089940, size: 0x0001733c)
      Checking zboot file signature .. Invalid image index...
    Processing 40_dviinit.8634_ES4_prod_000c.bin (start: 0xac0a0cc0, size: 0x00001864)
      Checking zboot file signature .. Not found.
      Trying xrpc_xload format .. OK
      Checking zboot file signature at 0x13000000 .. OK
      Decompressing to 0xb0400000 .. OK (11536/0x2d10).
      Load time total 98/116 msec.
      Execute at 0xb0400000 ..
        **** HDMI/DVI init applet starts ****
        Container addr = 0xac07e850
    File dvi.bin found
    Copying image from 0xac07e8e0 to 0xb0480000, size = 64
        Verify checksum from 0xb0480000, size 64 (0x40).
        Internal HDMI is used
        DVI bin file (dvi.bin) processing completed.
        **** HDMI/DVI init applet ends ****
      Returned result 0.
    Processing 41_xrpc_xload_irq_handler.172.1.bin (start: 0xac0a2570, size: 0x0002d4b4)
      Checking zboot file signature .. Not found.
      Trying xrpc_xload format .. OK
      Checking zboot file signature at 0x00000000 .. OK (but no ZBF header)
    Processing dvi.bin (start: 0xac07e8e0, size: 0x00000040)
      Checking zboot file signature .. Not found.
      Trying xrpc_xload format .. Failed (not an xrpc_xload file)
    _______________Checking For Fast Boot Flag___________________
    Fast Boot Flag not set.
    _______________Downloading App Record________________________
    Downloading Update Records
    Unable to locate, or use the MCast Info from Option-67...looking for Bootp Filename
    Unable to locate MCast Info from Bootp Filename
    OS Version is the same as or older than the current one
    _______________Launching App Image___________________________
    Image Size   : 21508032
    Image CRC    : 0x2ba3e7a2
    Computed CRC : 0x2ba3e7a2
    Data CRC is not being used
    Checking code object type
    Authenticate code image (discard adjustments made to data and len)
    SA-KSK Method Serial Number: 0x00000001
    SN Rules: not retrieved (SaErr=2356)
    Object Signature Authentication:  Rules=TEST  Method=3  SaErr=0
    Error: 0x0
    flashAddr: 0xa8000440
    90 02 00 00 00 39 29 b8 c0 00 00 00 c0 00 00 00 
    00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
    00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
    00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
    copying Kernel part to start address
    Start Address: 0x90020000
    Kernel Size  : 0x3929b8
    Memcpy complete
    Exiting decryptImage
    OS image is valid. Commencing hyper-jump [0x90020000]
    INIT: version 2.86 booting
    starting rcS
    Mounting /var...
    Mount of /dev/mtdblock/1 successful, a JFFS2 filesystem already exists...
    s: applet not found
    vm.min_free_kbytes = 2048
    /sbin/ldconfig: skipping /usr/X11R6/lib: No such file or directory
    Initializing random number generator... done.
    ## Start of S35installModules ##
    Installing kernel module llad.ko
        llad not installed, try installing...
    Using /lib/modules/2.6.15/llad.ko
        sleep for 0 seconds before future attempts...
    Installing kernel module em8xxx.ko
        em8xxx not installed, try installing...
    Using /lib/modules/2.6.15/em8xxx.ko
        sleep for 0 seconds before future attempts...
    Using /lib/modules/2.6.15/fip.ko
    Module                  Size  Used by    Tainted: P  
    fip 6480 0 - Live 0xc806f000
    em8xxx 2926736 0 - Live 0xcc560000
    llad 112032 1 em8xxx, Live 0xcc081000
    ## S35installModules complete ##
    ##Start of S38splashScreen##
    [HDMI] ========================== creating pDH ==========================
    [HDMI] Detected part at I2C device address 0x72: vendor 0x0001, device 9253, rev.0x02 (Silicon Image)
    [HDMI] Using the part: SiI9030 (4), Vendor ID is 0x0001 / 0x9253
    [HDMI]    ***   Clock changed, is now STABLE
    [HDMI] DHLoadEDIDBlock() failed to read EDID block 0
    [HDMI] DHLoadEDIDVersion1() failed to read EDID block 0
    [HDMI] DHLoadEDIDBlock() failed to read EDID block 0
    [HDMI] DHLoadEDIDVersion1() failed to read EDID block 0
    [HDMI] DHUpdateVideoPixelClock(74250000)
    [HDMI] DHSetHDMIMode(FALSE)
    outports_options.c: Application did not specify HDCP SRM, providing empty SRM!
    [HDMI] DHCancelHDCP()
    Initial Link is OK
    ##End of S38splashScreen##
    Starting network...
    eth0      Link encap:Ethernet  HWaddr 00:1E:6B:6C:FF:27  
              BROADCAST MULTICAST  MTU:1500  Metric:1
              RX packets:0 errors:0 dropped:0 overruns:0 frame:0
              TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000 
              RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
              Interrupt:46 
    lo        Link encap:Local Loopback  
              inet addr:127.0.0.1  Mask:255.0.0.0
              UP LOOPBACK RUNNING  MTU:16436  Metric:1
              RX packets:0 errors:0 dropped:0 overruns:0 frame:0
              TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:0 
              RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
    ## S45varupdate start ##
    Read only system: he30.mpp1.rush--17   Current /var version: he30.mpp1.rush--17...
    ## S45varupdate end ##
    ##Start of S50local##
    ln: /etc/dhcpc/dhcpc: File exists
    Checksum is 2c15e17865a4bdc4a0764797bac45728
    Revision is #he30.mpp1.rush--17#
    Reading TR-69 Parameters...
    Getting Hardware ID...67371438
    Getting Stage 1 Version...1.4.0.1
    Getting Stage 2 Version...4.4.0.7
    Getting Application Version...he30.mpp1.rush--17
    Getting Remote Designator...2
    Getting Front Panel Designator...3
    Getting DVB Designator...1
    Getting Smart Card Designator...1
    Getting RF Mod Designator...1
    Getting Video Outputs Designator...128
    Getting Multi SOC Designator...1
    Getting Hard Disk Designator...6
    Getting Secure Micro Designator...0
    Getting Vendor Class Information (VCI)...SAIPP430MC
    ATU is busy
    Source address not found...retrying
    ATU is busy
    Source address not found...retrying
    ATU is busy
    Source address not found...retrying
    Creating file /tmp/tr69params.config...
    DHCP Vendor Id: SAIPP430MC
    IP: 7-segment display detected
    Using /lib/modules/2.6.15/fpanel.ko
    Calling set_date_using_serial to ensure DHCP uses a random transaction ID.
    /usr/local/blinkLinkLED: Blink Link LED until dhcp completes successfully
    Thu Jan  4 11:23:39 UTC 2007
    Jan  4 11:23:39 dhcpcd[210]: Entering dhcpReboot
    Jan  4 11:23:39 dhcpcd[210]: Entering dhcpStart
    dhcpcd: MAC address = 00:1e:6b:6c:ff:27
    Jan  4 11:23:39 dhcpcd[210]: Entering dhcpInit
    ClassID  = "SAIPP430MC"
    ClientID = "61.12.0.32.35.30.34.34.31"
    Jan  4 11:23:39 dhcpcd[210]: broadcasting DHCP_DISCOVER
    Jan  4 11:23:39 dhcpcd[210]: Entering dhcpSendAndRecv
    Jan  4 11:23:39 dhcpcd[210]: Entering parseDhcpMsgRecv
    parseDhcpMsgRecv: 9 options received:
    i=1   len=4   option = 255.0.0.0
    i=3   len=4   option = 10.20.30.1
    i=6   len=4   option = 10.20.30.1
    i=28  len=4   option = 10.255.255.255
    i=51  len=4   option = 43200
    i=53  len=1   option = 2
    i=54  len=4   option = 10.20.30.1
    i=58  len=4   option = 21600
    i=59  len=4   option = 37800
    DhcpMsgRecv->yiaddr  = 10.20.30.140
    DhcpMsgRecv->siaddr  = 10.20.30.1
    DhcpMsgRecv->giaddr  = 0.0.0.0
    DhcpMsgRecv->sname   = ""
    DhcpMsgRecv->file   = ""
    ServerHardwareAddr   = 00.24.E8.AF.EF.D6
    Jan  4 11:23:39 dhcpcd[210]: dhcpIPaddrLeaseTime=43200 in DHCP server response.
    Jan  4 11:23:39 dhcpcd[210]: DHCP_OFFER received from  (10.20.30.1)
    Jan  4 11:23:39 dhcpcd[210]: Entering dhcpRequest
    Jan  4 11:23:39 dhcpcd[210]: broadcasting DHCP_REQUEST for 10.20.30.140
    Jan  4 11:23:39 dhcpcd[210]: Entering dhcpSendAndRecv
    Jan  4 11:23:39 dhcpcd[210]: Entering parseDhcpMsgRecv
    parseDhcpMsgRecv: 9 options received:
    i=1   len=4   option = 255.0.0.0
    i=3   len=4   option = 10.20.30.1
    i=6   len=4   option = 10.20.30.1
    i=28  len=4   option = 10.255.255.255
    i=51  len=4   option = 43200
    i=53  len=1   option = 5
    i=54  len=4   option = 10.20.30.1
    i=58  len=4   option = 21600
    i=59  len=4   option = 37800
    DhcpMsgRecv->yiaddr  = 10.20.30.140
    DhcpMsgRecv->siaddr  = 10.20.30.1
    DhcpMsgRecv->giaddr  = 0.0.0.0
    DhcpMsgRecv->sname   = ""
    DhcpMsgRecv->file   = ""
    ServerHardwareAddr   = 00.24.E8.AF.EF.D6
    Jan  4 11:23:39 dhcpcd[210]: dhcpIPaddrLeaseTime=43200 in DHCP server response.
    Jan  4 11:23:39 dhcpcd[210]: DHCP_ACK received from  (10.20.30.1)
    dhcpcd: your IP address = 10.20.30.140
    Jan  4 11:23:39 dhcpcd[221]: TimeMonitorThread:  Waiting on time to shift to absolute time.
    dhcpcd.exe: interface eth0 has been configured with new IP=10.20.30.140
    Jan  4 11:23:39 dhcpcd[212]: Entering do while state loop...
    Jan  4 11:23:39 dhcpcd[212]: Entering dhcpBound
    Using /lib/modules/2.6.15/fpanel.ko
    Using /lib/modules/2.6.15/fpanel.ko
    add the 224 route
    rm: cannot remove `/tmp/ntp.conf_new': No such file or directory
    Adding polling times to /etc/ntp.conf...
    killall: ntpd: no process killed
    timeServer not found - using ntpd
    starting dropbear
    FlashMonitor v3.1.0.0
    BuildDate: Feb  5 2009
    flashMonitor: No HPNA device present, exiting...
    starting dropbear with password logins disabled (-s).
    hpnaMonitor: No HPNA device present, exiting...
    Timezone Not Found - String from DHCP 
    CURTZ=
    Detected Linux 2.6...
    Initial IP is OK
    MBR is does not show 2 partitions...
    Manage XFS partitions...
    Current overcommit_memory value is 2
    Current overcommit_ratio value is 100
    1+0 records in
    1+0 records out
    increase dropbear priority
    278: old priority 0, new priority -5
    Partition check passed
    /dev/hda:
     setting drive write-caching to 0 (off)
    Found swap partition
    Setting up swapspace version 1, size = 255995904 bytes
    Enabling swap on /dev/hda1
    Found kernel and rootfs partition
    Running fsck.ext3 on /dev/hda3 3
    e2fsck 1.37 (21-Mar-2005)
    fsck.ext3 returned: 0
    Completed fsck.ext3 on /dev/hda3
    Running fsck.xfs on /dev/hda4 4
    Attempting mount to repair log file
    Mount succeeded for /dev/hda4
    Completed fsck.xfs on /dev/hda4
    Restoring overcommit_memory to 2
    Restoring overcommit_ratio to 100
    ##End of S50local##
    CHASSIS_SerialNumber=250441316-3
    BOARD_Version=67371438
    VENDOR_VERSION=SAIPP_2.0.18.9_myr_ipp_HE_vm3_vqe_DVR.1
    VER_HARDWARE=SAIPP430MC
    VER_SOFTWARE=he30.mpp1.rush--17
    BUILD_STAMP="build@buildvm26 on Thu Jan 28 14:05:17 IST 2010"
    ## Start of S99Myrio ##
    Filename				Type		Size	Used	Priority
    /dev/hda1                               partition	249992	0	-1
    /tmp/swapfs/swapfile                    file		131064	0	-2
    Using HDD storage for broker docs
    ln: /var/data/userinterface/userinterface: File exists
    mv: /usr/ceej/Fonts/SiegeCrashReport*: No such file or directory
    Putting reboot.log on HDD
    cp: /usr/local/standalone/*: No such file or directory
    Teletext Debug OFF
    Console debug OFF ... Using logger
    Jan  4 11:24:36 myrio_00_1E_6B_6C_FF_27 syslog.info syslogd started: BusyBox v1.00 (2006.10.31-18:31+0000)
    Jan  4 11:24:36 myrio_00_1E_6B_6C_FF_27 kern.notice kernel: klogd started: BusyBox v1.00 (2006.10.31-18:31+0000)
    Jan  4 11:24:36 myrio_00_1E_6B_6C_FF_27 kern.notice kernel: Linux version 2.6.15 (airman@tiger) (gcc version 3.4.2) #73 PREEMPT Wed Aug 5 13:57:51 EDT 2009
    Jan  4 11:24:36 myrio_00_1E_6B_6C_FF_27 kern.warn kernel: Configured for SMP863x (revision ES6/RevA), detected SMP8634 (revision ES7/RevB).
    Jan  4 11:24:36 myrio_00_1E_6B_6C_FF_27 kern.info kernel: SMP863x/SMP865x Enabled Devices under Linux/XENV 0x48000000 = 0x000202fa
    Jan  4 11:24:36 myrio_00_1E_6B_6C_FF_27 kern.info kernel:  BM/IDE Ethernet IR FIP I2CM I2CS USB SCARD
    Jan  4 11:24:36 myrio_00_1E_6B_6C_FF_27 kern.warn kernel: Valid MEMCFG found at 0x10000fc0.
    Jan  4 11:24:36 myrio_00_1E_6B_6C_FF_27 kern.warn kernel: CPU revision is: 00019068
    Jan  4 11:24:36 myrio_00_1E_6B_6C_FF_27 ker
    INIT: Entering runlevel: 2
    Jan  4 11:24:37 myrio_00_1E_6B_6C_FF_27 kern.info init: Entering runlevel: 2
    sh-3.00# Jan  4 11:24:37 myrio_00_1E_6B_6C_FF_27 kern.warn kernel: em8xxx [/work/svn_src/mrua_SMP8634/mrua_SMP8634_2.8.0.0_SA_rel2L2_AudioMpeg_test_build_facsprod_legacy_dev.mips.nodts/MRUA_src/rua/emhwlib_kernel/kernel_src/em8xxx_proc.c:118] proc_read_resources: dumping blocks of MM #0
    Jan  4 11:24:37 myrio_00_1E_6B_6C_FF_27 kern.warn kernel: em8xxx [/work/svn_src/mrua_SMP8634/mrua_SMP8634_2.8.0.0_SA_rel2L2_AudioMpeg_test_build_facsprod_legacy_dev.mips.nodts/MRUA_src/rua/emhwlib_kernel/kernel_src/em8xxx_proc.c:118] proc_read_resources: dumping blocks of MM #1
    Jan  4 11:24:37 myrio_00_1E_6B_6C_FF_27 kern.warn kernel: em8xxx [/work/svn_src/mrua_SMP8634/mrua_SMP8634_2.8.0.0_SA_rel2L2_AudioMpeg_test_build_facsprod_legacy_dev.mips.nodts/MRUA_src/rua/emhwlib_kernel/kernel_src/em8xxx_proc.c:118] proc_read_resources: dumping blocks of MM #2
    Jan  4 11:24:37 myrio_00_1E_6B_6C_FF_27 kern.warn kernel: em8xxx [/work/svn_src/mrua_SMP8634/mrua_SMP8634_2.8.0.0_SA_rel2L2_AudioMpeg_test_build_facsprod_legacy_dev.mips.nodts/MRUA_src/rua/emhwlib_kernel/kernel_src/em8xxx_proc.c:137] Cannot get allocated blocks
    Jan  4 11:24:37 myrio_00_1E_6B_6C_FF_27 kern.warn kernel: em8xxx [/work/svn_src/mrua_SMP8634/mrua_SMP8634_2.8.0.0_SA_rel2L2_AudioMpeg_test_build_facsprod_legacy_dev.mips.nodts/MRUA_src/rua/emhwlib_kernel/kernel_src/em8xxx_proc.c:118] proc_read_resources: dumping blocks of MM #3
    Jan  4 11:24:37 myrio_00_1E_6B_6C_FF_27 kern.warn kernel: em8xxx [/work/svn_src/mrua_SMP8634/mrua_SMP8634_2.8.0.0_SA_rel2L2_AudioMpeg_test_build_facsprod_legacy_dev.mips.nodts/MRUA_src/rua/emhwlib_kernel/kernel_src/em8xxx_proc.c:137] Cannot get allocated blocks
    Jan  4 11:24:37 myrio_00_1E_6B_6C_FF_27 kern.warn kernel: em8xxx [/work/svn_src/mrua_SMP8634/mrua_SMP8634_2.8.0.0_SA_rel2L2_AudioMpeg_test_build_facsprod_legacy_dev.mips.nodts/MRUA_src/rua/emhwlib_kernel/kernel_src/em8xxx_proc.c:118] proc_read_resources: dumping blocks of MM #4
    Jan  4 11:24:37 myrio_00_1E_6B_6C_FF_27 kern.warn kernel: em8xxx [/work/svn_src/mrua_SMP8634/mrua_SMP8634_2.8.0.0_SA_rel2L2_AudioMpeg_test_build_facsprod_legacy_dev.mips.nodts/MRUA_src/rua/emhwlib_kernel/kernel_src/em8xxx_proc.c:137] Cannot get allocated blocks
    Jan  4 11:24:37 myrio_00_1E_6B_6C_FF_27 kern.warn kernel: em8xxx [/work/svn_src/mrua_SMP8634/mrua_SMP8634_2.8.0.0_SA_rel2L2_AudioMpeg_test_build_facsprod_legacy_dev.mips.nodts/MRUA_src/rua/emhwlib_kernel/kernel_src/em8xxx_proc.c:118] proc_read_resources: dumping blocks of MM #5
    Jan  4 11:24:37 myrio_00_1E_6B_6C_FF_27 kern.warn kernel: em8xxx [/work/svn_src/mrua_SMP8634/mrua_SMP8634_2.8.0.0_SA_rel2L2_AudioMpeg_test_build_facsprod_legacy_dev.mips.nodts/MRUA_src/rua/emhwlib_kernel/kernel_src/em8xxx_proc.c:137] Cannot get allocated blocks
    Jan  4 11:24:37 myrio_00_1E_6B_6C_FF_27 kern.warn kernel: em8xxx [/work/svn_src/mrua_SMP8634/mrua_SMP8634_2.8.0.0_SA_rel2L2_AudioMpeg_test_build_facsprod_legacy_dev.mips.nodts/MRUA_src/rua/emhwlib_kernel/kernel_src/em8xxx_proc.c:118] proc_read_resources: dumping blocks of MM #0
    Jan  4 11:24:37 myrio_00_1E_6B_6C_FF_27 kern.warn kernel: em8xxx [/work/svn_src/mrua_SMP8634/mrua_SMP8634_2.8.0.0_SA_rel2L2_AudioMpeg_test_build_facsprod_legacy_dev.mips.nodts/MRUA_src/rua/emhwlib_kernel/kernel_src/em8xxx_proc.c:118] proc_read_resources: dumping blocks of MM #1
    Jan  4 11:24:37 myrio_00_1E_6B_6C_FF_27 kern.warn kernel: em8xxx [/work/svn_src/mrua_SMP8634/mrua_SMP8634_2.8.0.0_SA_rel2L2_AudioMpeg_test_build_facsprod_legacy_dev.mips.nodts/MRUA_src/rua/emhwlib_kernel/kernel_src/em8xxx_proc.c:118] proc_read_resources: dumping blocks of MM #2
    Jan  4 11:24:37 myrio_00_1E_6B_6C_FF_27 kern.warn kernel: em8xxx [/work/svn_src/mrua_SMP8634/mrua_SMP8634_2.8.0.0_SA_rel2L2_AudioMpeg_test_build_facsprod_legacy_dev.mips.nodts/MRUA_src/rua/emhwlib_kernel/kernel_src/em8xxx_proc.c:137] Cannot get allocated blocks
    Jan  4 11:24:37 myrio_00_1E_6B_6C_FF_27 kern.warn kernel: em8xxx [/work/svn_src/mrua_SMP8634/mrua_SMP8634_2.8.0.0_SA_rel2L2_AudioMpeg_test_build_facsprod_legacy_dev.mips.nodts/MRUA_src/rua/emhwlib_kernel/kernel_src/em8xxx_proc.c:118] proc_read_resources: dumping blocks of MM #3
    Jan  4 11:24:37 myrio_00_1E_6B_6C_FF_27 kern.warn kernel: em8xxx [/work/svn_src/mrua_SMP8634Jan  4 11:24:37


# Jtag


The jtag pinout is:

[[=image belgacom-tv-scientific-atlanta-IPP330HD-jtag-port-pinout.jpg]]

# Links 


* <http://www.t-hack.com/wiki/index.php/Main_Page>  
* <http://www.hacklabproject.org/drupal/content/openwrt-su-pirelli-stb>  
* <http://kf-repos.de/viewgit/>  
* <http://hy100wiki.algasystems.net/wiki/doku.php/azbox_firmware>  
* <https://supportforums.cisco.com/thread/2049948>  
* <http://pastebin.com/UetL13Ba>  
* <http://www.networkedmediatank.com/download/firmware/nmt/gpl/gpl.htm>  
* <http://213.202.123.24/forum/topic/digitalna-televizija/kako-iskoristiti-stari-maxtv-stb/69014.aspx?jumpto=1285045&sort=asc&view=flat&page=16>  