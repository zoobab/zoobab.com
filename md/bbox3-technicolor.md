

# About


Belgacom Box 3 (Bbox3) by Technicolor.

This seems to be the most deploied one, there is also the [[[bbox3-sagemcom | Bbox3 by Sagemcom]]], but this later model is not as widespread as the one by Technicolor.

# Ideas


The flash on the board is an SPI one with 8 pins, it should be fairly easy to dump the content of it, for example with a [bus pirate and flashrom](http://ho.ax/posts/2012/06/unbricking-a-macbook/).

# Toolchain openwrt support


There are some [new patches](https://github.com/openwrt-mirror/openwrt/commit/cb5996ddeb22a2de570222e85af223cc3b7870e2) for the ARC arch in openwrt trunk.

Now, LEDE has images for the ARC770 arch here, which should be able to boot on the BBOX3: <http://downloads.lede-project.org/releases/17.01.2/targets/arc770/generic/>  

# Serial port


There is a serial port on the side of the SoC, where you have to bridge 2 sides with a bit of solder in order to make the contact.

See the picture here:

[[=image bbox3-technicolor-serial-port-1.jpg size="medium"]]

Here I took the ground with the green wire:

[[=image bbox3-technicolor-serial-port-2.jpg size="medium"]]

Here if you zoom, you should notice that I had to bridge 2 pins on the PCB:

[[=image bbox3-technicolor-serial-port-3.jpg size="medium"]]

Here is the full serial log:


    Quantenna Mini U-Boot
    Version: 1.4.6 Built: Oct 08 2012 at 18:12:00
    Boot reached stage 64
    Boot reached stage 65
    QTN-EMAC
    Boot reached stage 80
    1G-FD
    Using QTN-EMAC device
    L2_TFTP start
    Filename 'qtn-uboot'.
    Load address: 0x88000000
    Loading: *
    T T T T 
    Retry count exceeded; starting again
    1G-FD
    Using QTN-EMAC device
    L2_TFTP start
    Filename 'qtn-uboot'.
    Load address: 0x88000000
    Loading: *
    T T T T 
    Retry count exceeded; starting again
    1G-FD
    Using QTN-EMAC device
    L2_TFTP start
    Filename 'qtn-uboot'.
    Load address: 0x88000000
    Loading: *
    T T T T 
    Retry count exceeded; starting again
    reset command
    Quantenna Mini U-Boot
    Version: 1.4.6 Built: Oct 08 2012 at 18:12:00
    Boot reached stage 64
    Boot reached stage 65
    QTN-EMAC
    Boot reached stage 80
    1G-FD
    Using QTN-EMAC device
    L2_TFTP start
    Filename 'qtn-uboot'.
    Load address: 0x88000000
    Loading: *
    T T T T 
    Retry count exceeded; starting again
    1G-FD
    Using QTN-EMAC device
    L2_TFTP start
    Filename 'qtn-uboot'.
    Load address: 0x88000000
    Loading: *
    T T T T 
    Retry count exceeded; starting again
    1G-FD
    Using QTN-EMAC device
    L2_TFTP start
    Filename 'qtn-uboot'.
    Load address: 0x88000000
    Loading: *
    T T T T 
    Retry count exceeded; starting again
    reset command
    Quantenna Mini U-Boot
    Version: 1.4.6 Built: Oct 08 2012 at 18:12:00
    Boot reached stage 64
    Boot reached stage 65
    QTN-EMAC
    Boot reached stage 80
    1G-FD
    Using QTN-EMAC device
    L2_TFTP start
    Filename 'qtn-uboot'.
    Load address: 0x88000000
    Loading: *
    T T T T 
    Retry count exceeded; starting again
    1G-FD
    Using QTN-EMAC device
    L2_TFTP start
    Filename 'qtn-uboot'.
    Load address: 0x88000000
    Loading: *
    T T T T 
    Retry count exceeded; starting again
    1G-FD
    Using QTN-EMAC device
    L2_TFTP start
    Filename 'qtn-uboot'.
    Load address: 0x88000000
    Loading: *
    T T T T 
    Retry count exceeded; starting again
    reset command
    Quantenna Mini U-Boot
    Version: 1.4.6 Built: Oct 08 2012 at 18:12:00
    Boot reached stage 64
    Boot reached stage 65
    QTN-EMAC
    Boot reached stage 80
    1G-FD
    Using QTN-EMAC device
    L2_TFTP start
    Filename 'qtn-uboot'.
    Load address: 0x88000000
    Loading: *
    T #########
    done
    Bytes transferred = 127992 (1f3f8 hex)
    Boot reached stage 81
    Boot reached stage 84
    Info: data uncached: addr=0xc0000000 size=1024MB
    Info: text at 0x88000000, stack at 0x8803e7fc(8192), heap at 0x88030000(51200), uboot size 155352
    Info: i-cache is enabled
    Info: d-cache is enabled
    Info: CPU freq is 400000000, dev freq is 125000000
    Info: Quantenna U-Boot version:1.4.10
    Info: TCH bootloader version:10.5.2.O
    Info: build date 'Mar 05 2014', time '12:46:33'
    spi clock: val=0x3 ctl=0x80298002
    spi clock: val=0x0 ctl=0x80280002
    SPI flash info:
    	name             : mx25l512e
    	jedec_id         : 0xc22010
    	sector size      : 4096
    	number of sector : 16
    	frequency        : 104000000
    	flags            : 0x2
    	lock             : 
    Boot reached stage 13
    Boot reached stage 12
    env size = 0x3ffc
    Valid CRC found in flash restoring env...
    Boot reached stage 11
    board config:etron16-160, emac1 b2b-rgmii 1000M, pa2
    BDA at 0x80002000
    In:    serial
    Out:   serial
    Err:   serial
    Boot reached stage 64
    Boot reached stage 65
    QTN-EMAC
    Hit any key to stop autoboot:  0 
    post_mask is null
    Boot reached stage 80
    1G-FD
    Using QTN-EMAC device
    L2_TFTP start
    Filename 'qtn-linux.lzma'.
    Load address: 0x82000000
    Loading: *
    #################################################################
    	 #################################################################
    	 #################################################################
    	 ##########################################################
    done
    Bytes transferred = 3692118 (385656 hex)
    Boot reached stage 81
    Boot reached stage 84
    Boot reached stage 1
    ## Booting kernel from Legacy Image at 82000000 ...
    Boot reached stage 2
    Boot reached stage 3
       Image Name:   ruby-linux
       Image Type:   arc Linux Kernel Image (lzma compressed)
       Data Size:    3683926 Bytes =  3.5 MB
       Load Address: 80302000
       Entry Point:  80302000
       Verifying Checksum ... OK
    Boot reached stage 4
    Boot reached stage 5
    Boot reached stage 6
    Boot reached stage 14
       Uncompressing Kernel Image ... OK
    Boot reached stage 7
    Boot reached stage 8
    Command line TAG setup
    Params->u.cmdline.cmdline earlyprintk=1 console=ttyS0,115200n8 mtdparts=spi_flash:20k(uboot),16k(uboot_env),-(data) hw_config_id=8001
    p earlyprintk=1 console=ttyS0,115200n8 mtdparts=spi_flash:20k(uboot),16k(uboot_env),-(data) hw_config_id=8001
    ## Transferring control to Linux (at address 80302000) ATAG parameters 880340a0 - 8803412c...
    [    0.000000] Linux version 2.6.30 (buildmgm@edgmwbuild226.edegem.eu.thmulti.com) (gcc version 4.2.1 (ARC_2.3)) #2 Wed Mar 5 12:57:24 CET 2014
    [    0.000000] Parsing ATAG parameters from bootloader
    [    0.000000] ATAG_CORE: successful parsing
    [    0.000000] ATAG_CMDLINE: command line = earlyprintk=1 console=ttyS0,115200n8 mtdparts=spi_flash:20k(uboot),16k(uboot_env),-(data) hw_config_id=8001
    [    0.000000] Board id: 8001
    [    0.000000] ATAG_HW_CONFIG_ID: hw_config_id = 8001
    [    0.000000] 
    [    0.000000]  Processor Family: ARC 700, Core ID: 0
    [    0.000000] CPU speed :	400.00 Mhz
    [    0.000000] Timers: 	TIMER1 TIMER0 
    [    0.000000] Interrupt Vect Base: 	0x88010800 
    [    0.000000] Peripheral Base: 	0x0 
    [    0.000000] Data UNCACHED Base (I/O): start 0xc0 Sz, 1024 MB 
    [    0.000000] ARC700 MMU Ver [2]
    [    0.000000]    uDTLB 8 entr, uITLB 4 entr, JTLB 128 entry/way, 2 ways
    [    0.000000] TLB Refill "will NOT" Flush uTLBs
    [    0.000000] Detected I-cache : 
    [    0.000000]   Type=2 way set-assoc, Line length=32, Size=16K (enabled)
    [    0.000000] Detected D-cache : 
    [    0.000000]   Type=4 way set-assoc, Line length=32, Size=16K (enabled)
    [    0.000000] Extensions:
    [    0.000000] Multiplier: 32x32 with ANY Result Reg   MAC Multiplier: Dual 16 x 16 and 32 x 16
    [    0.000000] CRC  Instrn: NA,   SWAP Instrn: Present   NORM Instrn: Present
    [    0.000000] Min-Max Instrn: Present,   Barrel Shift Rotate Instrn: Present
    [    0.000000] Ext Arith Instrn: Present
    [    0.000000] On node 0 totalpages: 8192
    [    0.000000] free_area_init_node: node 0, pgdat 80d581c0, node_mem_map 81000000
    [    0.000000]   Normal zone: 36 pages used for memmap
    [    0.000000]   Normal zone: 0 pages reserved
    [    0.000000]   Normal zone: 8156 pages, LIFO batch:0
    [    0.000000] Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 8156
    [    0.000000] Kernel command line: earlyprintk=1 console=ttyS0,115200n8 mtdparts=spi_flash:20k(uboot),16k(uboot_env),-(data) hw_config_id=8001
    [    0.000000] console [ruby_early0] enabled
    [    0.000000] RCU-based detection of stalled CPUs is enabled.
    [    0.000000] PID hash table entries: 256 (order: 8, 1024 bytes)
    [    0.000000] clockevent mode switch to [1]
    [    0.000000] clockevent mode switch to [2]
    [    0.000000] Dentry cache hash table entries: 8192 (order: 2, 32768 bytes)
    [    0.005000] Inode-cache hash table entries: 4096 (order: 1, 16384 bytes)
    [    0.020000] Memory: 51600KB available (2051K code,560K data, 8080K init)
    [    0.025000] Calibrating delay loop... 265.42 BogoMIPS (lpj=663552)
    [    0.145000] Mount-cache hash table entries: 1024
    [    0.155000] Starting ksoftirqd, stack (thread_info) at 88002000 cpu 0
    [    0.160000] net_namespace: 932 bytes
    [    0.165000] NET: Registered protocol family 16
    [    0.170000] Ruby heap in SRAM from 88010000 to 8801ffe0
    [    0.175000] Quantenna I2C device register
    [    0.185000] bio: create slab <bio-0> at 0
    [    0.195000] NET: Registered protocol family 2
    [    0.200000] IP route cache hash table entries: 2048 (order: 0, 8192 bytes)
    [    0.210000] TCP established hash table entries: 2048 (order: 1, 16384 bytes)
    [    0.215000] TCP bind hash table entries: 2048 (order: 0, 8192 bytes)
    [    0.220000] TCP: Hash tables configured (established 2048 bind 2048)
    [    0.225000] TCP reno registered
    [    0.230000] NET: Registered protocol family 1
    [    0.760000] JFFS2 version 2.2. (NAND) 
     2001-2006 Red Hat, Inc.
    [    0.765000] msgmni has been set to 100
    [    0.770000] io scheduler noop registered (default)
    [    0.775000] io scheduler anticipatory registered
    [    1.325000] Serial: 8250/16550 driver, 2 ports, IRQ sharing enabled
    [    1.335000] serial8250.0: ttyS0 at MMIO 0xf0000000 (irq = 48) is a 16550A
    [    1.345000] console handover: boot [ruby_early0] -> real [ttyS0]
    [    1.350000] brd: module loaded
    [    1.360000] loop: module loaded
    [    1.365000] 3 cmdlinepart partitions found on MTD device spi_flash
    [    1.370000] Creating 3 MTD partitions on "spi_flash":
    [    1.375000] 0x000000000000-0x000000005000 : "uboot"
    [    1.385000] 0x000000005000-0x000000009000 : "uboot_env"
    [    1.390000] 0x000000009000-0x000000010000 : "data"
    [    1.400000] spi_flash: SPI flash driver initialized successfully!
    [    1.405000] ruby_health loading
    [    1.410000] emac_eth version 1.0 Quantenna Communications, Inc.
    [    1.415000] emac_eth version 1.0 Quantenna Communications, Inc.
    [    1.420000] Random stuff 87
    [    1.555000] eth1_emac1: Arasan Ethernet found at 0xe8000000, irq 20
    [    1.560000] u32 classifier
    [    1.565000]     input device check on 
    [    1.570000]     Actions configured 
    [    1.570000] Netfilter messages via NETLINK v0.30.
    [    1.575000] nf_conntrack version 0.5.0 (988 buckets, 3952 max)
    [    1.585000] ip_tables: (C) 2000-2006 Netfilter Core Team
    [    1.590000] TCP cubic registered
    [    1.595000] NET: Registered protocol family 10
    [    1.600000] NET: Registered protocol family 17
    [    1.605000] 802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
    [    1.610000] All bugs added by David S. Miller <davem@redhat.com>
    [    1.620000] Freeing unused kernel memory: 8080k freed [80302000] TO [80ae6000]
    init started: BusyBox v1.10.3 (2014-03-05 12:47:20 CET)
    starting pid 32, tty '': '/etc/init.d/rcS'
    Initializing random number generator... done.
    [    2.525000] eth1_emac1: force link (1000/Full)
    Downloading qtn_prod.env (1).
    Failed to download qtn_prod.env ( tftp error : Access Violation )
    Downloading qtn_prod.env (2).
    Downloading qtn_custo.env (1).
    Downloading qtn_custo.sh (1).
    Updating eth_macaddr
    Updating wifi_mac_addrs
    Updating wireless_conf.txt
    Updating hostapd.conf
    Updating tch_upgrade.conf
    Updating tch_ntp.conf
    Updating tch_monitor.conf
    Updating admin.conf
    Updating tch_cwmp_conf
    Starting network...
    emac0 is unused, emac1 is eth1_0
    /sbin/ifup -a
    [    5.890000] eth1_0: force link (1000/Full)
    ifconfig: SIOCGIFFLAGS: No such device
    ifconfig: SIOCSIFADDR: No such device
    [    6.285000] eth1_0: force link (1000/Full)
    [    6.450000] device eth1_0 entered promiscuous mode
    [    6.480000] br0: port 1(eth1_0) entering forwarding state
    Starting wireless...
    Loading modules
    [    7.685000] qtn_debug: module license 'Proprietary' taints kernel.
    [    7.690000] Disabling lock debugging due to kernel taint
    modprobe: module i2cbus not found
    modprobe: failed to load module i2cbus
    modprobe: module qtsens not found
    modprobe: failed to load module qtsens
    [    7.950000] wlan using SRAM (offset:0x880100d8, size:0x688)
    [    8.165000] wlan: 0.8.4.2 (0.9.3.3)
    [    8.285000] qvspmod using SRAM (offset:0x88010768, size:0x1eb4)
    [    8.385000] qdrv using SRAM (offset:0x88012628, size:0xb2c4)
    Production mode
    Waiting for Wireless Events from interfaces...
    [    9.450000]  qdrv: firmware: requesting rdsp_driver.0.bin
    [    9.550000]  qdrv: firmware: requesting qtn_driver.qtn_ruby.0.bin
    [   10.480000] muc_print_init_shared: buf=550e1560
    [   10.485000] MuC: build date=Thu Nov 14 22:31:48 PST 2013
    [   10.490000] MuC: slow heap begin=0x000c5500 end=0x00145500
    [   10.495000] MuC: fast heap begin=0x80030800 end=0x80038800
    [   10.500000] MuC: stack start=0x8003e7a0 sp=0x8003ff04
    [   10.505000] MuC: calstate is 3 (prod), dcache on
    [   10.510000] MuC: scancnt=0
    [   10.515000] MuC: slow eth=0
    [   10.530000] MuC: POST RF loopback test is disabled
    [   10.650000] MuC: fd start=0xe5040300 count=48 size=100 end=0xe50415c0
    [   10.655000] MuC: TX QoS schedule=0
    [   10.655000] MuC: dynamic one-bit autocorrelation enabled
    [   10.660000] MuC: enable IRQs
    [   10.690000] QDRV: power adjust scancnt=0
    [   10.695000] QDRV: using default temperature profile
    [   10.700000] QDRV: could not read temperature sensor
    [   10.705000] MuC boot succeeded 0.235 seconds
    [   10.920000] VAP create succeeded 0.030 seconds
    Set channel 0
    [   12.065000] device wifi0 entered promiscuous mode
    [   12.240000] Enabling SSDP flooding
    SCS BRCM rxif mac a6:b1:e9:b1:ed:ef
    SCS using interface wifi0
    [   14.315000] WPS: push button is not configured
    [   14.325000] br0: port 2(wifi0) entering forwarding state
    Enabling beamforming
    [   14.940000] qdrv_sch_red: allocated 1536 511
    [   14.945000] qdrv_sch_red: attached to wifi0
    [   14.975000] qdrv_sch_red: allocated 512 127
    [   14.975000] qdrv_sch_red: attached to eth1_0
    [   15.165000] Enabling SCS
    SCS enabled
    [   15.685000] [2]Comparing register set Global control
    [   15.710000] [6]Comparing register set BB Global regs
    VSP enabled: 0
    [   16.435000] qdrv_radar_is_rdetection_required: ERROR - channel not yet set
    [   16.440000] MuC: ioctl_power_save, level: 0 -> 1
    /scripts/cmdloop starting call_qcsapi, at 00:00:16 up 0 min, load average: 0.59, 0.13, 0.04
    /scripts/cmdloop starting /sbin/tch_vb_discover, at 00:00:17 up 0 min, load average: 0.59, 0.13, 0.04
    killall: udhcpc: no process killed
    [   17.475000] br0: no IPv6 routers present
    udhcpc (v1.19.4) started
    Sending discover...
    tch_monitor.sh: no url defined
    BELGACOM CUSTO
    [   18.065000] <0,0,2,2,2,3,3,3
    [   18.065000] >
    starting pid 644, tty '/dev/ttyS0': '/bin/login'
    TG233 login: [   18.520000] RADAR: CAC started for channel 132 (5660 MHz)
    Sending discover...
    Sending discover...
    [   24.320000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   24.345000] RADAR: CAC started for channel 132 (5660 MHz)
    No lease, forking to background
    [   28.615000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   28.620000] RADAR: CAC started for channel 132 (5660 MHz)
    [   29.370000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   29.375000] RADAR: CAC started for channel 132 (5660 MHz)
    [   29.385000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   29.395000] RADAR: CAC started for channel 132 (5660 MHz)
    [   29.405000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   29.415000] RADAR: CAC started for channel 132 (5660 MHz)
    [   29.425000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   29.435000] RADAR: CAC started for channel 132 (5660 MHz)
    [   29.445000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   29.455000] RADAR: CAC started for channel 132 (5660 MHz)
    [   29.465000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   29.475000] RADAR: CAC started for channel 132 (5660 MHz)
    [   29.495000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   29.500000] RADAR: CAC started for channel 132 (5660 MHz)
    [   29.535000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   29.545000] RADAR: CAC started for channel 132 (5660 MHz)
    [   30.275000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   30.280000] RADAR: CAC started for channel 132 (5660 MHz)
    [   30.290000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   30.300000] RADAR: CAC started for channel 132 (5660 MHz)
    [   30.310000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   30.320000] RADAR: CAC started for channel 132 (5660 MHz)
    [   30.330000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   30.340000] RADAR: CAC started for channel 132 (5660 MHz)
    [   30.350000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   30.360000] RADAR: CAC started for channel 132 (5660 MHz)
    [   30.370000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   30.375000] RADAR: CAC started for channel 132 (5660 MHz)
    [   30.390000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   30.395000] RADAR: CAC started for channel 132 (5660 MHz)
    [   30.425000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   30.435000] RADAR: CAC started for channel 132 (5660 MHz)
    [   31.190000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   31.195000] RADAR: CAC started for channel 132 (5660 MHz)
    [   31.205000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   31.215000] RADAR: CAC started for channel 132 (5660 MHz)
    [   31.225000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   31.235000] RADAR: CAC started for channel 132 (5660 MHz)
    [   31.245000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   31.255000] RADAR: CAC started for channel 132 (5660 MHz)
    [   31.265000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   31.275000] RADAR: CAC started for channel 132 (5660 MHz)
    [   31.285000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   31.290000] RADAR: CAC started for channel 132 (5660 MHz)
    [   31.310000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   31.315000] RADAR: CAC started for channel 132 (5660 MHz)
    [   31.345000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   31.355000] RADAR: CAC started for channel 132 (5660 MHz)
    [   32.545000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   32.550000] RADAR: CAC started for channel 132 (5660 MHz)
    [   32.555000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   32.560000] RADAR: CAC started for channel 132 (5660 MHz)
    [   32.570000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   32.580000] RADAR: CAC started for channel 132 (5660 MHz)
    [   32.590000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   32.600000] RADAR: CAC started for channel 132 (5660 MHz)
    [   32.610000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   32.620000] RADAR: CAC started for channel 132 (5660 MHz)
    [   32.630000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   32.640000] RADAR: CAC started for channel 132 (5660 MHz)
    [   32.660000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   32.665000] RADAR: CAC started for channel 132 (5660 MHz)
    [   32.695000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   32.705000] RADAR: CAC started for channel 132 (5660 MHz)
    [   35.855000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   35.865000] RADAR: CAC started for channel 132 (5660 MHz)
    [   35.870000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   35.875000] RADAR: CAC started for channel 132 (5660 MHz)
    [   35.885000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   35.895000] RADAR: CAC started for channel 132 (5660 MHz)
    [   35.905000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   35.915000] RADAR: CAC started for channel 132 (5660 MHz)
    [   35.925000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   35.935000] RADAR: CAC started for channel 132 (5660 MHz)
    [   35.945000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   35.955000] RADAR: CAC started for channel 132 (5660 MHz)
    [   35.975000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   35.980000] RADAR: CAC started for channel 132 (5660 MHz)
    [   36.015000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   36.025000] RADAR: CAC started for channel 132 (5660 MHz)
    [   36.935000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   36.945000] RADAR: CAC started for channel 132 (5660 MHz)
    [   36.955000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   36.965000] RADAR: CAC started for channel 132 (5660 MHz)
    [   36.975000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   36.985000] RADAR: CAC started for channel 132 (5660 MHz)
    [   36.995000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   37.005000] RADAR: CAC started for channel 132 (5660 MHz)
    [   37.015000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   37.025000] RADAR: CAC started for channel 132 (5660 MHz)
    [   37.035000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   37.040000] RADAR: CAC started for channel 132 (5660 MHz)
    [   37.060000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   37.065000] RADAR: CAC started for channel 132 (5660 MHz)
    [   37.100000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   37.110000] RADAR: CAC started for channel 132 (5660 MHz)
    [   38.020000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   38.030000] RADAR: CAC started for channel 132 (5660 MHz)
    [   38.040000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   38.045000] RADAR: CAC started for channel 132 (5660 MHz)
    [   38.050000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   38.055000] RADAR: CAC started for channel 132 (5660 MHz)
    [   38.065000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   38.075000] RADAR: CAC started for channel 132 (5660 MHz)
    [   38.085000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   38.095000] RADAR: CAC started for channel 132 (5660 MHz)
    [   38.105000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   38.115000] RADAR: CAC started for channel 132 (5660 MHz)
    [   38.135000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   38.140000] RADAR: CAC started for channel 132 (5660 MHz)
    [   38.175000] RADAR: CAC stopped for channel 132 (5660 MHz)
    [   38.185000] RADAR: CAC started for channel 132 (5660 MHz)
    TG233 login: [  108.185000] RADAR: CAC completed for channel 132 (5660 MHz)
    [  130.885000] MuC: ioctl_power_save, level: 1 -> 5
    TG233 login: user
    Password: 
    Login incorrect
    TG233 login: user
    Password: 
    Login incorrect
    TG233 login: user
    Password: 
    Login incorrect
    starting pid 916, tty '/dev/ttyS0': '/bin/login'
    TG233 login: user
    Password: 
    Login incorrect
    TG233 login: user^H^H^H^H^H
    Password: 
    Login incorrect
    TG233 login: root
    Password: 
    Login incorrect
    starting pid 922, tty '/dev/ttyS0': '/bin/login'
    TG233 login: admin
    Password: 
    Login incorrect
    TG233 login: admin
    Password: 
    Login incorrect
    TG233 login: admin
    Password: 
    Login incorrect
    starting pid 928, tty '/dev/ttyS0': '/bin/login'
    TG233 login: adsm^H^H^H^H
    Password: 
    adminLogin incorrect
    TG233 login: admin
    Password: 
    Login incorrect
    TG233 login: Administray^Htor
    Password: 
    Login incorrect
    starting pid 944, tty '/dev/ttyS0': '/bin/login'
    TG233 login: Administrator
    Password: 
    Login incorrect
    TG233 login: Administrator
    Password: 
    Login incorrect
    TG233 login: Administrator
    Password: 
    Login incorrect
    starting pid 970, tty '/dev/ttyS0': '/bin/login'
    TG233 login: FE8101EEEC
    Password: 
    Login incorrect
    TG233 login: Administrator
    Password: 
    Login incorrect
    TG233 login: admin
    Password: 
    Login incorrect
    starting pid 981, tty '/dev/ttyS0': '/bin/login'
    TG233 login: admin
    Password: 
    Login incorrect
    TG233 login: 
    starting pid 982, tty '/dev/ttyS0': '/bin/login'
    TG233 login:


# Links


* <http://forums.modem-help.co.uk/viewtopic.php?p=23197>  
* <http://kernelnewbies.org/Linux_3.9#head-eaf1a08db8ff1ee7210c432ae3e0c84a5b125d62>  
* <https://github.com/vineetgarc/publish/blob/master/ELCE-2012-ARC-Linux.pdf?raw=true>  
* <https://wikidevi.com/wiki/Technicolor_TG233>  