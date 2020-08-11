# About


A USB board based on FT2232HL chip. I bought it for 7EUR.

[[=image ftdi-cjmcu-2232hl-90.jpg size="medium"]]

# Lsusb



    $ lsusb
    Bus 001 Device 007: ID 0403:6010 Future Technology Devices International, Ltd FT2232C/D/H Dual UART/FIFO IC



# Pinout


||~ left1 ||~ left2 ||~ right1 ||~ right2 ||
|| GND || 3V3 || GND || VCC ||
|| GND || 3V3 || GND || VCC ||
|| GND || 3V3 || CLK || CS ||
|| RST || AD0 || PWR || DAT ||
|| AD1 || AD2 || BC6 || BC7 ||
|| AD3 || 3V3 || 3V3 || BC5 ||
|| AD4 || AD5 || BC3 || BC4 ||
|| AD6 || AD7 || BC1 || BC2 ||
|| AC0 || AC1 || BD7 || BC0 ||
|| AC2 || AC3 || BD5 || BD6 ||
|| AC4 || 3V3 || 3V3 || BD4 ||
|| AC5 || AC6 || BD2 || BD3 ||
|| AC7 || SUS || BD0 || BD1 ||

# Voltage


3.3V or 5V?

# Linux gpio driver


Still have to find a working GPIO driver to address all the pins.

# Python driver


This driver should support it:

<https://github.com/eblot/pyftdi>  

But simple examples are hard to find, especially if you just want to toggle one pin.

# Links


* <https://github.com/unconfigured/ftdi_gpio>  
* <https://fr.aliexpress.com/item/CJMCU-2232-FT2232HL-USB-to-UART-FIFO-SPI-I2C-JTAG-RS232-module/32817939319.html>  