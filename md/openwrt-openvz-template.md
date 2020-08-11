# About


This page describes my attempt to run OpenWRT rootfs inside OpenVZ.

# Download


Download the openwrt-x86-generic-rootfs.tar.gz in the template directory, and run something like:


    root@trogir /vz/template/cache [80]# vzctl create 103 --ostemplate openwrt-x86-generic-rootfs
    Creating container private area (openwrt-x86-generic-rootfs)
    Warning: configuration file for distribution openwrt-x86-generic-rootfs not found, using defaults from /etc/vz/dists/default
    Performing postcreate actions
    CT configuration saved to /etc/vz/conf/103.conf
    Container private area was created
    root@trogir /vz/template/cache [81]# vzctl start 103
    Warning: configuration file for distribution openwrt-x86-generic-rootfs not found, using defaults from /etc/vz/dists/default
    Starting container ...
    Container is mounted
    Setting CPU units: 1000
    Container start in progress...
    root@trogir /vz/template/cache [82]#


# Fix the pts issue



    root@trogir /etc/vz/dists/scripts [71]# vzctl enter 102
    enter into CT 102 failed
    Unable to open pty: No such file or directory
    root@trogir /etc/vz/dists/scripts [72]# vzctl exec 102 mkdir -p /dev/pts
    root@trogir /etc/vz/dists/scripts [73]# vzctl exec 102  mount -t devpts none /dev/pts
    root@trogir /etc/vz/dists/scripts [74]# vzctl enter 102
    entered into CT 102
      _______                     ________        __
     |       |.-----.-----.-----.|  |  |  |.----.|  |_
     |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
     |_______||   __|_____|__|__||________||__|  |____|
              |__| W I R E L E S S   F R E E D O M
     -----------------------------------------------------
     ATTITUDE ADJUSTMENT (0.4, r31852)
     -----------------------------------------------------
      * 1/4 oz Vodka      Pour all ingredients into mixing
      * 1/4 oz Gin        tin with ice, strain into glass.
      * 1/4 oz Amaretto
      * 1/4 oz Triple sec
      * 1/4 oz Peach schnapps
      * 1/4 oz Sour mix
      * 1 splash Cranberry juice
     -----------------------------------------------------
    root@OpenWrt:/#


# Scripts


You can find more about it here: <https://github.com/zoobab/openwrt-openvz>  