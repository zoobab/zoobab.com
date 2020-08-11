

# Gallery


[[gallery]]

# Step 1: Get a root shell


Connect an ethernet cable between your PC and la Fonera, and the configure the ethernet interface on your linux laptop with the following IP address:
> ifconfig eth0 169.254.255.2 broadcast 169.254.255.255 netmask 255.255.0.0
Test your connexion with the router with ping
> ping -c 3 169.254.255.1
Then you can activate the SSH dropbear server on la Fonera with the following command (works for version below 0.7.xx) (local copy of [fondue.pl](http://zoobab.wikidot.com/local--files/fonera/fondue.pl)):
> echo -e '/usr/sbin/iptables -I INPUT 1 -p tcp --dport 22 -j ACCEPT\n/etc/init.d/dropbear' | perl fondue.pl 169.254.255.1 admin
Then you are able to have a shell on the box
> ssh root@169.254.255.1
> Password: admin
> root shell!

# Step 2: Install fon-telnet-redboot


Once you have a shell on the box, download on your laptop [fon-telnet-for-redboot_1_mips.ipk](http://download.berlin.freifunk.net/fonera/fon-telnet-for-redboot_1_mips.ipk) ([local copy](http://zoobab.wikidot.com/local--files/fonera/fon-telnet-for-redboot_1_mips.ipk)), and upload the package to the router fonera via scp:

> zoobab@mylaptop$ scp fon-telnet-for-redboot_1_mips.ipk root@169.254.255.1:/tmp
> Password: admin

Then login to the router

> ssh root@169.254.255.1
> Password: admin

And install the package via the following command:

> root@Fon$ ipkg install /tmp/fon-telnet-for-redboot_1_mips.ipk

It takes 10 seconds and you get a root shell back. Reboot the router by typing:

> root@Fon$ reboot

# Step3: Reflash with AP51 utils


Download the 3 following files on your harddisk: [openwrt-atheros-2.6-root.jffs2-64k](http://downloads.openwrt.org/kamikaze/7.09/atheros-2.6/openwrt-atheros-2.6-root.jffs2-64k),[openwrt-atheros-2.6-vmlinux.lzma](http://downloads.openwrt.org/kamikaze/7.09/atheros-2.6/openwrt-atheros-2.6-vmlinux.lzma), and [ap51-flash-1.0-42](http://download.berlin.freifunk.net/fonera/ap51-flash-1.0-42).

Then launch the ap-utils:

> chmod +x ap51-flash-1.0-38
> sudo ./ap51-flash-1.0-38 eth0 openwrt-atheros-2.6-root.jffs2-64k openwrt-atheros-2.6-vmlinux.lzma

It takes 10 minutes or so, go drink a coffee or tea.

# Step 4: JTAG La Fonera


## Pinout


[[=image Fonera-jtag-pinout.jpg]]

## Connections


Apparently the TRST and VCC pins needs to be connected together with a 100ohms resistor:

[[=image interface.png size="medium"]]

[[=image 28082009045b.jpg size="medium"]]

[[=image 28082009042.jpg size="medium"]]

[[=image 29082009054.jpg size="medium"]]

## Tjtag


I used Tjtag3, which has SPI support for the flash. You can find the sources and the binaries for Linux 32bits, 64bits and Windows in [[file tjtag3.zip | tjtag3.zip]].


    root@lehne /home/zoobab [21]# ./tjtag3 -probeonly /fc:25
    
    ==============================================
     EJTAG Debrick Utility v3.0 RC1 Tornado-MOD 
    ==============================================
    
    Probing bus ... Done
    
    Instruction Length set to 5
    
    CPU Chip ID: 00000000000000000000000000000001 (00000001)
    *** Found a Atheros AR531X/231X CPU chip ***
    
        - EJTAG IMPCODE ....... : 01000000010000000100000000000000 (40404000)
        - EJTAG Version ....... : 2.6
        - EJTAG DMA Support ... : No
        - EJTAG Implementation flags: R4k ASID_8 NoDMA MIPS32
    
    Issuing Processor / Peripheral Reset ...  ECR: 0x00000008 Done
    Enabling Memory Writes ... Skipped
    Halting Processor ... 
    00000000000100010000000000001000 (00110008)
    00000000000000000000000000001000 (00000008)
    <Processor Entered Debug Mode!> ... Done
    ^C
    root@lehne /home/zoobab [22]#


## Flash dumps


You need sometimes to power on/off the Fonera to have the dump working correctly with the command:


    root@lehne /home/zoobab [22]# ./tjtag3 -backup:wholeflash /fc:25


[[=image 29082009052b.jpg size="medium"]]

* [[file AR-CFE.BIN.SAVED_20090828_020552 | Bootloader AR-CFE.BIN.SAVED_20090828_020552]] (256KB)
* [[file AR-KERNEL.BIN.SAVED_20090828_015856 | Kernel AR-KERNEL.BIN.SAVED_20090828_015856]] (6.93MB)
* [[file AR-WHOLEFLASH.BIN.SAVED_20090828_014548 | Wholeflash AR-WHOLEFLASH.BIN.SAVED_20090828_014548]] (8MB)

## Reflashing with dumps


It takes a while (8 hours for me!) to reflash the complete flash chip with the [[[simple-jtag | simple jtag adaptor]]] on parallel port.

From the following webpage [Autopsy of a Fonera](http://the.firehou.se/2006/10/06/autopsy-of-a-fonera/), you can read:

> Two memory ICs are available on the Fonera, the first is an ST M25P64 serial flash, with a 50MHz SPI bus and 64Mbit capacity (8MB), in 300mil SO16 format. The fact that SPI has been chosen has the advantage that extra memory devices could be attached to the bus, **but it has the caveat that it is slower than a parallel bus. Thus, flashing a new firmware could take a rather long time.**

## Reflash only the bootloader


Since reflashing the whole chip with JTAG and a parallel port takes too much time for most people, it is useful to reflash only the bootloader (256KB=30mins instead of 8MB=8hours). I still have to try to reflash the [[file AR-CFE.BIN.SAVED_20090828_020552 | dumped bootloader]] on a virgin flash to see if I can easily use ap51 to rescue the machine.

Write the bootloader -- Work In Progress -- tjtag3 is segfaulting:


    Manual Flash Selection ... Done
    
    Flash Vendor ID: 00000000000000000000000000100000 (00000020)
    Flash Device ID: 00000000000000000010000000010111 (00002017)
    *** Manually Selected a STMicro M25P64             (8MB) Serial Flash Chip ***
    
        - Flash Chip Window Start .... : 1c000000
        - Flash Chip Window Length ... : 00800000
        - Selected Area Start ........ : a8000000
        - Selected Area Length ....... : 00040000
    
    *** You Selected to Flash the AR-CFE.BIN ***
    
    =========================
    Flashing Routine Started
    =========================
    Total Blocks to Erase: 0
    
    
    Loading AR-CFE.BIN to Flash Memory...
    [  0% Flashed]   a8000000: 00000000 00000000 00000000 00000000
    [  0% Flashed]   a8000010: 00000000 00000000 00000000 00000000
    [  0% Flashed]   a8000020: 00000000 00000000 00000000 00000000
    
    [...]
    
    [ 63% Flashed]   a8028ee0: 00000000 00000000 00000000 00000000
    [ 63% Flashed]   a8028ef0: 00000000 00000000 00000000 00000000
    [ 63% Flashed]   a8028f00: 00000000 Segmentation fault



## Todolist


On the todolist:

* blank the flash -- does not seem to work...
* test it with ap51
* find if OpenOCD or UrJTAG support SPI flashes

# Hardware list


* zoo03 00:18:84:24:07:78
* zoo20 00:18:84:24:A1:D0

# Urjtag



    root@buzek /home/zoobab [3]# jtag
    
    UrJTAG 0.9 #1476
    Copyright (C) 2002, 2003 ETC s.r.o.
    Copyright (C) 2007, 2008 Kolja Waschk and the respective authors
    
    UrJTAG is free software, covered by the GNU General Public License, and you are
    welcome to change it and/or distribute copies of it under certain conditions.
    There is absolutely no warranty for UrJTAG.
    
    WARNING: UrJTAG may damage your hardware!
    Type "quit" to exit, "help" for help.
    
    jtag> cable JTAGkey
    Connected to libftdi driver.
    jtag> detect
    IR length: 5
    Chain length: 1
    Device Id: 00000000000000000000000000000001 (0x0000000000000001)
      Unknown manufacturer!
    chain.c(149) Part 0 without active instruction
    chain.c(200) Part 0 without active instruction
    chain.c(149) Part 0 without active instruction
    jtag> initbus ejtag
    ejtag.c(292) EJCONTROL or EJIMPCODE register not found
    bus initialization failed!
    jtag>


Following the steps mentioned [here](http://www.linux-mips.com/wiki/JTAG):


    jtag> instruction length 5
    jtag> register IMP 32
    jtag> instruction IMPCODE 00011 IMP
    jtag> instruction IMPCODE
    jtag> shift ir
    jtag> shift dr
    jtag> dr
    01000000010000000100000000000000 (0x40404000)
    jtag>


# Links 


* <http://wiki.villagetelco.org/images/3/39/MP01_Hardware_Description_2010-05-02.pdf>  
* <http://villagetelco.svn.sourceforge.net/viewvc/villagetelco/jtagspi/README>  
* <http://wiki.villagetelco.org/index.php?title=Mesh_Potato_Firmware_How_To#Flashing_the_Boot_Loader_using_JTAG>  

# Comments


[[module Comments]]