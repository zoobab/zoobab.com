
    root@warsaw /home/zoobab/soft/HairyDairyMaid_WRT54G_Debrick_Utility_v48 [209]# ./wrt54g -backup:wholeflash /fc:12 /dma 
    
    ====================================
    WRT54G/GS EJTAG Debrick Utility v4.8
    ====================================
    
    Probing bus ... Done
    
    Instruction Length set to 8
    
    CPU Chip ID: 00010100011100010010000101111111 (1471217F)
    *** Found a Broadcom BCM4712 Rev 1 CPU chip ***
    
        - EJTAG IMPCODE ....... : 00000000100000000000100100000100 (00800904)
        - EJTAG Version ....... : 1 or 2.0
        - EJTAG DMA Support ... : Yes
        *** DMA Mode Forced On ***
    
    Issuing Processor / Peripheral Reset ... Done
    Enabling Memory Writes ... Done
    Halting Processor ... <Processor Entered Debug Mode!> ... Done
    Clearing Watchdog ... Done
    
    Manual Flash Selection ... Done
    
    Flash Vendor ID: 00000000000000000000000010001001 (00000089)
    Flash Device ID: 00000000000000001000100011000010 (000088C2)
    *** Manually Selected a Intel 28F160C3 1Mx16 TopB  (2MB) Flash Chip ***
    
        - Flash Chip Window Start .... : 1fc00000
        - Flash Chip Window Length ... : 00200000
        - Selected Area Start ........ : 1fc00000
        - Selected Area Length ....... : 00200000
    
    
    *** buffer overflow detected ***: ./wrt54g terminated
    ======= Backtrace: =========
    /lib/tls/i686/cmov/libc.so.6(__fortify_fail+0x48)[0xb7efc558]
    /lib/tls/i686/cmov/libc.so.6[0xb7efa680]
    /lib/tls/i686/cmov/libc.so.6[0xb7ef9d68]
    /lib/tls/i686/cmov/libc.so.6(_IO_default_xsputn+0xc8)[0xb7e6fa18]
    /lib/tls/i686/cmov/libc.so.6(_IO_vfprintf+0xf4a)[0xb7e428da]
    /lib/tls/i686/cmov/libc.so.6(__vsprintf_chk+0xa7)[0xb7ef9e17]
    /lib/tls/i686/cmov/libc.so.6(__sprintf_chk+0x2d)[0xb7ef9d5d]
    ./wrt54g[0x804a715]
    ./wrt54g[0x804b6ab]
    /lib/tls/i686/cmov/libc.so.6(__libc_start_main+0xe5)[0xb7e18685]
    ./wrt54g[0x80488f1]
    ======= Memory map: ========
    08048000-0804e000 r-xp 00000000 08:01 3410474    /home/zoobab/soft/HairyDairyMaid_WRT54G_Debrick_Utility_v48/wrt54g
    0804e000-0804f000 r--p 00005000 08:01 3410474    /home/zoobab/soft/HairyDairyMaid_WRT54G_Debrick_Utility_v48/wrt54g
    0804f000-08050000 rw-p 00006000 08:01 3410474    /home/zoobab/soft/HairyDairyMaid_WRT54G_Debrick_Utility_v48/wrt54g
    08050000-08073000 rw-p 08050000 00:00 0          [heap]
    b7e01000-b7e02000 rw-p b7e01000 00:00 0 
    b7e02000-b7f5a000 r-xp 00000000 08:01 2180087    /lib/tls/i686/cmov/libc-2.8.90.so
    b7f5a000-b7f5c000 r--p 00158000 08:01 2180087    /lib/tls/i686/cmov/libc-2.8.90.so
    b7f5c000-b7f5d000 rw-p 0015a000 08:01 2180087    /lib/tls/i686/cmov/libc-2.8.90.so
    b7f5d000-b7f60000 rw-p b7f5d000 00:00 0 
    b7f6a000-b7f77000 r-xp 00000000 08:01 2981999    /lib/libgcc_s.so.1
    b7f77000-b7f78000 r--p 0000c000 08:01 2981999    /lib/libgcc_s.so.1
    b7f78000-b7f79000 rw-p 0000d000 08:01 2981999    /lib/libgcc_s.so.1
    b7f79000-b7f7c000 rw-p b7f79000 00:00 0 
    b7f7c000-b7f96000 r-xp 00000000 08:01 2981911    /lib/ld-2.8.90.so
    b7f96000-b7f97000 r-xp b7f96000 00:00 0          [vdso]
    b7f97000-b7f98000 r--p 0001a000 08:01 2981911    /lib/ld-2.8.90.so
    b7f98000-b7f99000 rw-p 0001b000 08:01 2981911    /lib/ld-2.8.90.so
    bff21000-bff36000 rw-p bffeb000 00:00 0          [stack]
    Aborted
