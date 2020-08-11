# Introduction


The Philips SNA6600 is a ADSL and wireless router with 4 ports ethernet switch. It is a clone of the [<http://oldwiki.openwrt.org/OpenWrtDocs>  (2f)Hardware(2f)3Com(2f)3CRWDR100A(2d)72.html 3Com 3CRWDR100A], and it is based on the AR7 platform. It is widely sold in Belgium by the main ISP Belgacom under the product name "Belgacom ADSL wireless". 

# Pictures


[[gallery]]

# Serial port


## Pinout


A serial console can be connected to J4. The serial signals are at a 3.3V level, so you need to use a level convertor. The serial signal itself is 115200 baud, 8 databits, 1 stopbit, no parity (8N1).

The pinout for the serial is:

|| 9 || 7 || 5 || 3 || 1 ||
|| 10 || 8 || 6 || 4 || 2 ||

RX = 3
TX = 5
GND = 9
3.3V = 10

## Output


Put the output here:


    =~=~=~=~=~=~=~=~=~=~=~= PuTTY log 2009.11.29 20:43:38 =~=~=~=~=~=~=~=~=~=~=~=
    
    
    ====== console mode ======
      shift-0: enable debug
      shift-9: enable config
      ENTER  : show this help
    ==========================
    
    
    ====== console mode ======
      shift-0: enable debug
      shift-9: enable config
      ENTER  : show this help
    ==========================
    Running Console Debug... !!!
    
    
    
    ======= Console Debug =======
     (1)   Alert Mail Testing
     (2)   Web Upgrage
     (3)   Write Web
     (4)   Firmware Upgrage
     (5)   Write Firmware
     (6)   Warm Reboot
     (8)   Show B0,B1 Mem pool
     (a)   <MENU> gConfig
     (b)   <MENU> gSetting
     (c)   <MENU> DHCP Client
     (d)   <MENU> Dial
     (e)   <MENU> Ethernet
     (f)   <MENU> Firewall
     (p)   <MENU> PPPoE
     (s)   <MENU> System
     (w)   <MENU> Wireless
     (x)   Exit
     (?)   Help
    =============================
    [Debug]: user_drv : main loop begin !!!
    
    Reset ...
    
    Warm_Reboot(), rebooting ...
    TRAP(warmStart) : send ok!
    
    
    ===========================================================
     TI ADSL AR7300 Loader 0.69.2 build May  4 2006 11:22:20
                     Broad Net Technology, INC.
    ===========================================================
    MX29LV160B bottom boot 16-bit mode found
    
    Copying boot params.....DONE
    
    Press any key to enter command mode ...
    
    [AR7300 Boot]:
    
    ======================
     [U] Upload to Flash  
     [E] Erase Flash      
     [G] Run Runtime Code 
     [A] Set MAC Address 
     [#] Set Serial Number 
     [V] Set Board Version 
     [H] Set Options 
     [P] Print Boot Params 
    ======================
    
    [AR7300 Boot]:
    
    ======================
     [U] Upload to Flash  
     [E] Erase Flash      
     [G] Run Runtime Code 
     [A] Set MAC Address 
     [#] Set Serial Number 
     [V] Set Board Version 
     [H] Set Options 
     [P] Print Boot Params 
    ======================
    
    [AR7300 Boot]:
    
    ======================
     [U] Upload to Flash  
     [E] Erase Flash      
     [G] Run Runtime Code 
     [A] Set MAC Address 
     [#] Set Serial Number 
     [V] Set Board Version 
     [H] Set Options 
     [P] Print Boot Params 
    ======================
    
    [AR7300 Boot]:
    
    ======================
     [U] Upload to Flash  
     [E] Erase Flash      
     [G] Run Runtime Code 
     [A] Set MAC Address 
     [#] Set Serial Number 
     [V] Set Board Version 
     [H] Set Options 
     [P] Print Boot Params 
    ======================
    
    [AR7300 Boot]:
    
    ======================
     [U] Upload to Flash  
     [E] Erase Flash      
     [G] Run Runtime Code 
     [A] Set MAC Address 
     [#] Set Serial Number 
     [V] Set Board Version 
     [H] Set Options 
     [P] Print Boot Params 
    ======================
    
    [AR7300 Boot]:
    
    ======================
     [U] Upload to Flash  
     [E] Erase Flash      
     [G] Run Runtime Code 
     [A] Set MAC Address 
     [#] Set Serial Number 
     [V] Set Board Version 
     [H] Set Options 
     [P] Print Boot Params 
    ======================
    
    [AR7300 Boot]:
    
    ======================
     [U] Upload to Flash  
     [E] Erase Flash      
     [G] Run Runtime Code 
     [A] Set MAC Address 
     [#] Set Serial Number 
     [V] Set Board Version 
     [H] Set Options 
     [P] Print Boot Params 
    ======================
    
    [AR7300 Boot]:
    
    ======================
     [U] Upload to Flash  
     [E] Erase Flash      
     [G] Run Runtime Code 
     [A] Set MAC Address 
     [#] Set Serial Number 
     [V] Set Board Version 
     [H] Set Options 
     [P] Print Boot Params 
    ======================
    
    [AR7300 Boot]:
    
    ======================
     [U] Upload to Flash  
     [E] Erase Flash      
     [G] Run Runtime Code 
     [A] Set MAC Address 
     [#] Set Serial Number 
     [V] Set Board Version 
     [H] Set Options 
     [P] Print Boot Params 
    ======================
    
    [AR7300 Boot]:u
    
    
    UPLOAD Flash
    ---------------------------------------
        Area            Address      Length 
    ---------------------------------------
    [0] Boot            0xB0000000     128K
    [1] Configuration   0xB0020000     128K
    [2] Web Image       0xB0040000     832K
    [3] Code Image      0xB0110000     896K
    [4] Boot Params     0xB01F0000      64K
    [5] Flash Image     0xB0000000    2048K
    ---------------------------------------
    Enter area to UPLOAD: 
    ERROR: Not a valid area.
    
    
    [AR7300 Boot]:p
    
    
    MAC address     : 00-12-BF-3C-F9-AA
    Serial number   : J641026240
    Hardware version: 01
    Options         : 00-00-00-00-00-00
    
    [AR7300 Boot]:h
    
    
    Enter Boot Option (00-00-00-00-00-00-00): 
    Invalid Options
    
    
    [AR7300 Boot]:h
    
    
    Enter Boot Option (00-00-00-00-00-00-00): 
    
    
    [AR7300 Boot]:
    
    ======================
     [U] Upload to Flash  
     [E] Erase Flash      
     [G] Run Runtime Code 
     [A] Set MAC Address 
     [#] Set Serial Number 
     [V] Set Board Version 
     [H] Set Options 
     [P] Print Boot Params 
    ======================
    
    [AR7300 Boot]:V
    
    
    Enter Board Version (01): 
    
    
    [AR7300 Boot]:G
    
    Unzipping program from bank 2...done
    Try to find image for running...
    Unzipping program from bank 3...done
    In C_Entry() function ...
    install_exception 
    sys_irq_init() ...
    ##### _ftext      = 0x94000000
    ##### _fdata      = 0x941E4490
    ##### __bss_start = 0x942564B8
    ##### end         = 0x94D8D094
    ##### Backup Data from 0x941E4490 to 0x94DAD094~0x94E1F0BC len 466984
    ##### Backup Data completed
    ##### Backup Data verified
    Unzipping from B0040000 to 94F00000 ... done
    Uncompressed size = 723095
    Unzipping WEB...ok
    [INIT] MTinitialize ..
    userclk_init() ...
    Runtime code version: 0.42
    System startup...
    [INIT] Memory COLOR 0, 800000 bytes ..
    [INIT] Memory COLOR 1, 300000 bytes ..
    [INIT] Memory COLOR 2, 1399776 bytes ..
    DSL HAL Version: 06.00.01.00
    Sangam detected, rev 0x22
    timecode=5702705
    set dspfreq 250Mhz
    Sangam clock boost 250
    REG_VSERCLKSELR<-0x01
    Enable Analog PLL 
    
    SAR_FREQUNCY = 62500000Hz
    
    manu_id=00C2 chip_id=2249
    MX29LV160B bottom boot 16-bit mode found
    Set flash memory layout to Boot Parameters found !!!
    Bootcode version: 0.69.2
    Serial number: J641026240
    Hardware version: 01
    
    manu_id=00C2 chip_id=2249
    MX29LV160B bottom boot 16-bit mode found
    
    my CFGVersionMagic = 0x33343536, old CFGVersionMagic on flash = 0x33343536
    my CFGsize = 87776, my CFGDescSize = 16559
    my Version = 0.42, Version on flash= 0.42
    CFGsize on flash = 87776, CFGDescSize on flash = 16559
    (oldCfg) success to request memory, size:104335
    
    manu_id=00C2 chip_id=2249
    MX29LV160B bottom boot 16-bit mode found
    OldCfgHexSize:1870,	6256
    (tmpbuf) success to request memory, size:6256
    (oldCfgStrDesc) success to request memory, size:16559
    Unzipping from 94432500 to 9442E440 ... done
    Uncompressed size = 16557
    Tail : END_III_Config_t
    
    Size of Old CFG_DESC is :16557!!!
    MyCfgHexSize:6248
    Unzipping from 9442CBC0 to 94428B00 ... done
    Uncompressed size = 16557
    Size of my CFG_DESC is :16557!!!
    Tail : END_III_Config_t
    
    
    Restore Config file from ver:0.42!!!
    
    backup_hwlan 0 1
    Update TR69 config 
    default route: 0.0.0.0
    BufferInit:
    BUF_HDR_SZ=32 BUF_ALIGN_SZ=0 BUFFER_OFFSET=96
    BUF_BUFSZ0=384 BUF_BUFSZ1=1872
    NUM_OF_B0=0 NUM_OF_B1=1200
    BUF_POOL0_SZ=0 BUF_POOL1_SZ=2284800
    sizeof(BUFFER0)=416,sizeof(BUFFER1)=1904
    *BUF0=0x94805bc0 *BUF1=0x945d7eb0
    Altgn *BUF0=0x94805bc0 *BUF1=0x945d7eb0
    End at BUF0:0x94805bc0, BUF1:0x94805bb0
    
    BUF0[0]=0x94805bc0 BUF1[0]=0x945d7eb0
    
    buffer0 pointer init OK!
    buffer1 pointer init OK!
    time = 08/01/2003, 00:00:00
    Interface 0 ip = 127.0.0.1
    
    Memory request 2072 left 297928 ptr 942EE5E4
    Call tn7sar_malloc_dma_xfer() addr:B42EE5E4 size:2072
    MAC1 [RX=128 TX=1]: TI External PHY
    MAC Address: 00:12:bf:3c:f9:aa
    [VLAN] port: 0x0003 vlan: 0x000c
    [VLAN] ifno: 1 port: 3 vlan: 0x1030
    [VLAN] ifno: 1 port: 4 vlan: 0x1028
    time = 08/01/2003, 00:00:00
    
    manu_id=00C2 chip_id=2249
    MX29LV160B bottom boot 16-bit mode found
    br_MacAddress=00-12-BF-3C-F9-AA
    Interface 1 ip = 192.168.1.1
    
    hwlan_init : ifno 2 TIWLANifno = 2
    [HWLAN] MAC Address: 00:12:bf:3c:f9:ac
    time = 08/01/2003, 00:00:00
    Interface 2 ip = 192.168.1.1
    
    Init SAR ifno:3 chan:0 VPI/VCI:8/35
    Init PDSP ...
    Init PDSP done.
    Memory request 552 left 297376 ptr 942EEDFC
    Call tn7sar_malloc() addr:B42EEDFC size:552
    [aal5->os]2.IsrRegister(OsDev:942568a4, halIsr:94119c84, Interrupt:15)
    [aal5]halControl(HalDev:94d099e0, Key:OamMode, Action:Set, Value:94dacf3c)
    [aal5]halChannelSetup(HalDev:94d099e0, HalCh:94dace80, OsSetup:00000000)
      [aal5 Inst 0, Ch 0] Config Dump:
        TxNumBuffers  :00000128, TxNumQueues :00000002
        RxNumBuffers  :00000128, RxBufSize   :00001582
        TxServiceMax  :00000032, RxServiceMax:00000016
        RxBufferOffset:00000000, DaMask      :00000001
        CpcsUU        :00000000, Gfc         :00000000
        Clp           :00000000, Pti         :00000000
        Priority      :00000002, PktType     :00000000
        Vci           :00000035, Vpi         :00000008
        TxVc_CellRate :00015625, TxVc_QosType:00000002
        TxVc_Mbs      :00015625, TxVc_Pcr    :00015625
        TxVc_AtmHeader:08389168
    InitTcb(CH:0): tcbsize:48 allsize:6160 num:128
    Memory request 6160 left 291216 ptr 942EF024
    Call tn7sar_malloc_dma_xfer() addr:B42EF024 size:6160
    Memory request 6160 left 285056 ptr 942F0834
    Call tn7sar_malloc_dma_xfer() addr:B42F0834 size:6160
    InitRcb(CH:0): rcbsize:64 allsize:8208 num:128
    Memory request 8208 left 276848 ptr 942F2044
    Call tn7sar_malloc_dma_xfer() addr:B42F2044 size:8208
    Call halChannelSetup(), Ch:0
    (HalCh->TxVc_VpOffset)=00000000
    (HalCh->RxVc_VpOffset)=00000000
    Install SAR handler ...
    MAC Address: 00:12:bf:3c:f9:ab
    Interface 3 ip = 0.0.0.0
    
    Init SAR ifno:4 chan:1 VPI/VCI:0/32
    [aal5]halChannelSetup(HalDev:94d099e0, HalCh:94dace40, OsSetup:00000000)
      [aal5 Inst 0, Ch 1] Config Dump:
        TxNumBuffers  :00000064, TxNumQueues :00000002
        RxNumBuffers  :00000064, RxBufSize   :00001582
        TxServiceMax  :00000032, RxServiceMax:00000016
        RxBufferOffset:00000000, DaMask      :00000001
        CpcsUU        :00000000, Gfc         :00000000
        Clp           :00000000, Pti         :00000000
        Priority      :00000002, PktType     :00000000
        Vci           :00000032, Vpi         :00000000
        TxVc_CellRate :00015625, TxVc_QosType:00000002
        TxVc_Mbs      :00015625, TxVc_Pcr    :00015625
        TxVc_AtmHeader:00000512
    InitTcb(CH:1): tcbsize:48 allsize:3088 num:64
    Memory request 3088 left 273760 ptr 942F4054
    Call tn7sar_malloc_dma_xfer() addr:B42F4054 size:3088
    Memory request 3088 left 270672 ptr 942F4C64
    Call tn7sar_malloc_dma_xfer() addr:B42F4C64 size:3088
    InitRcb(CH:1): rcbsize:64 allsize:4112 num:64
    Memory request 4112 left 266560 ptr 942F5874
    Call tn7sar_malloc_dma_xfer() addr:B42F5874 size:4112
    Call halChannelSetup(), Ch:1
    (HalCh->TxVc_VpOffset)=00000001
    (HalCh->RxVc_VpOffset)=00000001
    MAC Address: 00:12:bf:3c:f9:ad
    
    manu_id=00C2 chip_id=2249
    MX29LV160B bottom boot 16-bit mode found
    br_MacAddress=00-12-BF-3C-F9-AA
    Interface 4 ip = 192.168.2.1
    
    Init SAR ifno:5 chan:2 VPI/VCI:1/32
    [aal5]halChannelSetup(HalDev:94d099e0, HalCh:94dace40, OsSetup:00000000)
      [aal5 Inst 0, Ch 2] Config Dump:
        TxNumBuffers  :00000064, TxNumQueues :00000002
        RxNumBuffers  :00000064, RxBufSize   :00001582
        TxServiceMax  :00000032, RxServiceMax:00000016
        RxBufferOffset:00000000, DaMask      :00000001
        CpcsUU        :00000000, Gfc         :00000000
        Clp           :00000000, Pti         :00000000
        Priority      :00000002, PktType     :00000000
        Vci           :00000032, Vpi         :00000001
        TxVc_CellRate :00015625, TxVc_QosType:00000002
        TxVc_Mbs      :00015625, TxVc_Pcr    :00015625
        TxVc_AtmHeader:01049088
    InitTcb(CH:2): tcbsize:48 allsize:3088 num:64
    Memory request 3088 left 263472 ptr 942F6884
    Call tn7sar_malloc_dma_xfer() addr:B42F6884 size:3088
    Memory request 3088 left 260384 ptr 942F7494
    Call tn7sar_malloc_dma_xfer() addr:B42F7494 size:3088
    InitRcb(CH:2): rcbsize:64 allsize:4112 num:64
    Memory request 4112 left 256272 ptr 942F80A4
    Call tn7sar_malloc_dma_xfer() addr:B42F80A4 size:4112
    Call halChannelSetup(), Ch:2
    (HalCh->TxVc_VpOffset)=00000002
    (HalCh->RxVc_VpOffset)=00000002
    MAC Address: 00:12:bf:3c:f9:ae
    Interface 5 ip = 192.168.2.1
    
    Init SAR ifno:6 chan:3 VPI/VCI:1/33
    [aal5]halChannelSetup(HalDev:94d099e0, HalCh:94dace40, OsSetup:00000000)
      [aal5 Inst 0, Ch 3] Config Dump:
        TxNumBuffers  :00000064, TxNumQueues :00000002
        RxNumBuffers  :00000064, RxBufSize   :00001582
        TxServiceMax  :00000032, RxServiceMax:00000016
        RxBufferOffset:00000000, DaMask      :00000001
        CpcsUU        :00000000, Gfc         :00000000
        Clp           :00000000, Pti         :00000000
        Priority      :00000002, PktType     :00000000
        Vci           :00000033, Vpi         :00000001
        TxVc_CellRate :00015625, TxVc_QosType:00000002
        TxVc_Mbs      :00015625, TxVc_Pcr    :00015625
        TxVc_AtmHeader:01049104
    InitTcb(CH:3): tcbsize:48 allsize:3088 num:64
    Memory request 3088 left 253184 ptr 942F90B4
    Call tn7sar_malloc_dma_xfer() addr:B42F90B4 size:3088
    Memory request 3088 left 250096 ptr 942F9CC4
    Call tn7sar_malloc_dma_xfer() addr:B42F9CC4 size:3088
    InitRcb(CH:3): rcbsize:64 allsize:4112 num:64
    Memory request 4112 left 245984 ptr 942FA8D4
    Call tn7sar_malloc_dma_xfer() addr:B42FA8D4 size:4112
    Call halChannelSetup(), Ch:3
    (HalCh->TxVc_VpOffset)=00000003
    (HalCh->RxVc_VpOffset)=00000003
    MAC Address: 00:12:bf:3c:f9:af
    Interface 6 ip = 192.168.2.1
    
    Init SAR ifno:7 chan:4 VPI/VCI:1/34
    [aal5]halChannelSetup(HalDev:94d099e0, HalCh:94dace40, OsSetup:00000000)
      [aal5 Inst 0, Ch 4] Config Dump:
        TxNumBuffers  :00000064, TxNumQueues :00000002
        RxNumBuffers  :00000064, RxBufSize   :00001582
        TxServiceMax  :00000032, RxServiceMax:00000016
        RxBufferOffset:00000000, DaMask      :00000001
        CpcsUU        :00000000, Gfc         :00000000
        Clp           :00000000, Pti         :00000000
        Priority      :00000002, PktType     :00000000
        Vci           :00000034, Vpi         :00000001
        TxVc_CellRate :00015625, TxVc_QosType:00000002
        TxVc_Mbs      :00015625, TxVc_Pcr    :00015625
        TxVc_AtmHeader:01049120
    InitTcb(CH:4): tcbsize:48 allsize:3088 num:64
    Memory request 3088 left 242896 ptr 942FB8E4
    Call tn7sar_malloc_dma_xfer() addr:B42FB8E4 size:3088
    Memory request 3088 left 239808 ptr 942FC4F4
    Call tn7sar_malloc_dma_xfer() addr:B42FC4F4 size:3088
    InitRcb(CH:4): rcbsize:64 allsize:4112 num:64
    Memory request 4112 left 235696 ptr 942FD104
    Call tn7sar_malloc_dma_xfer() addr:B42FD104 size:4112
    Call halChannelSetup(), Ch:4
    (HalCh->TxVc_VpOffset)=00000004
    (HalCh->RxVc_VpOffset)=00000004
    MAC Address: 00:12:bf:3c:f9:b0
    Interface 7 ip = 192.168.2.1
    
    Init SAR ifno:8 chan:5 VPI/VCI:1/35
    [aal5]halChannelSetup(HalDev:94d099e0, HalCh:94dace40, OsSetup:00000000)
      [aal5 Inst 0, Ch 5] Config Dump:
        TxNumBuffers  :00000064, TxNumQueues :00000002
        RxNumBuffers  :00000064, RxBufSize   :00001582
        TxServiceMax  :00000032, RxServiceMax:00000016
        RxBufferOffset:00000000, DaMask      :00000001
        CpcsUU        :00000000, Gfc         :00000000
        Clp           :00000000, Pti         :00000000
        Priority      :00000002, PktType     :00000000
        Vci           :00000035, Vpi         :00000001
        TxVc_CellRate :00015625, TxVc_QosType:00000002
        TxVc_Mbs      :00015625, TxVc_Pcr    :00015625
        TxVc_AtmHeader:01049136
    InitTcb(CH:5): tcbsize:48 allsize:3088 num:64
    Memory request 3088 left 232608 ptr 942FE114
    Call tn7sar_malloc_dma_xfer() addr:B42FE114 size:3088
    Memory request 3088 left 229520 ptr 942FED24
    Call tn7sar_malloc_dma_xfer() addr:B42FED24 size:3088
    InitRcb(CH:5): rcbsize:64 allsize:4112 num:64
    Memory request 4112 left 225408 ptr 942FF934
    Call tn7sar_malloc_dma_xfer() addr:B42FF934 size:4112
    Call halChannelSetup(), Ch:5
    (HalCh->TxVc_VpOffset)=00000005
    (HalCh->RxVc_VpOffset)=00000005
    MAC Address: 00:12:bf:3c:f9:b1
    Interface 8 ip = 192.168.2.1
    
    Init SAR ifno:9 chan:6 VPI/VCI:1/36
    [aal5]halChannelSetup(HalDev:94d099e0, HalCh:94dace40, OsSetup:00000000)
      [aal5 Inst 0, Ch 6] Config Dump:
        TxNumBuffers  :00000064, TxNumQueues :00000002
        RxNumBuffers  :00000064, RxBufSize   :00001582
        TxServiceMax  :00000032, RxServiceMax:00000016
        RxBufferOffset:00000000, DaMask      :00000001
        CpcsUU        :00000000, Gfc         :00000000
        Clp           :00000000, Pti         :00000000
        Priority      :00000002, PktType     :00000000
        Vci           :00000036, Vpi         :00000001
        TxVc_CellRate :00015625, TxVc_QosType:00000002
        TxVc_Mbs      :00015625, TxVc_Pcr    :00015625
        TxVc_AtmHeader:01049152
    InitTcb(CH:6): tcbsize:48 allsize:3088 num:64
    Memory request 3088 left 222320 ptr 94300944
    Call tn7sar_malloc_dma_xfer() addr:B4300944 size:3088
    Memory request 3088 left 219232 ptr 94301554
    Call tn7sar_malloc_dma_xfer() addr:B4301554 size:3088
    InitRcb(CH:6): rcbsize:64 allsize:4112 num:64
    Memory request 4112 left 215120 ptr 94302164
    Call tn7sar_malloc_dma_xfer() addr:B4302164 size:4112
    Call halChannelSetup(), Ch:6
    (HalCh->TxVc_VpOffset)=00000006
    (HalCh->RxVc_VpOffset)=00000006
    MAC Address: 00:12:bf:3c:f9:b2
    Interface 9 ip = 192.168.2.1
    
    Init SAR ifno:10 chan:7 VPI/VCI:1/37
    [aal5]halChannelSetup(HalDev:94d099e0, HalCh:94dace40, OsSetup:00000000)
      [aal5 Inst 0, Ch 7] Config Dump:
        TxNumBuffers  :00000064, TxNumQueues :00000002
        RxNumBuffers  :00000064, RxBufSize   :00001582
        TxServiceMax  :00000032, RxServiceMax:00000016
        RxBufferOffset:00000000, DaMask      :00000001
        CpcsUU        :00000000, Gfc         :00000000
        Clp           :00000000, Pti         :00000000
        Priority      :00000002, PktType     :00000000
        Vci           :00000037, Vpi         :00000001
        TxVc_CellRate :00015625, TxVc_QosType:00000002
        TxVc_Mbs      :00015625, TxVc_Pcr    :00015625
        TxVc_AtmHeader:01049168
    InitTcb(CH:7): tcbsize:48 allsize:3088 num:64
    Memory request 3088 left 212032 ptr 94303174
    Call tn7sar_malloc_dma_xfer() addr:B4303174 size:3088
    Memory request 3088 left 208944 ptr 94303D84
    Call tn7sar_malloc_dma_xfer() addr:B4303D84 size:3088
    InitRcb(CH:7): rcbsize:64 allsize:4112 num:64
    Memory request 4112 left 204832 ptr 94304994
    Call tn7sar_malloc_dma_xfer() addr:B4304994 size:4112
    Call halChannelSetup(), Ch:7
    (HalCh->TxVc_VpOffset)=00000007
    (HalCh->RxVc_VpOffset)=00000007
    MAC Address: 00:12:bf:3c:f9:b3
    Interface 10 ip = 192.168.2.1
    
    Init SAR ifno:11 chan:8 VPI/VCI:1/38
    [aal5]halChannelSetup(HalDev:94d099e0, HalCh:94dace40, OsSetup:00000000)
      [aal5 Inst 0, Ch 8] Config Dump:
        TxNumBuffers  :00000064, TxNumQueues :00000002
        RxNumBuffers  :00000064, RxBufSize   :00001582
        TxServiceMax  :00000032, RxServiceMax:00000016
        RxBufferOffset:00000000, DaMask      :00000001
        CpcsUU        :00000000, Gfc         :00000000
        Clp           :00000000, Pti         :00000000
        Priority      :00000002, PktType     :00000000
        Vci           :00000038, Vpi         :00000001
        TxVc_CellRate :00015625, TxVc_QosType:00000002
        TxVc_Mbs      :00015625, TxVc_Pcr    :00015625
        TxVc_AtmHeader:01049184
    InitTcb(CH:8): tcbsize:48 allsize:3088 num:64
    Memory request 3088 left 201744 ptr 943059A4
    Call tn7sar_malloc_dma_xfer() addr:B43059A4 size:3088
    Memory request 3088 left 198656 ptr 943065B4
    Call tn7sar_malloc_dma_xfer() addr:B43065B4 size:3088
    InitRcb(CH:8): rcbsize:64 allsize:4112 num:64
    Memory request 4112 left 194544 ptr 943071C4
    Call tn7sar_malloc_dma_xfer() addr:B43071C4 size:4112
    Call halChannelSetup(), Ch:8
    (HalCh->TxVc_VpOffset)=00000008
    (HalCh->RxVc_VpOffset)=00000008
    MAC Address: 00:12:bf:3c:f9:b4
    Interface 11 ip = 192.168.2.1
    
    Init SAR ifno:12 chan:9 VPI/VCI:1/39
    [aal5]halChannelSetup(HalDev:94d099e0, HalCh:94dace40, OsSetup:00000000)
      [aal5 Inst 0, Ch 9] Config Dump:
        TxNumBuffers  :00000064, TxNumQueues :00000002
        RxNumBuffers  :00000064, RxBufSize   :00001582
        TxServiceMax  :00000032, RxServiceMax:00000016
        RxBufferOffset:00000000, DaMask      :00000001
        CpcsUU        :00000000, Gfc         :00000000
        Clp           :00000000, Pti         :00000000
        Priority      :00000002, PktType     :00000000
        Vci           :00000039, Vpi         :00000001
        TxVc_CellRate :00015625, TxVc_QosType:00000002
        TxVc_Mbs      :00015625, TxVc_Pcr    :00015625
        TxVc_AtmHeader:01049200
    InitTcb(CH:9): tcbsize:48 allsize:3088 num:64
    Memory request 3088 left 191456 ptr 943081D4
    Call tn7sar_malloc_dma_xfer() addr:B43081D4 size:3088
    Memory request 3088 left 188368 ptr 94308DE4
    Call tn7sar_malloc_dma_xfer() addr:B4308DE4 size:3088
    InitRcb(CH:9): rcbsize:64 allsize:4112 num:64
    Memory request 4112 left 184256 ptr 943099F4
    Call tn7sar_malloc_dma_xfer() addr:B43099F4 size:4112
    Call halChannelSetup(), Ch:9
    (HalCh->TxVc_VpOffset)=00000009
    (HalCh->RxVc_VpOffset)=00000009
    MAC Address: 00:12:bf:3c:f9:b5
    Interface 12 ip = 192.168.2.1
    
    Init SAR ifno:13 chan:10 VPI/VCI:1/40
    [aal5]halChannelSetup(HalDev:94d099e0, HalCh:94dace40, OsSetup:00000000)
      [aal5 Inst 0, Ch 10] Config Dump:
        TxNumBuffers  :00000064, TxNumQueues :00000002
        RxNumBuffers  :00000064, RxBufSize   :00001582
        TxServiceMax  :00000032, RxServiceMax:00000016
        RxBufferOffset:00000000, DaMask      :00000001
        CpcsUU        :00000000, Gfc         :00000000
        Clp           :00000000, Pti         :00000000
        Priority      :00000002, PktType     :00000000
        Vci           :00000040, Vpi         :00000001
        TxVc_CellRate :00015625, TxVc_QosType:00000002
        TxVc_Mbs      :00015625, TxVc_Pcr    :00015625
        TxVc_AtmHeader:01049216
    InitTcb(CH:10): tcbsize:48 allsize:3088 num:64
    Memory request 3088 left 181168 ptr 9430AA04
    Call tn7sar_malloc_dma_xfer() addr:B430AA04 size:3088
    Memory request 3088 left 178080 ptr 9430B614
    Call tn7sar_malloc_dma_xfer() addr:B430B614 size:3088
    InitRcb(CH:10): rcbsize:64 allsize:4112 num:64
    Memory request 4112 left 173968 ptr 9430C224
    Call tn7sar_malloc_dma_xfer() addr:B430C224 size:4112
    Call halChannelSetup(), Ch:10
    (HalCh->TxVc_VpOffset)=0000000A
    (HalCh->RxVc_VpOffset)=0000000A
    MAC Address: 00:12:bf:3c:f9:b6
    Interface 13 ip = 192.168.2.1
    
    Init SAR ifno:14 chan:11 VPI/VCI:1/41
    [aal5]halChannelSetup(HalDev:94d099e0, HalCh:94dace40, OsSetup:00000000)
      [aal5 Inst 0, Ch 11] Config Dump:
        TxNumBuffers  :00000064, TxNumQueues :00000002
        RxNumBuffers  :00000064, RxBufSize   :00001582
        TxServiceMax  :00000032, RxServiceMax:00000016
        RxBufferOffset:00000000, DaMask      :00000001
        CpcsUU        :00000000, Gfc         :00000000
        Clp           :00000000, Pti         :00000000
        Priority      :00000002, PktType     :00000000
        Vci           :00000041, Vpi         :00000001
        TxVc_CellRate :00015625, TxVc_QosType:00000002
        TxVc_Mbs      :00015625, TxVc_Pcr    :00015625
        TxVc_AtmHeader:01049232
    InitTcb(CH:11): tcbsize:48 allsize:3088 num:64
    Memory request 3088 left 170880 ptr 9430D234
    Call tn7sar_malloc_dma_xfer() addr:B430D234 size:3088
    Memory request 3088 left 167792 ptr 9430DE44
    Call tn7sar_malloc_dma_xfer() addr:B430DE44 size:3088
    InitRcb(CH:11): rcbsize:64 allsize:4112 num:64
    Memory request 4112 left 163680 ptr 9430EA54
    Call tn7sar_malloc_dma_xfer() addr:B430EA54 size:4112
    Call halChannelSetup(), Ch:11
    (HalCh->TxVc_VpOffset)=0000000B
    (HalCh->RxVc_VpOffset)=0000000B
    MAC Address: 00:12:bf:3c:f9:b7
    Interface 14 ip = 192.168.2.1
    
    IFLNK_PPPOE init : (Linkp)ifno = 15 idx = 2
    IFLNK_PPPOE init : (Driverp)ifno = 15 idx = 3
    Interface 15 ip = 0.0.0.0
    
    MAC Address: 00:12:bf:3c:f9:aa
    [VLAN] port: 0x000c vlan: 0x0003
    [VLAN] ifno: 29 port: 1 vlan: 0x2024
    [VLAN] ifno: 29 port: 2 vlan: 0x2022
    time = 08/01/2003, 00:00:00
    Interface 29 ip = 192.168.2.1
    
    ruleCheck()> Group: 0,  Error: Useless rule index will be truncated
    ruleCheck()> Group: 1,  Error: Useless rule index will be truncated
    ruleCheck()> Group: 2,  Error: Useless rule index will be truncated
    CBAC rule format check succeed !!
    reqCBACBuf()> init match pool, Have: 1000
    Memory Address: 0x94d2b674 ~ 0x94d323f0
    reqCBACBuf()> init timeGap pool, Have: 10000
    Memory Address: 0x94d323f0 ~ 0x94d63144
    reqCBACBuf()> init sameHost pool, Have: 2000
    Memory Address: 0x94d63144 ~ 0x94d72b64
    CBAC rule pool initialized !!
    Init NAT data structure
    RUNTASK id=1 if_task if0...
    RUNTASK id=2 if_task if1...
    RUNTASK id=3 if_task if2...
    RUNTASK id=4 if_task if3...
    RUNTASK id=5 if_task if4...
    RUNTASK id=6 if_task if5...
    RUNTASK id=7 if_task if6...
    RUNTASK id=8 if_task if7...
    RUNTASK id=9 if_task if8...
    RUNTASK id=10 if_task if9...
    RUNTASK id=11 if_task if10...
    RUNTASK id=12 if_task if11...
    RUNTASK id=13 if_task if12...
    RUNTASK id=14 if_task if13...
    RUNTASK id=15 if_task if14...
    RUNTASK id=16 if_task if29...
    RUNTASK id=17 timer_task...
    RUNTASK id=18 conn_mgr...
    RUNTASK id=19 main_8021x...
    RUNTASK id=20 period_task...
    
    ========== ADSL Modem initialization OK ! ======
    
    RUNTASK id=21 dhcp_daemon...
    RUNTASK id=22 telnetd_main...
    [absread] flash_init: RAM's limitation is 16M
    Found PFS image@94f00000, uncompressed by boot-code!!
    httpd: listen at 192.168.1.1:80
    httpd: listen at 192.168.2.1:80
    httpd: listen at 0.0.0.0:8085
    RUNTASK httpd...
    RUNTASK id=27 dnsproxy...
    RUNTASK id=28 snmp_task...
    RUNTASK id=29 rip...
    RUNTASK id=30 ripout...
    RUNTASK id=31 dhcpd_mgmt_task...
    UPnP is disabled
    UPnP is enabled
    TR64 Device initialize success! slot=32
    update_device_OUI: OUI_str=0012BF
    [0] Allocate mailbox 0
    Starting Multitask...
    Initializing DSL interface ...
    Install ADSL handler ...
    Start programming PLL for Sangam chip
    clock_ ID = 0x00000009
    Run DSP at the preset frequency
    Begin DSP firmware Download ...
    Section count 200
    Not DSP PMEM/DMEM
    Section Addr: 147f9c00 Section Length: 15448 
    Special CO Profile found
    Not DSP PMEM/DMEM
    Section Addr: 147f2e00 Section Length: 12300 
    Not DSP PMEM/DMEM
    Section Addr: 147f8000 Section Length: 1186 
    Not DSP PMEM/DMEM
    Section Addr: 147f8800 Section Length: 4136 
    Not DSP PMEM/DMEM
    Section Addr: 147fdc00 Section Length: 924 
    OVERLAY PAGE #1 LEN=56128
    OVERLAY PAGE #2 LEN=23008
    OVERLAY PAGE #8 LEN=2304
    OVERLAY PAGE #7 LEN=32
    OVERLAY PAGE #3 LEN=43200
    OVERLAY PAGE #4 LEN=13568
    OVERLAY PAGE #5 LEN=9664
    OVERLAY PAGE #6 LEN=13760
    OVERLAY PAGE #9 LEN=34784
    OVERLAY PAGE #10 LEN=37056
    Wrote Image; Overlay Pages:11  Profiles:5
    POTS Service 
    DSL PHY control : 0 defined, 0x500
    DSP Firmware Download completed.
    Set DSP to 250MHz ...
    Modem Co
    TC_NOSYNC
    de: 06.02.[Overlay Page Done  1]
    00.60
    Train Mode: 0xff
    Training Mode: MMODE
    Start WatchDog ...
    MTstart2() begin  ...
    ifStrInit()> i:0, dtlStr:[Loop/Loop], rfStr[LB0], type:0, count:1
    ifStrInit()> i:1, dtlStr:[LAN 1/LAN1], rfStr[L1], type:1, count:1
    ifStrInit()> i:2, dtlStr:[WLAN1/WLAN1], rfStr[WL1], type:3, count:1
    ifStrInit()> i:3, dtlStr:[ATM 1/ATM1], rfStr[A1], type:5, count:1
    ifStrInit()> i:4, dtlStr:[ATM 2/ATM2], rfStr[A2], type:5, count:2
    ifStrInit()> i:5, dtlStr:[ATM 3/ATM3], rfStr[A3], type:5, count:3
    ifStrInit()> i:6, dtlStr:[ATM 4/ATM4], rfStr[A4], type:5, count:4
    ifStrInit()> i:7, dtlStr:[ATM 5/ATM5], rfStr[A5], type:5, count:5
    ifStrInit()> i:8, dtlStr:[ATM 6/ATM6], rfStr[A6], type:5, count:6
    ifStrInit()> i:9, dtlStr:[ATM 7/ATM7], rfStr[A7], type:5, count:7
    ifStrInit()> i:10, dtlStr:[ATM 8/ATM8], rfStr[A8], type:5, count:8
    ifStrInit()> i:11, dtlStr:[ATM 9/ATM9], rfStr[A9], type:5, count:9
    ifStrInit()> i:12, dtlStr:[ATM10/ATM10], rfStr[A10], type:5, count:10
    ifStrInit()> i:13, dtlStr:[ATM11/ATM11], rfStr[A11], type:5, count:11
    ifStrInit()> i:14, dtlStr:[ATM12/ATM12], rfStr[A12], type:5, count:12
    ifStrInit()> i:15, dtlStr:[PoE 1/PoE1], rfStr[P1], type:6, count:1
    ifStrInit()> i:16, dtlStr:[PoE 2/PoE2], rfStr[P2], type:6, count:2
    ifStrInit()> i:17, dtlStr:[PoE 3/PoE3], rfStr[P3], type:6, count:3
    ifStrInit()> i:18, dtlStr:[PoE 4/PoE4], rfStr[P4], type:6, count:4
    ifStrInit()> i:19, dtlStr:[PoE 5/PoE5], rfStr[P5], type:6, count:5
    ifStrInit()> i:20, dtlStr:[PoE 6/PoE6], rfStr[P6], type:6, count:6
    ifStrInit()> i:21, dtlStr:[PoE 7/PoE7], rfStr[P7], type:6, count:7
    ifStrInit()> i:22, dtlStr:[PoE 8/PoE8], rfStr[P8], type:6, count:8
    ifStrInit()> i:23, dtlStr:[PoE 9/PoE9], rfStr[P9], type:6, count:9
    ifStrInit()> i:24, dtlStr:[PoE10/PoE10], rfStr[P10], type:6, count:10
    ifStrInit()> i:25, dtlStr:[PoE11/PoE11], rfStr[P11], type:6, count:11
    ifStrInit()> i:26, dtlStr:[PoE12/PoE12], rfStr[P12], type:6, count:12
    ifStrInit()> i:27, dtlStr:[/], rfStr[], type:10, count:0
    ifStrInit()> i:28, dtlStr:[/], rfStr[], type:10, count:0
    ifStrInit()> i:30, dtlStr:[/], rfStr[], type:10, count:0
    TRAP(coldStart) : send ok!
    SSDP Initialization completed...
    TRAP(authenticationFailure) : send ok!
    FSstat: no such file
    
    TR64_Init() : read root xml '/tr64_igd.xml' failed code = 1 !!
    wlan_timer_init() ...
    restore_hwlan : 0
    
    
    ====== console mode ======
      shift-0: enable debug
      shift-9: enable config
      ENTER  : show this help
    ==========================
    
    
    ====== console mode ======
      shift-0: enable debug
      shift-9: enable config
      ENTER  : show this help
    ==========================
    
    
    ====== console mode ======
      shift-0: enable debug
      shift-9: enable config
      ENTER  : show this help
    ==========================
    Running Console Debug... !!!
    
    
    
    ======= Console Debug =======
     (1)   Alert Mail Testing
     (2)   Web Upgrage
     (3)   Write Web
     (4)   Firmware Upgrage
     (5)   Write Firmware
     (6)   Warm Reboot
     (8)   Show B0,B1 Mem pool
     (a)   <MENU> gConfig
     (b)   <MENU> gSetting
     (c)   <MENU> DHCP Client
     (d)   <MENU> Dial
     (e)   <MENU> Ethernet
     (f)   <MENU> Firewall
     (p)   <MENU> PPPoE
     (s)   <MENU> System
     (w)   <MENU> Wireless
     (x)   Exit
     (?)   Help
    =============================
    [Debug]: 
    
    
    ======= Console Debug =======
     (1)   Alert Mail Testing
     (2)   Web Upgrage
     (3)   Write Web
     (4)   Firmware Upgrage
     (5)   Write Firmware
     (6)   Warm Reboot
     (8)   Show B0,B1 Mem pool
     (a)   <MENU> gConfig
     (b)   <MENU> gSetting
     (c)   <MENU> DHCP Client
     (d)   <MENU> Dial
     (e)   <MENU> Ethernet
     (f)   <MENU> Firewall
     (p)   <MENU> PPPoE
     (s)   <MENU> System
     (w)   <MENU> Wireless
     (x)   Exit
     (?)   Help
    =============================
    [Debug]: 
    
    
    
    ========= Wireless ==========
     (2)   Enable/Disable Wireless Config
     (7)   Current channel
     (r)   Reset for COR=0x80
     (x)   Exit
     (?)   Help
    =============================
    [Debug|Wireless]: 
    
    
    ========= Wireless ==========
     (2)   Enable/Disable Wireless Config
     (7)   Current channel
     (r)   Reset for COR=0x80
     (x)   Exit
     (?)   Help
    =============================
    [Debug|Wireless]: 
    
    
    
    ========= Wireless ==========
     (2)   Enable/Disable Wireless Config
     (7)   Current channel
     (r)   Reset for COR=0x80
     (x)   Exit
     (?)   Help
    =============================
    [Debug|Wireless]: user_drv : main loop begin !!!
    
    
    
    ========= Wireless ==========
     (2)   Enable/Disable Wireless Config
     (7)   Current channel
     (r)   Reset for COR=0x80
     (x)   Exit
     (?)   Help
    =============================
    [Debug|Wireless]: period_task running 300
    
    user_drv : main loop begin !!!
    
    
    
    ========= Wireless ==========
     (2)   Enable/Disable Wireless Config
     (7)   Current channel
     (r)   Reset for COR=0x80
     (x)   Exit
     (?)   Help
    =============================
    [Debug|Wireless]: 
    Wireless enable : Y
    user_drv : main loop begin !!!
    
    
    
    ========= Wireless ==========
     (2)   Enable/Disable Wireless Config
     (7)   Current channel
     (r)   Reset for COR=0x80
     (x)   Exit
     (?)   Help
    =============================
    [Debug|Wireless]: 
    Wireless enable : N
    user_drv : main loop begin !!!
    
    Wireless enable : Y
    
    period_task running 360
    
    
    
    ======= Console Debug =======
     (1)   Alert Mail Testing
     (2)   Web Upgrage
     (3)   Write Web
     (4)   Firmware Upgrage
     (5)   Write Firmware
     (6)   Warm Reboot
     (8)   Show B0,B1 Mem pool
     (a)   <MENU> gConfig
     (b)   <MENU> gSetting
     (c)   <MENU> DHCP Client
     (d)   <MENU> Dial
     (e)   <MENU> Ethernet
     (f)   <MENU> Firewall
     (p)   <MENU> PPPoE
     (s)   <MENU> System
     (w)   <MENU> Wireless
     (x)   Exit
     (?)   Help
    =============================
    [Debug]: user_drv : main loop begin !!!
    
    
    
    
    ======== DHCP Client ========
     (0)   Release IP
     (1)   Renew IP
     (2)   Update IP
     (d)   Disable DHCP Client(gConfig)
     (e)   Enable DHCP Client(gConfig)
     (f)   Disable DHCP Client(gSetting)
     (g)   Enable DHCP Client(gSetting)
     (x)   Exit
     (?)   Help
    =============================
    [Debug|DHCP_CLT]: 
    
    
    ======== DHCP Client ========
     (0)   Release IP
     (1)   Renew IP
     (2)   Update IP
     (d)   Disable DHCP Client(gConfig)
     (e)   Enable DHCP Client(gConfig)
     (f)   Disable DHCP Client(gSetting)
     (g)   Enable DHCP Client(gSetting)
     (x)   Exit
     (?)   Help
    =============================
    [Debug|DHCP_CLT]: user_drv : main loop begin !!!
    user_drv : main loop begin !!!
    period_task running 420


# Bootloader


Here a copy of the sources for ADAM2 ([[file rebuilt.adam2-oleg.zip]]).

# Links


* <http://www.charlotte-et-sylvain.be/plus/occaz/>  
* http://oldwiki.openwrt.org/OpenWrtDocs(2f)Hardware(2f)3Com(2f)3CRWDR100A(2d)72.html
* <http://www.mirrorservice.org/sites/downloads.sourceforge.net/a/ar/ar7-firmware.berlios/>  
* <https://web.archive.org/web/20080108070730/http>  ://ar7-firmware.berlios.de/doc/loader.html.en