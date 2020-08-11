# Pictures


[[=image chinese-usb-serial-adaptor.jpg]]

# Dmesg



    [102374.228119] usb 7-2: USB disconnect, address 3
    [102374.228523] ch341-uart ttyUSB0: ch341-uart converter now disconnected from ttyUSB0
    [102374.228559] ch341 7-2:1.0: device disconnected
    [102384.848105] usb 7-2: new full speed USB device using uhci_hcd and address 4
    [102385.014151] usb 7-2: configuration #1 chosen from 1 choice
    [102385.020340] ch341 7-2:1.0: ch341-uart converter detected
    [102385.033129] usb 7-2: ch341-uart converter now attached to ttyUSB0


# Lsmod



    zoobab@buzek:~$ lsmod | grep ch
    ch341                   8352  0 
    usbserial              36232  2 ch341,ftdi_sio


# Price


6.50EUR