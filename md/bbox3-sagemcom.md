# Source code


Source code is published here:

<http://www.opensource-code.com/belgacom/>  

And I made a mirror here:

<http://filez.zoobab.com/openwrt/bbox3/mirrors/>  


    This file contains information about Opensource delivery for BBox3 project.
    
    The archive OpenSource_delivery_BBox3_ed5.tar.gz contains:
    - a directory modules that contains all modules under GPLv2 used in BBox3 distribution
    - a directory broadcom-kernel-3865b that contains the kernel used in BBox3
    - a directory openwrt that contains the system builder used to generate an image
    - a script install.sh
    
    
    In order to generate an image, do:
    $ ./install.sh
    
    This commande will populate the openwrt tree with files contained in modules
    Then, do:
    $ cd openwrt
    $ make menuconfig
    $ make world
    
    The generated image will be in bin/sagemcom/


# Sagemcom F@ST 3864


The Bbox3 is in fast a rebranded Sagemcom F@ST 3864b, as the file [boardparms.c](http://filez.zoobab.com/openwrt/bbox3/mirrors/OpenSource_delivery_BBox3/broadcom-kernel-3865b/bcm963xx/shared/opensource/boardparms/bcm963xx/boardparms.c) made by Broadcom  tell us:


    //The board profile for 3865b hardware (bbox3 belgacom)
    static bp_elem_t g_FAST3865b[] = {
      {bp_cpBoardId ,              .u.cp = "F@ST3865b"},
      {bp_ulDeviceOptions,         .u.ul = BP_DEVICE_OPTION_ENABLE_GMAC },
      {bp_ulGpioOverlay,           .u.ul =(
                                           BP_OVERLAY_PHY |
                                           BP_OVERLAY_SERIAL_LEDS |
                                           BP_OVERLAY_USB_DEVICE)},
    #ifndef SCOS_SUPPORT
      {bp_usGpioLedAdsl,           .u.us = BP_SERIAL_GPIO_4_AL},
      {bp_usGpioLedAdslFail,       .u.us = BP_SERIAL_GPIO_5_AL},
      //{bp_usGpioLedSesWireless,    .u.us = },                     //WPS set up LED
      {bp_usGpioLedWanData,        .u.us = BP_SERIAL_GPIO_6_AL},
      {bp_usGpioLedWanError,       .u.us = BP_SERIAL_GPIO_2_AL},
      {bp_usGpioLedBlPowerOn,      .u.us = BP_GPIO_20_AL},
      //{bp_usGpioLedBlStop,         .u.us = BP_GPIO_21_AL},
      {bp_usExtIntrResetToDefault, .u.us = BP_EXT_INTR_0},
      {bp_usExtIntrSesBtnWireless, .u.us = BP_EXT_INTR_1},
      {bp_usExtIntrWlanOnoff, .u.us = BP_EXT_INTR_2},
      {bp_usGpioEcoEnableBtn, .u.us = BP_GPIO_39_AL},
    #endif
      {bp_usAntInUseWireless,      .u.us = BP_WLAN_ANT_MAIN},
      {bp_usWirelessFlags,         .u.us = 0},
    
    
    // +----------------------+
    // |  PHY1      -- port 0 | not connected
    // |  PHY2      -- port 1 | not connected
    // |  PHY3      -- port 2 | not connected
    // |                      | 
    // |  GPHY1     -- port 3 |-----------------------------------------------------------  WAN
    // |                      |                  +-------------------+
    // |  RGMII 1   -- port 4 |------------------| IMP               |
    // |  RGMII 2 * -- port 5 |                  |                   |
    // |  RGMII 3   -- port 6 | not connected    | GPHY0 (not exist) |
    // |  RGMII 4 * -- port 7 |                  | GPHY1             |-------------------- LAN
    // |                      |                  | GPHY2             |-------------------- LAN
    // |        bcm63168      |                  | GPHY3             |-------------------- LAN
    // +----------------------+                  | GPHY4             |-------------------- LAN
    //                                           | RGMII -- port 5   |-------------------- LAN (Quantenna)
    //                                           |                   |
    //                                           |   Switch 53124S   |
    //                                           +-------------------+ 
    //  * (not available on 63168)
    // ---------------------------
