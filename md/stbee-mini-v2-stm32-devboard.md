# About


STBee Mini v2 STM32 devboard

# Japan


I could not find this board outside of Japan, so a local friend helped me to get one.

# Pictures


From the manufacturer Strawberry Linux: <<https://strawberry-linux.com/images/stbee-mini-v2_top.jpg>  >  

[[=image https://strawberry-linux.com/images/stbee-mini-v2_top.jpg]]

# Lsusb



    $ lsusb
    Bus 001 Device 005: ID 0483:df11 STMicroelectronics STM Device in DFU Mode


# Dmesg



    [ 3427.465146] usb 1-1.2: new full-speed USB device number 14 using ehci-pci
    [ 3427.544934] usb 1-1.2: New USB device found, idVendor=0483, idProduct=df11, bcdDevice= 2.00
    [ 3427.544943] usb 1-1.2: New USB device strings: Mfr=1, Product=2, SerialNumber=3
    [ 3427.544948] usb 1-1.2: Product: STM32 DFU
    [ 3427.544953] usb 1-1.2: Manufacturer: STMicroelectronics
    [ 3427.544957] usb 1-1.2: SerialNumber: HÿjfqHWPBg


# Blink


The ArduinoIDE does not seem to support this board.

# Links


* <https://strawberry-linux.com/catalog/items?code=32105>  
* <https://stastaka.wordpress.com/2012/07/12/stbee-mini/>  
* <https://www.gniibe.org/memo/development/fst-01/dfu-consideration.html>  
* <http://miqn.net/stbee-mini%e3%82%92swd%e3%81%a7%e3%83%87%e3%83%90%e3%83%83%e3%82%b0/>  