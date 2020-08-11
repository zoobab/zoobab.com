# Picture


[[image bdm4gdb_l.jpg]]

# Pinout


The BDM4JTAG has two connectors:

# 2x4 pins
# 2x8 pins

The 2x8 seems to be for PowerPC based devices.

# Standard JTAG pinout for PPC 4XX


|| TDO ||~ 1 ||~ 2 || NC ||
|| TDI ||~ 3 ||~ 4 || TRST ||
|| NC ||~ 5 ||~ 6 || VCC ||
|| TCK ||~ 7 ||~ 8 || NC ||
|| TMS ||~ 9 ||~ 10 || NC ||
|| SRESET ||~ 11 ||~ 12 || NC ||
|| NC ||~ 13 ||~ 14 || NC ||
|| NC ||~ 15 ||~ 16 || GND ||

# Urjtag


This cable seems to be supported by urjtag:


    jtag> help cable
    Usage: cable DRIVER [DRIVER_OPTS]
    Select JTAG cable type.
    
    DRIVER      name of cable
    DRIVER_OPTS options for the selected cable
    
    Type "cable DRIVER help" for info about options for cable DRIVER.
    
    List of supported cables:
    ARCOM         Arcom JTAG Cable
    ByteBlaster   Altera ByteBlaster/ByteBlaster II/ByteBlasterMV Parallel Port Download Cable
    UsbBlaster    Altera USB-Blaster Cable
    FT2232        Generic FTDI FT2232 Cable
    JTAGkey       Amontec JTAGkey (FT2232) Cable
    ARM-USB-OCD   Olimex ARM-USB-OCD[-TINY] (FT2232) Cable
    gnICE         Analog Devices Blackfin gnICE (FT2232) Cable (EXPERIMENTAL)
    OOCDLink-s    OOCDLink-s (FT2232) Cable (EXPERIMENTAL)
    Signalyzer    Xverve DT-USB-ST Signalyzer Tool (FT2232) Cable (EXPERIMENTAL)
    Turtelizer2   Turtelizer 2 Rev. B (FT2232) Cable (EXPERIMENTAL)
    USB-to-JTAG-IF USB to JTAG Interface (FT2232) Cable (EXPERIMENTAL)
    Flyswatter    TinCanTools Flyswatter (FT2232) Cable
    usbScarab2    KrisTech usbScarabeus2 (FT2232) Cable
    DLC5          Xilinx DLC5 JTAG Parallel Cable III
    EA253         ETC EA253 JTAG Cable
    EI012         ETC EI012 JTAG Cable
    IGLOO         Excelpoint IGLOO JTAG Cable
    KeithKoep     Keith & Koep JTAG cable
    Lattice       Lattice Parallel Port JTAG Cable
    MPCBDM        Mpcbdm JTAG cable
    TRITON        Ka-Ro TRITON Starterkit II (PXA255/250) JTAG Cable
    WIGGLER       Macraigor Wiggler JTAG Cable
    WIGGLER2      Modified (with CPU Reset) WIGGLER JTAG Cable
    xpc_int       Xilinx Platform Cable USB internal chain
    xpc_ext       Xilinx Platform Cable USB external chain
    jlink         Segger/IAR J-Link, Atmel SAM-ICE and others.
    jtag> cable MPCBDM help
    Usage: cable MPCBDM parallel PORTADDR
       or: cable MPCBDM ppdev PPDEV
    
    PORTADDR   parallel port address (e.g. 0x378)
    PPDEV      ppdev device (e.g. /dev/parport0)
    
    jtag>


# Links


* <http://www.bravekit.com/wiggler_arm_arm7_arm9_jtag_programmer_debugger_h-jtag_macraigor>  