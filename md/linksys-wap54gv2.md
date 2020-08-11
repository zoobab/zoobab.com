

# Pictures


[[gallery]]

# Hardware


||~ Brand ||~ Model ||~ FCC-ID ||~ Flash ||~ RAM ||~ USB ||~ Serial ||~ 4ports ||~ JTAG ||~ Notes ||
|| Linksys || WAP54G v2.0 || [  Q87-WAP54GV2](https://fjallfoss.fcc.gov/oetcf/eas/reports/ViewExhibitReport.cfm?mode=Exhibits&RequestTimeout=500&calledFromFrame=N&application_id=213890&fcc_id=&#039Q87-WAP54GV2&#039) || Intel TE28F160 C3BD70 || EtronTech EM638165TS-7 || N || 10pins? || N || Y || Notes ||

# Serial port


## Pinout


[[<image WAP54Gv2-PCB-J5-detail.jpg size="small"]]

## Minicom


115200 8N1 no softcontrol

# JTAG


## Pinout


> GND   O O   SW_RESET
> GND   O O   TCK
> GND   O O   TMS
> GND   O O   TDO
> GND   O O   TDI
> GND   O #   TRST_L

[[<image pinout.png size="small"]]

## With JTAGKey Tiny


I rechecked the connexions of my Amontec JTAGKey tiny, and tried another GND then the one that was written on the board, and it works now:

[[=image 270320101094.jpg size="medium"]]

> jtag> cable JTAGkey
> Connected to libftdi driver.
> jtag> detect
> IR length: 8
> Chain length: 1
> Device Id: 00010100011100010010000101111111 (0x000000001471217F)
>  Manufacturer: Broadcom
>  Part(0):         BCM4712
>  Stepping:     Ver 1
>  Filename:     /usr/share/urjtag/broadcom/bcm4712/bcm4712
> jtag> 

> jtag> print
>  No. Manufacturer              Part                 Stepping Instruction          Register                        
>    0 Broadcom                  BCM4712              Ver 1    BYPASS               BR                              
> 
> Active bus:
> *0: EJTAG compatible bus driver via PrAcc (JTAG part No. 0)
>         start: 0x00000000, length: 0x20000000, data width: 8 bit
>         start: 0x20000000, length: 0x20000000, data width: 16 bit
>         start: 0x40000000, length: 0x20000000, data width: 32 bit


I also took the Vref from the serial port on the board:

[[=image 270320101093.jpg size="medium"]]

## CFE.BIN


CFE image [here](http://zoobab.wikidot.com/local--files/linksys-wap54gv2/CFE.BIN.WAP54GV2).

## WHOLEFLASH.BIN


Here.

# Serial output



    CFE version 1.0.37 for BCM947XX (32bit,SP,LE)
    Build Date: Fri Dec 12 02:01:12 CST 2003 (vlinux@Test)
    Copyright (C) 2000,2001,2002,2003 Broadcom Corporation.
    
    Initializing Arena.
    Initializing Devices.
    CPU type 0x29007: 192MHz
    Total memory: 0x2000000 bytes (32MB)
    
    Total memory used by CFE:  0x8032B9F0 - 0x80430EF0 (1070336)
    Initialized Data:          0x8032B9F0 - 0x8032DB40 (8528)
    BSS Area:                  0x8032DB40 - 0x8032EEF0 (5040)
    Local Heap:                0x8032EEF0 - 0x8042EEF0 (1048576)
    Stack Area:                0x8042EEF0 - 0x80430EF0 (8192)
    Text (code) segment:       0x80300000 - 0x80309420 (37920)
    Boot area (physical):      0x00431000 - 0x00471000
    Relocation Factor:         I:00000000 - D:00000000
    
    Reading :: Failed.: Error
    CFE>



    CFE> ifconfig
    Network interface has not been configured
    *** command status = 0
    CFE> printenv
    Variable Name        Value
    -------------------- --------------------------------------------------
    BOOT_CONSOLE         uart0
    CFE_VERSION          1.0.37
    CFE_BOARDNAME        BCM947XX
    CFE_MEMORYSIZE       32
    STARTUP              go;
    *** command status = 0
    CFE>


# Firmwares


* [wap54gv2.2.06-with-boot_wait-on.trx](http://zoobab.wikidot.com/local--files/linksys-wap54gv2/wap54gv2.2.06-with-boot_wait-on.trx)

# Links


* [Sorgonet: Howto revive a bricked WAP54G](http://www.sorgonet.com/network/wap54gbricked/)