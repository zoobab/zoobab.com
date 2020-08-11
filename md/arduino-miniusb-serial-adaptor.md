# Introduction


Many shops selling the Arduino also sell some kind of the USB serial adaptor named the "Mini USB Adapter". It is based on the FT232RL, which is used to make the USB to serial conversion. This adaptor can be used as a USB-serial adaptor for having the serial console of many routers, such as La [[[Fonera]]].

# Warning


While some routers has been tolerant to 5v input, it is dangerous to connect such 5v TX pins to a router which accepts 3.3v.

# Pictures


[[gallery]]

# Kernel messages


When you plug it in, here are the kernel messages:


    [   74.316066] usb 6-1: new full speed USB device using uhci_hcd and address 4
    [   74.509490] usb 6-1: configuration #1 chosen from 1 choice
    [   74.513157] ftdi_sio 6-1:1.0: FTDI USB Serial Device converter detected
    [   74.515847] usb 6-1: Detected FT232RL
    [   74.515909] usb 6-1: FTDI USB Serial Device converter now attached to ttyUSB0


# Usage of the jumper


When searching on the internet, it is unclear what is the role of the jumper. Initially, I thought this was to swicth between 5v and 3.3v, but this is actually not the case. Instead, the jumper is used to enable/disable the 5V power coming from the USB.

# Links


* <http://arduino.cc/en/Main/MiniUSB>  
* <http://hackerspace.be/SerialAdaptor-3.3v5v>  
* <http://www.tektonica.com/?category=3&product_id=16>  
* <http://www.droids.it/data_sheets/990.004%20datasheet.pdf>  