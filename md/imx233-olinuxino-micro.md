[[f>toc]]

# About


[<https://www.olimex.com/dev/imx233-olinuxino-micro.html>   Olimex] is selling a cheap linux board based on the Freescale IMX233 SoC.

[[=image iMX233-OLinuXino-Micro-1.jpg size="large"]]

# Specifications


* iMX233 454Mhz ARM9 processor
* 64MB RAM
* SD-card reader
* TV PAL/NTSC video output
* one USB High-Speed host port
* 60 GPIO pins

# Notes


I had to pay via Paypal because their webpage form was a bit broken, since it was requiring frames. I went on IRC, and people recommend me to order via Paypal. It would be better if Olimex invests into a trusted payment broker, which is not the case right now. For another order of some Atmega43u4 boards, Olimex even asked me to send my credit card number via email.

# Serial messages


On the serial console, I got the following error messages:


    0x8020a01d
    0x8020a01d
    0x8020a01d
    0x8020a01d
    0x8020a01d
    0x8020a01d
    0x80502008
    0x8020a01d
    0x80502008
    0x8020a01d
    0x80502008
    0x8020a01d
    0x80502008
    0x8020a01d
    0x80502008
    0x8020a01d


According to the [Error codes document](http://forums.freescale.com/freescale/attachments/freescale/IMXCOMM/165/1/IMX23_ROM_Error_Codes.pdf) for the IMX233:


    0x8020a01d: ERROR_DDI_SD_DRIVER_GROUP
    0x80502008: ERROR_ROM_USB_DRIVER_GROUP


It seems the bootloader cannot boot over the SD card nor the USB drive. Maybe the partition table was wrongly made.

Without an SD card it says:


    0x80502008
              0x8020a01d
    0x8020a014
    0x8020a014
    0x8020a014
    0x80502008
              0x8020a014
    0x80502008
              0x8020a014
    0x80502008
              0x8020a014


# Serial output



    HTLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLFC
    PowerPrep start initialize power...
    Battery Voltage = 0.65V
    No battery or bad battery					detected!!!.Disabling battery					voltage measurements./r/nLLCMay 11 201215:26:EMI_CTRL 0x1C08404init_ddr_mt46v32m10Frac 0x92926192
    start change cpu fr
    LLLLLLLFCLJUncompressing Linux... done, booting the kernel.
    Linux version 2.6.35.3_OLinuXinoR4 (hehopmajieh@hehopmajieh-office) (gcc version 4.7.1 20120421 (prerelease) (GCC) ) #11 PREEMPT Mon May 21 10:27:52 EEST 2012
    CPU: ARM926EJ-S [41069265] revision 5 (ARMv5TEJ), cr=00053177
    CPU: VIVT data cache, VIVT instruction cache
    Machine: iMX233-OLinuXino low cost board
    Memory policy: ECC disabled, Data cache writeback
    Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 16256
    Kernel command line: noinitrd console=ttyAM0,115200 root=/dev/mmcblk0p2 rw rootwait ssp1=mmc
    PID hash table entries: 256 (order: -2, 1024 bytes)
    Dentry cache hash table entries: 8192 (order: 3, 32768 bytes)
    Inode-cache hash table entries: 4096 (order: 2, 16384 bytes)
    Memory: 64MB = 64MB total
    Memory: 57208k/57208k available, 8328k reserved, 0K highmem
    Virtual kernel memory layout:
        vector  : 0xffff0000 - 0xffff1000   (   4 kB)
        fixmap  : 0xfff00000 - 0xfffe0000   ( 896 kB)
        DMA     : 0xfde00000 - 0xffe00000   (  32 MB)
        vmalloc : 0xc4800000 - 0xf0000000   ( 696 MB)
        lowmem  : 0xc0000000 - 0xc4000000   (  64 MB)
        modules : 0xbf000000 - 0xc0000000   (  16 MB)
          .init : 0xc0008000 - 0xc0026000   ( 120 kB)
          .text : 0xc0026000 - 0xc033d000   (3164 kB)
          .data : 0xc0356000 - 0xc0381a00   ( 175 kB)
    Hierarchical RCU implementation.
    	RCU-based detection of stalled CPUs is disabled.
    	Verbose stalled-CPUs detection is disabled.
    NR_IRQS:224
    Console: colour dummy device 80x30
    console [ttyAM0] enabled
    Calibrating delay loop... 226.91 BogoMIPS (lpj=1134592)
    pid_max: default: 32768 minimum: 301
    Security Framework initialized
    Mount-cache hash table entries: 512
    CPU: Testing write buffer coherency: ok
    regulator: core version 0.5
    NET: Registered protocol family 16
    regulator: vddd: 800 <--> 1575 mV at 1550 mV fast normal 
    regulator: vdddbo: 800 <--> 1575 mV fast normal 
    regulator: vdda: 1500 <--> 2275 mV at 1750 mV fast normal 
    regulator: vddio: 2800 <--> 3575 mV at 3300 mV fast normal 
    regulator: overall_current: fast normal 
    regulator: mxs-duart-1: fast normal 
    regulator: mxs-bl-1: fast normal 
    regulator: mxs-i2c-1: fast normal 
    regulator: mmc_ssp-1: fast normal 
    regulator: mmc_ssp-2: fast normal 
    regulator: charger-1: fast normal 
    regulator: power-test-1: fast normal 
    regulator: cpufreq-1: fast normal 
    i.MX IRAM pool: 28 KB@0xc4808000
    bio: create slab <bio-0> at 0
    SCSI subsystem initialized
    usbcore: registered new interface driver usbfs
    usbcore: registered new interface driver hub
    usbcore: registered new device driver usb
    Advanced Linux Sound Architecture Driver Version 1.0.23.
    Switching to clocksource mxs clock source
    NET: Registered protocol family 2
    IP route cache hash table entries: 1024 (order: 0, 4096 bytes)
    TCP established hash table entries: 2048 (order: 2, 16384 bytes)
    TCP bind hash table entries: 2048 (order: 1, 8192 bytes)
    TCP: Hash tables configured (established 2048 bind 2048)
    TCP reno registered
    UDP hash table entries: 256 (order: 0, 4096 bytes)
    UDP-Lite hash table entries: 256 (order: 0, 4096 bytes)
    NET: Registered protocol family 1
    Trying to unpack rootfs image as initramfs...
    rootfs image is not initramfs (junk in compressed archive); looks like an initrd
    Freeing initrd memory: 4096K
    Bus freq driver module loaded
    WARNING : No battery connected !
    Aborting power driver initialization
    mxs-battery: probe of mxs-battery.0 failed with error 1
    msgmni has been set to 119
    alg: No test for stdrng (krng)
    cryptodev: driver loaded.
    io scheduler noop registered
    io scheduler deadline registered
    io scheduler cfq registered (default)
    Console: switching to colour frame buffer device 80x30
    mxs-duart.0: ttyAM0 at MMIO 0x80070000 (irq = 0) is a DebugUART
    brd: module loaded
    loop: module loaded
    usbcore: registered new interface driver smsc95xx
    usbmon: debugfs is not available
    ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
    fsl-ehci fsl-ehci: Freescale On-Chip EHCI Host Controller
    fsl-ehci fsl-ehci: new USB bus registered, assigned bus number 1
    fsl-ehci fsl-ehci: irq 11, io base 0x80080000
    fsl-ehci fsl-ehci: USB 2.0 started, EHCI 1.00
    usb usb1: New USB device found, idVendor=1d6b, idProduct=0002
    usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
    usb usb1: Product: Freescale On-Chip EHCI Host Controller
    usb usb1: Manufacturer: Linux 2.6.35.3_OLinuXinoR4 ehci_hcd
    usb usb1: SerialNumber: fsl-ehci
    hub 1-0:1.0: USB hub found
    hub 1-0:1.0: 1 port detected
    Initializing USB Mass Storage driver...
    usbcore: registered new interface driver usb-storage
    USB Mass Storage support registered.
    usbcore: registered new interface driver libusual
    MXS RTC driver v1.0 hardware v2.0.0
    mxs-rtc mxs-rtc.0: rtc core: registered mxs-rtc as rtc0
    IR NEC protocol handler initialized
    IR RC5(x) protocol handler initialized
    IR RC6 protocol handler initialized
    IR JVC protocol handler initialized
    IR Sony protocol handler initialized
    mxs watchdog: initialized, heartbeat 19 sec
    mxs-mmc: MXS SSP Controller MMC Interface driver
    ssp_set_rate: error -110
    mxs-mmc mxs-mmc.0: mmc0: MXS SSP MMC DMAIRQ 14 ERRIRQ 15 
    dcp dcp.0: DCP crypto enabled.!
    usbcore: registered new interface driver usbhid
    usbhid: USB HID core driver
    mxs-adc-audio mxs-adc-audio.0: MXS ADC/DAC Audio Codec 
    No device for DAI mxs adc/dac
    No device for DAI mxs adc/dac
    asoc: mxs adc/dac <-> mxs adc/dac mapping ok
    ALSA device list:
      #0: MXS EVK (mxs adc/dac)
    TCP cubic registered
    NET: Registered protocol family 17
    mxs-rtc mxs-rtc.0: setting system clock to 1970-01-01 00:00:10 UTC (10)
    Waiting for root device /dev/mmcblk0p2...
    mmc0: new high speed SD card at address 0007
    mmcblk0: mmc0:0007 SD02G 1.83 GiB 
     mmcblk0: p1 p2
    EXT2-fs (mmcblk0p2): warning: mounting unchecked fs, running e2fsck is recommended
    VFS: Mounted root (ext2 filesystem) on device 179:2.
    Freeing init memory: 120K
    INIT: 
    version 2.88 booting
    Using makefile-style concurrent boot in runlevel S.
    Starting the hotplug events dispatcher: udevd.
    Synthesizing the initial hotplug events...udevd-work[418]: error opening ATTR{/sys/class/sound/controlC0/../uevent} for writing: No such file or directory
    done.
    Waiting for /dev to be fully populated...done.
    Activating swap...done.
    Checking root file system...fsck from util-linux-ng 2.17.2
    /lib/init/rw/rootdev was not cleanly unmounted, check forced.
    /lib/init/rw/rootdev: |==                                      |  4.7%   
    /lib/init/rw/rootdev: |====                                    /  9.3%   
    /lib/init/rw/rootdev: |======                                  - 14.0%   
    /lib/init/rw/rootdev: |=======                                 \ 18.7%   
    /lib/init/rw/rootdev: |=========                               | 23.3%   
    /lib/init/rw/rootdev: |===========                             / 28.0%   
    /lib/init/rw/rootdev: |=============                           - 32.7%   
    /lib/init/rw/rootdev: |===============                         \ 37.3%   
    /lib/init/rw/rootdev: |=================                       | 42.0%   
    /lib/init/rw/rootdev: |===================                     / 46.7%   
    /lib/init/rw/rootdev: |=====================                   - 51.3%   
    /lib/init/rw/rootdev: |======================                  \ 56.0%   
    /lib/init/rw/rootdev: |========================                | 60.7%   
    /lib/init/rw/rootdev: |==========================              / 65.3%   
    /lib/init/rw/rootdev: |============================            - 70.0%   
    /lib/init/rw/rootdev: |============================            \ 70.2%   
    /lib/init/rw/rootdev: |============================            | 71.1%   
    /lib/init/rw/rootdev: |=============================           / 72.4%   
    /lib/init/rw/rootdev: |=============================           - 73.6%   
    /lib/init/rw/rootdev: |==============================          \ 74.6%   
    /lib/init/rw/rootdev: |==============================          | 75.7%   
    /lib/init/rw/rootdev: |===============================         / 76.5%   
    /lib/init/rw/rootdev: |===============================         - 77.5%   
    /lib/init/rw/rootdev: |===============================         \ 78.4%   
    /lib/init/rw/rootdev: |================================        | 79.5%   
    /lib/init/rw/rootdev: |================================        / 80.5%   
    /lib/init/rw/rootdev: |=================================       - 82.0%   
    /lib/init/rw/rootdev: |=================================       \ 82.8%   
    /lib/init/rw/rootdev: |==================================      | 83.8%   
    /lib/init/rw/rootdev: |==================================      / 84.9%   
    /lib/init/rw/rootdev: |==================================      - 86.1%   
    /lib/init/rw/rootdev: |===================================     \ 87.3%   
    /lib/init/rw/rootdev: |===================================     | 88.3%   
    /lib/init/rw/rootdev: |====================================    / 89.6%   
    Rebuilding directory: |===========                     - 33.3%  49871
    /lib/init/rw/rootdev: |=====================================   \ 93.6%   
    /lib/init/rw/rootdev: |======================================  | 95.8%   
    /lib/init/rw/rootdev: |======================================= / 96.8%   
    /lib/init/rw/rootdev: |========================================- 99.5%   
    /lib/init/rw/rootdev: |========================================| 100.0%   
                                                                                   
    /lib/init/rw/rootdev: ***** REBOOT LINUX *****
    /lib/init/rw/rootdev: 10097/119040 files (0.2% non-contiguous), 80422/475904 blocks
    fsck died with exit status 3
    [31mfailed (code 3).
    [39;49m
    The file system check corrected errors on the root partition but requested that the system be restarted. ... 
    [31mfailed!
    [39;49m
    The system will be restarted in 5 seconds. ... 
    [33m(warning).
    [39;49m
    Restarting system.
    HTLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLFC
    PowerPrep start initialize power...
    Battery Voltage = 2.14V
    No battery or bad battery					detected!!!.Disabling battery					voltage measurements./r/nLLCMay 11 201215:26:EMI_CTRL 0x1C08404init_ddr_mt46v32m10Frac 0x92926192
    start change cpu fr
    LLLLLLLFCLJUncompressing Linux... done, booting the kernel.
    Linux version 2.6.35.3_OLinuXinoR4 (hehopmajieh@hehopmajieh-office) (gcc version 4.7.1 20120421 (prerelease) (GCC) ) #11 PREEMPT Mon May 21 10:27:52 EEST 2012
    CPU: ARM926EJ-S [41069265] revision 5 (ARMv5TEJ), cr=00053177
    CPU: VIVT data cache, VIVT instruction cache
    Machine: iMX233-OLinuXino low cost board
    Memory policy: ECC disabled, Data cache writeback
    Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 16256
    Kernel command line: noinitrd console=ttyAM0,115200 root=/dev/mmcblk0p2 rw rootwait ssp1=mmc
    PID hash table entries: 256 (order: -2, 1024 bytes)
    Dentry cache hash table entries: 8192 (order: 3, 32768 bytes)
    Inode-cache hash table entries: 4096 (order: 2, 16384 bytes)
    Memory: 64MB = 64MB total
    Memory: 57208k/57208k available, 8328k reserved, 0K highmem
    Virtual kernel memory layout:
        vector  : 0xffff0000 - 0xffff1000   (   4 kB)
        fixmap  : 0xfff00000 - 0xfffe0000   ( 896 kB)
        DMA     : 0xfde00000 - 0xffe00000   (  32 MB)
        vmalloc : 0xc4800000 - 0xf0000000   ( 696 MB)
        lowmem  : 0xc0000000 - 0xc4000000   (  64 MB)
        modules : 0xbf000000 - 0xc0000000   (  16 MB)
          .init : 0xc0008000 - 0xc0026000   ( 120 kB)
          .text : 0xc0026000 - 0xc033d000   (3164 kB)
          .data : 0xc0356000 - 0xc0381a00   ( 175 kB)
    Hierarchical RCU implementation.
    	RCU-based detection of stalled CPUs is disabled.
    	Verbose stalled-CPUs detection is disabled.
    NR_IRQS:224
    Console: colour dummy device 80x30
    console [ttyAM0] enabled
    Calibrating delay loop... 226.91 BogoMIPS (lpj=1134592)
    pid_max: default: 32768 minimum: 301
    Security Framework initialized
    Mount-cache hash table entries: 512
    CPU: Testing write buffer coherency: ok
    regulator: core version 0.5
    NET: Registered protocol family 16
    regulator: vddd: 800 <--> 1575 mV at 1550 mV fast normal 
    regulator: vdddbo: 800 <--> 1575 mV fast normal 
    regulator: vdda: 1500 <--> 2275 mV at 1750 mV fast normal 
    regulator: vddio: 2800 <--> 3575 mV at 3300 mV fast normal 
    regulator: overall_current: fast normal 
    regulator: mxs-duart-1: fast normal 
    regulator: mxs-bl-1: fast normal 
    regulator: mxs-i2c-1: fast normal 
    regulator: mmc_ssp-1: fast normal 
    regulator: mmc_ssp-2: fast normal 
    regulator: charger-1: fast normal 
    regulator: power-test-1: fast normal 
    regulator: cpufreq-1: fast normal 
    i.MX IRAM pool: 28 KB@0xc4808000
    bio: create slab <bio-0> at 0
    SCSI subsystem initialized
    usbcore: registered new interface driver usbfs
    usbcore: registered new interface driver hub
    usbcore: registered new device driver usb
    Advanced Linux Sound Architecture Driver Version 1.0.23.
    Switching to clocksource mxs clock source
    NET: Registered protocol family 2
    IP route cache hash table entries: 1024 (order: 0, 4096 bytes)
    TCP established hash table entries: 2048 (order: 2, 16384 bytes)
    TCP bind hash table entries: 2048 (order: 1, 8192 bytes)
    TCP: Hash tables configured (established 2048 bind 2048)
    TCP reno registered
    UDP hash table entries: 256 (order: 0, 4096 bytes)
    UDP-Lite hash table entries: 256 (order: 0, 4096 bytes)
    NET: Registered protocol family 1
    Trying to unpack rootfs image as initramfs...
    rootfs image is not initramfs (junk in compressed archive); looks like an initrd
    Freeing initrd memory: 4096K
    Bus freq driver module loaded
    WARNING : No battery connected !
    Aborting power driver initialization
    mxs-battery: probe of mxs-battery.0 failed with error 1
    msgmni has been set to 119
    alg: No test for stdrng (krng)
    cryptodev: driver loaded.
    io scheduler noop registered
    io scheduler deadline registered
    io scheduler cfq registered (default)
    Console: switching to colour frame buffer device 80x30
    mxs-duart.0: ttyAM0 at MMIO 0x80070000 (irq = 0) is a DebugUART
    brd: module loaded
    loop: module loaded
    usbcore: registered new interface driver smsc95xx
    usbmon: debugfs is not available
    ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
    fsl-ehci fsl-ehci: Freescale On-Chip EHCI Host Controller
    fsl-ehci fsl-ehci: new USB bus registered, assigned bus number 1
    fsl-ehci fsl-ehci: irq 11, io base 0x80080000
    fsl-ehci fsl-ehci: USB 2.0 started, EHCI 1.00
    usb usb1: New USB device found, idVendor=1d6b, idProduct=0002
    usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
    usb usb1: Product: Freescale On-Chip EHCI Host Controller
    usb usb1: Manufacturer: Linux 2.6.35.3_OLinuXinoR4 ehci_hcd
    usb usb1: SerialNumber: fsl-ehci
    hub 1-0:1.0: USB hub found
    hub 1-0:1.0: 1 port detected
    Initializing USB Mass Storage driver...
    usbcore: registered new interface driver usb-storage
    USB Mass Storage support registered.
    usbcore: registered new interface driver libusual
    MXS RTC driver v1.0 hardware v2.0.0
    mxs-rtc mxs-rtc.0: rtc core: registered mxs-rtc as rtc0
    IR NEC protocol handler initialized
    IR RC5(x) protocol handler initialized
    IR RC6 protocol handler initialized
    IR JVC protocol handler initialized
    IR Sony protocol handler initialized
    mxs watchdog: initialized, heartbeat 19 sec
    mxs-mmc: MXS SSP Controller MMC Interface driver
    ssp_set_rate: error -110
    mxs-mmc mxs-mmc.0: mmc0: MXS SSP MMC DMAIRQ 14 ERRIRQ 15 
    dcp dcp.0: DCP crypto enabled.!
    usbcore: registered new interface driver usbhid
    usbhid: USB HID core driver
    mxs-adc-audio mxs-adc-audio.0: MXS ADC/DAC Audio Codec 
    No device for DAI mxs adc/dac
    No device for DAI mxs adc/dac
    asoc: mxs adc/dac <-> mxs adc/dac mapping ok
    ALSA device list:
      #0: MXS EVK (mxs adc/dac)
    TCP cubic registered
    NET: Registered protocol family 17
    mxs-rtc mxs-rtc.0: setting system clock to 1970-01-01 00:00:57 UTC (57)
    Waiting for root device /dev/mmcblk0p2...
    mmc0: new high speed SD card at address 0007
    mmcblk0: mmc0:0007 SD02G 1.83 GiB 
     mmcblk0: p1 p2
    VFS: Mounted root (ext2 filesystem) on device 179:2.
    Freeing init memory: 120K
    INIT: 
    version 2.88 booting
    Using makefile-style concurrent boot in runlevel S.
    Starting the hotplug events dispatcher: udevd.
    Synthesizing the initial hotplug events...udevd-work[423]: error opening ATTR{/sys/class/sound/controlC0/../uevent} for writing: No such file or directory
    done.
    Waiting for /dev to be fully populated...done.
    Activating swap...done.
    Checking root file system...fsck from util-linux-ng 2.17.2
    /lib/init/rw/rootdev: clean, 10097/119040 files, 80422/475904 blocks
    done.
    Cleaning up ifupdown....
    Setting up networking....
    Loading kernel modules...done.
    Activating lvm and md swap...done.
    Checking file systems...fsck from util-linux-ng 2.17.2
    done.
    Mounting local filesystems...done.
    Activating swapfile swap...done.
    Cleaning up temporary files....
    Configuring network interfaces...cat: /sys/class/net/usb0/address: No such file or directory
    run-parts: /etc/network/if-pre-up.d/00-persistent-mac exited with return code 1
    cat: /sys/class/net/usb0/address: No such file or directory
    run-parts: /etc/network/if-pre-up.d/00-persistent-mac exited with return code 1a
    SIOCSIFHWADDR: No such device
    Failed to bring up usb0.
    done.
    Cleaning up temporary files....
    Setting kernel variables ...done.
    INIT: 
    Entering runlevel: 2
    Using makefile-style concurrent boot in runlevel 2.
    Starting NTP server: ntpd.
    Starting OpenBSD Secure Shell server: sshd.
    Debian GNU/Linux 6.0 debian ttyAM0
    debian login:


# GPIO


Some GPIOs are already exposed in /sys/class/gpio:


    root@debian:/sys/class/gpio# ls -al
    total 0
    drwxr-xr-x 30 root root    0 Jan  1 02:00 .
    drwxr-xr-x 23 root root    0 Jan  1 02:00 ..
    --w-------  1 root root 4096 Jan  1 02:00 export
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpio0
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpio1
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpio16
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpio17
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpio19
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpio2
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpio20
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpio23
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpio24
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpio25
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpio3
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpio30
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpio31
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpio4
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpio5
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpio51
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpio52
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpio53
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpio55
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpio56
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpio6
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpio65
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpio7
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpio91
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpio92
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpiochip0
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpiochip32
    drwxr-xr-x  3 root root    0 Jan  1 02:00 gpiochip64
    --w-------  1 root root 4096 Jan  1 02:00 unexport
    root@debian:/sys/class/gpio#


# Cpuinfo



    root@debian:~# cat /proc/cpuinfo 
    Processor       : ARM926EJ-S rev 5 (v5l)
    BogoMIPS        : 226.91
    Features        : swp half thumb fastmult edsp java 
    CPU implementer : 0x41
    CPU architecture: 5TEJ
    CPU variant     : 0x0
    CPU part        : 0x926
    CPU revision    : 5
    
    Hardware        : iMX233-OLinuXino low cost board
    Revision        : 0000
    Serial          : 0000000000000000


# Problems


The debian kernel provided does not have any modules. For example, I plugged in some ethernet over USB card (asix module) which is missing.

# Similar devices


## Chumby One


It seems the [Chumby One](http://wiki.chumby.com/index.php/Main_Page) is also based on the IMX233, has the same amount of RAM.

## Philips VP5500


It is also based on some IMX processor, not sure if it is the same SoC.

# Links


* <http://dangerousprototypes.com/2012/07/04/olinuxino-micro/>  
* https://www.olimex.com/dev/imx233-olinuxino-micro.html
* <http://olimex.wordpress.com/2012/04/27/imx233-olinuxino-micro-76x42-mm-single-board-linux-computer/>  
* <http://wiki.chumby.com/index.php/Hacking_Linux_for_chumby>  
* <http://www.mikrocontroller.net/articles/PHILIPS_VP5500_VoIP_Telefon>  
* <http://www.eewiki.net/display/linuxonarm/iMX233-OLinuXino>  
* <http://www.downtowndougbrown.com/2011/03/chumby-one-cross-compiler-qt/>  
* <http://www.jann.cc/2012/08/23/building_a_kernel_3_x_for_the_olinuxino_from_sources.html>  
* <http://wiki.openwrt.org/toh/tp-link/olinuxino>  