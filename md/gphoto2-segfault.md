
    zoobab@sabayonx86-64 /home/zoobab/bak/mtk6577 [128]$ gphoto2 --get-all-files --force-overwrite
    Saving file as 1450520904017.jpg                                               
                                                                                   
    *** Error ***              
    PTP I/O Error
    *** Error (-7: 'I/O problem') ***       
    
    For debugging messages, please use the --debug option.
    Debugging messages may help finding a solution to your problem.
    If you intend to send any error or debug messages to the gphoto
    developer mailing list <gphoto-devel@lists.sourceforge.net>, please run
    gphoto2 as follows:
    
        env LANG=C gphoto2 --debug --debug-logfile=my-logfile.txt --get-all-files --force-overwrite
    
    Please make sure there is sufficient quoting around the arguments.
    
    *** Error in `gphoto2': corrupted double-linked list: 0x0000557637693da0 ***
    ======= Backtrace: =========
    /lib64/libc.so.6(+0x77a17)[0x7fd70e820a17]
    /lib64/libc.so.6(+0x7d897)[0x7fd70e826897]
    /lib64/libc.so.6(+0x7e8fa)[0x7fd70e8278fa]
    /lib64/libusb-1.0.so.0(libusb_free_transfer+0x1d)[0x7fd706766e9d]
    /usr/lib64/libgphoto2_port/0.12.0/usb1.so(+0x236e)[0x7fd70697836e]
    /lib64/libusb-1.0.so.0(+0x9a78)[0x7fd706767a78]
    /lib64/libusb-1.0.so.0(+0xac0c)[0x7fd706768c0c]
    /lib64/libusb-1.0.so.0(+0xee22)[0x7fd70676ce22]
    /lib64/libusb-1.0.so.0(+0x9719)[0x7fd706767719]
    /lib64/libusb-1.0.so.0(libusb_handle_events_timeout_completed+0xb7)[0x7fd7067683f7]
    /lib64/libusb-1.0.so.0(libusb_handle_events+0x1f)[0x7fd7067684ef]
    /usr/lib64/libgphoto2_port/0.12.0/usb1.so(+0x1bd5)[0x7fd706977bd5]
    /usr/lib/libgphoto2_port.so.12(gp_port_close+0x6c)[0x7fd70f894dbc]
    /usr/lib/libgphoto2.so.6(gp_camera_exit+0xc7)[0x7fd70faa7237]
    /usr/lib/libgphoto2.so.6(gp_camera_free+0x72)[0x7fd70faa7462]
    /usr/lib/libgphoto2.so.6(gp_camera_unref+0x75)[0x7fd70faa76f5]
    gphoto2(+0x1168e)[0x55763588e68e]
    gphoto2(+0x833a)[0x55763588533a]
    /lib64/libc.so.6(__libc_start_main+0x114)[0x7fd70e7c9a94]
    gphoto2(+0x90ad)[0x5576358860ad]
    ======= Memory map: ========
    55763587d000-55763589c000 r-xp 00000000 08:01 8264124                    /usr/bin/gphoto2
    557635a9c000-557635a9d000 r--p 0001f000 08:01 8264124                    /usr/bin/gphoto2
    557635a9d000-557635a9e000 rw-p 00020000 08:01 8264124                    /usr/bin/gphoto2
    557635a9e000-557635aa2000 rw-p 00000000 00:00 0 
    557637656000-5576376dc000 rw-p 00000000 00:00 0                          [heap]
    7fd6fc000000-7fd6fc021000 rw-p 00000000 00:00 0 
    7fd6fc021000-7fd700000000 ---p 00000000 00:00 0 
    7fd700d8e000-7fd702644000 r-xp 00000000 08:01 4734398                    /usr/lib64/libicudata.so.55.1
    7fd702644000-7fd702843000 ---p 018b6000 08:01 4734398                    /usr/lib64/libicudata.so.55.1
    7fd702843000-7fd702844000 r--p 018b5000 08:01 4734398                    /usr/lib64/libicudata.so.55.1
    7fd702844000-7fd702845000 rw-p 018b6000 08:01 4734398                    /usr/lib64/libicudata.so.55.1
    7fd702ec0000-7fd702ed6000 r-xp 00000000 08:01 5243623                    /usr/lib64/gcc/x86_64-pc-linux-gnu/4.9.3/libgcc_s.so.1
    7fd702ed6000-7fd7030d5000 ---p 00016000 08:01 5243623                    /usr/lib64/gcc/x86_64-pc-linux-gnu/4.9.3/libgcc_s.so.1
    7fd7030d5000-7fd7030d6000 r--p 00015000 08:01 5243623                    /usr/lib64/gcc/x86_64-pc-linux-gnu/4.9.3/libgcc_s.so.1
    7fd7030d6000-7fd7030d7000 rw-p 00016000 08:01 5243623                    /usr/lib64/gcc/x86_64-pc-linux-gnu/4.9.3/libgcc_s.so.1
    7fd7030d7000-7fd7031e6000 r-xp 00000000 08:01 5243629                    /usr/lib64/gcc/x86_64-pc-linux-gnu/4.9.3/libstdc++.so.6.0.20
    7fd7031e6000-7fd7033e5000 ---p 0010f000 08:01 5243629                    /usr/lib64/gcc/x86_64-pc-linux-gnu/4.9.3/libstdc++.so.6.0.20
    7fd7033e5000-7fd7033ef000 r--p 0010e000 08:01 5243629                    /usr/lib64/gcc/x86_64-pc-linux-gnu/4.9.3/libstdc++.so.6.0.20
    7fd7033ef000-7fd7033f0000 rw-p 00118000 08:01 5243629                    /usr/lib64/gcc/x86_64-pc-linux-gnu/4.9.3/libstdc++.so.6.0.20
    7fd7033f0000-7fd703405000 rw-p 00000000 00:00 0 
    7fd70486f000-7fd704884000 r-xp 00000000 08:01 8264257                    /lib64/libz.so.1.2.8
    7fd704884000-7fd704a83000 ---p 00015000 08:01 8264257                    /lib64/libz.so.1.2.8
    7fd704a83000-7fd704a84000 r--p 00014000 08:01 8264257                    /lib64/libz.so.1.2.8
    7fd704a84000-7fd704a85000 rw-p 00015000 08:01 8264257                    /lib64/libz.so.1.2.8
    7fd704a85000-7fd704c2d000 r-xp 00000000 08:01 4734405                    /usr/lib64/libicuuc.so.55.1
    7fd704c2d000-7fd704e2c000 ---p 001a8000 08:01 4734405                    /usr/lib64/libicuuc.so.55.1
    7fd704e2c000-7fd704e3e000 r--p 001a7000 08:01 4734405                    /usr/lib64/libicuuc.so.55.1
    7fd704e3e000-7fd704e3f000 rw-p 001b9000 08:01 4734405                    /usr/lib64/libicuuc.so.55.1
    7fd704e3f000-7fd704e43000 rw-p 00000000 00:00 0 
    7fd704e43000-7fd7050e9000 r-xp 00000000 08:01 4734399                    /usr/lib64/libicui18n.so.55.1
    7fd7050e9000-7fd7052e8000 ---p 002a6000 08:01 4734399                    /usr/lib64/libicui18n.so.55.1
    7fd7052e8000-7fd7052fa000 r--p 002a5000 08:01 4734399                    /usr/lib64/libicui18n.so.55.1
    7fd7052fa000-7fd7052fb000 rw-p 002b7000 08:01 4734399                    /usr/lib64/libicui18n.so.55.1
    7fd7052fb000-7fd705478000 r-xp 00000000 08:01 4734906                    /usr/lib64/libxml2.so.2.9.2
    7fd705478000-7fd705677000 ---p 0017d000 08:01 4734906                    /usr/lib64/libxml2.so.2.9.2
    7fd705677000-7fd705680000 r--p 0017c000 08:01 4734906                    /usr/lib64/libxml2.so.2.9.2
    7fd705680000-7fd705682000 rw-p 00185000 08:01 4734906                    /usr/lib64/libxml2.so.2.9.2
    7fd705682000-7fd705683000 rw-p 00000000 00:00 0 
    7fd705683000-7fd705729000 r-xp 00000000 08:01 8920557                    /usr/lib64/libgphoto2/2.5.8/ptp2.so
    7fd705729000-7fd705929000 ---p 000a6000 08:01 8920557                    /usr/lib64/libgphoto2/2.5.8/ptp2.so
    7fd705929000-7fd705937000 r--p 000a6000 08:01 8920557                    /usr/lib64/libgphoto2/2.5.8/ptp2.so
    
    7fd705937000-7fd705948000 rw-p 000b4000 08:01 8920557                    /usr/lib64/libgphoto2/2.5.8/ptp2.so
    7fd705948000-7fd705949000 ---p 00000000 00:00 0 
    7fd705949000-7fd706149000 rw-p 00000000 00:00 0                          [stack:30955]
    7fd706149000-7fd70614e000 r-xp 00000000 08:01 8126694                    /lib64/libattr.so.1.1.0
    7fd70614e000-7fd70634d000 ---p 00005000 08:01 8126694                    /lib64/libattr.so.1.1.0
    7fd70634d000-7fd70634e000 r--p 00004000 08:01 8126694                    /lib64/libattr.so.1.1.0
    7fd70634e000-7fd70634f000 rw-p 00005000 08:01 8126694                    /lib64/libattr.so.1.1.0
    7fd70634f000-7fd706354000 r-xp 00000000 08:01 8126698                    /lib64/libcap.so.2.24
    7fd706354000-7fd706554000 ---p 00005000 08:01 8126698                    /lib64/libcap.so.2.24
    7fd706554000-7fd706555000 r--p 00005000 08:01 8126698                    /lib64/libcap.so.2.24
    7fd706555000-7fd706556000 rw-p 00006000 08:01 8126698                    /lib64/libcap.so.2.24
    7fd706556000-7fd70655d000 r-xp 00000000 08:01 12059139                   /lib64/librt-2.21.so
    7fd70655d000-7fd70675c000 ---p 00007000 08:01 12059139                   /lib64/librt-2.21.so
    7fd70675c000-7fd70675d000 r--p 00006000 08:01 12059139                   /lib64/librt-2.21.so
    7fd70675d000-7fd70675e000 rw-p 00007000 08:01 12059139                   /lib64/librt-2.21.so
    7fd70675e000-7fd706775000 r-xp 00000000 08:01 8126762                    /lib64/libusb-1.0.so.0.1.0
    7fd706775000-7fd706974000 ---p 00017000 08:01 8126762                    /lib64/libusb-1.0.so.0.1.0
    7fd706974000-7fd706975000 r--p 00016000 08:01 8126762                    /lib64/libusb-1.0.so.0.1.0
    7fd706975000-7fd706976000 rw-p 00017000 08:01 8126762                    /lib64/libusb-1.0.so.0.1.0
    7fd706976000-7fd70697d000 r-xp 00000000 08:01 8920583                    /usr/lib64/libgphoto2_port/0.12.0/usb1.so
    7fd70697d000-7fd706b7d000 ---p 00007000 08:01 8920583                    /usr/lib64/libgphoto2_port/0.12.0/usb1.so
    7fd706b7d000-7fd706b7e000 r--p 00007000 08:01 8920583                    /usr/lib64/libgphoto2_port/0.12.0/usb1.so
    7fd706b7e000-7fd706b7f000 rw-p 00008000 08:01 8920583                    /usr/lib64/libgphoto2_port/0.12.0/usb1.so
    7fd706b7f000-7fd70d0b0000 r--p 00000000 08:01 5112473                    /usr/lib64/locale/locale-archive
    7fd70d0b0000-7fd70d0c0000 r-xp 00000000 08:01 4734049                    /usr/lib64/libbsd.so.0.7.0
    7fd70d0c0000-7fd70d2bf000 ---p 00010000 08:01 4734049                    /usr/lib64/libbsd.so.0.7.0
    7fd70d2bf000-7fd70d2c0000 r--p 0000f000 08:01 4734049                    /usr/lib64/libbsd.so.0.7.0
    7fd70d2c0000-7fd70d2c1000 rw-p 00010000 08:01 4734049                    /usr/lib64/libbsd.so.0.7.0
    7fd70d2c1000-7fd70d2c2000 rw-p 00000000 00:00 0 
    7fd70d2c2000-7fd70d2c7000 r-xp 00000000 08:01 8258904                    /usr/lib64/libXdmcp.so.6.0.0
    7fd70d2c7000-7fd70d4c6000 ---p 00005000 08:01 8258904                    /usr/lib64/libXdmcp.so.6.0.0
    7fd70d4c6000-7fd70d4c7000 r--p 00004000 08:01 8258904                    /usr/lib64/libXdmcp.so.6.0.0
    7fd70d4c7000-7fd70d4c8000 rw-p 00005000 08:01 8258904                    /usr/lib64/libXdmcp.so.6.0.0
    7fd70d4c8000-7fd70d4cb000 r-xp 00000000 08:01 4733918                    /usr/lib64/libXau.so.6.0.0
    7fd70d4cb000-7fd70d6ca000 ---p 00003000 08:01 4733918                    /usr/lib64/libXau.so.6.0.0
    7fd70d6ca000-7fd70d6cb000 r--p 00002000 08:01 4733918                    /usr/lib64/libXau.so.6.0.0
    7fd70d6cb000-7fd70d6cc000 rw-p 00003000 08:01 4733918                    /usr/lib64/libXau.so.6.0.0
    7fd70d6cc000-7fd70d6f4000 r-xp 00000000 08:01 13386425                   /usr/lib64/libxcb.so.1.1.0
    7fd70d6f4000-7fd70d8f3000 ---p 00028000 08:01 13386425                   /usr/lib64/libxcb.so.1.1.0
    7fd70d8f3000-7fd70d8f4000 r--p 00027000 08:01 13386425                   /usr/lib64/libxcb.so.1.1.0
    7fd70d8f4000-7fd70d8f5000 rw-p 00028000 08:01 13386425                   /usr/lib64/libxcb.so.1.1.0
    7fd70d8f5000-7fd70d94d000 r-xp 00000000 08:01 8339801                    /lib64/libncurses.so.6.0
    7fd70d94d000-7fd70db4d000 ---p 00058000 08:01 8339801                    /lib64/libncurses.so.6.0
    7fd70db4d000-7fd70db51000 r--p 00058000 08:01 8339801                    /lib64/libncurses.so.6.0
    7fd70db51000-7fd70db52000 rw-p 0005c000 08:01 8339801                    /lib64/libncurses.so.6.0
    7fd70db52000-7fd70db53000 rw-p 00000000 00:00 0 
    7fd70db53000-7fd70db58000 r-xp 00000000 08:01 8265135                    /lib64/libgpm.so.1.20.0
    7fd70db58000-7fd70dd57000 ---p 00005000 08:01 8265135                    /lib64/libgpm.so.1.20.0
    7fd70dd57000-7fd70dd58000 r--p 00004000 08:01 8265135                    /lib64/libgpm.so.1.20.0
    7fd70dd58000-7fd70dd59000 rw-p 00005000 08:01 8265135                    /lib64/libgpm.so.1.20.0
    7fd70dd59000-7fd70de90000 r-xp 00000000 08:01 4733916                    /usr/lib64/libX11.so.6.3.0
    7fd70de90000-7fd70e090000 ---p 00137000 08:01 4733916                    /usr/lib64/libX11.so.6.3.0
    7fd70e090000-7fd70e091000 r--p 00137000 08:01 4733916                    /usr/lib64/libX11.so.6.3.0
    7fd70e091000-7fd70e096000 rw-p 00138000 08:01 4733916                    /usr/lib64/libX11.so.6.3.0
    7fd70e096000-7fd70e199000 r-xp 00000000 08:01 12059115                   /lib64/libm-2.21.so
    7fd70e199000-7fd70e398000 ---p 00103000 08:01 12059115                   /lib64/libm-2.21.so
    7fd70e398000-7fd70e399000 r--p 00102000 08:01 12059115                   /lib64/libm-2.21.so
    7fd70e399000-7fd70e39a000 rw-p 00103000 08:01 12059115                   /lib64/libm-2.21.so
    7fd70e39a000-7fd70e39c000 r-xp 00000000 08:01 12059113                   /lib64/libdl-2.21.so
    7fd70e39c000-7fd70e59c000 ---p 00002000 08:01 12059113                   /lib64/libdl-2.21.so
    7fd70e59c000-7fd70e59d000 r--p 00002000 08:01 12059113                   /lib64/libdl-2.21.so
    7fd70e59d000-7fd70e59e000 rw-p 00003000 08:01 12059113                   /lib64/libdl-2.21.so
    7fd70e59e000-7fd70e5a8000 r-xp 00000000 08:01 4734464                    /usr/lib64/libltdl.so.7.3.1
    7fd70e5a8000-7fd70e7a7000 ---p 0000a000 08:01 4734464                    /usr/lib64/libltdl.so.7.3.1
    7fd70e7a7000-7fd70e7a8000 r--p 00009000 08:01 4734464                    /usr/lib64/libltdl.so.7.3.1
    7fd70e7a8000-7fd70e7a9000 rw-p 0000a000 08:01 4734464                    /usr/lib64/libltdl.so.7.3.1
    7fd70e7a9000-7fd70e94f000 r-xp 00000000 08:01 12059107                   /lib64/libc-2.21.so
    7fd70e94f000-7fd70eb4e000 ---p 001a6000 08:01 12059107                   /lib64/libc-2.21.so
    7fd70eb4e000-7fd70eb52000 r--p 001a5000 08:01 12059107                   /lib64/libc-2.21.so
    7fd70eb52000-7fd70eb54000 rw-p 001a9000 08:01 12059107                   /lib64/libc-2.21.so
    7fd70eb54000-7fd70eb59000 rw-p 00000000 00:00 0 
    7fd70eb59000-7fd70eb64000 r-xp 00000000 08:01 4734677                    /usr/lib64/libpopt.so.0.0.0
    7fd70eb64000-7fd70ed64000 ---p 0000b000 08:01 4734677                    /usr/lib64/libpopt.so.0.0.0
    7fd70ed64000-7fd70ed65000 r--p 0000b000 08:01 4734677                    /usr/lib64/libpopt.so.0.0.0
    7fd70ed65000-7fd70ed66000 rw-p 0000c000 08:01 4734677                    /usr/lib64/libpopt.so.0.0.0
    7fd70ed66000-7fd70eda6000 r-xp 00000000 08:01 8336276                    /lib64/libreadline.so.6.3
    7fd70eda6000-7fd70efa6000 ---p 00040000 08:01 8336276                    /lib64/libreadline.so.6.3
    7fd70efa6000-7fd70efa8000 r--p 00040000 08:01 8336276                    /lib64/libreadline.so.6.3
    7fd70efa8000-7fd70efaf000 rw-p 00042000 08:01 8336276                    /lib64/libreadline.so.6.3
    7fd70efaf000-7fd70efb0000 rw-p 00000000 00:00 0 
    7fd70efb0000-7fd70efe2000 r-xp 00000000 08:01 4734212                    /usr/lib64/libexif.so.12.3.3
    7fd70efe2000-7fd70f1e2000 ---p 00032000 08:01 4734212                    /usr/lib64/libexif.so.12.3.3
    7fd70f1e2000-7fd70f1f5000 r--p 00032000 08:01 4734212                    /usr/lib64/libexif.so.12.3.3
    7fd70f1f5000-7fd70f1f6000 rw-p 00045000 08:01 4734212                    /usr/lib64/libexif.so.12.3.3
    7fd70f1f6000-7fd70f20e000 r-xp 00000000 08:01 12059135                   /lib64/libpthread-2.21.so
    7fd70f20e000-7fd70f40d000 ---p 00018000 08:01 12059135                   /lib64/libpthread-2.21.so
    7fd70f40d000-7fd70f40e000 r--p 00017000 08:01 12059135                   /lib64/libpthread-2.21.so
    7fd70f40e000-7fd70f40f000 rw-p 00018000 08:01 12059135                   /lib64/libpthread-2.21.so
    7fd70f40f000-7fd70f413000 rw-p 00000000 00:00 0 
    7fd70f413000-7fd70f470000 r-xp 00000000 08:01 1182937                    /usr/lib64/libjpeg.so.62.1.0
    7fd70f470000-7fd70f66f000 ---p 0005d000 08:01 1182937                    /usr/lib64/libjpeg.so.62.1.0
    7fd70f66f000-7fd70f670000 r--p 0005c000 08:01 1182937                    /usr/lib64/libjpeg.so.62.1.0
    7fd70f670000-7fd70f671000 rw-p 0005d000 08:01 1182937                    /usr/lib64/libjpeg.so.62.1.0
    7fd70f671000-7fd70f68c000 r-xp 00000000 08:01 8266073                    /usr/lib64/libaa.so.1.0.4
    7fd70f68c000-7fd70f88b000 ---p 0001b000 08:01 8266073                    /usr/lib64/libaa.so.1.0.4
