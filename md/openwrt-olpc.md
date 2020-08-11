#  Step 1: Download the image


Download the ext2 image [here](http://downloads.openwrt.org/snapshots/olpc/openwrt-olpc-ext2.image) (52 MB).

#  Step 2: Copy it to your SD card with DD


dd if=openwrt-olpc-ext2.image of=/dev/sdc

# Step 3: Plug and Boot


## Via an USB card reader


I put the SD card into an USB card reader and connect it to the XO.

It boots the kernel, but it seems that the kernel fails to find the root partition sda2, maybe the device sda itself:

[[gallery size="small"]]
: 100_9942.jpg
: 100_9943.jpg
[[/gallery]]

## Via an SD card in the slot


It gives another error if you put the SD card directly in the SD card slot of the XO:

[[gallery size="small"]]
: Proper_SD_Card_Insertion.jpg
: 100_9947.jpg
[[/gallery]]

# Step 4: Try with the squashfs image


The [squashfs image](http://downloads.openwrt.org/snapshots/olpc/openwrt-olpc-squashfs.image) (with USB reader of via the SD card reader) gives the same errors.

# Step 5: Report a bug when it does not work


I have submitted a [bug report](https://dev.openwrt.org/ticket/4574) on the dev.openwrt.org system: Ticket #4574 (new defect) Kernel of the OLPC image on SD card does find the root partition on sda2.