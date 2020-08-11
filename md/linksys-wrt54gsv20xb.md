# Pictures


[[gallery]]

# Hardware


||~ Brand ||~ Model ||~ FCC-ID ||~ Flash ||~ RAM ||~ USB ||~ Serial ||~ 4ports ||~ JTAG ||~ Notes ||
|| Linksys || WRT54GS v2.0 XB || ??????????? || 4MB Intel TE28F320 || 32MB Mira XXXXXXXX || N || Y || Y || Y || Notes ||

# JTAG


## Pinout


[[=image pinout.png size="small"]]

## Urjtag


> root@warsaw /home/zoobab [2]# jtag 
> 
> UrJTAG 0.8 #1067
> Copyright (C) 2002, 2003 ETC s.r.o.
> Copyright (C) 2007, 2008 Kolja Waschk and the respective authors
> 
> UrJTAG is free software, covered by the GNU General Public License, and you are
> welcome to change it and/or distribute copies of it under certain conditions.
> There is absolutely no warranty for UrJTAG.
> 
> WARNING: UrJTAG may damage your hardware!
> Type "quit" to exit, "help" for help.
> 
> jtag> cable JTAGkey ftdi-mpsse 0403:cff8
> Initializing on FTDI device 0403:cff8
> jtag> detect
> Warning: TDO seems to be stuck at 1
> jtag>

## Urjtag with Wiggler


> root@warsaw /home/zoobab [6]# jtag
> 
> UrJTAG 0.8 #1067
> Copyright (C) 2002, 2003 ETC s.r.o.
> Copyright (C) 2007, 2008 Kolja Waschk and the respective authors
> 
> UrJTAG is free software, covered by the GNU General Public License, and you are
> welcome to change it and/or distribute copies of it under certain conditions.
> There is absolutely no warranty for UrJTAG.
> 
> WARNING: UrJTAG may damage your hardware!
> Type "quit" to exit, "help" for help.
> 
> jtag> cable WIGGLER parallel 0x378
> Initializing parallel port at 0x378
> jtag> detect
> IR length: 8
> Chain length: 1
> Device Id: 00010100011100010010000101111111 (0x000000001471217F)
>   Manufacturer: Broadcom
>   Part(0):         BCM4712
>   Stepping:     Ver 1
>   Filename:     /usr/local/share/urjtag/broadcom/bcm4712/bcm4712
> Please use the 'include' command instead of 'script'
> -E- Error: Illegal character # (/043) at line 1:
> jtag> initbus ejtag
> jtag> detectflash 0x000000000
> ejtag.c(217) EJCONTROL or EJIMPCODE register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> dev ID=0000   man ID=0000
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> ejtag.c(113) EJADDRESS, EJDATA or EJCONTROL register not found
> amd_detect: mid 0, did 0
> Flash not found!
> jtag>