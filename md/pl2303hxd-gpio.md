

# About


I was hunting for many days for a USB dongle that would provide GPIO entries in the form of entries in /sys/class/gpio.

I found the [Oneping.com.tw](http://www.oneping.com.tw) PL2303 breakout board with the chip PL2303 HXD (or HX revD), which has nice 2.54mm pins for 4 GPIOs (GP0, GP1, GP2, GP3). According to the datasheet, there seems to be 4 auxiliary GPIOs (so 8 GPIOs in total), but there is no documentation on how to use them. 

[Oneping](http://www.oneping.com.tw) produces 3 different versions of the board for different GPIO output voltages: 1.6V, 3.3V, 5V. I own the 3.3V version.

[[=image pl2303-gpio-oneping.jpg size="medium"]]

# Kernel patch


Wang YanQing wrote a [patch](http://comments.gmane.org/gmane.linux.usb.general/113746) [[file pl2303-gpio-sysfs.patch | (local copy pl2303-gpio-sysfs.patch)]] to recent kernels (this is one is tested against 3.16, 4.1) in order to expose those GPIOs in /sys/class/gpio.

First, you have to install or to download the kernel sources of your kernel, if you install them via your distribution, they will be put on /usr/src/:


    root@sabayonx86-64 /usr/src [21]# equo install "sys-kernel/sabayon-sources-4.1.12"
    ╠  @@ Calculating dependencies...
    ╠  ## [N] [sabayon-weekly] sys-kernel/sabayon-sources-4.1.12|0
    ╠  @@ Packages needing to be installed/updated/downgraded: 1
    ╠  @@ Packages needing to be removed: 0
    ╠  @@ Download size: 0b
    ╠  @@ Used disk space: 558.3MB
    ╠  @@ You need at least: 770.3MB of free space
    ╠  ::: >>>  (1/1) 1 package
    ╠    ## Downloading: 1 package
    ╠    ## ( mirror #1 ) [sys-kernel:sabayon-sources-4.1.12.749d89a47c204e21eba4525de38e3042e896f6d4~0.tbz2] @ http://na.mirror.garr.it
    ╠   ## Aggregated download: 1 item
    ╠    # [1] na.mirror.garr.it => sys-kernel:sabayon-sources-4.1.12.749d89a47c204e21eba4525de38e3042e896f6d4~0.tbz2
    ╠    ## Checking package checksum...
    ╠    ## ( mirror #1 ) [sys-kernel:sabayon-sources-4.1.12.749d89a47c204e21eba4525de38e3042e896f6d4~0.tbz2] success @ http://na.mirror.garr.it
    ╠  +++ >>>  (1/1) sys-kernel/sabayon-sources-4.1.12
    ╠    ## Unpacking: sys-kernel:sabayon-sources-4.1.12.749d89a47c204e21eba4525de38e3042e896f6d4~0.tbz2



    root@sabayonx86-64 /usr/src [27]# ls -lha
    total 36K
    drwxr-xr-x  6 root root 4.0K Feb 25 18:46 .
    drwxr-xr-x 21 root root 4.0K Feb 25 18:42 ..
    -rw-r--r--  1 root root    0 Nov 19  2005 .keep
    lrwxrwxrwx  1 root root   19 Feb 25 18:45 linux -> linux-4.1.0-sabayon
    drwxr-xr-x 25 root root 4.0K Feb 25 18:44 linux-4.1.0-sabayon
    -rw-r--r--  1 root root 9.3K Sep  4  2014 pl2303-gpio-sysfs.patch
    drwxr-xr-x  7 root root 4.0K Oct  8  2014 rpm
    drwxr-xr-x  4 root root 4.0K Feb  1 15:02 spl-0.6.5.3
    drwxr-xr-x  4 root root 4.0K Feb  1 15:02 zfs-0.6.5.3


I can download the patch here:


    root@sabayonx86-64 /usr/src [29]# wget http://zoobab.wdfiles.com/local--files/pl2303hxd-gpio/pl2303-gpio-sysfs.patch
    --2016-02-25 18:48:38--  http://zoobab.wdfiles.com/local--files/pl2303hxd-gpio/pl2303-gpio-sysfs.patch
    Resolving zoobab.wdfiles.com... 54.165.29.53
    Connecting to zoobab.wdfiles.com|54.165.29.53|:80... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 9517 (9.3K) [text/x-diff]
    Saving to: ‘pl2303-gpio-sysfs.patch’
    
    pl2303-gpio-sysfs.patch         100%[========================================================>]   9.29K  --.-KB/s   in 0.002s 
    
    2016-02-25 18:48:39 (5.64 MB/s) - ‘pl2303-gpio-sysfs.patch’ saved [9517/9517]
    
    root@sabayonx86-64 /usr/src [30]# ls -lha
    total 36K
    drwxr-xr-x  6 root root 4.0K Feb 25 18:48 .
    drwxr-xr-x 21 root root 4.0K Feb 25 18:42 ..
    -rw-r--r--  1 root root    0 Nov 19  2005 .keep
    lrwxrwxrwx  1 root root   19 Feb 25 18:45 linux -> linux-4.1.0-sabayon
    drwxr-xr-x 25 root root 4.0K Feb 25 18:44 linux-4.1.0-sabayon
    -rw-r--r--  1 root root 9.3K Sep  4  2014 pl2303-gpio-sysfs.patch
    drwxr-xr-x  7 root root 4.0K Oct  8  2014 rpm
    drwxr-xr-x  4 root root 4.0K Feb  1 15:02 spl-0.6.5.3
    drwxr-xr-x  4 root root 4.0K Feb  1 15:02 zfs-0.6.5.3
    root@sabayonx86-64 /usr/src [31]#


I had to add a symlink from "a" to "linux":


    root@sabayonx86-64 /usr/src [31]# ln -s linux a
    root@sabayonx86-64 /usr/src [32]# l
    total 28
    lrwxrwxrwx  1 root root    5 Feb 25 18:49 a -> linux
    lrwxrwxrwx  1 root root   19 Feb 25 18:45 linux -> linux-4.1.0-sabayon
    drwxr-xr-x 25 root root 4096 Feb 25 18:44 linux-4.1.0-sabayon
    -rw-r--r--  1 root root 9517 Sep  4  2014 pl2303-gpio-sysfs.patch
    drwxr-xr-x  7 root root 4096 Oct  8  2014 rpm
    drwxr-xr-x  4 root root 4096 Feb  1 15:02 spl-0.6.5.3
    drwxr-xr-x  4 root root 4096 Feb  1 15:02 zfs-0.6.5.3


Now apply the patch:


    root@sabayonx86-64 /usr/src [33]# patch -p0 < pl2303-gpio-sysfs.patch 
    (Stripping trailing CRs from patch; use --binary to disable.)
    patching file a/drivers/usb/serial/Kconfig
    Hunk #1 succeeded at 519 (offset 3 lines).
    (Stripping trailing CRs from patch; use --binary to disable.)
    patching file a/drivers/usb/serial/pl2303.c
    Hunk #2 succeeded at 32 with fuzz 2 (offset -102 lines).
    Hunk #5 succeeded at 246 (offset 3 lines).
    Hunk #6 succeeded at 478 (offset 3 lines).
    Hunk #7 succeeded at 507 (offset 3 lines).
    Hunk #8 succeeded at 521 (offset 3 lines).


Then go to the linux directory, and run "make menuconfig":

The go to "-> Device Drivers -> USB support -> USB Serial Converter support -> USB Prolific 2303 Single Port Serial Driver -> USB Prolific 2303 Single Port GPIOs support".

[[=image pl2303-gpio-sysfs-make-menuconfig.png]]

When you will save, it will have this block in the .config file:


    +config USB_SERIAL_PL2303_GPIO
    +       bool "USB Prolific 2303 Single Port GPIOs support"
    +       depends on USB_SERIAL_PL2303 && GPIOLIB
    +       ---help---
    +         Say Y here if you want to use GPIOs on PL2303 USB Serial single port
    +         adapter from Prolific.
    +
    +         It supports 2 dedicated GPIOs on PL2303HXA, 4 dedicated GPIOs on
    +         PL2303HXD and PL2303RA currently.
    +         If unsure, say N.


Now, you can compile all the serial modules:


    root@sabayonx86-64 /usr/src/linux [15]# make SUBDIRS=drivers/usb/serial modules -j5
      CC [M]  drivers/usb/serial/usb-serial.o
      CC [M]  drivers/usb/serial/generic.o
      CC [M]  drivers/usb/serial/bus.o
      CC [M]  drivers/usb/serial/aircable.o
      CC [M]  drivers/usb/serial/ark3116.o
      CC [M]  drivers/usb/serial/belkin_sa.o
      CC [M]  drivers/usb/serial/ch341.o
      CC [M]  drivers/usb/serial/cp210x.o
      CC [M]  drivers/usb/serial/cyberjack.o
      CC [M]  drivers/usb/serial/cypress_m8.o
      CC [M]  drivers/usb/serial/digi_acceleport.o
    [...]


You will then have a pl2303.ko compiled:


    root@sabayonx86-64 /usr/src/linux/drivers/usb/serial [20]# ls -1 pl*.ko
    pl2303.ko


Try to unload/load it:


    root@sabayonx86-64 /usr/src/linux/drivers/usb/serial [26]# rmmod pl2303; insmod ./pl2303.ko ; lsmod | grep pl2303
    pl2303                 11963  0
    usbserial              25891  1 pl2303


You will then see in /sys/class/gpio that there is now a gpiochip available:


    root@sabayon /sys/class/gpio [2]# l
    total 0
    --w------- 1 root root 4096 Sep  4 10:25 export
    --w------- 1 root root 4096 Sep  4 10:25 unexport
    root@sabayon /sys/class/gpio [3]# l
    total 0
    --w------- 1 root root 4096 Sep  4 10:25 export
    lrwxrwxrwx 1 root root    0 Sep  4 10:26 gpiochip252 -> ../../devices/pci0000:00/0000:00:1a.0/usb3/3-1/3-1:1.0/gpio/gpiochip252
    --w------- 1 root root 4096 Sep  4 10:25 unexport


You can export the 4 GPIOs with echo:


    root@sabayon /sys/class/gpio [22]# echo 252 > export
    root@sabayon /sys/class/gpio [23]# echo 253 > export
    root@sabayon /sys/class/gpio [24]# echo 254 > export
    root@sabayon /sys/class/gpio [25]# echo 255 > export
    root@sabayon /sys/class/gpio [26]# l
    total 0
    --w------- 1 root root 4096 Sep  4 16:02 export
    lrwxrwxrwx 1 root root    0 Sep  4 16:01 gpio252 -> ../../devices/pci0000:00/0000:00:1a.0/usb3/3-1/3-1:1.0/gpio/gpio252
    lrwxrwxrwx 1 root root    0 Sep  4 16:02 gpio253 -> ../../devices/pci0000:00/0000:00:1a.0/usb3/3-1/3-1:1.0/gpio/gpio253
    lrwxrwxrwx 1 root root    0 Sep  4 16:02 gpio254 -> ../../devices/pci0000:00/0000:00:1a.0/usb3/3-1/3-1:1.0/gpio/gpio254
    lrwxrwxrwx 1 root root    0 Sep  4 16:02 gpio255 -> ../../devices/pci0000:00/0000:00:1a.0/usb3/3-1/3-1:1.0/gpio/gpio255
    lrwxrwxrwx 1 root root    0 Sep  4 15:59 gpiochip252 -> ../../devices/pci0000:00/0000:00:1a.0/usb3/3-1/3-1:1.0/gpio/gpiochip252
    --w------- 1 root root 4096 Sep  4 15:59 unexport


Toggling the pins on the shell works, but I have to test the toggling speed with a C program.

I am noting a change in voltage from 0V to 3.3V with this:


    root@sabayon /sys/class/gpio [32]# while true; do sleep 1; echo 0 > gpio252/value; sleep 1; echo 1 > gpio252/value; done


Which confirms that it is working as expected.

# Test with an HXA


I had an RS232 (using 12V) adaptor laying around, tried it as well, GP1 and GP0 were exposed:


    root@sabayon /sys/class/gpio [26]# l
    total 0
    --w------- 1 root root 4096 Sep  4 18:35 export
    lrwxrwxrwx 1 root root    0 Sep  4 18:35 gpio254 -> ../../devices/pci0000:00/0000:00:1d.0/usb6/6-2/6-2:1.0/gpio/gpio254
    lrwxrwxrwx 1 root root    0 Sep  4 18:35 gpio255 -> ../../devices/pci0000:00/0000:00:1d.0/usb6/6-2/6-2:1.0/gpio/gpio255
    lrwxrwxrwx 1 root root    0 Sep  4 18:34 gpiochip254 -> ../../devices/pci0000:00/0000:00:1d.0/usb6/6-2/6-2:1.0/gpio/gpiochip254
    --w------- 1 root root 4096 Sep  4 18:34 unexport


But I could not change the status of the pin:


    root@sabayon /sys/class/gpio [22]# echo 1 > gpio255/value 
    root@sabayon /sys/class/gpio [23]# cat gpio255/value 
    0


I don't know why...

I also tried with a chinese clone (small chip covered with some black paste), got the same error, could export the 2 GPIOs, but could not write to them. 

# Android app and USB sniffing


The android app PL2303GPIOActivity.apk provides an GUI to toggle the 4 GPIO pins **and the 4 auxiliary pins** (this is a feature NOT documented anywhere). The app only works on some tablet versions of Android. After fighting with different tablets which supports OTG, I decided to give Android-x86-4.4-r1 a shot on my Lenovo X200 laptop, and it works like a charm. The only problem is that the kernel does not have support for usbmon, so I will need to recompile the whole thing to be able the sniff the USB packets. Stay tuned!

# Todo


* Find a decent and simple speed tester for sysfs gpio pins
* Test avrdude and urjtag with GPIO cable support
* Blink a LED
* Speed comparison with RaspberryPi GPIO bitbanging
* Order some chips PL2303TB with 12 GPIOs 
* Find out how to disable the RI/DCD/DSR/CTS pins in order to use them as GPIOs (look at the source code of the android app)

# Other chips


## Cypress


Cypress has also pushed a [patch](http://article.gmane.org/gmane.linux.kernel.gpio/3978) to support 12 GPIOs over USB with the CYUSBS234. A [devboard CYUSBS232](http://www.mouser.be/ProductDetail/Cypress-Semiconductor/CYUSBS232/?qs=%2fha2pyFaduib4nxEOn47igcAfL4601LNLXM8NRpiehteo3rZvw%252bZlw%3d%3d) is available at Mouser, including the standalone [chip CY7C65213-28PVXI](http://www.mouser.be/Search/ProductDetail.aspx?qs=dOK1vf2izjvExqwVZ7qYig%3d%3d) in SOP28 format.

Sparkfun sells now a nice [breakout board](https://www.sparkfun.com/products/13830) with this Cypress chip.

## FTDI


Just discovered this patch posted in June on the LKML: <https://lkml.org/lkml/2014/6/9/406>   . It is not merged in mainline because kernel guys are nagging about it, so I am trying it now on the [[[ftdi-gpios-sysfs |ftdi-gpios-sysfs]]] page.

# Links


* <https://www.youtube.com/watch?v=XZD3mCYBnwM>  
* <http://www.oneping.com.tw/p_usb2ttl_16_18V.htm>  
* <https://github.com/juluosdev/studygroups/wiki/PL2303HXD-Adapter>  
* <https://play.google.com/store/apps/details?id=tw.com.prolific.pl2303hxdgpio>  
* <http://www.oneping.com.tw/Technical_Articles/t-PL2303-Android.htm>  
* <http://www.oneping.com.tw/downlaod/driver/Android/PL2303_Android.zip>  
* <http://www.cnx-software.com/2014/10/20/add-gpios-to-windows-linux-android-computers-and-devices-with-ftdi-usb-adapters-breakout-boards/>  
* <http://ncrmnt.org/wp/2014/11/04/esp8266-and-pl2303hx-gpio-adventures/>  
* <https://github.com/nekromant/pl2303gpio>  
* <http://resolaqq.blogspot.be/2015/08/pl-2303hxd-usb-ttl.html>  
* <http://www.tme.vn/Product.aspx?id=1734#page=pro_info>  

# Comments


[[module Comments]]