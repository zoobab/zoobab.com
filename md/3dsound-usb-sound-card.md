# Dmesg



    [46366.573049] input: USB  AUDIO   as /devices/pci0000:00/0000:00:1d.1/usb7/7-2/7-2:1.3/input/input20
    [46366.573171] generic-usb 0003:1130:F211.0009: input,hidraw0: USB HID v1.10 Device [USB  AUDIO  ] on usb-0000:00:1d.1-2/input3
    [46366.576415] input: USB  AUDIO   as /devices/pci0000:00/0000:00:1d.1/usb7/7-2/7-2:1.4/input/input21
    [46366.576541] generic-usb 0003:1130:F211.000A: input,hidraw1: USB HID v1.10 Device [USB  AUDIO  ] on usb-0000:00:1d.1-2/input4
    [46367.172061] 18:1:1: endpoint lacks sample rate attribute bit, cannot set.
    [46367.175058] 18:2:1: endpoint lacks sample rate attribute bit, cannot set.
    [46367.189062] 18:2:1: endpoint lacks sample rate attribute bit, cannot set.
    [46367.194068] 18:1:1: endpoint lacks sample rate attribute bit, cannot set.
    [46367.215082] 18:2:1: endpoint lacks sample rate attribute bit, cannot set.


# Lsusb



    Bus 007 Device 017: ID 1130:f211 Tenx Technology, Inc. TP6911 Audio Headset


# Lsusb -v



    Bus 007 Device 017: ID 1130:f211 Tenx Technology, Inc. TP6911 Audio Headset
    Device Descriptor:
      bLength                18
      bDescriptorType         1
      bcdUSB               1.10
      bDeviceClass            0 (Defined at Interface level)
      bDeviceSubClass         0 
      bDeviceProtocol         0 
      bMaxPacketSize0         8
      idVendor           0x1130 Tenx Technology, Inc.
      idProduct          0xf211 TP6911 Audio Headset
      bcdDevice            5.10
      iManufacturer           0 
      iProduct                2 USB  AUDIO  
      iSerial                 0 
      bNumConfigurations      1
      Configuration Descriptor:
        bLength                 9
        bDescriptorType         2
        wTotalLength          243
        bNumInterfaces          5
        bConfigurationValue     1
        iConfiguration          0 
        bmAttributes         0x80
          (Bus Powered)
        MaxPower              500mA
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        0
          bAlternateSetting       0
          bNumEndpoints           0
          bInterfaceClass         1 Audio
          bInterfaceSubClass      1 Control Device
          bInterfaceProtocol      0 
          iInterface              0 
          AudioControl Interface Descriptor:
            bLength                10
            bDescriptorType        36
            bDescriptorSubtype      1 (HEADER)
            bcdADC               1.00
            wTotalLength           71
            bInCollection           2
            baInterfaceNr( 0)       1
            baInterfaceNr( 1)       2
          AudioControl Interface Descriptor:
            bLength                12
            bDescriptorType        36
            bDescriptorSubtype      2 (INPUT_TERMINAL)
            bTerminalID             1
            wTerminalType      0x0101 USB Streaming
            bAssocTerminal          0
            bNrChannels             2
            wChannelConfig     0x0003
              Left Front (L)
              Right Front (R)
            iChannelNames           0 
            iTerminal               0 
          AudioControl Interface Descriptor:
            bLength                10
            bDescriptorType        36
            bDescriptorSubtype      6 (FEATURE_UNIT)
            bUnitID                 2
            bSourceID               1
            bControlSize            1
            bmaControls( 0)      0x01
              Mute
            bmaControls( 1)      0x02
              Volume
            bmaControls( 2)      0x02
              Volume
            iFeature                0 
          AudioControl Interface Descriptor:
            bLength                 9
            bDescriptorType        36
            bDescriptorSubtype      3 (OUTPUT_TERMINAL)
            bTerminalID             3
            wTerminalType      0x0301 Speaker
            bAssocTerminal          0
            bSourceID               2
            iTerminal               0 
          AudioControl Interface Descriptor:
            bLength                12
            bDescriptorType        36
            bDescriptorSubtype      2 (INPUT_TERMINAL)
            bTerminalID             4
            wTerminalType      0x0201 Microphone
            bAssocTerminal          0
            bNrChannels             1
            wChannelConfig     0x0001
              Left Front (L)
            iChannelNames           0 
            iTerminal               0 
          AudioControl Interface Descriptor:
            bLength                 9
            bDescriptorType        36
            bDescriptorSubtype      6 (FEATURE_UNIT)
            bUnitID                 5
            bSourceID               4
            bControlSize            1
            bmaControls( 0)      0x01
              Mute
            bmaControls( 1)      0x02
              Volume
            iFeature                0 
          AudioControl Interface Descriptor:
            bLength                 9
            bDescriptorType        36
            bDescriptorSubtype      3 (OUTPUT_TERMINAL)
            bTerminalID             6
            wTerminalType      0x0101 USB Streaming
            bAssocTerminal          0
            bSourceID               5
            iTerminal               0 
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        1
          bAlternateSetting       0
          bNumEndpoints           0
          bInterfaceClass         1 Audio
          bInterfaceSubClass      2 Streaming
          bInterfaceProtocol      0 
          iInterface              0 
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        1
          bAlternateSetting       1
          bNumEndpoints           1
          bInterfaceClass         1 Audio
          bInterfaceSubClass      2 Streaming
          bInterfaceProtocol      0 
          iInterface              0 
          AudioStreaming Interface Descriptor:
            bLength                 7
            bDescriptorType        36
            bDescriptorSubtype      1 (AS_GENERAL)
            bTerminalLink           1
            bDelay                  1 frames
            wFormatTag              1 PCM
          AudioStreaming Interface Descriptor:
            bLength                11
            bDescriptorType        36
            bDescriptorSubtype      2 (FORMAT_TYPE)
            bFormatType             1 (FORMAT_TYPE_I)
            bNrChannels             2
            bSubframeSize           2
            bBitResolution         16
            bSamFreqType            1 Discrete
            tSamFreq[ 0]        48000
          Endpoint Descriptor:
            bLength                 9
            bDescriptorType         5
            bEndpointAddress     0x01  EP 1 OUT
            bmAttributes            9
              Transfer Type            Isochronous
              Synch Type               Adaptive
              Usage Type               Data
            wMaxPacketSize     0x00c0  1x 192 bytes
            bInterval               1
            bRefresh                0
            bSynchAddress           0
            AudioControl Endpoint Descriptor:
              bLength                 7
              bDescriptorType        37
              bDescriptorSubtype      1 (EP_GENERAL)
              bmAttributes         0x00
              bLockDelayUnits         0 Undefined
              wLockDelay              0 Undefined
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        2
          bAlternateSetting       0
          bNumEndpoints           0
          bInterfaceClass         1 Audio
          bInterfaceSubClass      2 Streaming
          bInterfaceProtocol      0 
          iInterface              0 
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        2
          bAlternateSetting       1
          bNumEndpoints           1
          bInterfaceClass         1 Audio
          bInterfaceSubClass      2 Streaming
          bInterfaceProtocol      0 
          iInterface              0 
          AudioStreaming Interface Descriptor:
            bLength                 7
            bDescriptorType        36
            bDescriptorSubtype      1 (AS_GENERAL)
            bTerminalLink           6
            bDelay                  1 frames
            wFormatTag              1 PCM
          AudioStreaming Interface Descriptor:
            bLength                11
            bDescriptorType        36
            bDescriptorSubtype      2 (FORMAT_TYPE)
            bFormatType             1 (FORMAT_TYPE_I)
            bNrChannels             1
            bSubframeSize           2
            bBitResolution         16
            bSamFreqType            1 Discrete
            tSamFreq[ 0]        24000
          Endpoint Descriptor:
            bLength                 9
            bDescriptorType         5
            bEndpointAddress     0x83  EP 3 IN
            bmAttributes            9
              Transfer Type            Isochronous
              Synch Type               Adaptive
              Usage Type               Data
            wMaxPacketSize     0x0030  1x 48 bytes
            bInterval               1
            bRefresh                0
            bSynchAddress           0
            AudioControl Endpoint Descriptor:
              bLength                 7
              bDescriptorType        37
              bDescriptorSubtype      1 (EP_GENERAL)
              bmAttributes         0x00
              bLockDelayUnits         0 Undefined
              wLockDelay              0 Undefined
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        3
          bAlternateSetting       0
          bNumEndpoints           1
          bInterfaceClass         3 Human Interface Device
          bInterfaceSubClass      1 Boot Interface Subclass
          bInterfaceProtocol      1 Keyboard
          iInterface              0 
            HID Device Descriptor:
              bLength                 9
              bDescriptorType        33
              bcdHID               1.10
              bCountryCode           33 US
              bNumDescriptors         1
              bDescriptorType        34 Report
              wDescriptorLength      41
             Report Descriptors: 
               ** UNAVAILABLE **
          Endpoint Descriptor:
            bLength                 7
            bDescriptorType         5
            bEndpointAddress     0x82  EP 2 IN
            bmAttributes            3
              Transfer Type            Interrupt
              Synch Type               None
              Usage Type               Data
            wMaxPacketSize     0x0008  1x 8 bytes
            bInterval              10
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        4
          bAlternateSetting       0
          bNumEndpoints           1
          bInterfaceClass         3 Human Interface Device
          bInterfaceSubClass      1 Boot Interface Subclass
          bInterfaceProtocol      1 Keyboard
          iInterface              0 
            HID Device Descriptor:
              bLength                 9
              bDescriptorType        33
              bcdHID               1.10
              bCountryCode           33 US
              bNumDescriptors         1
              bDescriptorType        34 Report
              wDescriptorLength      35
             Report Descriptors: 
               ** UNAVAILABLE **
          Endpoint Descriptor:
            bLength                 7
            bDescriptorType         5
            bEndpointAddress     0x84  EP 4 IN
            bmAttributes            3
              Transfer Type            Interrupt
              Synch Type               None
              Usage Type               Data
            wMaxPacketSize     0x0008  1x 8 bytes
            bInterval              10
    Device Status:     0x0000
      (Bus Powered)
