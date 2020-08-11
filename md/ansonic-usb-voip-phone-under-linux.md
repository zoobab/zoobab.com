# Dmesg



    [38687.765145] input: Conwiseꂠꂠ chnology USB Device as /devices/pci0000:00/0000:00:1d.0/usb6/6-1/6-1:1.3/input/input24
    [38687.765241] generic-usb 0003:0E5E:6611.0006: input,hidraw1: USB HID v1.11 Device [Conwiseꂠꂠ chnology USB Device] on usb-0000:00:1d.0-1/input3
    [38687.794564] usbcore: registered new interface driver snd-usb-audio
    [38703.296548] usb 6-1: USB disconnect, address 6
    [38705.024143] usb 6-1: new full speed USB device using uhci_hcd and address 7
    [38705.200385] usb 6-1: configuration #1 chosen from 1 choice
    [38705.235361] input: Conwiseꂠꂠ chnology USB Device as /devices/pci0000:00/0000:00:1d.0/usb6/6-1/6-1:1.3/input/input25
    [38705.235538] generic-usb 0003:0E5E:6611.0007: input,hidraw1: USB HID v1.11 Device [Conwiseꂠꂠ chnology USB Device] on usb-0000:00:1d.0-1/input3
    [38707.232374] usb 6-1: USB disconnect, address 7
    [38707.233229] cannot submit datapipe for urb 0, error -19: no device
    [38707.508096] usb 6-1: new full speed USB device using uhci_hcd and address 8
    [38707.685580] usb 6-1: configuration #1 chosen from 1 choice
    [38707.726334] input: Conwiseꂠꂠ chnology USB Device as /devices/pci0000:00/0000:00:1d.0/usb6/6-1/6-1:1.3/input/input26
    [38707.726514] generic-usb 0003:0E5E:6611.0008: input,hidraw1: USB HID v1.11 Device [Conwiseꂠꂠ chnology USB Device] on usb-0000:00:1d.0-1/input3


# Lsusb


It does not show any name in the lsusb output, only the USB-ID 0e5e:6611 :


    zoobab@buzek /home/zoobab 14:55 # lsusb 
    Bus 004 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 007 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 006 Device 009: ID 0e5e:6611


# Pictures


[[image ansonic-usb-voip-phone.jpg]]

# Links


* <http://people.debian.org.tw/~chihchun/2006/11/28/hacking-lobos-lb-sp110/>  