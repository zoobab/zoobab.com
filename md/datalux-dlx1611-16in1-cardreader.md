# Pictures

[[=image hama-usb-2-0-card-reader.jpg]]

# Lsusb



    # lsusb 
    Bus 002 Device 084: ID 0dda:2005 Integrated Circuit Solution, Inc. Datalux DLX-1611 16in1 Card Reader


# SDHC support?


When I plug in an 8GB Compact Flash Kingston Elite Pro, here are the following kernel messages (Linux version 2.6.31-20-vserver (buildd@hassium) (gcc version 4.4.1 (Ubuntu 4.4.1-4ubuntu9) ) #58~ppa1-Ubuntu SMP Fri Mar 19 08:02:02 UTC 2010):

[[=image kingston-cf-8-gb-elite-pro-133.jpg]]


    [ 5872.712305] usb 2-1: new high speed USB device using ehci_hcd and address 35
    [ 5872.854523] usb 2-1: configuration #1 chosen from 1 choice
    [ 5872.855743] scsi163 : SCSI emulation for USB Mass Storage devices
    [ 5872.856049] usb-storage: device found at 35
    [ 5872.856054] usb-storage: waiting for device to settle before scanning
    [ 5877.856765] usb-storage: device scan complete
    [ 5877.858188] scsi 163:0:0:0: Direct-Access     Hama     CF  Card Reader  9323 PQ: 0 ANSI: 0
    [ 5877.963802] usb 2-1: USB disconnect, address 35
    [ 5877.964899] sd 163:0:0:0: Attached scsi generic sg1 type 0
    [ 5877.965478] sd 163:0:0:0: [sdb] READ CAPACITY failed
    [ 5877.965485] sd 163:0:0:0: [sdb] Result: hostbyte=DID_NO_CONNECT driverbyte=DRIVER_OK
    [ 5877.965495] sd 163:0:0:0: [sdb] Sense not available.
    [ 5877.965528] sd 163:0:0:0: [sdb] Write Protect is off
    [ 5877.965535] sd 163:0:0:0: [sdb] Mode Sense: 00 80 00 00
    [ 5877.965541] sd 163:0:0:0: [sdb] Assuming drive cache: write through
    [ 5877.965853] sd 163:0:0:0: [sdb] READ CAPACITY failed
    [ 5877.965859] sd 163:0:0:0: [sdb] Result: hostbyte=DID_NO_CONNECT driverbyte=DRIVER_OK
    [ 5877.965867] sd 163:0:0:0: [sdb] Sense not available.
    [ 5877.965896] sd 163:0:0:0: [sdb] Assuming drive cache: write through
    [ 5877.965903] sd 163:0:0:0: [sdb] Attached SCSI removable disk
    [ 5878.308291] usb 2-1: new high speed USB device using ehci_hcd and address 36
    [ 5878.446138] usb 2-1: configuration #1 chosen from 1 choice
    [ 5878.447083] scsi164 : SCSI emulation for USB Mass Storage devices
    [ 5878.447463] usb-storage: device found at 36
    [ 5878.447468] usb-storage: waiting for device to settle before scanning
