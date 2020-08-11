# Adafruit


Adafruit is selling a [clone of the Teensy](http://www.adafruit.com/index.php?main_page=product_info&cPath=42&products_id=296) board for 20USD, an arduino like which runs only over USB. Adafruit has more infos about his board [here](http://ladyada.net/products/atmega32u4breakout/).

[[=image atmega32u4_LRG.jpg size="medium"]]

# Lsusb


Plugging in the device on the USB shows an unknown device with a vendor ID of 239a and a product ID of 0001:


    zoobab@buzek /home/zoobab [48]$ lsusb 
    Bus 008 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 007 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 006 Device 004: ID 239a:0001  
    Bus 006 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 005 Device 002: ID 0a5c:5801 Broadcom Corp. BCM5880 Secure Applications Processor with fingerprint swipe sensor
    Bus 005 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 004 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 003 Device 006: ID 413c:8160 Dell Computer Corp. 
    Bus 003 Device 005: ID 413c:8162 Dell Computer Corp. 
    Bus 003 Device 004: ID 413c:8161 Dell Computer Corp. 
    Bus 003 Device 003: ID 0a5c:4500 Broadcom Corp. BCM2046B1 USB 2.0 Hub (part of BCM2046 Bluetooth)
    Bus 003 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 002 Device 005: ID 413c:8147 Dell Computer Corp. F3507g Mobile Broadband Module
    Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    zoobab@buzek /home/zoobab [49]$


# Dmesg


The device appears as an ACM serial device:


    [32936.502785] usb 6-1: new full speed USB device using uhci_hcd and address 5
    [32936.685451] cdc_acm 6-1:1.0: ttyACM0: USB ACM device


# Avrdude



    zoobab@buzek /home/zoobab [20]$ avrdude -p m32u4 -P /dev/ttyACM0 -c avr109
    
    Connecting to programmer: .
    Found programmer: Id = "LUFACDC"; type = S
        Software Version = 1.0; No Hardware Version given.
    Programmer supports auto addr increment.
    Programmer supports buffered memory access with buffersize=128 bytes.
    
    Programmer supports the following devices:
        Device code: 0x44
    
    avrdude: AVR device initialized and ready to accept instructions
    
    Reading | ################################################## | 100% 0.01s
    
    avrdude: Device signature = 0x1e9587
    
    avrdude: safemode: Fuses OK
    
    avrdude done.  Thank you.
    
    zoobab@buzek /home/zoobab [21]$


# Flash Opendous-jtag HEX file


There is an open source project named [Opendous-jtag](http://code.google.com/p/opendous-jtag/) to transform this device into a JTAG cable. They publish a binary HEX [opendous-jtag-atmeg32u4.hex](http://opendous-jtag.googlecode.com/files/opendous-jtag-atmeg32u4.hex) which is ready to be flashed:
 

    avrdude -p m32u4 -P /dev/ttyACM0 -c avr109 -u -U flash:w:opendous-jtag-atmeg32u4.hex


Once flashed, the device will not show up as a ttyACM device anymore.

There is a need to compile the special openocd for it:


    wget http://opendous-jtag.googlecode.com/files/openocd-0.4.0.opendous.estick.tar.bz2
    tar jxf openocd-0.4.0.opendous.estick.tar.bz2
    cd openocd-0.4.0.opendous.estick
    ./configure --prefix=/opt/arm --enable-opendous
    make 
    make install


# 3.3volts support?


Most of the JTAG lines are in 3.3v, while the device outputs 5v. Maybe there is a [way to run the chip in 3.3v](http://elasticsheep.com/2010/01/reading-an-sd-card-part-2-teensy-2-0/).