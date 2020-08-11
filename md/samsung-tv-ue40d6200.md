# Firmware


[T-GAS6DEUC_1014.0.exe](http://org.downloadcenter.samsung.com/downloadfile/ContentsFile.aspx?CDSite=UNI_BE&CttFileID=3856193&CDCttType=FM&ModelType=N&ModelName=UE40D6200TS&VPath=FM/201112/20111224123821980/T-GAS6DEUC_1015.2.exe)

# Binwalk



    zoobab@buzek /home/zoobab [178]$ binwalk T-GAS6DEUC_1014.0.exe 
    
    DECIMAL         HEX             DESCRIPTION
    -------------------------------------------------------------------------------------------------------
    34690220        0x21154AC       gzip compressed data, ASCII, has CRC, has comment, comment, encrypted, last modified: Sun Aug  3 00:52:36 2014
    39428785        0x259A2B1       JFFS2 filesystem (old) data big endian, JFFS node length: 312415


# dd



    zoobab@buzek /home/zoobab [179]$ dd if=T-GAS6DEUC_1014.0.exe of=file.gz bs=1 skip=34690220
    zoobab@buzek /home/zoobab [180]$ gunzip file.gz 
    gzip: file.gz is encrypted -- not supported


Trying with the jffs2 image:


    zoobab@buzek /home/zoobab [181]$ dd if=T-GAS6DEUC_1014.0.exe of=file.jffs2 bs=1 skip=39428785


Trying to mount the image:


    zoobab@buzek /home/zoobab [196]$ sudo bash
    root@buzek /home/zoobab [1]# mount -o loop -t jffs2 ./file.jffs2 ./dir
    mount: wrong fs type, bad option, bad superblock on /dev/loop0,
           missing codepage or helper program, or other error
           In some cases useful info is found in syslog - try
           dmesg | tail  or so


# Serial port


There seems to be a [3.3v serial port TTL](http://wiki.samygo.tv/index.php5/Ex-Link_Cable_for_C/D_Series) mapped on the VGA connector:

[[=image serial-port-3.3v-samsung-samygo.jpg size="medium"]]

[[=image serial-port-3.3v-samsung-samygo-3pins.jpg size="medium"]]

Here is the serial output from the bootloader stage:


    > S 0067 onboot(May 17 2011-16:18:53)
    GenoaS with Parma, GenoaS only [SELP] preset_lpj manual setting 2392064
    prefetch=0x71800000
    [SDP EINTR] 30 External interrupt is registered 
    [SDP EINTR] 31 External interrupt is registered 
    [SDP INTR MERGER] 29 interrupt merger is registered 
    [i2c_init] i2c 5 line is not initialize
    [i2c_init] i2c 6 line is not initialize
    [i2c_init] i2c 7 line is not initialize
    ================================================================================
     SAMSUNG Genoa-S Kernel
     Version : 1008 RELEASE
     Applied Last Patch Number : 0198
    ================================================================================
    init started: VDLinux-BusyBox v1.14.3-VD Linux VDLinux.1.2.1.x (2011-01-18 10:51:51 KST)
    starting pid 26, tty '/dev/ttyS3': '/etc/rc.local'
    /etc/rc.local start!!!!
    =====================================================================
      ROOTFS VERSION : "Genoa.S 1014" KERNEL MODULE VERSION : "1007_197"
    ===========================================##### send signal from USER, SIG : 0, init(1)->???(26) sys_kill
    starting pid 35, tty '/dev/ttyS3': '-/bin/sh'
    /etc/profile start!! 
    [sdp_mmch_isr] DTO Interrupt not caused!!!!
    ====================================================================
    [SELP] fsr module load!!(1007 RELEASE preempt mod_unload ARMv7 )
    ====================================================================
    ====================================================================
    [SELP] fsr_stl module load!!(1007 RELEASE preempt mod_unload ARMv7 )
    ====================================================================
    ====================================================================
    [SELP] rfs_glue module load!!(1007 RELEASE preempt mod_unload ARMv7 )
    ====================================================================
    ====================================================================
    [SELP] rfs_fat module load!!(1007 RELEASE preempt mod_unload ARMv7 )
    ====================================================================
    mount mtd_rwarea
    1st partition!!
    mount mtd_exe
    mount mtd_rocommon
    mount mtd_appext
    mount mtd_appext 1st partition!!!
    Application is started..
    Run FastLogo...
    ====================================================================
    [SELP] FastLogo module load!!(1008 RELEASE preempt mod_unload ARMv7 )
    ====================================================================
    ====================================================================
    [SELP] samdrv module load!!(1008 RELEASE preempt mod_unload ARMv7 )
    ====================================================================
    ##### System Execution!!! #####
     Call.. CFastBoot() 
    TDConfigList Building
    TDaStore Building...
    0. SEMCO DVB TC TDaTunerSemcoTC Building...
    0. SEMCO DVB TC TDaDemodSemcoTC Building...
    1. SEMCO DVB TCS TDaTunerSemcoTC SemcoSi2173 Building...
    1. SEMCO DVB TCS TDaDemodSemcoTC  SemcoSi2173 Building...
    [sdp_i2c_open] i2c 7 line is not initialize
    2. TDaTunerSkyISDB Building...
    2. TDaDemodSkyISDB Building...
    3. SEMCO Taiwan TDaTunerSemcoSiT Building...
    3. SEMCO Taiwan TDaDemodSemcoSiT Building...
    4. SEMCO Si2173 TDaTunerSi2173ATSC Building...
    4. SEMCO Si2173 TDaDemodulator Building...
    5. SEMCO SA/NT TDaTunerSemco Building...
    5. SEMCO SA/NT TDaDemodulator Building...
    6. TDaTunerSemcoISDB_TS Building...
    6. TDaDemodSemcoISDB_TS Building...
    7. TDaTunerSemcoISDB_TS Building...
    7. TDaDemodSemcoISDB_TS Building...
    9. SEMCO DVB T2CS2 Tuner  Building...
    9. SEMCO DVB T2CS2 Demoulator Building...
    10. SEMCO Si2173 TDaTunerSi2173DVB Building...
    10. SEMCO Si2173 TDsDemodSi2173DVB Building...
    11. SEMCO AVL Tuner T2CS2 Building...
    11. SEMCO  AVL Demodulator T2CS2 Building
    12. ALPS DVB TCS TDaTunerALPSTCS Building...
    12. ALPS DVB TCS TDaDemodALPSTCS  Building...
    TDaAudioAmp0 Building...
    TDaAudioAmp1 Building...
    new FunctionI2C...
    TDsSamMicomDownload...
    TDaSystem Building...
    TDaAudioProcessor Building...
    SDP1007 Processor Building...
    LEDDriver Building...
    TDaScaler0 Building...
    TDaScaler1 Building...
    TDaScaler2 Building...
    TDaScaler3 Building...
    TDaAnalogVideoProcessor Building...
    TDaDemux 0 Building...
    TDaDemux 1 Building...
    TDaMpeg Building...
    TDaMpeg Building...
    TDaCompProcessor Building...
    TDaHdmiProcessor Building...
    TDaPcProcessor Building...
    TDaHdmiSwitch Building...
    TDaCommonInterface Building...
    TDaSmartCardInterface Building...
    TDaFeeder Building...
    TDaImage Building...
    TDaTeleText Building...
    TDaRecorder 1 Building...
    TDaRecorder 2 Building...
    TDaAnalogVideoSwitch Building...
    TDaStore PC DDC Building...
    TDcSamGpio::Create...
    GASFRC3D/NAPOLI TDaPanel0[LCD] Building...
    GASFRC3D/NAPOLI TDaVideoEnhancer0[LCD] Building...
    TDaPanel1[PDP] Building...
    TDaVideoEnhancer1[PDP] Building...
    3D IC Building...
    TDaCP0 Building...
    TDaCP1 Building...
    	>>[ERR:TDcSamMicomInterface.cpp] HotelVar_Init():2453 Null Fuction Call !!!Must Check Implementation Code...
    	>>[ERR:TDcSamMicomInterface.cpp] t_Main_Hotel():2712 NULL - Hotel TV Function to set  Hotel Receive Flag
    [BootFromMicom]Get Boot Status : 1
    ############## Find Factory_Part1.dat File in mtd_exe ##################
    ############## Find Factory_Part2.dat File in mtd_exe ##################
    		FixedId : Nvram[23] vs File[23] 
    		WBId : Nvram[13] vs File[13]
    		WB ADC(Part1) Id : Nvram[11] vs File[11]
    		EER Basic Id : Nvram[120] vs File[120]
    		EERId Custom : Nvram[132] vs File[132]
    		FACId : Nvram[22] vs File[22]
    	>>[ERR:TDaSystem.cpp] InitSystemDevice_Hotel():3675 Null Fuction Call !!!Must Check Implementation Code...
    InitSystemDevice (GenoaS) DVB : Config file selected /mtd_exe/Genoa_S_DVB_PV_512M.cfg
    <-- SDAL VERSION : SDAL-GENOAS-COMMON-V1.0.27-110905-027 -->
    Running CheckMemoryMap....
     ******** spIIoSys_GetRevisionID ***********
     ******** spIIoSys_GetRevisionID = 1 ***********
    WARNING: This program not compiled for -t option
    Genoa-S CPLD CLK SettingsSdCommon_WriteRegister 0x300308a8:0x2
     SdCommon_WriteRegister 0x30030d88:0x7300
     [GS][TS_Margin][0]
    [GS][0x300308c4][Read][0x1]
    [GS][uiTempRegister][0]
    TS Hold Magin Settings 0
    	>>[ERR:TDsSystem.cpp] Create_Hotel():8973 NULL Fuction Call !!!Must Check Implementation Code...
    ##### TDsSystem::SetDependence Mode [3] 
    [CAM][Tick:2690]CAM Card Status changed : 2 -> 1
    Data Transferred to Store...[384]!!!
    Data Transferred to ScreenObject...[384]!!!
    [PVRSSFactory::Build(),LINE:82 ] 
    	>>[ERR:TDiDemodulator.cpp] InstallEwsCallBack():176 Null Fuction Call !!!Must Check Implementation Code...
    	>>[ERR:TDiDemodulator.cpp] InstallSignalQualityCallBack():182 Null Fuction Call !!!Must Check Implementation Code...
    API_DeviceInit
    [1;34;40m[Tuner Init] [Start :2980] 
    ========SEMCO Driver TCS 20101129 ===========
    ################ PANEL TYPE : 120Hz 2D TCON ################
    Initialize TCON
    Checking CPLD Blank...
    CPLD Size = 41390
    lFileSize = 41390
    CRC matched: CRC value = 446B
    CRC MATCHED, GO AHEAD!
    ACTION: BLANKCHECK
    *******************************************
    chiprev : 1
    Part : 73
    Rom ID : 7
    Major : 4
    Minor : 0
    *******************************************
    [Tuner Init]1. Firmware Load Start Time:3020
    == [20110301][EU Ver 13][US Ver 8]Update Load Firmware ROM 7==
    Unrecognized device
    elapsed time = 40 ms
    exec_result = 0
    exit_code = 6
    error_address = 0
    Device not recognized!
    CPLD Device is not found.
    DevLdAsic_Init <IN>
    	>>[ERR:TDsLocalDimmingPanel.cpp] Create():2349 LDAsic Init Error~!
    t_GENOAS_FRC3D_Init() : start 
    t_GASFRC3D_Init() : Start
    t_GASFRC3D_Set_Init() : Start 
    ====== Send Jack ID Command to SubMicom ! =====
    [t_SetDefaultInputVHzWithCountryType] (LocalSet:0xb)  (eInputVHz:0x2)
    t_GASFRC3D_Set_InitForNapoli() : readGPIOValue = GPIO_HIGH 
    t_PARMA_3D_Init() : start 
    t_PARMA3D_Init() : Start
    t_PARMA3D_Set_Init() : Start 
    t_PARMA3D_Chk_LedPdp() : [CHECK LCD_PDP] : [TD_PANEL_LCD], [Sel_Parma] : [E_PARMA3D_FOR_LED]
    [ERROR][Drv_IIC_RW():925] i2c read operation failed
    [ERROR][Drv_IIC_RW():926] requested channel : 6
    [ERROR][Drv_IIC_RW():927] requested chip id : 0xc0
    [ERROR][Drv_IIC_RW():939] requested sub addr : 0x50
    [ERROR][Drv_IIC_RW():942] requested byte count : 2
    ---------- can't open save file type [0] ------------
    [ERROR][Drv_IIC_RW():925] i2c read operation failed
    [ERROR][Drv_IIC_RW():926] requested channel : 6
    [ERROR][Drv_IIC_RW():927] requested chip id : 0xc0
    [ERROR][Drv_IIC_RW():939] requested sub addr : 0x50
    [ERROR][Drv_IIC_RW():942] requested byte count : 2
    ---------- can't open save file type [0] ------------
    [ERROR][Drv_IIC_RW():925] i2c read operation failed
    [ERROR][Drv_IIC_RW():926] requested channel : 6
    [ERROR][Drv_IIC_RW():927] requested chip id : 0xc0
    [ERROR][Drv_IIC_RW():939] requested sub addr : 0x50
    [ERROR][Drv_IIC_RW():942] requested byte count : 2
    ---------- can't open save file type [0] ------------
    	>>[ERR:PARMA3DShare.cpp] m_PARMA3D_ReadIIC():562 [PARMA3D] addr = 0x0500 Read fails
    t_PARMA3D_CheckExist() : uReadValue => [0x00000000]
    t_PARMA3D_CheckExist() : without PARMA3D!!!
    	>>[ERR:PARMA3DShare.cpp] t_PARMA3D_Set_Init():3833 PARMA3D is NOT DETECTED !!!! 
    	>>[ERR:PARMA3DShare.cpp] t_PARMA_3D_MajorCmd():790 PARMA3D is NOT DETECTED !!!! 
    [ERROR][Drv_IIC_RW():925] i2c read operation failed
    [ERROR][Drv_IIC_RW():926] requested channel : 5
    [ERROR][Drv_IIC_RW():927] requested chip id : 0xcc
    [ERROR][Drv_IIC_RW():939] requested sub addr : 0x13e4
    [ERROR][Drv_IIC_RW():942] requested byte count : 2
    ---------- can't open save file type [0] ------------
    [ERROR][Drv_IIC_RW():925] i2c read operation failed
    [ERROR][Drv_IIC_RW():926] requested channel : 5
    [ERROR][Drv_IIC_RW():927] requested chip id : 0xcc
    [ERROR][Drv_IIC_RW():939] requested sub addr : 0x13e4
    [ERROR][Drv_IIC_RW():942] requested byte count : 2
    ---------- can't open save file type [0] ------------
    [ERROR][Drv_IIC_RW():925] i2c read operation failed
    [ERROR][Drv_IIC_RW():926] requested channel : 5
    [ERROR][Drv_IIC_RW():927] requested chip id : 0xcc
    [ERROR][Drv_IIC_RW():939] requested sub addr : 0x13e4
    [ERROR][Drv_IIC_RW():942] requested byte count : 2
    ---------- can't open save file type [0] ------------
    	>>[ERR:NapoliShare.cpp] m_Napoli_ReadIIC():5165 [NAPOLI] addr = 0x13e4 Read fails
    m_SetBackendDevice() : Check Backend Device [0]
    t_GASFRC3D_Set_BackendDevice() : Check Backend Device [0]
    TDsGASFRC3DPanel::SetPanelInput Is Enable:0[BootFromMicom]Get Boot Status : 1
    [BootFromMicom]Get Master Power Reset : [0]
    Brightness Sensor is OK!!!
    SensorGain   = 16 
    fConstant[0] = 1527.378052 
    fConstant[1] = 1.983414 
    fConstant[2] = 0.101670 
    fConstant[3] = 0.152500 
    FBInfo.Validation = 1
    FBInfo.ChannelStatus = 1
    FBInfo.SourceID = 53
    FBInfo.SourceMode = 513
    FBInfo.AudioDescriptionID = 65535, AudioType = 65535
    		>>> t_GetFastBootInfo 0
    t_GASFRC3D_Ctrl_EmitterSync() : Start
    ##### TDsSystem::SetDependence Mode [2] 
    [TDaSystem::SamPivotModeConfig]SdCommon_PivotConfig is deleted !!!
    [TDaSystem::SamPivotModeConfig] PivotConfig Size [1920 * 1080], Mode [3]  
    Rectangle Helper Common FHD 1920*1080 Setting!!
    Country EU : Table index:0 Size of array:4 
    Country EU : Table index:1 Size of array:4 
    Country EU : Table index:2 Size of array:4 
    Country EU : Table index:3 Size of array:11 
    Country EU : Table index:4 Size of array:8 
    Country EU : Table index:5 Size of array:15 
    [TDaScaler::GetInitVideoConfig] (LocalSet:0xb) (PanelType:0x0) (BackendDevice:0x0) (GenoaS120HzPlusPanel:0x0) (ConfigType:0x1c80)
    [ERROR][SdGfx_Get():178] NULL Pointer Handling Error !!
    	>>[ERR:TDcGraphicScaler.cpp] t_GraphicGet():1279 [G-Main]Read fail Drv Data
    Rectangle Helper Common FHD 1920*1080 Setting!!
    Country EU : Table index:0 Size of array:4 
    Country EU : Table index:1 Size of array:4 
    Country EU : Table index:2 Size of array:4 
    Country EU : Table index:3 Size of array:11 
    Country EU : Table index:4 Size of array:8 
    Country EU : Table index:5 Size of array:15 
    [TDaScaler::GetInitVideoConfig] (LocalSet:0xb) (PanelType:0x0) (BackendDevice:0x0) (GenoaS120HzPlusPanel:0x0) (ConfigType:0x1c80)
    Rectangle Helper Common FHD 1920*1080 Setting!!
    Country EU : Table index:0 Size of array:4 
    Country EU : Table index:1 Size of array:4 
    Country EU : Table index:2 Size of array:4 
    Country EU : Table index:3 Size of array:11 
    Country EU : Table index:4 Size of array:8 
    Country EU : Table index:5 Size of array:15 
    [TDaScaler::GetInitVideoConfig] (LocalSet:0xb) (PanelType:0x0) (BackendDevice:0x0) (GenoaS120HzPlusPanel:0x0) (ConfigType:0x1c80)
    [ERROR][Mute():483] Not support Error, eVideoId : 2
    Rectangle Helper Common FHD 1920*1080 Setting!!
    Country EU : Table index:0 Size of array:4 
    Country EU : Table index:1 Size of array:4 
    Country EU : Table index:2 Size of array:4 
    Country EU : Table index:3 Size of array:11 
    Country EU : Table index:4 Size of array:8 
    Country EU : Table index:5 Size of array:15 
    [TDaScaler::GetInitVideoConfig] (LocalSet:0xb) (PanelType:0x0) (BackendDevice:0x0) (GenoaS120HzPlusPanel:0x0) (ConfigType:0x1c80)
    [ERROR][locSetSRSParam():1032] SRS : Not Support Mode (6)
    [1;41m Factory Data [39], Set Func Sensitivity [0x27] 
     WF Type : 0
    [1;41m Factory Data [0], Set Func Proximity [0x0] 
    	>>[ERR:TDsParma3DPanel.cpp] SetLVDSInputFormat():374 Not Define Dependence !!!
    [ Fast Boot ] [ Panel Control Type : 2 ] 
    	>>[ERR:TDiVideoEnhancer.cpp] SetPictureInformation():177 Null Fuction Call !!!Must Check Implementation Code...
    [Tuner Init]2. Firmware Load End Time:3600
    [Tuner Init]1. LoadVideofilter 3620
    [ Fast Boot ] [ Panel Control Type : 1 ] 
    ------------ PVCC Real On Off:1
    TDsGASFRC3DPanel::SetPanelInput Is Enable:1
     WooferType is NONE, skip initialize.
    ### eSrc 0x0, Audio Format [Not Support String 27], DDCompMode RF, Factory value -9, Real set value to SDAL 0
    [Tuner Init]2. LoadVideofilter 4000
    [Tuner Init]3. LoadVideofilter 4000
    [Tuner Init]2. Firmware Time:4000,FirmwareErrorStatus:0
    [Tuner Init] 1.Si2167_L1_Demod_init_after_reset :4010
    		>>> t_PlayMelody 0
    DOWNLOAD IS OK, CRC is good and equal to 0xe723 59171
    =====[20110331]Si2167 Patch Version 85=========
    [Tuner Init] 2.Si2167_L1_Demod_init_after_reset :4560
    SemcoSi_Configure Demod Version:Si2167_A10(0x311)
    LNB Chip Change INIT Read: 0x91
    [1;34;40m[Tuner Init][End :4560][SPEND TIME:1580ms]
    MonitorSemcoTCS Create
    Change TS Delay:0
    TS CLK Delay : 0 
    Country Set:11
    -------------------------------------------
    ===    Selected Tuner on Factory : 3 th !!! ===  
    -------------------------------------------
    SiI9489 Register value : 9489
     SiI9489 HDMI CheckNVM_VGA_EDID() is Success!!!!!!! 
     SiI9489 HDMI CheckNVM_EDID() is Success!!!!!!! 
     SII9489Monitor Create!
    ==== HDMI [SRC num :1], [ID: 0x47], [HP STATE: 0xf]
    LNB Power 13V
    Polarisation:4,bCableCompensation:0
    Set LNB Power!!! 1
    === [Num of Scart of this model : 1] ===
    === auto scart enable ===
    		>>> t_CheckFastBoot 1
    ============ CHECK FAST BOOT Exception ===========
    ------------ Inverter sw Real On Off:1
    4840 Set Panel mute Off 
    [TDsSamPanel::SetInverterForGenoaSPanelMute] Call bOnOff:1
    ------------ Inverter sw Real On Off:1
    	>>[ERR:TDiVideoEnhancer.cpp] SetPictureInformation():177 Null Fuction Call !!!Must Check Implementation Code...
    [ Fast Boot ] [ Panel Control Type : 3 ] 
    Alreay changed New MAC address, so that's ok
    	## Core Software Platform (TM) 1.1 : DTP-SP-0085 (RELEASE)
    		 Copyright (C) SAMSUNG Electronics Co.,Ltd.
    CSP No sched_yield()
    TCMW::Initialize() start
    [SS][EventSender::InstallFreezeCallback(),LINE:111 ] 
    [PVRSSFactory::getPVRSSRecorder(),LINE:199 ] " DriverType = [0] "
    [PVRSSFactory::getPVRSSRecorder(),LINE:200 ] " RecorderNumber = [0] , MaxRecorderNumber = [2] "
    [PVRSSFactory::getPVRSSRecorder(),LINE:214 ] " System RecorderDriver is Created"
    [PVRSSFactory::getPVRSSRecorder(),LINE:228 ] " PVRSSFactory will create m_recorder[0]"
    [SS] [ERR][RecordMonitor.cpp:stopRecordReadyAlram():173] readyAlarm is not created.
    [SS][ #-1 ][CRecordController::changeState(),LINE:371 ] " State Change : [NULL] ---> [RecorderNoneState] "
    [SS] [ERR][RecordMonitor.cpp:stopRecordReadyAlram():173] readyAlarm is not created.
    [PVRSSFactory::getPVRSSRecorder(),LINE:232 ] " PVRSSFactory will return m_recorder[0]"
    [PVRSSFactory::getPVRSSPlayer(),LINE:247 ] " DriverType = [0] "
    [PVRSSFactory::getPVRSSPlayer(),LINE:248 ] " PlayerNumber = [0], MaxPlayerNumber=[1] "
    [PVRSSFactory::getPVRSSPlayer(),LINE:261 ] " System PlayerDriver is Created "
    CTrickPlayerManager::GetTrickPlayerManager() m_pTrickPlayerManager == NULL)
    CTrickPlayerManager::GetTrickPlayerManager() GetTrickPlayer[0] == NULL)
    [PVRSSFactory::getPVRSSPlayer(),LINE:274 ] " PVRSSFactory will create m_player[0]"
    [SS] [PLY] [ PVRSSPlayer.cpp::CPVRSSPlayer(), LINE:42 ] 
    [PVRSSFactory::getPVRSSPlayer(),LINE:277 ] " PVRSSFactory will return m_player[0]"
    ProfileManager::t_CompareMagicKey() line[567]	Offset 0 Size 4]
    ProfileManager::t_CompareMagicKey() line[575]	CRC: 82251030, magicKey: 82251030
    ProfileManager::Init() line[75]	Mark 7209
     SII9489   Toggle HPD when Boot Up HDMI[1e]
    ##### TDsSystem::SetDependence Mode [4] 
    ################## Arsenal is Normal ##################
    Arsenal Reg : 0x805, Val : 0x1601
    ***** MICOM POWER OFF factory value[ON] ***** 
    		>>> CheckSystemNormal
            Profile        AgentID         Offset           Size
    [DEFAULT/Info] 0 :              43             17              0             2c
    [DEFAULT/Info] 1 : Data:
    [DEFAULT/Info] 2 : 0 0 0 0 0 0 cb be ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 
    [DEFAULT/Info] 3 : ff ff ff ff ff ff ff ff 0 0 0 0 
    [DEFAULT/Info] 4 : -----------------------------------------------------------------
    [DEFAULT/Info] 5 :              43             19             2c              c
    [DEFAULT/Info] 6 : Data:
    [DEFAULT/Info] 7 : 0 0 0 0 ff ff ff ff 1 3 c6 0 
    [DEFAULT/Info] 8 : -----------------------------------------------------------------
    [DEFAULT/Info] 9 :              43             21             38             10
    [DEFAULT/Info] 10 : Data:
    [DEFAULT/Info] 11 : ff ff ff ff ff ff ff ff ff ff 5a 6 ff ff ff ff 
    [DEFAULT/Info] 12 : -----------------------------------------------------------------
    [DEFAULT/Info] 13 :              43             23             48             24
    [DEFAULT/Info] 14 : Data:
    [DEFAULT/Info] 15 : 0 0 0 0 0 0 0 0 0 0 0 0 c 0 0 0 1 0 0 0 3c 0 0 0 1 0 0 0 0 0 0 0 
    [DEFAULT/Info] 16 : 0 0 0 0 
    [DEFAULT/Info] 17 : -----------------------------------------------------------------
    [DEFAULT/Info] 18 :              43             26             6c             18
    [DEFAULT/Info] 19 : Data:
    [DEFAULT/Info] 20 : ff ff ff ff 0 0 0 0 ff ff ff ff 0 0 0 0 ff ff ff ff 0 0 0 0 
    [DEFAULT/Info] 21 : -----------------------------------------------------------------
    [DEFAULT/Info] 22 : ####Reset TCTvManagerBase::Create####
    [DEFAULT/Info] 23 : ####Reset Channel Magic Key !  old = 1101004 new = 1101004 !!!####
    [DEFAULT/Debugging] 24 : FlagHospitalMode[0]
    [M_TMS/Fatal] 25 : TCServiceProviderMemory::Load() => Couldn't create file /mtd_chmap/ServiceProviders
    [M_TMS/Fatal] 26 : TCNameMemory::Load() => Couldn't create file /mtd_chmap/DefaultAuthority
    [M_TMS/Fatal] 27 : TCBouquetMemory::Load() => Couldn't create file /mtd_chmap/Bouquets
    [DEFAULT/Debugging] 28 : TCChSortModeDB::LoadSortMode Cannot Open File /mtd_chmap/ChSortMode
    [DEFAULT/Debugging] 29 : FlagUseHotelMixedMap, factoryMapUse[0]
    [DEFAULT/Debugging] 30 : FlagUseHotelMixedMap, hotelProductType[0]
    [DEFAULT/Debugging] 31 : TCTransponderAgent::m_Initialize, startTime[6140]
    [DEFAULT/Debugging] 32 : TCTransponderAgent::m_Initialize, EndTime[6210]
    [DEFAULT/Fatal] 33 : TCWindowInfoManager_DVB::t_ChangeCountry  (WindowId:1 TvMode:0  Country:69,BroadCasterId :-1)
    [DEFAULT/Fatal] 34 : TCWindowInfoManager_DVB::t_ChangeCountry  (WindowId:6 TvMode:0  Country:69,BroadCasterId :-1)
    [DEFAULT/Fatal] 35 : TCWindowInfoManager_DVB::t_ChangeCountry  (WindowId:7 TvMode:0  Country:69,BroadCasterId :-1)
    [DEFAULT/Fatal] 36 : TCWindowInfoManager_DVB::t_ChangeCountry  (WindowId:2 TvMode:0  Country:69,BroadCasterId :-1)
    [DEFAULT/Fatal] 37 : TCWindowInfoManager_DVB::t_ChangeCountry  (WindowId:4 TvMode:1  Country:69,BroadCasterId :-1)
    [DEFAULT/Fatal] 38 : TCWindowInfoManager_DVB::t_ChangeCountry  (WindowId:9 TvMode:0  Country:69,BroadCasterId :-1)
    [DEFAULT/Debugging] 39 : LSC Resource enabled! Network support : 2 (1 : Cable, 2 : WiFi Ext., 3: WiFi Int.
    [DEFAULT/Debugging] 40 : [TCIMSUtil::AddInfoManager] Failed to add InfoManager to list.
    [DEFAULT/Fatal] 41 : [t_FillChannelInfo] FoundChannel - retVal:0 65535(65535-65535),4
    [M_DSM_OC/Fatal] 42 : [TCObjManagerBase::Create] Country = 69 
    [M_DSM_OC/Fatal] 43 : [TCObjManagerBase::Create] PROFILE MHEG
    TCMW::Initialize() end
    Shadow 2.5 (revision number: DTP-BP-Shadow-0217-Genoa-DEU-09-Release) is being initialized.0 (4294967295): Initialize Cubic Motion Profile v2.5.0217-05
    [DTVInputService::t_Create] m_nKeyInputTime = 6670
    ################################
    t_InitializeComponentsProfile 
    ################################[DEFAULT/Warning] 44 : Specified confliction type has already been set !!
    [DEFAULT/Warning] 45 : Specified confliction type has already been set !!
    [DEFAULT/Warning] 46 : Specified confliction type has already been set !!
    [DEFAULT/Warning] 47 : Specified confliction type has already been set !!
    [DEFAULT/Warning] 48 : Specified confliction type has already been set !!
    [DEFAULT/Warning] 49 : Specified confliction type has already been set !!
    [DEFAULT/Warning] 50 : Specified confliction type has already been set !!
    ################################
    t_InitComponents 
    ################################[Error!!!] unsupported project country
    Not a GINGA_NCL build
    APP_INITIALIZE(); end
    [DEFAULT/Debugging] 51 : MW Initilize Completed
    [DEFAULT/Debugging] 52 : WaitForFastBoot End
    [DEFAULT/Debugging] 53 : TCBootingChannelInfo::Set is called...[BootReason : -1][RealBootReason : -1]
     TPCTv::Power, ######## 3 ######## Param : 0
    ==================================================
    ------------------- NORMAL MODE ------------------
    ==================================================
     TPCTv::Power, Return Value Check : 1
    ### eSrc 0x0, Audio Format [Not Support String 27], DDCompMode RF, Factory value -9, Real set value to SDAL 0
    [SS][EventSender::InstallEventCallback(),LINE:43 ] 
    ==================================================
    --------------- NORMAL MODE COMPLETE--------------
    ==================================================
    System proccess  >>>>>  [ SYSTEM_READY ] 
    ePowerType => POWER_TYPE_PICTURE_ON
    [TPAWindow.cpp][ConnectSource][WID:0][CALL]..
    Start System Monitor -> Reading:0, Channel:0x0, Slave_addr:[0x0][0x0]
    [TDScaler][Connect]eOutVideoID = 0x0, eBackendId = 0x4, eWindowID = 0x0
    [TDScaler]eExtOutId = 0xd, eOutVideoId = 0x0
    [TDScaler]eSource = 0x901, m_ePipSourceMode = 0x0, m_ePreSrcMode:0x0
    [TDScaler][VidId:0][3401] (CVBS OnOff:1)
    [Scaler]
     TDResolution_k : [15]
    TDResolutionInfo_t [720], [576], [0], [0], [864], [625], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [2305], [0], [4], [17], [0], [0]
    Source : 0x901, WindowType : 0 ExtInID : 0, BackEndID : 4, tdRet=0 
    ### eSrc 0x901, Audio Format [Not Support String 27], DDCompMode RF, Factory value -9, Real set value to SDAL 0
    SPI_ERROR[0xf03] = spIDp_SetScaling(hDp)
    [ERROR][Set():1364] Error : hdiExeScaling
    	>>[ERR:TDsSamVideoEnhancer.cpp] SetScartRGBVideoSignalTypeInfo():651  - SDAL ERROR [-1] !!!
    [TPAWindow.cpp][ConnectSource][WID:0][END]..
    SPI_ERROR[0xf03] = spIDp_SetSdScaling(hDp)
    [ERROR][Set():1364] Error : hdiExeScaling
    [TDScaler][VidId:2][770] (VideoOnOff:1)
    ==================== DCDsmManager pid = 61
    [1;34;40m[TCS TUNER][System:1][CurrentFreq: 0][CenterFreq :0][Symbol:0][BW:8,QAM:64][ASystem:0] 
    [0m 
    		Setting DVB-T Si2173_Configure
    [Check 3D Status...]
    3D Mode to Set: [0],
    [VSI] 3D Mode: [0],
    [DSP] 3D Mode: [0],
    [RES] 3D Mode: [0]
    Skip 3D Mode Last Memory Setting...[OFF] or Auto Detected 3D Mode!!!
    [Scaler]
     TDResolution_k : [15]
    TDResolutionInfo_t [720], [576], [0], [0], [864], [625], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [2305], [0], [4], [17], [0], [0]
    [BackEnd]
     TDResolution_k : [15]
    TDResolutionInfo_t [720], [576], [0], [0], [864], [625], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [2305], [0], [4], [17], [0], [0]
    	>>[ERR:TDsSamVideoEnhancer.cpp] m_SetWBColorToneFromFactory():8766 Invalid White Balance OSD 
    [TDaScaler][SetGeometry][ID:0]Geometry (0, 0, 1920, 1080)
    [TDaScaler][SetCapture][ID:0]Capture (30, 17, 658, 540)
    [ERROR][hdiSetAudioDelay():644] EXTOUT AUDIO DELAY : Extout source type is error(18)
    	>>[ERR:TDsSamAudioProcessor.cpp] t_SetAudioSpeakerDelay():2514  - SDAL ERROR [-1] !!!
    [1;34;40mTS Mute ON 
    ============>TDaShare::m_StreamPath:1
    	>>[ERR:TDiDemux.cpp] SetInputType():208 Null Fuction Call !!!Must Check Implementation Code...
    [TPAWindow.cpp][ConnectSource][WID:4][CALL]..
    [TDScaler][Connect]eOutVideoID = 0x2, eBackendId = 0x0, eWindowID = 0x3
    [TDScaler]eExtOutId = 0x1, eOutVideoId = 0x2
    [TDScaler]eSource = 0x201, m_ePipSourceMode = 0x0, m_ePreSrcMode:0x901
    [Scaler]
     TDResolution_k : [21]
    TDResolutionInfo_t [720], [576], [0], [0], [864], [625], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [513], [1], [0], [17], [0], [0]
    Source : 0x201, WindowType : 4 ExtInID : 0, BackEnd====================================================================
    [SELP] sdp_mac module load!!(1007 RELEASE preempt mod_unload ARMv7 )
    ====================================================================
    ID : 7, tdRet=0 
    [ERROR][StopPcr():595] [WARN] PCR is already stopped!! 
    	>>[ERR:TDsSamAudioProcessor.cpp] Connect():672  - SDAL ERROR [-1] !!!
    [TPAWindow.cpp][ConnectSource][WID:4][END]..
    	>>[ERR:TDiDemux.cpp] SetInputType():208 Null Fuction Call !!!Must Check Implementation Code...
    [ERROR][hdiAllocDec():2640] Video Format is Error 0x11 
    [ERROR][hdiAllocDec():2647] Decoder alloc fail
    [ERROR][SdAVDec_VideoStart():1123] <Out> Allocate VideoDecoder failed
    	>>[ERR:TDsSamMpeg.cpp] StartVideoDecoding():797  - SDAL ERROR [-1] !!!
    [ERROR][StartAudio():304] PLAY ENGINE FAIL 
    	>>[ERR:TDsSamMpeg.cpp] StartAudioDecoding():1986  - SDAL ERROR [-2] !!!
    [ERROR][StopPcr():595] [WARN] PCR is already stopped!! 
    	>>[ERR:TDsSamVideoEnhancer.cpp] m_SetWBColorToneFromFactory():8802 Invalid Color Tone(0)
    [(null)/Fatal] 54 : [SetEtherMAC][line:2021] Set MAC eth0 [8c:c8:cd:15:f3:a2]
    t_GASFRC3D_SetAutoMotionPlus() : Motion Plus Demo OFF
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Turn Glass to OFF
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Glass Callback not registered
    Set3DMode() : Start, TD3dEffectMode_k = 0, iVideoPlane = 0 iBackendDevice:0
    t_Set3DModeForGenoaAlone(): Game/MJC Mode is same 
    [ERROR][SetStereoscopicScreenMode():264] Not Supported StereoScopic Resolution(1920, 1080)!!!
    SetStereoscopicScreenMode, 395, Not supported Screen
    [M_EXT/Fatal] 55 : FlagSystemReady == false -> MUTE OFF by DMS
    ## [EnableScreen] Screen(0), Caller(2)
    ## [EnableScreen] Screen(1), Caller(2)
    [DEFAULT/Debugging] 56 : [t_OnSystemReady:6662] First, Display Channel Banner Start(8340)
    [TDScaler][VidId:0][544] (Mute OnOff:0)
    8c:c8:cd:15:f3:a2
    [AP_FRONTRUNNER/Fatal] 57 : [t_Create][line:225] Wired Module Loaded...
    [SSL_library_init] Initializing...
    mount mtd_emanual
    [A_APPMW/Fatal] 58 : [CAppUtil::CheckResetAfterPnpOTN]
    [A_APPMW/Fatal] 59 : [CAppUtil::CheckResetAfterPnpOTN] PnPcheck File doesn't exist
    [SSL_library_init] already intialized...
    [DevMgr/Fatal] 60 : [GetInstance:43] MutexSafeCreator Success...
    [DevMgr/Fatal] 61 : [Get:177] Device Manager START...
    [DevMgr/Fatal] 62 : [t_OnEvent:301] DeviceManager::MESSAGE_FLASH_INFO_UPDATED : DeviceKEY(1), DeviceID(0)
    	[virtual DevicePollingFLASH::~DevicePollingFLASH()]
    [AP_FRONTRUNNER/Fatal] 63 : [t_Create][line:235] DeviceManager Created...
    [AP_INFOLINK/Fatal] 64 : CNNaviAppBase::t_Create()
    [AP_INFOLINK/Fatal] 65 : CNNaviLoadingBase::Create()
    [AP_INFOLINK/Fatal] 66 : Create Loading OSD for TV or Monitor
    [AP_INFOLINK/Fatal] 67 : END CNNaviLoadingBase::Create()
    [AP_INFOLINK/Fatal] 68 : CNNaviMsg::Create()
    [A_MHEG_PORTING_LAYER/Fatal] 69 : CHTTPDispatcher: created m_pHttpIf
    [A_MHEG_PORTING_LAYER/Fatal] 70 : CHTTPDispatcher: created m_pHttps
    [A_MHEG_LIFECYCLE/Fatal] 71 : (g_pAppTV->ExistChannel(curCh.Key(), &ch) failed
    NetworkManager
    Create
    NetworkDHCPMonitor::GetInstance() 
    [A_MHEG_LIFECYCLE/Fatal] 72 : (g_pAppTV->ExistChannel(curCh.Key(), &ch) failed
     CEManualOSDInfo::Initialize()  ~~~~~ Current Pannel horizontal is 1920 
    [NET_MW/Fatal] 73 : [GetInstance][line:125] Already created...
    [AP_NET_SETUP/Fatal] 74 : [void CreateNetworkManager()][line:82]  [ StartDeviceMonitoring ] 
    BTHIDProfile : 1RemoteconServiceStatus : 1GlassesServiceStatus : 1BTAVProfile : 0HeadSetServiceStatus : 0[DEFAULT/Warning] 75 : Specified confliction type has already been set !!
     bootReason not BOOT_REASON_ONTIME!! (-1) 
     CMediaAppUtil::IsMediaSource() false! 
    [DEFAULT/Debugging] 76 :  [CMovieDemoAppBase::t_Create - 103] Begin
    [DEFAULT/Debugging] 77 :  [CMovieDemoAppBase::t_Create - 174] End
    [PSA] [CheckPlayreadyKey:356] PlayReady Key (in SS) is already exist.
    [SSL_library_init] already intialized...
    [CIP_KERNEL] /dev/tfsr6
    [CIP_KERNEL] ae5c is authuld length : file open success(rootfs)  
    [CIP_KERNEL] >>> (/bin/authuld) file is successfully authenticated <<< 
    [0;31;40m[CIP_AUTHULD] 
    [0;37;40m====================================================
    [0;31;40m[CIP_AUTHULD] 
    [0;37;40m	     Authuld Version : 1.6 : REL
    [0;31;40m[CIP_AUTHULD] 
    [0;37;40m====================================================
    [NET_MW/Fatal] 78 : [GetNetworkInfo][line:340] file path = /mtd_rwarea/network_Wired_info not found. Initialize the info file.... 
    [NET_MW/Fatal] 79 : [GetDNSMode][line:873] file path = /mtd_rwarea/network_Wired_info not found. Initialize the info file.... 
    NetworkDHCPMonitor::GetInstance() 
    Already created...
    => Auto : ifconfig eth0 up
    [ERROR][StopPcr():595] [WARN] PCR is already stopped!! 
    [ERROR][StopPcr():595] [WARN] PCR is already stopped!! 
    [ERROR][StartAudio():304] PLAY ENGINE FAIL 
    	>>[ERR:TDsSamMpeg.cpp] StartAudioDecoding():1986  - SDAL ERROR [-2] !!!
    [Scaler]
     TDResolution_k : [21]
    TDResolutionInfo_t [720], [576], [0], [0], [864], [625], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [513], [1], [0], [17], [0], [0]
    [TDaScaler][SetGeometry][ID:2]Geometry (0, 0, 720, 576)
    SPI_ERROR[0xf03] = spIDp_SetSdScaling(hDp)
    [ERROR][Set():1364] Error : hdiExeScaling
    	>>[ERR:TDsSamScaler.cpp] SetGeometry():863  - SDAL ERROR [-1] !!!
    	>>[ERR:TDsSamScaler.cpp] SetGeometry():868 [ID:2]It failed in setting a geometry!!! (0, 0, 720, 576)
    [TDaScaler][SetCapture][ID:2]Capture (0, 0, 720, 576)
    	>>[ERR:TDiSystem.cpp] SetNetworkInitialized():960 Null Fuction Call !!!Must Check Implementation Code...
    [DEFAULT/Warning] 80 : Specified confliction type has already been set !!
    UPnP_ERR::	DLNA: DLNA UPnP_CD_RegisterCallback(dmr/SamsungMRDesc.xml) --> handle [0]
    [NET_SS/Fatal] 81 : [ActivateDHCP][line:658] udhcpc -i eth0 -T 2 -b&
    udhcpc (v1.14.3-VD Linux VDLinux.1.2.1.x) started
    Sending discover...
    Sending select for 192.168.42.141...
    Lease of 192.168.42.141 obtained, lease time 43200
    bool checkFilesState(const char*) XML files are good
    UPnP_ERR::	DLNA: DLNA UPnP_CD_RegisterCallback(rcr/RemoteControlReceiver.xml) --> handle [1]
    Mutex Create Successful
    deleting routers
    route: ioctl 0x890c failed: No such process
    Mutex Create Successful
    [AP_FRONTRUNNER/Fatal] 82 : [t_OnEvent][line:345] MESSAGE_APP_INITIALIZED received
    [DevMgr/Fatal] 83 : [ExecuteCommand:475] COMMAND_LOAD_USB_MODULES...
    [DevMgr/Fatal] 84 : [Get:43] DeadlockProber Success...
    [LoadUSBModules:1117] Start...
    adding dns 192.168.42.1
    osl_wireless_initialization~!!
    LLTD Service Start~!!
    DEVICE =  eth0
    DEVICE =  eth0
    [AP_SWU/Fatal] 85 : [IsDualBSP][line:1371] This is Dual BSP!!!!!!!!!!!!!!!!!!
    DEVICE =  eth0
    DEVICE =  eth0
    DEVICE =  eth
    [AP_SWU/Fatal] 86 : [m_Check_VirtualPartition][line:8031] Single User Upgrade
    	insmod usbcore...
    	insmod ehci_hcd...
    ####### Header = 12, 0
    	insmod ohci_hcd...
    	insmod usb_storage...
    USB : Exit Load USB module... Elapsed Time:1150msec.
    [DevMgr/Fatal] 87 : [ExecuteCommand:502] Case(4) Done... Elapsed Time:1150msec.
    [AP_FRONTRUNNER/Fatal] 88 : [t_OnEvent][line:355] USB Module Loaded...
    [DevMgr/Fatal] 89 : [ExecuteCommand:442] COMMAND_START_MONITORING...
    	usb_storage found...
    	ohci_hcd found...
    	ehci_hcd found...
    	usbcore found...
    [DevMgr/Fatal] 90 : [t_OnEvent:301] DeviceManager::MESSAGE_FLASH_INFO_UPDATED : DeviceKEY(1), DeviceID(0)
    [DevMgr/Fatal] 91 : [t_OnEvent:231] DeviceManager::MESSAGE_USB_INSMOD_COMPLETE : (15)
    [AP_BT_APP/Fatal] 92 : [virtual bool CBluetoothAppBase::t_OnEvent(const PTEvent*)][line:1361] [CBluetoothAppBase]MESSAGE_USB_INSMOD_COMPLETE
    [BT_SS/Fatal] 93 : [LoadBluetoothModule][line:114] [BluetoothUtility] /sbin/insmod /mtd_cmmlib/BT_LIB/btusb.ko
    [DEFAULT/Debugging] 94 :  [CUSBApp::t_OnEvent - 304] 
    [DEFAULT/Debugging] 95 :  [CUSBApp::t_OnEvent - 304] 
    [DEFAULT/Debugging] 96 :  [CUSBApp::t_OnEvent - 304] 
    [DEFAULT/Debugging] 97 :  [CUSBApp::t_OnEvent - 304] 
    [DEFAULT/Debugging] 98 :  [CUSBApp::t_OnEvent - 304] 
    [DEFAULT/Debugging] 99 :  [CUSBApp::t_OnEvent - 304] 
    [DEFAULT/Debugging] 100 :  [CUSBApp::t_OnEvent - 304] 
    [DEFAULT/Debugging] 101 :  [CUSBApp::t_OnEvent - 304] 
    [DEFAULT/Debugging] 102 :  [CUSBApp::t_OnEvent - 304] 
    [DEFAULT/Debugging] 103 :  [CUSBApp::t_OnEvent - 304] 
    [DEFAULT/Debugging] 104 :  [CUSBApp::t_OnEvent - 304] 
    [DEFAULT/Debugging] 105 :  [CUSBApp::t_OnEvent - 304] 
    [DEFAULT/Debugging] 106 :  [CUSBApp::t_OnEvent - 304] 
    [DEFAULT/Debugging] 107 :  [CUSBApp::t_OnEvent - 304] 
    [DEFAULT/Debugging] 108 :  [CUSBApp::t_OnEvent - 304] 
    [DEFAULT/Debugging] 109 :  [CUSBApp::t_OnEvent - 304] 
    [DEFAULT/Debugging] 110 :  [CUSBApp::t_OnEvent - 304] 
    [DEFAULT/Debugging] 111 :  [CUSBApp::t_OnEvent - 304] 
    [DEFAULT/Debugging] 112 :  [CUSBApp::t_OnEvent - 304] 
    ====================================================================
    [SELP] btusb module load!!(1008 RELEASE preempt mod_unload ARMv7 )
    ====================================================================
    [DEFAULT/Debugging] 113 :  [CUSBApp::t_OnEvent - 304] 
    [DEFAULT/Debugging] 114 :  [CUSBApp::t_OnEvent - 304] 
    [DEFAULT/Debugging] 115 :  [CUSBApp::t_OnEvent - 304] 
    [DevMgr/Fatal] 116 : [InitiateAllDevices:722] All devices are initiated!!!
    [DevMgr/Fatal] 117 : [ExecuteCommand:502] Case(2) Done... Elapsed Time:60msec.
    [AP_FRONTRUNNER/Fatal] 118 : [t_OnEvent][line:373] StartMonitoring Done...
    [BT_MW/Fatal] 119 : [LoadBluetoothModule][line:373] OK!!!
    usb 3-1: This device have invalid speed info
    usb 3-1: If you see this error log, please send me log and connecting device info.  Kim, Kyung-Sik(ksfree.kim@samsung.com)
    [NET_SS/Fatal] 120 : [LoadWirelessStaModule][line:2827] NETWORK TYPE : NETWORK_SUPPORT_WIFI_EXT
    [NET_SS/Fatal] 121 : [LoadWirelessStaModule][line:2845] WIFI MODULE - EXT TYPE (RALINK STA)
    [NET_SS/Fatal] 122 : [LoadWirelessStaModule][line:2908] insmod rtutil3572sta.ko ...
    [NET_SS/Fatal] 123 : [LoadWirelessStaModule][line:2910] insmod rtutil3572sta.ko ... - Done !!
    [NET_SS/Fatal] 124 : [LoadWirelessStaModule][line:2918] insmod rt3572sta.ko ...
    [NET_SS/Fatal] 125 : [LoadWirelessStaModule][line:2920] insmod rt3572sta.ko ... - Done !!
    [NET_SS/Fatal] 126 : [LoadWirelessStaModule][line:2928] insmod rtnet3572sta.ko ...
    [NET_SS/Fatal] 127 : [LoadWirelessStaModule][line:2930] insmod rtnet3572sta.ko ... - Done !!
    usb 3-1.1: This device have invalid speed info
    usb 3-1.1: If you see this error log, please send me log and connecting device info.  Kim, Kyung-Sik(ksfree.kim@samsung.com)
    usb 3-1.2: This device have invalid speed info
    usb 3-1.2: If you see this error log, please send me log and connecting device info.  Kim, Kyung-Sik(ksfree.kim@samsung.com)
    usb 3-1.3: This device have invalid speed info
    usb 3-1.3: If you see this error log, please send me log and connecting device info.  Kim, Kyung-Sik(ksfree.kim@samsung.com)
    [BT_SS/Fatal] 128 : [StartBluetoothServer][line:145] /mtd_cmmlib/BT_LIB/bsa_server -all=0 -u /mtd_rwarea/&
    [BT_MW/Fatal] 129 : [InitializeBluetooth][line:443] OK!!!
    sd 0:0:0:0: [sda] Assuming drive cache: write through
    sd 0:0:0:0: [sda] Assuming drive cache: write through
    BSA_trace 1@00h:00m:15s:396ms: Starting Bluetooth Daemon
    BSA_trace 2@00h:00m:15s:440ms: Command [all] with arg [0]
    BSA_trace 3@00h:00m:15s:440ms: [ all ] trace level = 0
    [DevMgr_MSC/Fatal] 130 : [Update:320] Total:1   Modified:0   Added:1   Removed:0
    [DEFAULT/Debugging] 131 :  [CUSBApp::t_OnEvent - 304] 
    	[222] Add New Device : 0
    [DevMgr/Fatal] 132 : [t_OnEvent:194] DeviceManager::MESSAGE_MSC_CONNECTED : DeviceKEY(2), DeviceID(0)
    >>>==================================================
    MSC Device# : 1
    	Device ID = 0
    	  Device Name = sda
    	  Vendor Name = LaCie   
    	  Model Name = iamaKey         
    	  Serial Number = 2713bbe37a9026
    	  BUS Info = 2-1.4
    	  LUN = 0
    		Partition ID = 0
    		  SCSI Device Path = /dev/sda
    		  Mount Path = /dtv/usb/sda
    		  File System Type = VFAT
    		  Total/Free = 3940824/725132
    ==================================================<<<
    [DEFAULT/Debugging] 133 :  [CUSBApp::ValidationCheck - 561] 
    [DEFAULT/Debugging] 134 :  [CUSBApp::CanDemoPlay - 585] 
    [DEFAULT/Debugging] 135 :  [CUSBApp::CheckAndActivateDemo - 428] false  
    [/dtv/usb/sda/SMRTNTKY/WSETTING.WFC]
    [ GetPlugAccessInfo FALSE]
    [DEFAULT/Debugging] 136 :  [CUSBApp::CheckPlugAccess - 451] CheckPlugAccess  false  
    [DEFAULT/Debugging] 137 :  [CUSBApp::OnPartitonAddedEvent - 629]  Booting Time 
    [BT_SS/Fatal] 138 : [ReadRomBdAddress][line:1831] [BluetoothDeviceBroadcom::ReadRomBdAddress]Flash BD address: 60-6B-BD-BD-AE-59
    [BT_SS/Fatal] 139 : [Set3DSyncDetection][line:2475] Set3DSyncDetection : [Disable]
    [BT_SS/Fatal] 140 : [ReadRomBdAddress][line:1831] [BluetoothDeviceBroadcom::ReadRomBdAddress]Flash BD address: 60-6B-BD-BD-AE-59
    [BT_SS/Fatal] 141 : [Set3DModeOffSetForBroadCast][line:2178] m_b3DOffsetBroadcast[0], m_frame_period[60001]... I would make 3DGS as open
    FIXED SELP: no partition Media Connected
    [BT_MW/Fatal] 142 : [StartBluetooth][line:645] OK!!!
    [AP_BT_APP/Fatal] 143 : [virtual bool CBluetoothAppBase::t_OnEvent(const PTEvent*)][line:1198] [CBluetoothAppBase]EVENT_BT_SERVICE_STARTED
    [BT_SS/Fatal] 144 : [SetShutterInfoForBroadCast][line:2452] shutter info exceeds 65535. m_frame_period[60001], m_DutyForShuttering[125]
    [BT_SS/Fatal] 145 : [Set3DModeOffSetForBroadCast][line:2178] m_b3DOffsetBroadcast[0], m_frame_period[60001]... I would make 3DGS as open
    [BT_SS/Fatal] 146 : [Set3DOffsetBroadcastOnOff][line:2460] Set3DOffsetBroadcastOnOff : [Disable]
    [BT_SS/Fatal] 147 : [SetShutterInfoForBroadCast][line:2452] shutter info exceeds 65535. m_frame_period[60001], m_DutyForShuttering[125]
    [BT_SS/Fatal] 148 : [Set3DModeOffSetForBroadCast][line:2178] m_b3DOffsetBroadcast[0], m_frame_period[60001]... I would make 3DGS as open
    [BT_SS/Fatal] 149 : [Set3DSyncDetection][line:2475] Set3DSyncDetection : [Disable]
    [A_APPMW/Fatal] 150 : >>>> Function OSD Type : NOT SUPPORT
    [CIP_KERNEL] Success!! Authuld is successfully completed.
    ==================== DCSwdManager pid = 61
    [TDScaler][VidId:0][544] (Mute OnOff:1)
    [TPAWindow.cpp][DisconnectSource][WID:0][CALL]..
    [Check 3D Status...]
    3D Mode to Set: [0],
    [VSI] 3D Mode: [0],
    [DSP] 3D Mode: [0],
    [RES] 3D Mode: [0]
    Skip 3D Mode Last Memory Setting...[OFF] or Auto Detected 3D Mode!!!
    [TDScaler][Disconnect] (VideoId:0)
    [TPAWindow.cpp][DisconnectSource][WID:0][END]..
    [TPAWindow.cpp][ConnectSource][WID:0][CALL]..
    [TDScaler][Connect]eOutVideoID = 0x0, eBackendId = 0x0, eWindowID = 0x0
    [TDScaler]eExtOutId = 0xd, eOutVideoId = 0x0
    [TDScaler]eSource = 0x201, m_ePipSourceMode = 0x0, m_ePreSrcMode:0x901
    [TDScaler][VidId:0][3401] (CVBS OnOff:1)
    ####### Header = 12, 0
    [36:640230][DEBUG][CUniPlayerMediator][18] 
    [36:640707][DEBUG][InstallResolutionCallback][648] 
    [36:640983][DEBUG][InstallResolutionCallbackForClip][657] 
    [Scaler]
     TDResolution_k : [21]
    TDResolutionInfo_t [720], [576], [0], [0], [864], [625], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [513], [0], [4], [17], [0], [0]
    Source : 0x201, WindowType : 0 ExtInID : 0, BackEndID : 7, tdRet=0 
    ### eSrc 0x201, Audio Format [Not Support String 27], DDCompMode RF, Factory value -9, Real set value to SDAL 0
    [InstallAudioMuteCallback][894]
    [TPAWindow.cpp][ConnectSource][WID:0][END]..
    [TDScaler][VidId:0][544] (Mute OnOff:1)
    [ERROR][StopPcr():595] [WARN] PCR is already stopped!! 
    [ERROR][StopPcr():595] [WARN] PCR is already stopped!! 
    [ERROR][StartAudio():304] PLAY ENGINE FAIL 
    	>>[ERR:TDsSamMpeg.cpp] StartAudioDecoding():1986  - SDAL ERROR [-2] !!!
    [Scaler]
     TDResolution_k : [21]
    TDResolutionInfo_t [720], [576], [0], [0], [864], [625], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [513], [1], [0], [17], [0], [0]
    [Check 3D Status...]
    3D Mode to Set: [0],
    [VSI] 3D Mode: [0],
    [DSP] 3D Mode: [0],
    [RES] 3D Mode: [0]
    Skip 3D Mode Last Memory Setting...[OFF] or Auto Detected 3D Mode!!!
    [Check 3D Status...]
    3D Mode to Set: [0],
    [VSI] 3D Mode: [0],
    [DSP] 3D Mode: [0],
    [RES] 3D Mode: [0]
    Skip 3D Mode Last Memory Setting...[OFF] or Auto Detected 3D Mode!!!
    [Scaler]
     TDResolution_k : [21]
    TDResolutionInfo_t [720], [576], [0], [0], [864], [625], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [513], [0], [4], [17], [0], [0]
    [BackEnd]
     TDResolution_k : [21]
    TDResolutionInfo_t [720], [576], [0], [0], [864], [625], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [513], [0], [4], [17], [0], [0]
    [TDaScaler][SetGeometry][ID:0]Geometry (0, 0, 1920, 1080)
    [TDaScaler][SetCapture][ID:0]Capture (0, 0, 720, 576)
    [ERROR][hdiSetAudioDelay():644] EXTOUT AUDIO DELAY : Extout source type is error(18)
    	>>[ERR:TDsSamAudioProcessor.cpp] t_SetAudioSpeakerDelay():2514  - SDAL ERROR [-1] !!!
    Motion Plus setting same...
    t_GASFRC3D_SetAutoMotionPlus() : Motion Plus Demo OFF
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Turn Glass to OFF
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Glass Callback Registered, Run Callback. (3D : OFF, Param : 109122216)
    [BT_SS/Fatal] 151 : [Set3DOffsetBroadcastOnOff][line:2460] Set3DOffsetBroadcastOnOff : [Disable]
    [BT_SS/Fatal] 152 : [SetShutterInfoForBroadCast][line:2452] shutter info exceeds 65535. m_frame_period[60001], m_DutyForShuttering[125]
    [BT_SS/Fatal] 153 : [Set3DModeOffSetForBroadCast][line:2178] m_b3DOffsetBroadcast[0], m_frame_period[60001]... I would make 3DGS as open
    [BT_SS/Fatal] 154 : [Set3DSyncDetection][line:2475] Set3DSyncDetection : [Disable]
    Set3DMode() : Start, TD3dEffectMode_k = 0, iVideoPlane = 0 iBackendDevice:0
    t_Set3DModeForGenoaAlone(): Game/MJC Mode is same 
    [ERROR][SetStereoscopicScreenMode():264] Not Supported StereoScopic Resolution(1920, 1080)!!!
    SetStereoscopicScreenMode, 395, Not supported Screen
    ## RunApp [CallThread=0x6a629460] App (2) runs App(ChannelSearch:8), nRunData(0x0), nRunOption(0x0) ##
    DynamicControl:7, FullOSD:true 
    ####### Header = 12, 0
    ## StopApp [CallThread=0x70a6b460] App (8) stops App(ChannelSearch:8), nStopData(0x0), nStopOption(0x8) ##
    DynamicControl:7, FullOSD:false 
    [A_MHEG_LIFECYCLE/Fatal] 155 : (g_pAppTV->ExistChannel(curCh.Key(), &ch) failed
    ####### Header = 12, 0
    [AP_INFOLINK/Fatal] 156 : Call START BG Mode!!!
    [AP_INFOLINK/Fatal] 157 : GetCurrentFC Return True
    [AP_INFOLINK/Fatal] 158 : GetCurrentFC LineValue is = [0]
    [AP_INFOLINK/Fatal] 159 : START BG Mode!!!
    [SSL_library_init] already intialized...
    [AP_INFOLINK/Fatal] 160 : CInfoLink2WrapperReal::dlopenWrapper()
    [AP_INFOLINK/Fatal] 161 : filename is = [libSefBroker.so]
    [AP_INFOLINK/Fatal] 162 : END CInfoLink2WrapperReal::dlopenWrapper()
    [CSEFDebug::Create(16)] Creator called.
    [CSEFDebug::SetLogLevel(31)] level = 0
    [CSEFDebug::SetDebugModule(46)] Log module = 0, onOff = 0
    [CSEFDebug::SetDebugModule(46)] Log module = 1, onOff = 0
    [CSEFDebug::SetDebugModule(46)] Log module = 2, onOff = 0
    ## RunApp [CallThread=0x6a629460] App (2) runs App(Source Browser:11), nRunData(0x0), nRunOption(0x0) ##
    [A_SOURCE_BROWSER/Fatal] 163 : CSourceApp::t_OnEndActivating()
    [AP_INFOLINK/Fatal] 164 : Update is False
    [AP_INFOLINK/Fatal] 165 : *****************************************************
    [AP_INFOLINK/Fatal] 166 : **** Infomation for connecting with hub-site ****
    [AP_INFOLINK/Fatal] 167 : *****************************************************
    [AP_INFOLINK/Fatal] 168 :  Server Type : Operating
    [AP_INFOLINK/Fatal] 169 :  TVID : H3CN4UQJFDTJM
    [AP_INFOLINK/Fatal] 170 :  Mac Address : 8cc8cd15f3a2
    [AP_INFOLINK/Fatal] 171 :  Firmware : T-INFOLINK2011-1007
    [AP_INFOLINK/Fatal] 172 :  Country Code : BE
    [AP_INFOLINK/Fatal] 173 :  Model Code : Genoa
    [AP_INFOLINK/Fatal] 174 : *****************************************************
    [AP_INFOLINK/Fatal] 175 : Update is True
    [A_SOURCE_BROWSER/Fatal] 176 : [CSourceManagerUtil::GetList()] [217] ulPlugStatus = 700000 
    [GetIcon]  device id = -1 , return NULL!!!  
    ####### Header = 12, 0
    [GetIcon]  device id = -1 , return NULL!!!  
    [AP_INFOLINK/Fatal] 177 : Verify Path = [/mtd_down/widgets/manager/10110000001]
    [WPS]: HW protection
    verified = 1
    [AP_INFOLINK/Fatal] 178 : CNNaviAppBase::SaveUnsafeMode()
    [AP_INFOLINK/Fatal] 179 : Create Widget Manager ID => 10110000001
    (DbgMaple) [AP_BROWSER/Fatal] 180 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/ae/aeWidgetEngine.cpp:901 in createSmartSideBarByWidgetInfo() 
    (DbgMaple) [AP_BROWSER/Fatal] 181 : Enter createSmartSideBar (id : 10110000001)
    (DbgMaple) [AP_BROWSER/Fatal] 182 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/am/amWidget.cpp:50 in onTaskCreate() 
    (DbgMaple) [AP_BROWSER/Fatal] 183 : Enter CWidget::onTaskCreate (widget : 0x6b6c008[10110000001], task : 0x6b6c0b0) (SCREEN NUMBER=1)
    (DbgMaple) [AP_BROWSER/Fatal] 184 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/ae/aeWidgetEngine.cpp:1077 in createSmartSideBarByWidgetInfo() 
    (DbgMaple) [AP_BROWSER/Fatal] 185 : Exit createSmartSideBar (id : 10110000001)
    [AP_INFOLINK/Fatal] 186 : CWidgetEngine::createSmartSideBar returns TRUE
    [AP_INFOLINK/Fatal] 187 : Unsafe Mode --> Wait Mode
    [AP_INFOLINK/Fatal] 188 : Call activateSmartSideBar
    (DbgMaple) [AP_BROWSER/Fatal] 189 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/ae/aeWidgetEngine.cpp:1223 in activateSmartSideBar() 
    (DbgMaple) [AP_BROWSER/Fatal] 190 : Enter activateSmartSideBar (id : 10110000001)
    (DbgMaple) [AP_BROWSER/Fatal] 191 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/am/amManagerWidget.cpp:457 in onActivateManagerWidget() 
    (DbgMaple) [AP_BROWSER/Fatal] 192 : onActivateManagerWidget
    (DbgMaple) [AP_BROWSER/Fatal] 193 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/plProcess.c:767 in pl_InitStaticPLClass() 
    (DbgMaple) [AP_BROWSER/Fatal] 194 : [Maple Side Plugin] "Camera" plugin is not supported in this application.
    (DbgMaple) [AP_BROWSER/Fatal] 195 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/plProcess.c:767 in pl_InitStaticPLClass() 
    (DbgMaple) [AP_BROWSER/Fatal] 196 : [Maple Side Plugin] "Skype" plugin is not supported in this application.
    (DbgMaple) [AP_BROWSER/Fatal] 197 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/plProcess.c:767 in pl_InitStaticPLClass() 
    (DbgMaple) [AP_BROWSER/Fatal] 198 : [Maple Side Plugin] "Remote" plugin is not supported in this application.
    (DbgMaple) [AP_BROWSER/Fatal] 199 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/ae/aeWidgetEngine.cpp:1253 in activateSmartSideBar() 
    (DbgMaple) [AP_BROWSER/Fatal] 200 : Exit activateSmartSideBar (id : 10110000001)
    [AP_INFOLINK/Fatal] 201 : CWidgetEngine::activateSmartSideBar returns TRUE
    [AP_INFOLINK/Fatal] 202 : Update is True
    [AP_INFOLINK/Fatal] 203 : Start!!! Waiting Activate Ready Event for Changing Wait Mode => Safe Mode!!
    ## StopApp [CallThread=0x70c6b460] App (11) stops App(Source Browser:11), nStopData(0x0), nStopOption(0x0) ##
    [A_SOURCE_BROWSER/Fatal] 204 : CSourceApp::t_OnEndDeactivating()
    ####### Header = 12, 0
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 58284
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 42328
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 42322
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 45702
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 53299
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 44496
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 34906
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 35490
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 41004
    [0m 
    Singletone emp is running. name:[AppCommon] Emp:[42328] , Client:[41004] ,  Option:[SINGLETON]  , Status:[2][CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 34635
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 47969
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 35482
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 39278
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 34507
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 39918
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 56668
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 41372
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 58545
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 59603
    [0m 
    Task GetSystemVersion : [1] 
    (DbgAlert) [AP_WIDGET/Fatal] 205 : alert() : [Smart Hub Log] [Widget Manager Ver.]  3.624
    (DbgAlert) [AP_WIDGET/Fatal] 206 : alert() : [Smart Hub Log] [Browser Ver.] 6.0.00067(Windows; U; en-US; rv:1.8.1.11; Gecko/20071129; Firefox/2.5.0)
    Task GetSystemVersion : [0] 
    (DbgAlert) [AP_WIDGET/Fatal] 207 : alert() : [Smart Hub Log] [LEEUM Ver.] DTP-BP-0621-42
    (DbgAlert) [AP_WIDGET/Fatal] 208 : alert() : [Smart Hub Log] [COMP Ver.] DTP-AP-COMP-639-Genoa_DEU-74
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 42848
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 59025
    [0m 
    GetServerType in plNNavi_pscomm.cpp . line 287
    (DbgMaple) [AP_BROWSER/Fatal] 209 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/am/amManagerWidget.cpp:457 in onActivateManagerWidget() 
    (DbgMaple) [AP_BROWSER/Fatal] 210 : onActivateManagerWidget
    (DbgAlert) [AP_WIDGET/Fatal] 211 : alert() : [Smart Hub Log] ########## Activate ##########
    Hi there deliah wildweed 159
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 54039
    [0m 
    Singletone emp is running. name:[TV] Emp:[47969] , Client:[54039] ,  Option:[SINGLETON]  , Status:[2][AP_INFOLINK/Fatal] 212 : Setting m_SafeAlarm->Reset(TIME_OUT_STOP, 0);
    [AP_INFOLINK/Fatal] 213 : Wait Mode --> Safe Mode
    [AP_INFOLINK/Fatal] 214 : ### MESSAGE_WEBSVC_ACTIVATE_READY_WM ###, m_bFirstStart [1]
    [AP_INFOLINK/Fatal] 215 : m_CountryCode [BE]
    [AP_INFOLINK/Fatal] 216 : m_bStartConnect is [1]
    Hi there deliah wildweed 159
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 35617
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 35785
    [0m 
    ## RunApp [CallThread=0x6a629460] App (2) runs App(Source Browser:11), nRunData(0x0), nRunOption(0x0) ##
    [A_SOURCE_BROWSER/Fatal] 217 : CSourceApp::t_OnEndActivating()
    [A_SOURCE_BROWSER/Fatal] 218 : [CSourceManagerUtil::GetList()] [217] ulPlugStatus = 700000 
    [GetIcon]  device id = -1 , return NULL!!!  
    ####### Header = 12, 0
    [GetIcon]  device id = -1 , return NULL!!!  
    [InstallResourceRequestCallback][811]
    ## StopApp [CallThread=0x70c6b460] App (11) stops App(Source Browser:11), nStopData(0x0), nStopOption(0x0) ##
    [A_SOURCE_BROWSER/Fatal] 219 : CSourceApp::t_OnEndDeactivating()
    [89:74291][DEBUG][InstallResourceRequestCallback][812] 
    @@@[SSSO SOURCE_TYPE_DTV1] [SsSourceBase.cpp] ControlAudioClip, ControlType[1]
    [TDScaler][VidId:0][544] (Mute OnOff:1)
    [TPAWindow.cpp][DisconnectSource][WID:0][CALL]..
    [Check 3D Status...]
    3D Mode to Set: [0],
    [VSI] 3D Mode: [0],
    [DSP] 3D Mode: [0],
    [RES] 3D Mode: [0]
    Skip 3D Mode Last Memory Setting...[OFF] or Auto Detected 3D Mode!!!
    [Check 3D Status...]
    3D Mode to Set: [0],
    [VSI] 3D Mode: [0],
    [DSP] 3D Mode: [0],
    [RES] 3D Mode: [0]
    Skip 3D Mode Last Memory Setting...[OFF] or Auto Detected 3D Mode!!!
    [TDScaler][Disconnect] (VideoId:0)
    [89:125012][DEBUG][UninstallResolutionCallback][794] 
    [89:125091][DEBUG][UninstallResolutionCallbackForClip][802] 
    [89:125808][DEBUG][UninstallAudioMuteCallback][904] 
    	>>[ERR:TDsSamDemux.cpp] SetAudioDescriptionId():1451 Invalid Audio Descriptio PID... 
    [TPAWindow.cpp][DisconnectSource][WID:0][END]..
    ####### Header = 12, 0
    [TPAWindow.cpp][ConnectSource][WID:0][CALL]..
    [TDScaler][Connect]eOutVideoID = 0x0, eBackendId = 0x4, eWindowID = 0x0
    [TDScaler]eExtOutId = 0xd, eOutVideoId = 0x0
    [TDScaler]eSource = 0x901, m_ePipSourceMode = 0x0, m_ePreSrcMode:0x201
    [TDScaler][VidId:0][3401] (CVBS OnOff:1)
    [Scaler]
     TDResolution_k : [15]
    TDResolutionInfo_t [720], [576], [0], [0], [864], [625], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [2305], [0], [4], [17], [0], [0]
    Source : 0x901, WindowType : 0 ExtInID : 0, BackEndID : 4, tdRet=0 
    ### eSrc 0x901, Audio Format [Not Support String 27], DDCompMode RF, Factory value -9, Real set value to SDAL 0
    [TPAWindow.cpp][ConnectSource][WID:0][END]..
    [Check 3D Status...]
    3D Mode to Set: [0],
    [VSI] 3D Mode: [0],
    [DSP] 3D Mode: [0],
    [RES] 3D Mode: [0]
    Skip 3D Mode Last Memory Setting...[OFF] or Auto Detected 3D Mode!!!
    [Scaler]
     TDResolution_k : [15]
    TDResolutionInfo_t [720], [576], [0], [0], [864], [625], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [2305], [0], [4], [17], [0], [0]
    [BackEnd]
     TDResolution_k : [15]
    TDResolutionInfo_t [720], [576], [0], [0], [864], [625], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [2305], [0], [4], [17], [0], [0]
    [TDaScaler][SetGeometry][ID:0]Geometry (0, 0, 1920, 1080)
    [TDaScaler][SetCapture][ID:0]Capture (30, 17, 658, 540)
    [ERROR][hdiSetAudioDelay():644] EXTOUT AUDIO DELAY : Extout source type is error(18)
    	>>[ERR:TDsSamAudioProcessor.cpp] t_SetAudioSpeakerDelay():2514  - SDAL ERROR [-1] !!!
    Motion Plus setting same...
    t_GASFRC3D_SetAutoMotionPlus() : Motion Plus Demo OFF
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Turn Glass to OFF
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Glass Callback Registered, Run Callback. (3D : OFF, Param : 109122216)
    [BT_SS/Fatal] 220 : [Set3DOffsetBroadcastOnOff][line:2460] Set3DOffsetBroadcastOnOff : [Disable]
    [BT_SS/Fatal] 221 : [SetShutterInfoForBroadCast][line:2452] shutter info exceeds 65535. m_frame_period[60001], m_DutyForShuttering[125]
    [BT_SS/Fatal] 222 : [Set3DModeOffSetForBroadCast][line:2178] m_b3DOffsetBroadcast[0], m_frame_period[60001]... I would make 3DGS as open
    [BT_SS/Fatal] 223 : [Set3DSyncDetection][line:2475] Set3DSyncDetection : [Disable]
    Set3DMode() : Start, TD3dEffectMode_k = 0, iVideoPlane = 0 iBackendDevice:0
    t_Set3DModeForGenoaAlone(): Game/MJC Mode is same 
    [ERROR][SetStereoscopicScreenMode():264] Not Supported StereoScopic Resolution(1920, 1080)!!!
    SetStereoscopicScreenMode, 395, Not supported Screen
    [TDScaler][VidId:0][544] (Mute OnOff:0)
    [BT_SS/Fatal] 224 : [SetShutterInfoForBroadCast][line:2452] shutter info exceeds 65535. m_frame_period[60001], m_DutyForShuttering[125]
    [BT_SS/Fatal] 225 : [Set3DModeOffSetForBroadCast][line:2178] m_b3DOffsetBroadcast[0], m_frame_period[60001]... I would make 3DGS as open
    ## RunApp [CallThread=0x6a629460] App (2) runs App(InfoLink3:67), nRunData(0x0), nRunOption(0x0) ##
    Set3DEffectFunction Called...[false] Power Off Sequence [0])
    (DbgMaple) [AP_BROWSER/Fatal] 226 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/am/amApplication.cpp:1302 in show() 
    (DbgMaple) [AP_BROWSER/Fatal] 227 : CApplication::show (app : 0x6b6c008, task : 0x6b6c0b0) (SCREEN NUMBER=1)
    (DbgMaple) [AP_BROWSER/Fatal] 228 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/am/amApplication.cpp:1304 in show() 
    (DbgMaple) [AP_BROWSER/Fatal] 229 : CApplication::show current screen resolution (1920x1080), widget resolution (1280x720)
    (DbgMaple) [AP_BROWSER/Fatal] 230 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/am/amApplication.cpp:1323 in show() 
    (DbgMaple) [AP_BROWSER/Fatal] 231 : CApplication::show change resolution (SCREEN NUMBER=1) (SCREEN RESOLUTION[1280x720])
    Hi there deliah wildweed 159
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 38516
    [0m 
    Singletone emp is running. name:[TV] Emp:[47969] , Client:[38516] ,  Option:[SINGLETON]  , Status:[2][CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 57028
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 56125
    [0m 
    ####### Header = 12, 0
    [AP_INFOLINK/Fatal] 232 : Setting m_SafeAlarm->Reset(TIME_OUT_STOP, 0);
    [AP_INFOLINK/Fatal] 233 : ### MESSAGE_WEBSVC_ACTIVATE_READY_WM ###, m_bFirstStart [0]
    [AP_INFOLINK/Fatal] 234 : Update is False
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 53985
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 49034
    [0m 
    (DbgAlert) [AP_WIDGET/Fatal] 235 : alert() : [Smart Hub Log] @@@@@ video mute ON @@@@@
    [TDScaler][VidId:0][544] (Mute OnOff:1)
    (DbgAlert) [AP_WIDGET/Fatal] 236 : alert() : [Smart Hub Log] SmartHomeMain.setFocus() ==> UISmartHome.call
    ####### Header = 12, 0
    [AP_INFOLINK/Fatal] 237 : Setting m_SafeAlarm->Reset(TIME_OUT_STOP, 0);
    [AP_INFOLINK/Fatal] 238 : ### MESSAGE_WEBSVC_ACTIVATE_READY_WM ###, m_bFirstStart [0]
    [AP_INFOLINK/Fatal] 239 : Update is False
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 41511
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 60542
    [0m 
    Set3DEffectFunction Called...[false] Power Off Sequence [0])
    DynamicControl:5, FullOSD:true 
    (DbgAlert) [AP_WIDGET/Fatal] 240 : alert() : [Smart Hub Log] SET HIGHLIGHT....
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 40284
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 52052
    [0m 
    [DEFAULT/Debugging] 241 : CApp::SendEvent Event Receiver NULL-app[101]
    ####### Header = 12, 0
    (DbgAlert) [AP_WIDGET/Fatal] 242 : alert() : [Smart Hub Log]  @@@@@@@ SetPIG @@@@@@
    [TDaScaler][SetGeometry][ID:0]Geometry (60, 112, 482, 274)
    [TDaScaler][SetCapture][ID:0]Capture (26, 15, 668, 544)
    [DEFAULT/Debugging] 243 : CApp::SendEvent Event Receiver NULL-app[101]
    (DbgAlert) [AP_WIDGET/Fatal] 244 : alert() : [Smart Hub Log] @@@@@ video mute OFF @@@@@
    [TDScaler][VidId:0][544] (Mute OnOff:0)
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 40538
    [0m 
    Singletone emp is running. name:[NNavi] Emp:[35490] , Client:[40538] ,  Option:[SINGLETON]  , Status:[2][CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 57114
    [0m 
    Singletone emp is running. name:[Network] Emp:[59603] , Client:[57114] ,  Option:[SINGLETON]  , Status:[2][CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 53394
    [0m 
    Singletone emp is running. name:[ExternalWidgetInterface] Emp:[41372] , Client:[53394] ,  Option:[SINGLETON]  , Status:[2][CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 46492
    [0m 
    Singletone emp is running. name:[TV] Emp:[47969] , Client:[46492] ,  Option:[SINGLETON]  , Status:[2][CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 47193
    [0m 
    Singletone emp is running. name:[TVMW] Emp:[45702] , Client:[47193] ,  Option:[SINGLETON]  , Status:[2][CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 53731
    [0m 
    Singletone emp is running. name:[Device] Emp:[39918] , Client:[53731] ,  Option:[SINGLETON]  , Status:[2](DbgAlert) [AP_WIDGET/Fatal] 245 : alert() : [Smart Hub Log] SmartHomeMain.setFocus() ==> WMAgreement 6
    ####### Header = 12, 0
    GetServerType in plNNavi_pscomm.cpp . line 287
    GetServerType in plNNavi_pscomm.cpp . line 287
    (DbgAlert) [AP_WIDGET/Fatal] 246 : alert() : [Smart Hub Log] SmartHomeMain.setFocus() ==> WMMain.normalMode
    ####### Header = 12, 0
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 51509
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 59471
    [0m 
    @@@[SSSO SOURCE_TYPE_DTV1] [SsSourceBase.cpp] ControlAudioClip, ControlType[1]
    [TPAWindow.cpp][DisconnectSource][WID:4][CALL]..
    [TDScaler][Disconnect] (VideoId:2)
    [TPAWindow.cpp][DisconnectSource][WID:4][END]..
    	>>[ERR:TDiDemux.cpp] SetInputType():208 Null Fuction Call !!!Must Check Implementation Code...
    [ERROR][StopPcr():595] [WARN] PCR is already stopped!! 
    [ERROR][StopPcr():595] [WARN] PCR is already stopped!! 
    [UninstallResourceRequestCallback][822]
    GetServerType in plNNavi_pscomm.cpp . line 287
    [TDScaler][VidId:2][770] (VideoOnOff:0)
    [TDScaler][VidId:0][544] (Mute OnOff:1)
    [TPAWindow.cpp][DisconnectSource][WID:0][CALL]..
    [Check 3D Status...]
    3D Mode to Set: [0],
    [VSI] 3D Mode: [0],
    [DSP] 3D Mode: [0],
    [RES] 3D Mode: [0]
    Skip 3D Mode Last Memory Setting...[OFF] or Auto Detected 3D Mode!!!
    [TDScaler][Disconnect] (VideoId:0)
    [TPAWindow.cpp][DisconnectSource][WID:0][END]..
    Task SetBannerState : [0] 
    [AP_INFOLINK/Fatal] 247 : RunFlashApp app = [12]
    [AP_INFOLINK/Fatal] 248 : RunFlashApp Data = [/mtd_down/widgets/normal/11111000010/./yt_lbl_ext.swf]
    [AP_INFOLINK/Fatal] 249 : RunFlashApp ID = []
    [AP_INFOLINK/Fatal] 250 : RunFlashApp PW = []
    ## RunApp [CallThread=0x6f66b460] App (67) runs App(Flash App 1.2:72), nRunData(0x22b80795), nRunOption(0x0) ##
    (DbgMaple) [AP_BROWSER/Fatal] 251 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/ae/aeWidgetEngine.cpp:1295 in deactivateSmartSideBar() 
    (DbgMaple) [AP_BROWSER/Fatal] 252 : Enter deactivateSmartSideBar (id : 10110000001)
    (DbgMaple) [AP_BROWSER/Fatal] 253 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/am/amApplication.cpp:1386 in hide() 
    (DbgMaple) [AP_BROWSER/Fatal] 254 : CApplication::hide (app : 0x6b6c008, task : 0x6b6c0b0)
    [InstallResourceRequestCallback][811]
    [130:341376][DEBUG][InstallResourceRequestCallback][812] 
    [130:341453][DEBUG][InstallAudioFormatCallback][937] 
    [130:341891][DEBUG][InstallResolutionCallback][648] 
    [TPAWindow.cpp][ConnectSource][WID:0][CALL]..
    [TDScaler][Connect]eOutVideoID = 0x0, eBackendId = 0xb, eWindowID = 0x0
    [TDScaler]eExtOutId = 0xd, eOutVideoId = 0x0
    [TDScaler]eSource = 0x2000, m_ePipSourceMode = 0x0, m_ePreSrcMode:0x901
    [TDScaler][VidId:0][3401] (CVBS OnOff:1)
    [Scaler]
     TDResolution_k : [24]
    TDResolutionInfo_t [1920], [1080], [0], [0], [2640], [1125], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [8192], [0], [4], [17], [0], [0]
    [130:357331][DEBUG][InstallVideoMuteCallback][1037] 
    [InstallAudioMuteCallback][894]
    [Check 3D Status...]
    3D Mode to Set: [0],
    [VSI] 3D Mode: [0],
    [DSP] 3D Mode: [0],
    [RES] 3D Mode: [0]
    Skip 3D Mode Last Memory Setting...[OFF] or Auto Detected 3D Mode!!!
    [Scaler]
     TDResolution_k : [24]
    TDResolutionInfo_t [1920], [1080], [0], [0], [2640], [1125], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [8192], [0], [4], [17], [0], [0]
    [BackEnd]
     TDResolution_k : [24]
    TDResolutionInfo_t [1920], [1080], [0], [0], [2640], [1125], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [8192], [0], [4], [17], [0], [0]
    (DbgAlert) [AP_WIDGET/Fatal] 255 : alert() : [Smart Hub Log] @@@@@ ReleasePIG @@@@@
    [TDaScaler][SetGeometry][ID:0]Geometry (0, 0, 1920, 1080)
    [TDaScaler][SetCapture][ID:0]Capture (0, 0, 1920, 1080)
    [ERROR][hdiSetAudioDelay():644] EXTOUT AUDIO DELAY : Extout source type is error(18)
    	>>[ERR:TDsSamAudioProcessor.cpp] t_SetAudioSpeakerDelay():2514  - SDAL ERROR [-1] !!!
    [ERROR][hdiSetAudioDelay():644] EXTOUT AUDIO DELAY : Extout source type is error(18)
    	>>[ERR:TDsSamAudioProcessor.cpp] SetDelay():2027  - SDAL ERROR [-1] !!!
    t_GASFRC3D_SetAutoMotionPlus() : Motion Plus Demo OFF
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Turn Glass to OFF
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Glass Callback Registered, Run Callback. (3D : OFF, Param : 109122216)
    [BT_SS/Fatal] 256 : [Set3DOffsetBroadcastOnOff][line:2460] Set3DOffsetBroadcastOnOff : [Disable]
    [BT_SS/Fatal] 257 : [SetShutterInfoForBroadCast][line:2452] shutter info exceeds 65535. m_frame_period[60001], m_DutyForShuttering[125]
    [BT_SS/Fatal] 258 : [Set3DModeOffSetForBroadCast][line:2178] m_b3DOffsetBroadcast[0], m_frame_period[60001]... I would make 3DGS as open
    [BT_SS/Fatal] 259 : [Set3DSyncDetection][line:2475] Set3DSyncDetection : [Disable]
    Set3DMode() : Start, TD3dEffectMode_k = 0, iVideoPlane = 0 iBackendDevice:0
    t_Set3DModeForGenoaAlone(): Game/MJC Mode is same 
    SetStereoscopicScreenMode, 395, Not supported Screen
    [130:933963][DEBUG][SetResolutionDone][666] 
    (DbgMaple) [AP_BROWSER/Fatal] 260 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/am/amManagerWidget.cpp:479 in onDeactivateManagerWidget() 
    (DbgMaple) [AP_BROWSER/Fatal] 261 : onDeactivateManagerWidget
    (DbgAlert) [AP_WIDGET/Fatal] 262 : alert() : [Smart Hub Log] ########## Deactivate ##########
    DynamicControl:5, FullOSD:false 
    [TPAWindow.cpp][ConnectSource][WID:0][END]..
    [DEFAULT/Debugging] 263 :  [CMovieDemoAppBase::t_OnEvent - 427] EVENT_SET_MEDIA 
    Task SendEventToDevice : [4] [0] 
    (DbgAlert) [AP_WIDGET/Fatal] 264 : alert() : [Smart Hub Log] UISmartHome.hide()   pMoveOut undefined
    ####### Header = 12, 0
    Task SetBannerState : [0] 
    (DbgMaple) [AP_BROWSER/Fatal] 265 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/ae/aeWidgetEngine.cpp:1310 in deactivateSmartSideBar() 
    (DbgMaple) [AP_BROWSER/Fatal] 266 : Exit deactivateSmartSideBar (id : 10110000001)
    [AP_INFOLINK/Fatal] 267 : CWidgetEngine::deactivateSmartSideBar returns TRUE
    [AP_INFOLINK/Fatal] 268 : Setting m_SafeAlarm->Reset(TIME_OUT_STOP, 0);
    Set3DEffectFunction Called...[true] Power Off Sequence [0])
    [FLASH_APP/Fatal] 269 : Width from config.xml is 1280
    [FLASH_APP/Fatal] 270 : Height from config.xml is 720
    [FLASH_APP/Fatal] 271 : Width : 1280, Height : 720
    DynamicControl:5, FullOSD:true 
    Set3DEffectFunction Called...[false] Power Off Sequence [0])
    ## [ShowScreen] Screen(1), Caller(72)
    ############################
    /home1/dblee/Genoa/GS_R_AP/AP_FlashPlayer/SC1.2/source/ae/kernel/platformloaders/linux/AELoader.cpp-InitializeStagecraftLibrary_12
    ############################
    ############################
    /home1/dblee/Genoa/GS_R_AP/AP_FlashPlayer/SC1.2/source/ae/kernel/platformloaders/linux/AELoader.cpp-InitializeAEKernel_12
    ############################
    (DbgAlert) [AP_WIDGET/Fatal] 272 : alert() : [Smart Hub Log] LOSE HIGHLIGHT....
    [FLASH_APP/Fatal] 273 : @@@@@@ Flash Var string : vendor=samsung&model=UE40D6200&SKU=UE40D6200&firmware=2011-09-28&remote=RC13&lang=fr&country=US&cpid=&cppw=
    libDeviceAPI.so is opened!
    [FLASH_PLAYER/Fatal] 274 : @@@@ Create General Render Plane
    ####### Header = 12, 0
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    **************************************************************************************
    **************************************************************************************
      OPEN MEDIA : flash://Movie:// 
    **************************************************************************************
    **************************************************************************************
    [ROSE_MW    ] [CMediaManager][GetMedia]  MOVIE 
    [ROSE_MW    ] CREATE PLAYER, USE CASE[ 0 ]
    [163:412496][INFO][SetOutputArea][1010] CALLED, BUT TOO LATE
    [163:516199][DEBUG][t_GetResolutionInfo][11946] GET RESOLUTION FAILED
    [SetTotalBufferSize][2408] ID:[78e3a58]	TOTAL BUFFER SIZE = 5000 kB
    [SetTotalBufferSize][2409] ID:[78e3a58]	AUDIO Q SIZE = 2500 kB
    [SetTotalBufferSize][2410] ID:[78e3a58]	VIDEO Q SIZE = 2500 kB
    [SetBufferSizeForPlay][2425] ID:[78e3a58]	PRE ROLLING FOR PLAY SIZE = 1 kB
    [SetBufferSizeForResume][2442] ID:[78e3a58]	PRE ROLLING FOR RESUME SIZE = 5 kB
    [Play][1133] ID:[78e3a58]	PLAY CALLED!!!
    [163:538452][DEBUG][AssignPlayer][446] 
    [163:538541][DEBUG][AssignPlayer][464] PLAYER 0 [0x78e3a58] IS ASSIGNED
    [163:561903][DEBUG][GetPanelSize][2979] 1920 x 1080 PANEL CONFIGURED
    [t_StartPlayThread][8622] ID:[78e3a58]	TIMESLICE [16]ms
    [m_SelectStreams][7180] ID:[78e3a58]	STREAMS SELECTED DONE V[0] A[1] S[-1]
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300033]  MESSAGE[0]  CALLER[m_SelectStreams]  LINE[7182]
    [CSubtitleProcessor][Create] RESET
    [CSubtitleProcessor][Start] CALLED
    [CSubtitleProcessor][Start] FLAG START : 0
    [CSubtitleProcessor][display_thread] TIMESLICE [8]ms
    [CSubtitleProcessor][Start] DONE : 1
    [CPlayer][t_StartPlayThread] AUDIO QUEUE CREATED ...
    [163:579704][INFO][SelectQueue][949] USER ID [ 0 ], StrNum [ 1 ] Q[0x7796b28]
    [CPlayer][t_StartPlayThread] AUDIO QUEUE CREATED .....[0]
    [t_WhatToUse] Codec ID [0x15002] [86018]
    [163:580491][INFO][Open][62] [CAudioDecoder][Open] AUDIO STREAM FOUND [1]
    ### eSrc 0x2000, Audio Format [Not Support String 27], DDCompMode RF, Factory value -9, Real set value to SDAL 0
    [163:611420][DEBUG][openAudioDecoder][1193] OPEN AUDIO DECODER SUCCESS
    [163:611493][INFO][Open][74] [CAudioDecoder][Open] AUDIO HW CODEC OPEN SUCCESS .....
    [163:611540][INFO][m_PrepareAudioResources][12507] AUDIO CODEC OPEN SUCCESS ID[0].....
    [t_AudioThread][6132] ID:[78e3a58]	ID[0]- NUMBER OF FRAMES:[0]
    [t_AudioThread][6133] ID:[78e3a58]	ID[0]-TIME BASE DEN[1000] NUM[1]
    [t_AudioThread][6134] ID:[78e3a58]	ID[0]-EXTRA DATA SIZE:[2]
    [t_AudioThread][6136] ID:[78e3a58]	ID[0]-USER INFO:[0]
    [CPlayer][t_StartPlayThread] AUDIO THREAD CREATED .....[0]
    [CPlayer][t_StartPlayThread] VIDEO Q INIT (NORMAL).....
    [CPlayer][t_StartPlayThread] VIDEO QUEUE CREATED .....
    [t_WhatToUse] Codec ID [0x1c] [28]
    -- HW VIDEO CODEC : ,h264,
    	>>[ERR:TDiMpeg.cpp] GetAllowedVideoBitrate():741 Null Fuction Call !!!Must Check Implementation Code...
    [CPlayer][t_StartPlayThread] VIDEO THREAD CREATED .....
    openVideoDecoder---2176
    [163:720253][DEBUG][openVideoDecoder][2183] OPEN VIDEO DECODER SUCCESS
    [163:720351][DEBUG][UploadPlaybackInfo][2146] 
    #######################
    ### PLAY START !!!! ###
    #######################
    [CVideoDecoder][Open] VIDEO PIXEL FORMAT: [0]
    [CVideoDecoder][Open] HW VIDEO CODEC OPEN SUCCESS .....
    [163:720545][INFO][Open][47] [CVideoRenderer][Open] OPEN DISPLAY.. 
    [TDScaler][Connect]eOutVideoID = 0x0, eBackendId = 0xb, eWindowID = 0x0
    [TDScaler]eExtOutId = 0xd, eOutVideoId = 0x0
    [TDScaler]eSource = 0x2001, m_ePipSourceMode = 0x0, m_ePreSrcMode:0x2000
    [TDScaler][VidId:0][3401] (CVBS OnOff:1)
    [163:721346][DEBUG][setVideoMute][1780] SCALER MUTE [MAIN] : ON
    	>>[ERR:TDiScaler.cpp] SetCurrentMediaType():234 Null Fuction Call !!!Must Check Implementation Code...
    [163:730772][INFO][m_PrepareVideoResources][12421] VIDEO DECODER & RENDERER ARE OPENED
    [t_VideoThread][4309] ID:[78e3a58]	TIME BASE DEN[1000] NUM[1]
    [t_VideoThread][4310] ID:[78e3a58]	TIMEBASE UNRELIABLE = 1
    [CPlayer][t_StartPlayThread] AUDIO PLAY THREAD CREATED .....[0]
    [CPlayer][t_StartPlayThread] DISPLAY THREAD CREATED .....
    [t_StartPlayThread][8722] ID:[78e3a58]	TOTAL BUFFER SIZE = 5000 kB
    [t_StartPlayThread][8723] ID:[78e3a58]	AUDIO Q SIZE = 2500 kB
    [t_StartPlayThread][8724] ID:[78e3a58]	VIDEO Q SIZE = 2500 kB
    [t_StartPlayThread][8725] ID:[78e3a58]	BUFFERING TIMEOUT = 30 s
    [t_StartPlayThread][8726] ID:[78e3a58]	NUMBER OF STREAMS: [2]
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[101]  CALLER[t_BufferingStart]  LINE[1634]
    [m_ControlBuffer][8000] ID:[78e3a58]	****** GROUND ZERO --> BUFFERING
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (9 / 1024) = 0%
    [m_ControlBuffer][8163] ID:[78e3a58]	****** BUFFERING END A FRAME#[1/0] V FRAME#[1/0] TIME[0ms/30000ms] A SIZE[0KB/2500KB] V SIZE[7KB/2500KB]
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[102]  CALLER[t_BufferingEnd]  LINE[1693]
    [ERROR][hdiDecodeAudioFrame():1286] spIAe_DecodeAudioFrame 0xf00
    	>>[ERR:TDsSamMpeg.cpp] DecodeAudioFrame():2844  - SDAL ERROR [-1] !!!
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[101]  CALLER[t_BufferingStart]  LINE[1634]
    [m_ControlBuffer][8000] ID:[78e3a58]	****** GROUND ZERO --> BUFFERING
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (170 / 5120) = 3%
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[3]  CALLER[m_ControlBuffer]  LINE[8248]
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (452 / 5120) = 8%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (1004 / 5120) = 19%
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[19]  CALLER[m_ControlBuffer]  LINE[8248]
    [m_ControlBuffer][8163] ID:[78e3a58]	****** BUFFERING END A FRAME#[3/0] V FRAME#[1/0] TIME[1ms/30000ms] A SIZE[0KB/2500KB] V SIZE[12KB/2500KB]
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[102]  CALLER[t_BufferingEnd]  LINE[1693]
    -- VIDEO CALLBACK !!! 0, 1280, 0, 720 , frmaerate=25000
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[101]  CALLER[t_BufferingStart]  LINE[1634]
    [m_ControlBuffer][8000] ID:[78e3a58]	****** GROUND ZERO --> BUFFERING
    [m_ControlBuffer][8163] ID:[78e3a58]	****** BUFFERING END A FRAME#[0/0] V FRAME#[1/0] TIME[0ms/30000ms] A SIZE[0KB/2500KB] V SIZE[16KB/2500KB]
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[102]  CALLER[t_BufferingEnd]  LINE[1693]
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[101]  CALLER[t_BufferingStart]  LINE[1634]
    [m_ControlBuffer][8000] ID:[78e3a58]	****** GROUND ZERO --> BUFFERING
    [m_ControlBuffer][8163] ID:[78e3a58]	****** BUFFERING END A FRAME#[1/0] V FRAME#[1/0] TIME[0ms/30000ms] A SIZE[0KB/2500KB] V SIZE[19KB/2500KB]
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[102]  CALLER[t_BufferingEnd]  LINE[1693]
    [CPlayer][t_UpdateScreen] WAITING FOR THE FIRST AUDIO FRAME ..... 1  ID[0]
    [163:907039][INFO][t_OpenAudioRenderer][12101] iSampleRate[ 44100 ], iChannels[ 2 ], iFormat[ 4 ], bLittleEndian[ 1 ]
    [ERROR][locStartI2sTx():1203] Sound0 Speaker is Not Connected...
    [163:924946][DEBUG][SetAudioMute][807] SOUND MUTE : ON
    [t_HandleAudioMuteCallBack] bOn=1, PreState=PLAY_STATE_STOP
    [t_AudioThread][6603] ID:[78e3a58]	CHANNELS:[2]
    [t_AudioThread][6604] ID:[78e3a58]	SAMPLE WIDTH IN BYTES:[4]
    [t_AudioThread][6605] ID:[78e3a58]	RATE:[44100]
    [t_AudioThread][6606] ID:[78e3a58]	AUDIO BYTES PER SEC:[352800]
    *****************************
    *****************************
    *****************************
    AST: [14781560]
    *****************************
    *****************************
    *****************************
    [163:932220][DEBUG][t_GetResolutionInfo][11929] [HW] W[1280] H[720] FR[25000] PRG[0] RES[27]
    [163:932322][DEBUG][t_SetResolutionInfo][11586] FPA
    [163:932396][DEBUG][UploadResolution][705] [MAIN][ON] W[1280] H[720] FR[25000] PRG[0] RES[27] BR[0] CODEC[3] FORMAT[4] EFFECT MODE[0], ASPECT_RATIO[0]
    [163:932823][DEBUG][setVideoQuality][1425] T[ 0 ]
    [CPlayer][t_UpdateScreen] RESOLUTION SETTING IS NOT DONE!!! 
    [Scaler]
     TDResolution_k : [27]
    TDResolutionInfo_t [1280], [720], [0], [0], [1980], [750], [0], [25000], [0], [0], [0], [0], [0], [0], [0], [0], [12800], [0], [4], [3], [0], [0]
    [BackEnd]
     TDResolution_k : [27]
    TDResolutionInfo_t [1280], [720], [0], [0], [1980], [750], [0], [25000], [0], [0], [0], [0], [0], [0], [0], [0], [12800], [0], [4], [3], [0], [0]
    [164:192302][DEBUG][t_GetSizeInfo][2206] FOR PLAYER ID : 0
    [164:192451][DEBUG][t_GetResolutionInfo][11929] [HW] W[1280] H[720] FR[25000] PRG[0] RES[27]
    [164:192708][DEBUG][GetOutputArea][1035] RESOLUTION [1280x720]
    [164:204554][DEBUG][GetOutputArea][1040] DISPLAY AREA [0x0]
    [164:204667][DEBUG][t_GetSizeInfo][2229] CAPTURE[0/0/1280/720]  GEOMETRY[0/0/1920/1080]
    [TDaScaler][SetGeometry][ID:0]Geometry (0, 0, 1920, 1080)
    [TDaScaler][SetCapture][ID:0]Capture (0, 0, 1280, 720)
    [ERROR][hdiSetAudioDelay():644] EXTOUT AUDIO DELAY : Extout source type is error(18)
    	>>[ERR:TDsSamAudioProcessor.cpp] t_SetAudioSpeakerDelay():2514  - SDAL ERROR [-1] !!!
    t_GASFRC3D_SetAutoMotionPlus() : Motion Plus Demo OFF
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Turn Glass to OFF
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Glass Callback Registered, Run Callback. (3D : OFF, Param : 109122216)
    [BT_SS/Fatal] 275 : [Set3DOffsetBroadcastOnOff][line:2460] Set3DOffsetBroadcastOnOff : [Disable]
    [BT_SS/Fatal] 276 : [SetShutterInfoForBroadCast][line:2452] shutter info exceeds 65535. m_frame_period[60001], m_DutyForShuttering[125]
    [BT_SS/Fatal] 277 : [Set3DModeOffSetForBroadCast][line:2178] m_b3DOffsetBroadcast[0], m_frame_period[60001]... I would make 3DGS as open
    [BT_SS/Fatal] 278 : [Set3DSyncDetection][line:2475] Set3DSyncDetection : [Disable]
    Set3DMode() : Start, TD3dEffectMode_k = 0, iVideoPlane = 0 iBackendDevice:0
    t_Set3DModeForGenoaAlone(): Game/MJC Mode is same 
    SetStereoscopicScreenMode, 395, Not supported Screen
    [164:624845][DEBUG][SetResolutionDone][666] 
    [164:624979][DEBUG][SetResolutionDone][673] PLAYER 0 [0x78e3a58] IS DONE
    [BT_SS/Fatal] 279 : [SetShutterInfoForBroadCast][line:2452] shutter info exceeds 65535. m_frame_period[60001], m_DutyForShuttering[125]
    [BT_SS/Fatal] 280 : [Set3DModeOffSetForBroadCast][line:2178] m_b3DOffsetBroadcast[0], m_frame_period[60001]... I would make 3DGS as open
    [164:669393][DEBUG][setVideoMute][1780] SCALER MUTE [MAIN] : OFF
    [TDScaler][VidId:0][544] (Mute OnOff:0)
    [164:669823][DEBUG][setVideoMute][1780] SCALER MUTE [MAIN] : OFF
    CVideoRenderer::Mute Off
    *****************************
    *****************************
    *****************************
    VST: [14848568]
    *****************************
    *****************************
    *****************************
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300033]  MESSAGE[3]  CALLER[t_UpdateScreen]  LINE[3451]
    @@@@ send event of FLASHAPP_SET_MOVIEPLAY_ON
    *****************************
    *****************************
    *****************************
    MODIIED ID:(0)'s AST: [14848568]
    *****************************
    *****************************
    *****************************
    [164:670846][DEBUG][SetAudioMute][807] SOUND MUTE : OFF
    [t_HandleAudioMuteCallBack] bOn=0, PreState=PLAY_STATE_STOP
    [t_AudioThread][6574] ID:[78e3a58]	WARNNING: AUDIO FRAME EARLY BY MORE THAN 200000 MICRO SEC [D557000] > [S23219]
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
     |> ROSE PTS(    1040) START PTS(       0) FLASH PTS(    1080) RUN TIME( 0: 1: 8) STATUS(4) 	 BUFFER(1831 KBtyes) ooo 
     |> ROSE PTS(    2240) START PTS(       0) FLASH PTS(    2280) RUN TIME( 0: 2:28) STATUS(4) 	 BUFFER(3075 KBtyes) ooo 
     |> ROSE PTS(    3280) START PTS(       0) FLASH PTS(    3320) RUN TIME( 0: 3:32) STATUS(4) 	 BUFFER(4024 KBtyes) ooo 
     |> ROSE PTS(    4320) START PTS(       0) FLASH PTS(    4360) RUN TIME( 0: 4:36) STATUS(4) 	 BUFFER(3905 KBtyes) ooo 
     |> ROSE PTS(    5520) START PTS(       0) FLASH PTS(    5560) RUN TIME( 0: 5:56) STATUS(4) 	 BUFFER(3703 KBtyes) ooo 
     |> ROSE PTS(    6560) START PTS(       0) FLASH PTS(    6600) RUN TIME( 0: 6:60) STATUS(4) 	 BUFFER(3499 KBtyes) ooo 
     |> ROSE PTS(    7600) START PTS(       0) FLASH PTS(    7640) RUN TIME( 0: 7:64) STATUS(4) 	 BUFFER(3326 KBtyes) ooo 
     |> ROSE PTS(    8800) START PTS(       0) FLASH PTS(    8840) RUN TIME( 0: 8:84) STATUS(4) 	 BUFFER(3147 KBtyes) ooo 
     |> ROSE PTS(    9840) START PTS(       0) FLASH PTS(    9880) RUN TIME( 0: 9:88) STATUS(4) 	 BUFFER(3004 KBtyes) ooo 
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300033]  MESSAGE[6]  CALLER[Pause]  LINE[1515]
    @@@@ send event of FLASHAPP_SET_MOVIEPLAY_OFF
    [175:153557][DEBUG][UploadPlaybackInfo][2146] 
    #######################
    ### PLAY PAUSE !!!! ###
    #######################
    [175:200129][DEBUG][SetAudioMute][807] SOUND MUTE : ON
    [t_HandleAudioMuteCallBack] bOn=1, PreState=PLAY_STATE_START
    [175:220684][INFO][closeAudioOutput][689] AUDIO DISCONNECT SUCCESS
    [175:220890][ERROR][Render][226] AUDIO RENDERER WAS NOT OPENED
     || FLASH PTS(   10520) RUN TIME( 0:10:52) STATUS(5) 	 BUFFER(2940 KBtyes) ooo 
     || FLASH PTS(   10520) RUN TIME( 0:10:52) STATUS(5) 	 BUFFER(2940 KBtyes) ooo 
     || FLASH PTS(   10520) RUN TIME( 0:10:52) STATUS(5) 	 BUFFER(2940 KBtyes) ooo 
     || FLASH PTS(   10520) RUN TIME( 0:10:52) STATUS(5) 	 BUFFER(2940 KBtyes) ooo 
     || FLASH PTS(   10520) RUN TIME( 0:10:52) STATUS(5) 	 BUFFER(2940 KBtyes) ooo 
     || FLASH PTS(   10520) RUN TIME( 0:10:52) STATUS(5) 	 BUFFER(2940 KBtyes) ooo 
     || FLASH PTS(   10520) RUN TIME( 0:10:52) STATUS(5) 	 BUFFER(2940 KBtyes) ooo 
     || FLASH PTS(   10520) RUN TIME( 0:10:52) STATUS(5) 	 BUFFER(2940 KBtyes) ooo 
    [Stop][1252] ID:[78e3a58]	CALLED BY USER
    [t_SetPlaySpeed][1776] ID:[78e3a58]	CALLED!!! speed[ 1.000000 ]
    [CPlayer][t_AudioPlayThread] ID:[126761560] AUDIO PLAY THREAD TERMINATED .....
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300033]  MESSAGE[3]  CALLER[t_SetPlaySpeed]  LINE[1855]
    @@@@ send event of FLASHAPP_SET_MOVIEPLAY_ON
    [179:453933][DEBUG][UploadPlaybackInfo][2146] 
    #######################
    ### PLAY START !!!! ###
    #######################
    [CSubtitleProcessor][Stop] CALLED
    [CSubtitleProcessor][Stop] FLAG START : 1
    [CSubtitleProcessor][Stop] TRY TO STOP OTHERS ....
    [CSubtitleProcessor][t_StopAll] WAITING FOR SUBTITLE THREAD TO BE TERMINATED.. SR[0]...
    [CPlayer][t_DisplayThread] DISPLAY THREAD TERMINATED .....
    [t_StartPlayThread][9411] ID:[78e3a58]	WAITING FOR OTHER THREADS TO BE TERMINATED..  V[0] A[0] VR[1] AR[1]
    [CSubtitleProcessor][t_StopAll] WAITING FOR SUBTITLE THREAD TO BE TERMINATED.. SR[0]...
    [CSubtitleProcessor][t_StopAll] WAITING FOR SUBTITLE THREAD TO BE TERMINATED.. SR[0]...
    [CSubtitleProcessor][t_StopAll] WAITING FOR SUBTITLE THREAD TO BE TERMINATED.. SR[0]...
    [CSubtitleProcessor][t_StopAll] WAITING FOR SUBTITLE THREAD TO BE TERMINATED.. SR[0]...
    [CSubtitleProcessor][t_StopAll] WAITING FOR SUBTITLE THREAD TO BE TERMINATED.. SR[0]...
    [CSubtitleProcessor][Stop] TRY TO DEINIT CAPTION ....
    [CSubtitleProcessor][Stop] STOPPING SUBTITLE THREADS DONE ....
    [CSubtitleProcessor][Stop] DENIED : 0
    [179:528488][ERROR][Close][150] AUDIO RENDERER WAS NOT OPENED
    [CPlayer][Stop] WAITING AUDIO[0] FLAGS [D(0), R(1), REDIRECT(1)]=[1, 1, 1] or [1, 1, 3] or [1, 0, 2]
    *************DEADLOCK PROBING RESULT*************
    	AUDIO HEADQUEUE:0
    	AUDIO DECODER:0
    	AUDIO RENDERER:0
    *************************************************
    [179:536244][DEBUG][closeAudioDecoder][1220] CLOSE AUDIO DECODER
    [179:536370][INFO][t_ReleaseResourceID][3283] _RESOURCE_ eResType[ 2 ], eResID[ 0 ]
    [t_AudioThread][6932] ID:[78e3a58]	AUDIO THREAD TERMINATED
    [t_StartPlayThread][9411] ID:[78e3a58]	WAITING FOR OTHER THREADS TO BE TERMINATED..  V[0] A[1] VR[1] AR[1]
    [179:537130][DEBUG][setVideoMute][1780] SCALER MUTE [MAIN] : ON
    [TDScaler][VidId:0][544] (Mute OnOff:1)
    CVideoRenderer::Mute On
    [179:546769][ERROR][t_Mute][248] VIDEO RENDERER WAS NOT OPENED
    [179:546885][DEBUG][UploadResolution][705] [MAIN][OFF] W[0] H[0] FR[0] PRG[0] RES[0] BR[0] CODEC[-1] FORMAT[4] EFFECT MODE[0], ASPECT_RATIO[0]
    [179:547292][DEBUG][setVideoQuality][1425] T[ 0 ]
    [CPlayer][t_CloseAllVideoResource] RESOLUTION SETTING IS NOT DONE!!! 
    [Check 3D Status...]
    3D Mode to Set: [0],
    [VSI] 3D Mode: [0],
    [DSP] 3D Mode: [0],
    [RES] 3D Mode: [0]
    Skip 3D Mode Last Memory Setting...[OFF] or Auto Detected 3D Mode!!!
    [Scaler]
     TDResolution_k : [24]
    TDResolutionInfo_t [1920], [1080], [0], [0], [2640], [1125], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [8192], [0], [4], [17], [0], [0]
    [BackEnd]
     TDResolution_k : [24]
    TDResolutionInfo_t [1920], [1080], [0], [0], [2640], [1125], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [8192], [0], [4], [17], [0], [0]
    [CPlayer][Stop] WAITING VIDEO FLAGS [D(0), R(1), REDIRECT(1)]=[1, 1, 1] or [1, 1, 3] or [1, 0, 2]
    *************DEADLOCK PROBING RESULT*************
    	VIDEO HEADQUEUE:0
    	VIDEO DECODER:0
    	VIDEO RENDERER:0
    *************************************************
    [TDaScaler][SetCapture][ID:0]Capture (0, 0, 1920, 1080)
    [t_StartPlayThread][9411] ID:[78e3a58]	WAITING FOR OTHER THREADS TO BE TERMINATED..  V[0] A[1] VR[1] AR[1]
    [t_StartPlayThread][9411] ID:[78e3a58]	WAITING FOR OTHER THREADS TO BE TERMINATED..  V[0] A[1] VR[1] AR[1]
    [t_StartPlayThread][9411] ID:[78e3a58]	WAITING FOR OTHER THREADS TO BE TERMINATED..  V[0] A[1] VR[1] AR[1]
    [ERROR][hdiSetAudioDelay():644] EXTOUT AUDIO DELAY : Extout source type is error(18)
    	>>[ERR:TDsSamAudioProcessor.cpp] t_SetAudioSpeakerDelay():2514  - SDAL ERROR [-1] !!!
    t_GASFRC3D_SetAutoMotionPlus() : Motion Plus Demo OFF
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Turn Glass to OFF
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Glass Callback Registered, Run Callback. (3D : OFF, Param : 109122216)
    [BT_SS/Fatal] 281 : [Set3DOffsetBroadcastOnOff][line:2460] Set3DOffsetBroadcastOnOff : [Disable]
    [BT_SS/Fatal] 282 : [SetShutterInfoForBroadCast][line:2452] shutter info exceeds 65535. m_frame_period[60001], m_DutyForShuttering[125]
    [BT_SS/Fatal] 283 : [Set3DModeOffSetForBroadCast][line:2178] m_b3DOffsetBroadcast[0], m_frame_period[60001]... I would make 3DGS as open
    [t_StartPlayThread][9411] ID:[78e3a58]	WAITING FOR OTHER THREADS TO BE TERMINATED..  V[0] A[1] VR[1] AR[1]
    [BT_SS/Fatal] 284 : [Set3DSyncDetection][line:2475] Set3DSyncDetection : [Disable]
    Set3DMode() : Start, TD3dEffectMode_k = 0, iVideoPlane = 0 iBackendDevice:0
    t_Set3DModeForGenoaAlone(): Game/MJC Mode is same 
    SetStereoscopicScreenMode, 395, Not supported Screen
    [179:890092][DEBUG][SetResolutionDone][666] 
    [179:890206][DEBUG][SetResolutionDone][673] PLAYER 0 [0x78e3a58] IS DONE
    [BT_SS/Fatal] 285 : [SetShutterInfoForBroadCast][line:2452] shutter info exceeds 65535. m_frame_period[60001], m_DutyForShuttering[125]
    [BT_SS/Fatal] 286 : [Set3DModeOffSetForBroadCast][line:2178] m_b3DOffsetBroadcast[0], m_frame_period[60001]... I would make 3DGS as open
    	>>[ERR:TDiScaler.cpp] SetCurrentMediaType():234 Null Fuction Call !!!Must Check Implementation Code...
    [179:892207][DEBUG][setVideoMute][1780] SCALER MUTE [MAIN] : ON
    [TDScaler][Disconnect] (VideoId:0)
    [179:892456][INFO][t_ReleaseResourceID][3283] _RESOURCE_ eResType[ 1 ], eResID[ 0 ]
    [179:892511][INFO][Close][88] [CVideoRenderer][Close] DISPLAY CLOSED.. 
    UNINSTALL CALLBACK!!!!!!!
    [179:936150][INFO][t_ReleaseResourceID][3283] _RESOURCE_ eResType[ 0 ], eResID[ 0 ]
    [179:936261][DEBUG][UploadPlaybackInfo][2146] 
    ######################
    ### PLAY STOP !!!! ###
    ######################
    [179:936369][DEBUG][closeVideoDecoder][2300] CLOSE VIDEO DECODER
    [CPlayer][t_VideoThread] ID:[126761560] VIDEO THREAD TERMINATED .....
    [Stop][1392] ID:[78e3a58]	WAITING DEMUXER THREAD DONE!!!
    *************DEADLOCK PROBING RESULT*************
    	AV READ FRAME:0
    	AV SEEK FRAME:0
    *************************************************
    [CPlayer][t_StartPlayThread] TERMINATE VIDEO RESOURCES
    [CPlayer][t_StartPlayThread] TERMINATE AUDIO RESOURCES
    [179:942908][ERROR][Close][150] AUDIO RENDERER WAS NOT OPENED
    [CPlayer][t_StartPlayThread] ID:[126761560] MAIN DEMUX THREAD TERMINATED .....
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300033]  MESSAGE[5]  CALLER[t_StartPlayThread]  LINE[9497]
    @@@@ send event of FLASHAPP_SET_MOVIEPLAY_OFF
    [Stop][1423] ID:[78e3a58]	STOPPING THREADS DONE
    [SetOutputICT][2086]
    [SetOutputICT][2091] m_CallBackICT == NULL
    [SetOutputMacrovision][2039]
    [SetOutputMacrovision][2044]
     m_CallBackMacroVision== NULL[SetOutputVBIData][2063]
    [SetOutputVBIData][2068] m_CallBackVBIData == NULL
    [180:40690][DEBUG][ReleasePlayer][535] 
    [180:40734][DEBUG][ReleasePlayer][541] PLAYER 0 [0x78e3a58]IS RELEASED
    ========================== ELAPSED TIME CHECKER ==========================
    TIME: 1-1. GET MEDIA 	(197 ms)
    TIME: 1-4. DELAY BTWN GETMEDIA TO PLAY 	(125 ms)
    TIME: 2-1. PLAY->BEFORE START DEMUX 	(202 ms)
    TIME: 2-2. START DEMUX -> BUFFERING ENDS 	(63 ms)
    TIME: 2-3. BUFFERING ENDS -> FIRST FRAME DECODED 	(20 ms)
    TIME: 2-4. FIRST FRAME DECODED -> BEFORE VIDEO QUALITY SETTING 	(107 ms)
    TIME: 2-5. VIDEO QUALITY SETTING -> FIRST FRAME DISPLAYED 	(737 ms)
    TIME: 3. TOTAL TIME FOR FIRST FRAME DISPLAY 	(1454 ms)
    TIME: 4-1. TRICK STOP 	(9 ms)
    TIME: 4-2. SUBTITLE STOP 	(74 ms)
    TIME: 4-3. AUDIO STOP 	(8 ms)
    TIME: 4-4. VIDEO STOP 	(399 ms)
    TIME: 4-5. 	VIDEO RENDERER STOP 	(355 ms)
    TIME: 4-6. 	VIDEO DECODER STOP 	(43 ms)
    TIME: 4-7. DEMUXER STOP 	(103 ms)
    TIME: 4-8. MACROVISION RESET 	(0 ms)
    TIME: 5. TOTAL TIME FOR STOP  	(596 ms)
    ==========================================================================
    [180:41924][ERROR][Close][600] [0x6c86540] MEDIA CLOSE FAIL
    [0;40;31m bye~ Player Destructor end
    ================================
    [~SamsungStreamPlayer(0, 0x79500f0)] DESTROYED...	END !!!
    ================================
    ~QueuedFrames: 
    ~QueuedFrames: 
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    **************************************************************************************
    **************************************************************************************
      OPEN MEDIA : flash://Movie:// 
    **************************************************************************************
    **************************************************************************************
    [ROSE_MW    ] [CMediaManager][GetMedia]  MOVIE 
    [ROSE_MW    ] CREATE PLAYER, USE CASE[ 0 ]
    [181:442255][INFO][SetOutputArea][1010] CALLED, BUT TOO LATE
    [181:544377][DEBUG][t_GetResolutionInfo][11946] GET RESOLUTION FAILED
    [SetTotalBufferSize][2408] ID:[78e3a58]	TOTAL BUFFER SIZE = 5000 kB
    [SetTotalBufferSize][2409] ID:[78e3a58]	AUDIO Q SIZE = 2500 kB
    [SetTotalBufferSize][2410] ID:[78e3a58]	VIDEO Q SIZE = 2500 kB
    [SetBufferSizeForPlay][2425] ID:[78e3a58]	PRE ROLLING FOR PLAY SIZE = 1 kB
    [SetBufferSizeForResume][2442] ID:[78e3a58]	PRE ROLLING FOR RESUME SIZE = 5 kB
    [Play][1133] ID:[78e3a58]	PLAY CALLED!!!
    [181:545170][DEBUG][AssignPlayer][446] 
    [181:545220][DEBUG][AssignPlayer][464] PLAYER 0 [0x78e3a58] IS ASSIGNED
    [181:547068][DEBUG][GetPanelSize][2979] 1920 x 1080 PANEL CONFIGURED
    [t_StartPlayThread][8622] ID:[78e3a58]	TIMESLICE [16]ms
    [m_SelectStreams][7180] ID:[78e3a58]	STREAMS SELECTED DONE V[0] A[1] S[-1]
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300033]  MESSAGE[0]  CALLER[m_SelectStreams]  LINE[7182]
    [CSubtitleProcessor][Start] CALLED
    [CSubtitleProcessor][Start] FLAG START : 0
    [CSubtitleProcessor][Start] DONE : 1
    [CPlayer][t_StartPlayThread] AUDIO QUEUE CREATED ...
    [181:548838][INFO][SelectQueue][949] USER ID [ 0 ], StrNum [ 1 ] Q[0x78f2a50]
    [CPlayer][t_StartPlayThread] AUDIO QUEUE CREATED .....[0]
    [t_WhatToUse] Codec ID [0x15002] [86018]
    [181:549148][INFO][Open][62] [CAudioDecoder][Open] AUDIO STREAM FOUND [1]
    ### eSrc 0x2000, Audio Format [Not Support String 27], DDCompMode RF, Factory value -9, Real set value to SDAL 0
    [181:549805][DEBUG][openAudioDecoder][1193] OPEN AUDIO DECODER SUCCESS
    [181:549880][INFO][Open][74] [CAudioDecoder][Open] AUDIO HW CODEC OPEN SUCCESS .....
    [181:550015][INFO][m_PrepareAudioResources][12507] AUDIO CODEC OPEN SUCCESS ID[0].....
    [t_AudioThread][6132] ID:[78e3a58]	ID[0]- NUMBER OF FRAMES:[0]
    [t_AudioThread][6133] ID:[78e3a58]	ID[0]-TIME BASE DEN[1000] NUM[1]
    [t_AudioThread][6134] ID:[78e3a58]	ID[0]-EXTRA DATA SIZE:[2]
    [t_AudioThread][6136] ID:[78e3a58]	ID[0]-USER INFO:[0]
    [CSubtitleProcessor][display_thread] TIMESLICE [8]ms
    [CPlayer][t_StartPlayThread] AUDIO THREAD CREATED .....[0]
    [CPlayer][t_StartPlayThread] VIDEO Q INIT (NORMAL).....
    [CPlayer][t_StartPlayThread] VIDEO QUEUE CREATED .....
    [t_WhatToUse] Codec ID [0x1c] [28]
    -- HW VIDEO CODEC : ,h264,
    	>>[ERR:TDiMpeg.cpp] GetAllowedVideoBitrate():741 Null Fuction Call !!!Must Check Implementation Code...
    [CPlayer][t_StartPlayThread] VIDEO THREAD CREATED .....
    [CPlayer][t_StartPlayThread] AUDIO PLAY THREAD CREATED .....[0]
    [CPlayer][t_StartPlayThread] DISPLAY THREAD CREATED .....
    [t_StartPlayThread][8722] ID:[78e3a58]	TOTAL BUFFER SIZE = 5000 kB
    [t_StartPlayThread][8723] ID:[78e3a58]	AUDIO Q SIZE = 2500 kB
    [t_StartPlayThread][8724] ID:[78e3a58]	VIDEO Q SIZE = 2500 kB
    [t_StartPlayThread][8725] ID:[78e3a58]	BUFFERING TIMEOUT = 30 s
    [t_StartPlayThread][8726] ID:[78e3a58]	NUMBER OF STREAMS: [2]
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[101]  CALLER[t_BufferingStart]  LINE[1634]
    [m_ControlBuffer][8000] ID:[78e3a58]	****** GROUND ZERO --> BUFFERING
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (9 / 1024) = 0%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (242 / 1024) = 23%
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[23]  CALLER[m_ControlBuffer]  LINE[8248]
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (258 / 1024) = 25%
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[25]  CALLER[m_ControlBuffer]  LINE[8248]
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (295 / 1024) = 28%
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[28]  CALLER[m_ControlBuffer]  LINE[8248]
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (311 / 1024) = 30%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (348 / 1024) = 33%
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[33]  CALLER[m_ControlBuffer]  LINE[8248]
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (364 / 1024) = 35%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (401 / 1024) = 39%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (417 / 1024) = 40%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (454 / 1024) = 44%
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[44]  CALLER[m_ControlBuffer]  LINE[8248]
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (470 / 1024) = 45%
    openVideoDecoder---2176
    [181:909910][DEBUG][openVideoDecoder][2183] OPEN VIDEO DECODER SUCCESS
    [181:909984][DEBUG][UploadPlaybackInfo][2146] 
    #######################
    ### PLAY START !!!! ###
    #######################
    [CVideoDecoder][Open] VIDEO PIXEL FORMAT: [0]
    [CVideoDecoder][Open] HW VIDEO CODEC OPEN SUCCESS .....
    [181:910156][INFO][Open][47] [CVideoRenderer][Open] OPEN DISPLAY.. 
    [TDScaler][Connect]eOutVideoID = 0x0, eBackendId = 0xb, eWindowID = 0x0
    [TDScaler]eExtOutId = 0xd, eOutVideoId = 0x0
    [TDScaler]eSource = 0x2001, m_ePipSourceMode = 0x0, m_ePreSrcMode:0x2001
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (507 / 1024) = 49%
    [TDScaler][VidId:0][3401] (CVBS OnOff:1)
    [181:911487][DEBUG][setVideoMute][1780] SCALER MUTE [MAIN] : ON
    	>>[ERR:TDiScaler.cpp] SetCurrentMediaType():234 Null Fuction Call !!!Must Check Implementation Code...
    [181:911641][INFO][m_PrepareVideoResources][12421] VIDEO DECODER & RENDERER ARE OPENED
    [t_VideoThread][4309] ID:[78e3a58]	TIME BASE DEN[1000] NUM[1]
    [t_VideoThread][4310] ID:[78e3a58]	TIMEBASE UNRELIABLE = 1
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (523 / 1024) = 51%
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[51]  CALLER[m_ControlBuffer]  LINE[8248]
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (560 / 1024) = 54%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (576 / 1024) = 56%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (613 / 1024) = 59%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (629 / 1024) = 61%
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[61]  CALLER[m_ControlBuffer]  LINE[8248]
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (666 / 1024) = 65%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (682 / 1024) = 66%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (719 / 1024) = 70%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (735 / 1024) = 71%
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[71]  CALLER[m_ControlBuffer]  LINE[8248]
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (772 / 1024) = 75%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (788 / 1024) = 76%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (825 / 1024) = 80%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (841 / 1024) = 82%
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[82]  CALLER[m_ControlBuffer]  LINE[8248]
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (878 / 1024) = 85%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (894 / 1024) = 87%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (931 / 1024) = 90%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (947 / 1024) = 92%
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[92]  CALLER[m_ControlBuffer]  LINE[8248]
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (963 / 1024) = 94%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (979 / 1024) = 95%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (995 / 1024) = 97%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (1011 / 1024) = 98%
    [m_ControlBuffer][8163] ID:[78e3a58]	****** BUFFERING END A FRAME#[20/0] V FRAME#[14/0] TIME[341ms/30000ms] A SIZE[0KB/2500KB] V SIZE[0KB/2500KB]
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[102]  CALLER[t_BufferingEnd]  LINE[1693]
    [ERROR][hdiDecodeAudioFrame():1286] spIAe_DecodeAudioFrame 0xf00
    	>>[ERR:TDsSamMpeg.cpp] DecodeAudioFrame():2844  - SDAL ERROR [-1] !!!
    -- VIDEO CALLBACK !!! 0, 1280, 0, 720 , frmaerate=24000
    [CPlayer][t_UpdateScreen] WAITING FOR THE FIRST AUDIO FRAME ..... 1  ID[0]
    [CPlayer][t_UpdateScreen] WAITING FOR THE FIRST AUDIO FRAME ..... 2  ID[0]
    [CPlayer][t_UpdateScreen] WAITING FOR THE FIRST AUDIO FRAME ..... 3  ID[0]
    [182:211817][INFO][t_OpenAudioRenderer][12101] iSampleRate[ 44100 ], iChannels[ 2 ], iFormat[ 4 ], bLittleEndian[ 1 ]
    [ERROR][locStartI2sTx():1203] Sound0 Speaker is Not Connected...
    [182:213299][DEBUG][SetAudioMute][807] SOUND MUTE : ON
    [t_HandleAudioMuteCallBack] bOn=1, PreState=PLAY_STATE_STOP
    [t_AudioThread][6603] ID:[78e3a58]	CHANNELS:[2]
    [t_AudioThread][6604] ID:[78e3a58]	SAMPLE WIDTH IN BYTES:[4]
    [t_AudioThread][6605] ID:[78e3a58]	RATE:[44100]
    [t_AudioThread][6606] ID:[78e3a58]	AUDIO BYTES PER SEC:[352800]
    *****************************
    *****************************
    *****************************
    AST: [16427516]
    *****************************
    *****************************
    *****************************
    [182:256287][DEBUG][t_GetResolutionInfo][11929] [HW] W[1280] H[720] FR[24000] PRG[0] RES[3]
    [182:256415][DEBUG][t_SetResolutionInfo][11586] FPA
    [182:256610][DEBUG][UploadResolution][705] [MAIN][ON] W[1280] H[720] FR[24000] PRG[0] RES[3] BR[0] CODEC[3] FORMAT[4] EFFECT MODE[0], ASPECT_RATIO[0]
    [182:257134][DEBUG][setVideoQuality][1425] T[ 0 ]
    [CPlayer][t_UpdateScreen] RESOLUTION SETTING IS NOT DONE!!! 
    [TDScaler][VidId:0][544] (Mute OnOff:1)
    182260 Set Panel mute On 
    [TDsSamPanel::SetInverterForGenoaSPanelMute] Call bOnOff:0
    ------------ Inverter sw Real On Off:0
    [WINDOW_MAIN]#####Panel Mute ON #####
    ##### Mute [ON] In SetResolution Sequence~!!! #####
    [Scaler]
     TDResolution_k : [3]
    TDResolutionInfo_t [1280], [720], [0], [0], [1650], [750], [0], [24000], [0], [0], [0], [0], [0], [0], [0], [0], [12800], [0], [4], [3], [0], [48]
    [BackEnd]
     TDResolution_k : [3]
    TDResolutionInfo_t [1280], [720], [0], [0], [1650], [750], [0], [24000], [0], [0], [0], [0], [0], [0], [0], [0], [12800], [0], [4], [3], [0], [48]
    [GASFRC3DShare::t_CheckFramePackingTableUsingRealVHzForGenoaAlone] (vHz:0) (bIsVHz23980:0)
    [182:733317][DEBUG][t_GetSizeInfo][2206] FOR PLAYER ID : 0
    [182:733463][DEBUG][t_GetResolutionInfo][11929] [HW] W[1280] H[720] FR[24000] PRG[0] RES[3]
    [182:733527][DEBUG][GetOutputArea][1035] RESOLUTION [1280x720]
    [182:733710][DEBUG][GetOutputArea][1040] DISPLAY AREA [0x0]
    [182:734175][DEBUG][t_GetSizeInfo][2229] CAPTURE[0/0/1280/720]  GEOMETRY[0/0/1920/1080]
    [TDaScaler][SetGeometry][ID:0]Geometry (0, 0, 1920, 1080)
    [TDaScaler][SetCapture][ID:0]Capture (0, 0, 1280, 720)
    [ERROR][hdiSetAudioDelay():644] EXTOUT AUDIO DELAY : Extout source type is error(18)
    	>>[ERR:TDsSamAudioProcessor.cpp] t_SetAudioSpeakerDelay():2514  - SDAL ERROR [-1] !!!
    t_GASFRC3D_SetAutoMotionPlus() : Motion Plus Demo OFF
    GetBluetoothDelayFor3DVideoSync() is not 50/60HZ source
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Turn Glass to OFF
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Glass Callback Registered, Run Callback. (3D : OFF, Param : 109122216)
    [BT_SS/Fatal] 287 : [Set3DOffsetBroadcastOnOff][line:2460] Set3DOffsetBroadcastOnOff : [Disable]
    [BT_SS/Fatal] 288 : [SetShutterInfoForBroadCast][line:2452] shutter info exceeds 65535. m_frame_period[60001], m_DutyForShuttering[125]
    [BT_SS/Fatal] 289 : [Set3DModeOffSetForBroadCast][line:2178] m_b3DOffsetBroadcast[0], m_frame_period[60001]... I would make 3DGS as open
    [BT_SS/Fatal] 290 : [Set3DSyncDetection][line:2475] Set3DSyncDetection : [Disable]
    Set3DMode() : Start, TD3dEffectMode_k = 0, iVideoPlane = 0 iBackendDevice:0
    t_Set3DModeForGenoaAlone(): Game/MJC Mode is same 
    SetStereoscopicScreenMode, 395, Not supported Screen
    182940 Set Panel mute Off 
    [TDsSamPanel::SetInverterForGenoaSPanelMute] Call bOnOff:1
    ------------ Inverter sw Real On Off:1
    [WINDOW_MAIN]#####Panel Mute OFF #####
    ##### Mute [OFF] In SetResolution Sequence~!!! #####
    [183:1044][DEBUG][SetResolutionDone][666] 
    [183:1117][DEBUG][SetResolutionDone][673] PLAYER 0 [0x78e3a58] IS DONE
    GetBluetoothDelayFor3DVideoSync() is not 50/60HZ source
    [BT_SS/Fatal] 291 : [SetShutterInfoForBroadCast][line:2452] shutter info exceeds 65535. m_frame_period[60001], m_DutyForShuttering[125]
    [BT_SS/Fatal] 292 : [Set3DModeOffSetForBroadCast][line:2178] m_b3DOffsetBroadcast[0], m_frame_period[60001]... I would make 3DGS as open
    [183:88464][DEBUG][setVideoMute][1780] SCALER MUTE [MAIN] : OFF
    [TDScaler][VidId:0][544] (Mute OnOff:0)
    [183:89106][DEBUG][setVideoMute][1780] SCALER MUTE [MAIN] : OFF
    CVideoRenderer::Mute Off
    *****************************
    *****************************
    *****************************
    VST: [16506306]
    *****************************
    *****************************
    *****************************
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300033]  MESSAGE[3]  CALLER[t_UpdateScreen]  LINE[3451]
    @@@@ send event of FLASHAPP_SET_MOVIEPLAY_ON
    *****************************
    *****************************
    *****************************
    MODIIED ID:(0)'s AST: [16506306]
    *****************************
    *****************************
    *****************************
    [183:90458][DEBUG][SetAudioMute][807] SOUND MUTE : OFF
    [t_HandleAudioMuteCallBack] bOn=0, PreState=PLAY_STATE_STOP
    [t_AudioThread][6574] ID:[78e3a58]	WARNNING: AUDIO FRAME EARLY BY MORE THAN 200000 MICRO SEC [D1811000] > [S23219]
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
     |> ROSE PTS(    1125) START PTS(       0) FLASH PTS(    1126) RUN TIME( 0: 1:12) STATUS(4) 	 BUFFER(3999 KBtyes) ooo 
     |> ROSE PTS(    2168) START PTS(       0) FLASH PTS(    2210) RUN TIME( 0: 2:21) STATUS(4) 	 BUFFER(3856 KBtyes) ooo 
     |> ROSE PTS(    3210) START PTS(       0) FLASH PTS(    3211) RUN TIME( 0: 3:21) STATUS(4) 	 BUFFER(3714 KBtyes) ooo 
     |> ROSE PTS(    4253) START PTS(       0) FLASH PTS(    4254) RUN TIME( 0: 4:25) STATUS(4) 	 BUFFER(3578 KBtyes) ooo 
     |> ROSE PTS(    5254) START PTS(       0) FLASH PTS(    5255) RUN TIME( 0: 5:25) STATUS(4) 	 BUFFER(3423 KBtyes) ooo 
     |> ROSE PTS(    6296) START PTS(       0) FLASH PTS(    6297) RUN TIME( 0: 6:29) STATUS(4) 	 BUFFER(3276 KBtyes) ooo 
     |> ROSE PTS(    7339) START PTS(       0) FLASH PTS(    7340) RUN TIME( 0: 7:34) STATUS(4) 	 BUFFER(3129 KBtyes) ooo 
     |> ROSE PTS(    8340) START PTS(       0) FLASH PTS(    8341) RUN TIME( 0: 8:34) STATUS(4) 	 BUFFER(2958 KBtyes) ooo 
     |> ROSE PTS(    9384) START PTS(       0) FLASH PTS(    9426) RUN TIME( 0: 9:42) STATUS(4) 	 BUFFER(2777 KBtyes) ooo 
     |> ROSE PTS(   10426) START PTS(       0) FLASH PTS(   10427) RUN TIME( 0:10:42) STATUS(4) 	 BUFFER(2529 KBtyes) ooo 
     |> ROSE PTS(   11468) START PTS(       0) FLASH PTS(   11469) RUN TIME( 0:11:46) STATUS(4) 	 BUFFER(2068 KBtyes) ooo 
     |> ROSE PTS(   12469) START PTS(       0) FLASH PTS(   12470) RUN TIME( 0:12:47) STATUS(4) 	 BUFFER(1865 KBtyes) ooo 
     |> ROSE PTS(   13512) START PTS(       0) FLASH PTS(   13513) RUN TIME( 0:13:51) STATUS(4) 	 BUFFER(1573 KBtyes) ooo 
     |> ROSE PTS(   14555) START PTS(       0) FLASH PTS(   14556) RUN TIME( 0:14:55) STATUS(4) 	 BUFFER(4375 KBtyes) ooo 
     |> ROSE PTS(   15556) START PTS(       0) FLASH PTS(   15557) RUN TIME( 0:15:55) STATUS(4) 	 BUFFER(4081 KBtyes) ooo 
     |> ROSE PTS(   16598) START PTS(       0) FLASH PTS(   16599) RUN TIME( 0:16:59) STATUS(4) 	 BUFFER(3796 KBtyes) ooo 
     |> ROSE PTS(   17641) START PTS(       0) FLASH PTS(   17642) RUN TIME( 0:17:64) STATUS(4) 	 BUFFER(2877 KBtyes) ooo 
     |> ROSE PTS(   18684) START PTS(       0) FLASH PTS(   18685) RUN TIME( 0:18:68) STATUS(4) 	 BUFFER(2613 KBtyes) ooo 
     |> ROSE PTS(   19685) START PTS(       0) FLASH PTS(   19686) RUN TIME( 0:19:68) STATUS(4) 	 BUFFER(2331 KBtyes) ooo 
     |> ROSE PTS(   20728) START PTS(       0) FLASH PTS(   20729) RUN TIME( 0:20:72) STATUS(4) 	 BUFFER(1989 KBtyes) ooo 
     |> ROSE PTS(   21729) START PTS(       0) FLASH PTS(   21730) RUN TIME( 0:21:73) STATUS(4) 	 BUFFER(1717 KBtyes) ooo 
     |> ROSE PTS(   22771) START PTS(       0) FLASH PTS(   22772) RUN TIME( 0:22:77) STATUS(4) 	 BUFFER(1266 KBtyes) ooo 
     |> ROSE PTS(   23772) START PTS(       0) FLASH PTS(   23773) RUN TIME( 0:23:77) STATUS(4) 	 BUFFER(4059 KBtyes) ooo 
     |> ROSE PTS(   24816) START PTS(       0) FLASH PTS(   24858) RUN TIME( 0:24:85) STATUS(4) 	 BUFFER(2999 KBtyes) ooo 
     |> ROSE PTS(   25858) START PTS(       0) FLASH PTS(   25859) RUN TIME( 0:25:85) STATUS(4) 	 BUFFER(2708 KBtyes) ooo 
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300033]  MESSAGE[6]  CALLER[Pause]  LINE[1515]
    @@@@ send event of FLASHAPP_SET_MOVIEPLAY_OFF
    [209:422067][DEBUG][UploadPlaybackInfo][2146] 
    #######################
    ### PLAY PAUSE !!!! ###
    #######################
    [209:432125][DEBUG][SetAudioMute][807] SOUND MUTE : ON
    [t_HandleAudioMuteCallBack] bOn=1, PreState=PLAY_STATE_START
    [209:452285][INFO][closeAudioOutput][689] AUDIO DISCONNECT SUCCESS
    [209:452454][ERROR][Render][226] AUDIO RENDERER WAS NOT OPENED
    [Stop][1252] ID:[78e3a58]	CALLED BY USER
    [t_SetPlaySpeed][1776] ID:[78e3a58]	CALLED!!! speed[ 1.000000 ]
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300033]  MESSAGE[3]  CALLER[t_SetPlaySpeed]  LINE[1855]
    @@@@ send event of FLASHAPP_SET_MOVIEPLAY_ON
    [209:529582][DEBUG][UploadPlaybackInfo][2146] 
    #######################
    ### PLAY START !!!! ###
    #######################
    [CSubtitleProcessor][Stop] CALLED
    [CSubtitleProcessor][Stop] FLAG START : 1
    [CSubtitleProcessor][Stop] TRY TO STOP OTHERS ....
    [CSubtitleProcessor][t_StopAll] WAITING FOR SUBTITLE THREAD TO BE TERMINATED.. SR[0]...
    [CPlayer][t_DisplayThread] DISPLAY THREAD TERMINATED .....
    [CPlayer][t_AudioPlayThread] ID:[126761560] AUDIO PLAY THREAD TERMINATED .....
    [t_StartPlayThread][9411] ID:[78e3a58]	WAITING FOR OTHER THREADS TO BE TERMINATED..  V[0] A[0] VR[1] AR[1]
    [CSubtitleProcessor][t_StopAll] WAITING FOR SUBTITLE THREAD TO BE TERMINATED.. SR[0]...
    [CSubtitleProcessor][t_StopAll] WAITING FOR SUBTITLE THREAD TO BE TERMINATED.. SR[0]...
    [CSubtitleProcessor][t_StopAll] WAITING FOR SUBTITLE THREAD TO BE TERMINATED.. SR[0]...
    [CSubtitleProcessor][t_StopAll] WAITING FOR SUBTITLE THREAD TO BE TERMINATED.. SR[0]...
    [CSubtitleProcessor][t_StopAll] WAITING FOR SUBTITLE THREAD TO BE TERMINATED.. SR[0]...
    [CSubtitleProcessor][t_StopAll] WAITING FOR SUBTITLE THREAD TO BE TERMINATED.. SR[0]...
    [t_StartPlayThread][9411] ID:[78e3a58]	WAITING FOR OTHER THREADS TO BE TERMINATED..  V[0] A[0] VR[1] AR[1]
    [CSubtitleProcessor][Stop] TRY TO DEINIT CAPTION ....
    [CSubtitleProcessor][Stop] STOPPING SUBTITLE THREADS DONE ....
    [CSubtitleProcessor][Stop] DENIED : 0
    [209:616348][ERROR][Close][150] AUDIO RENDERER WAS NOT OPENED
    [CPlayer][Stop] WAITING AUDIO[0] FLAGS [D(0), R(1), REDIRECT(1)]=[1, 1, 1] or [1, 1, 3] or [1, 0, 2]
    *************DEADLOCK PROBING RESULT*************
    	AUDIO HEADQUEUE:0
    	AUDIO DECODER:0
    	AUDIO RENDERER:0
    *************************************************
    [209:624219][DEBUG][closeAudioDecoder][1220] CLOSE AUDIO DECODER
    [209:624316][INFO][t_ReleaseResourceID][3283] _RESOURCE_ eResType[ 2 ], eResID[ 0 ]
    [t_AudioThread][6932] ID:[78e3a58]	AUDIO THREAD TERMINATED
    [209:625160][DEBUG][setVideoMute][1780] SCALER MUTE [MAIN] : ON
    [TDScaler][VidId:0][544] (Mute OnOff:1)
    CVideoRenderer::Mute On
    [209:625691][ERROR][t_Mute][248] VIDEO RENDERER WAS NOT OPENED
    [209:625789][DEBUG][UploadResolution][705] [MAIN][OFF] W[0] H[0] FR[0] PRG[0] RES[0] BR[0] CODEC[-1] FORMAT[4] EFFECT MODE[0], ASPECT_RATIO[0]
    [209:626169][DEBUG][setVideoQuality][1425] T[ 0 ]
    [CPlayer][t_CloseAllVideoResource] RESOLUTION SETTING IS NOT DONE!!! 
    [Check 3D Status...]
    3D Mode to Set: [0],
    [VSI] 3D Mode: [0],
    [DSP] 3D Mode: [0],
    [RES] 3D Mode: [0]
    Skip 3D Mode Last Memory Setting...[OFF] or Auto Detected 3D Mode!!!
    [TDScaler][VidId:0][544] (Mute OnOff:1)
    209630 Set Panel mute On 
    [CPlayer][Stop] WAITING VIDEO FLAGS [D(0), R(1), REDIRECT(1)]=[1, 1, 1] or [1, 1, 3] or [1, 0, 2]
    *************DEADLOCK PROBING RESULT*************
    	VIDEO HEADQUEUE:0
    	VIDEO DECODER:0
    	VIDEO RENDERER:0
    *************************************************
    [TDsSamPanel::SetInverterForGenoaSPanelMute] Call bOnOff:0
    ------------ Inverter sw Real On Off:0
    [WINDOW_MAIN]#####Panel Mute ON #####
    ##### Mute [ON] In SetResolution Sequence~!!! #####
    [Scaler]
     TDResolution_k : [24]
    TDResolutionInfo_t [1920], [1080], [0], [0], [2640], [1125], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [8192], [0], [4], [17], [0], [0]
    [BackEnd]
     TDResolution_k : [24]
    TDResolutionInfo_t [1920], [1080], [0], [0], [2640], [1125], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [8192], [0], [4], [17], [0], [0]
    [t_StartPlayThread][9411] ID:[78e3a58]	WAITING FOR OTHER THREADS TO BE TERMINATED..  V[0] A[1] VR[1] AR[1]
    [TDaScaler][SetCapture][ID:0]Capture (0, 0, 1920, 1080)
    [t_StartPlayThread][9411] ID:[78e3a58]	WAITING FOR OTHER THREADS TO BE TERMINATED..  V[0] A[1] VR[1] AR[1]
    [t_StartPlayThread][9411] ID:[78e3a58]	WAITING FOR OTHER THREADS TO BE TERMINATED..  V[0] A[1] VR[1] AR[1]
    [ERROR][hdiSetAudioDelay():644] EXTOUT AUDIO DELAY : Extout source type is error(18)
    	>>[ERR:TDsSamAudioProcessor.cpp] t_SetAudioSpeakerDelay():2514  - SDAL ERROR [-1] !!!
    [ERROR][hdiSetAudioDelay():644] EXTOUT AUDIO DELAY : Extout source type is error(18)
    	>>[ERR:TDsSamAudioProcessor.cpp] SetDelay():2027  - SDAL ERROR [-1] !!!
    t_GASFRC3D_SetAutoMotionPlus() : Motion Plus Demo OFF
    [t_StartPlayThread][9411] ID:[78e3a58]	WAITING FOR OTHER THREADS TO BE TERMINATED..  V[0] A[1] VR[1] AR[1]
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Turn Glass to OFF
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Glass Callback Registered, Run Callback. (3D : OFF, Param : 109122216)
    [BT_SS/Fatal] 293 : [Set3DOffsetBroadcastOnOff][line:2460] Set3DOffsetBroadcastOnOff : [Disable]
    [BT_SS/Fatal] 294 : [SetShutterInfoForBroadCast][line:2452] shutter info exceeds 65535. m_frame_period[60001], m_DutyForShuttering[125]
    [BT_SS/Fatal] 295 : [Set3DModeOffSetForBroadCast][line:2178] m_b3DOffsetBroadcast[0], m_frame_period[60001]... I would make 3DGS as open
    [BT_SS/Fatal] 296 : [Set3DSyncDetection][line:2475] Set3DSyncDetection : [Disable]
    Set3DMode() : Start, TD3dEffectMode_k = 0, iVideoPlane = 0 iBackendDevice:0
    t_Set3DModeForGenoaAlone(): Game/MJC Mode is same 
    SetStereoscopicScreenMode, 395, Not supported Screen
    209950 Set Panel mute Off 
    [TDsSamPanel::SetInverterForGenoaSPanelMute] Call bOnOff:1
    ------------ Inverter sw Real On Off:1
    [WINDOW_MAIN]#####Panel Mute OFF #####
    ##### Mute [OFF] In SetResolution Sequence~!!! #####
    [210:4933][DEBUG][SetResolutionDone][666] 
    [210:5000][DEBUG][SetResolutionDone][673] PLAYER 0 [0x78e3a58] IS DONE
    [BT_SS/Fatal] 297 : [SetShutterInfoForBroadCast][line:2452] shutter info exceeds 65535. m_frame_period[60001], m_DutyForShuttering[125]
    [BT_SS/Fatal] 298 : [Set3DModeOffSetForBroadCast][line:2178] m_b3DOffsetBroadcast[0], m_frame_period[60001]... I would make 3DGS as open
    	>>[ERR:TDiScaler.cpp] SetCurrentMediaType():234 Null Fuction Call !!!Must Check Implementation Code...
    [210:8233][DEBUG][setVideoMute][1780] SCALER MUTE [MAIN] : ON
    [TDScaler][Disconnect] (VideoId:0)
    [210:8470][INFO][t_ReleaseResourceID][3283] _RESOURCE_ eResType[ 1 ], eResID[ 0 ]
    [210:8536][INFO][Close][88] [CVideoRenderer][Close] DISPLAY CLOSED.. 
    UNINSTALL CALLBACK!!!!!!!
    [t_StartPlayThread][9411] ID:[78e3a58]	WAITING FOR OTHER THREADS TO BE TERMINATED..  V[0] A[1] VR[1] AR[1]
    [210:24159][INFO][t_ReleaseResourceID][3283] _RESOURCE_ eResType[ 0 ], eResID[ 0 ]
    [210:24257][DEBUG][UploadPlaybackInfo][2146] 
    ######################
    ### PLAY STOP !!!! ###
    ######################
    [210:24360][DEBUG][closeVideoDecoder][2300] CLOSE VIDEO DECODER
    [CPlayer][t_VideoThread] ID:[126761560] VIDEO THREAD TERMINATED .....
    [Stop][1392] ID:[78e3a58]	WAITING DEMUXER THREAD DONE!!!
    *************DEADLOCK PROBING RESULT*************
    	AV READ FRAME:0
    	AV SEEK FRAME:0
    *************************************************
    [CPlayer][t_StartPlayThread] TERMINATE VIDEO RESOURCES
    [CPlayer][t_StartPlayThread] TERMINATE AUDIO RESOURCES
    [210:26003][ERROR][Close][150] AUDIO RENDERER WAS NOT OPENED
    [CPlayer][t_StartPlayThread] ID:[126761560] MAIN DEMUX THREAD TERMINATED .....
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300033]  MESSAGE[5]  CALLER[t_StartPlayThread]  LINE[9497]
    @@@@ send event of FLASHAPP_SET_MOVIEPLAY_OFF
    [Stop][1423] ID:[78e3a58]	STOPPING THREADS DONE
    [SetOutputICT][2086]
    [SetOutputICT][2091] m_CallBackICT == NULL
    [SetOutputMacrovision][2039]
    [SetOutputMacrovision][2044]
     m_CallBackMacroVision== NULL[SetOutputVBIData][2063]
    [SetOutputVBIData][2068] m_CallBackVBIData == NULL
    [210:128328][DEBUG][ReleasePlayer][535] 
    [210:128372][DEBUG][ReleasePlayer][541] PLAYER 0 [0x78e3a58]IS RELEASED
    ========================== ELAPSED TIME CHECKER ==========================
    TIME: 1-1. GET MEDIA 	(1 ms)
    TIME: 1-4. DELAY BTWN GETMEDIA TO PLAY 	(102 ms)
    TIME: 2-1. PLAY->BEFORE START DEMUX 	(29 ms)
    TIME: 2-2. START DEMUX -> BUFFERING ENDS 	(341 ms)
    TIME: 2-3. BUFFERING ENDS -> FIRST FRAME DECODED 	(24 ms)
    TIME: 2-4. FIRST FRAME DECODED -> BEFORE VIDEO QUALITY SETTING 	(315 ms)
    TIME: 2-5. VIDEO QUALITY SETTING -> FIRST FRAME DISPLAYED 	(833 ms)
    TIME: 3. TOTAL TIME FOR FIRST FRAME DISPLAY 	(1648 ms)
    TIME: 4-1. TRICK STOP 	(1 ms)
    TIME: 4-2. SUBTITLE STOP 	(86 ms)
    TIME: 4-3. AUDIO STOP 	(8 ms)
    TIME: 4-4. VIDEO STOP 	(399 ms)
    TIME: 4-5. 	VIDEO RENDERER STOP 	(383 ms)
    TIME: 4-6. 	VIDEO DECODER STOP 	(15 ms)
    TIME: 4-7. DEMUXER STOP 	(103 ms)
    TIME: 4-8. MACROVISION RESET 	(0 ms)
    TIME: 5. TOTAL TIME FOR STOP  	(600 ms)
    ==========================================================================
    [210:129412][ERROR][Close][600] [0x6c86540] MEDIA CLOSE FAIL
    [0;40;31m bye~ Player Destructor end
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    **************************************************************************************
    **************************************************************************************
      OPEN MEDIA : flash://Movie:// 
    **************************************************************************************
    **************************************************************************************
    [ROSE_MW    ] [CMediaManager][GetMedia]  MOVIE 
    [ROSE_MW    ] CREATE PLAYER, USE CASE[ 0 ]
    [210:710314][INFO][SetOutputArea][1010] CALLED, BUT TOO LATE
    [210:812187][DEBUG][t_GetResolutionInfo][11946] GET RESOLUTION FAILED
    [SetTotalBufferSize][2408] ID:[78e3a58]	TOTAL BUFFER SIZE = 5000 kB
    [SetTotalBufferSize][2409] ID:[78e3a58]	AUDIO Q SIZE = 2500 kB
    [SetTotalBufferSize][2410] ID:[78e3a58]	VIDEO Q SIZE = 2500 kB
    [SetBufferSizeForPlay][2425] ID:[78e3a58]	PRE ROLLING FOR PLAY SIZE = 1 kB
    [SetBufferSizeForResume][2442] ID:[78e3a58]	PRE ROLLING FOR RESUME SIZE = 5 kB
    [Play][1133] ID:[78e3a58]	PLAY CALLED!!!
    [210:813031][DEBUG][AssignPlayer][446] 
    [210:813081][DEBUG][AssignPlayer][464] PLAYER 0 [0x78e3a58] IS ASSIGNED
    [210:813948][DEBUG][GetPanelSize][2979] 1920 x 1080 PANEL CONFIGURED
    [t_StartPlayThread][8622] ID:[78e3a58]	TIMESLICE [16]ms
    [m_SelectStreams][7180] ID:[78e3a58]	STREAMS SELECTED DONE V[0] A[1] S[-1]
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300033]  MESSAGE[0]  CALLER[m_SelectStreams]  LINE[7182]
    [CSubtitleProcessor][Start] CALLED
    [CSubtitleProcessor][Start] FLAG START : 0
    [CSubtitleProcessor][Start] DONE : 1
    [CPlayer][t_StartPlayThread] AUDIO QUEUE CREATED ...
    [210:814643][INFO][SelectQueue][949] USER ID [ 0 ], StrNum [ 1 ] Q[0x78f3178]
    [CPlayer][t_StartPlayThread] AUDIO QUEUE CREATED .....[0]
    [t_WhatToUse] Codec ID [0x15002] [86018]
    [210:814950][INFO][Open][62] [CAudioDecoder][Open] AUDIO STREAM FOUND [1]
    ### eSrc 0x2000, Audio Format [Not Support String 27], DDCompMode RF, Factory value -9, Real set value to SDAL 0
    [210:815452][DEBUG][openAudioDecoder][1193] OPEN AUDIO DECODER SUCCESS
    [210:815519][INFO][Open][74] [CAudioDecoder][Open] AUDIO HW CODEC OPEN SUCCESS .....
    [210:815563][INFO][m_PrepareAudioResources][12507] AUDIO CODEC OPEN SUCCESS ID[0].....
    [t_AudioThread][6132] ID:[78e3a58]	ID[0]- NUMBER OF FRAMES:[0]
    [t_AudioThread][6133] ID:[78e3a58]	ID[0]-TIME BASE DEN[1000] NUM[1]
    [t_AudioThread][6134] ID:[78e3a58]	ID[0]-EXTRA DATA SIZE:[2]
    [t_AudioThread][6136] ID:[78e3a58]	ID[0]-USER INFO:[0]
    [CSubtitleProcessor][display_thread] TIMESLICE [8]ms
    [CPlayer][t_StartPlayThread] AUDIO THREAD CREATED .....[0]
    [CPlayer][t_StartPlayThread] VIDEO Q INIT (NORMAL).....
    [CPlayer][t_StartPlayThread] VIDEO QUEUE CREATED .....
    [t_WhatToUse] Codec ID [0x1c] [28]
    -- HW VIDEO CODEC : ,h264,
    	>>[ERR:TDiMpeg.cpp] GetAllowedVideoBitrate():741 Null Fuction Call !!!Must Check Implementation Code...
    [CPlayer][t_StartPlayThread] VIDEO THREAD CREATED .....
    [CPlayer][t_StartPlayThread] AUDIO PLAY THREAD CREATED .....[0]
    [CPlayer][t_StartPlayThread] DISPLAY THREAD CREATED .....
    [t_StartPlayThread][8722] ID:[78e3a58]	TOTAL BUFFER SIZE = 5000 kB
    [t_StartPlayThread][8723] ID:[78e3a58]	AUDIO Q SIZE = 2500 kB
    [t_StartPlayThread][8724] ID:[78e3a58]	VIDEO Q SIZE = 2500 kB
    [t_StartPlayThread][8725] ID:[78e3a58]	BUFFERING TIMEOUT = 30 s
    [t_StartPlayThread][8726] ID:[78e3a58]	NUMBER OF STREAMS: [2]
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[101]  CALLER[t_BufferingStart]  LINE[1634]
    [m_ControlBuffer][8000] ID:[78e3a58]	****** GROUND ZERO --> BUFFERING
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (9 / 1024) = 0%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (242 / 1024) = 23%
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[23]  CALLER[m_ControlBuffer]  LINE[8248]
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (258 / 1024) = 25%
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[25]  CALLER[m_ControlBuffer]  LINE[8248]
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (295 / 1024) = 28%
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[28]  CALLER[m_ControlBuffer]  LINE[8248]
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (311 / 1024) = 30%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (348 / 1024) = 33%
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[33]  CALLER[m_ControlBuffer]  LINE[8248]
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (364 / 1024) = 35%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (401 / 1024) = 39%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (417 / 1024) = 40%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (454 / 1024) = 44%
    openVideoDecoder---2176
    [211:158053][DEBUG][openVideoDecoder][2183] OPEN VIDEO DECODER SUCCESS
    [211:158118][DEBUG][UploadPlaybackInfo][2146] 
    #######################
    ### PLAY START !!!! ###
    #######################
    [CVideoDecoder][Open] VIDEO PIXEL FORMAT: [0]
    [CVideoDecoder][Open] HW VIDEO CODEC OPEN SUCCESS .....
    [211:158278][INFO][Open][47] [CVideoRenderer][Open] OPEN DISPLAY.. 
    [TDScaler][Connect]eOutVideoID = 0x0, eBackendId = 0xb, eWindowID = 0x0
    [TDScaler]eExtOutId = 0xd, eOutVideoId = 0x0
    [TDScaler]eSource = 0x2001, m_ePipSourceMode = 0x0, m_ePreSrcMode:0x2001
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[44]  CALLER[m_ControlBuffer]  LINE[8248]
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (470 / 1024) = 45%[TDScaler][VidId:0][3401] (CVBS OnOff:1)
    [211:159145][DEBUG][setVideoMute][1780] SCALER MUTE [MAIN] : ON
    	>>[ERR:TDiScaler.cpp] SetCurrentMediaType():234 Null Fuction Call !!!Must Check Implementation Code...
    [211:159301][INFO][m_PrepareVideoResources][12421] VIDEO DECODER & RENDERER ARE OPENED
    [t_VideoThread][4309] ID:[78e3a58]	TIME BASE DEN[1000] NUM[1]
    [t_VideoThread][4310] ID:[78e3a58]	TIMEBASE UNRELIABLE = 1
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (486 / 1024) = 47%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (502 / 1024) = 49%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (518 / 1024) = 50%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (534 / 1024) = 52%
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[52]  CALLER[m_ControlBuffer]  LINE[8248]
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (571 / 1024) = 55%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (587 / 1024) = 57%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (603 / 1024) = 58%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (640 / 1024) = 62%
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[62]  CALLER[m_ControlBuffer]  LINE[8248]
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (656 / 1024) = 64%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (672 / 1024) = 65%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (709 / 1024) = 69%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (725 / 1024) = 70%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (741 / 1024) = 72%
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[72]  CALLER[m_ControlBuffer]  LINE[8248]
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (778 / 1024) = 75%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (794 / 1024) = 77%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (810 / 1024) = 79%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (847 / 1024) = 82%
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[82]  CALLER[m_ControlBuffer]  LINE[8248]
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (863 / 1024) = 84%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (900 / 1024) = 87%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (916 / 1024) = 89%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (932 / 1024) = 91%
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[91]  CALLER[m_ControlBuffer]  LINE[8248]
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (969 / 1024) = 94%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (985 / 1024) = 96%
    [m_ControlBuffer][8245] ID:[78e3a58]	****** BUFFERING...  (1001 / 1024) = 97%
    [m_ControlBuffer][8163] ID:[78e3a58]	****** BUFFERING END A FRAME#[23/0] V FRAME#[13/0] TIME[343ms/30000ms] A SIZE[0KB/2500KB] V SIZE[0KB/2500KB]
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300035]  MESSAGE[102]  CALLER[t_BufferingEnd]  LINE[1693]
    -- VIDEO CALLBACK !!! 0, 1280, 0, 720 , frmaerate=24000
    [ERROR][hdiDecodeAudioFrame():1286] spIAe_DecodeAudioFrame 0xf00
    	>>[ERR:TDsSamMpeg.cpp] DecodeAudioFrame():2844  - SDAL ERROR [-1] !!!
    [CPlayer][t_UpdateScreen] WAITING FOR THE FIRST AUDIO FRAME ..... 1  ID[0]
    [CPlayer][t_UpdateScreen] WAITING FOR THE FIRST AUDIO FRAME ..... 2  ID[0]
    [CPlayer][t_UpdateScreen] WAITING FOR THE FIRST AUDIO FRAME ..... 3  ID[0]
    [211:788592][INFO][t_OpenAudioRenderer][12101] iSampleRate[ 44100 ], iChannels[ 2 ], iFormat[ 4 ], bLittleEndian[ 1 ]
    [ERROR][locStartI2sTx():1203] Sound0 Speaker is Not Connected...
    [211:789513][DEBUG][SetAudioMute][807] SOUND MUTE : ON
    [t_HandleAudioMuteCallBack] bOn=1, PreState=PLAY_STATE_STOP
    [t_AudioThread][6603] ID:[78e3a58]	CHANNELS:[2]
    [t_AudioThread][6604] ID:[78e3a58]	SAMPLE WIDTH IN BYTES:[4]
    [t_AudioThread][6605] ID:[78e3a58]	RATE:[44100]
    [t_AudioThread][6606] ID:[78e3a58]	AUDIO BYTES PER SEC:[352800]
    *****************************
    *****************************
    *****************************
    AST: [19089362]
    *****************************
    *****************************
    *****************************
    [211:836217][DEBUG][t_GetResolutionInfo][11929] [HW] W[1280] H[720] FR[24000] PRG[0] RES[3]
    [211:836355][DEBUG][t_SetResolutionInfo][11586] FPA
    [211:836447][DEBUG][UploadResolution][705] [MAIN][ON] W[1280] H[720] FR[24000] PRG[0] RES[3] BR[0] CODEC[3] FORMAT[4] EFFECT MODE[0], ASPECT_RATIO[0]
    [211:836770][DEBUG][setVideoQuality][1425] T[ 0 ]
    [CPlayer][t_UpdateScreen] RESOLUTION SETTING IS NOT DONE!!! 
    [TDScaler][VidId:0][544] (Mute OnOff:1)
    211840 Set Panel mute On 
    [TDsSamPanel::SetInverterForGenoaSPanelMute] Call bOnOff:0
    ------------ Inverter sw Real On Off:0
    [WINDOW_MAIN]#####Panel Mute ON #####
    ##### Mute [ON] In SetResolution Sequence~!!! #####
    [Scaler]
     TDResolution_k : [3]
    TDResolutionInfo_t [1280], [720], [0], [0], [1650], [750], [0], [24000], [0], [0], [0], [0], [0], [0], [0], [0], [12800], [0], [4], [3], [0], [120]
    [BackEnd]
     TDResolution_k : [3]
    TDResolutionInfo_t [1280], [720], [0], [0], [1650], [750], [0], [24000], [0], [0], [0], [0], [0], [0], [0], [0], [12800], [0], [4], [3], [0], [120]
    [GASFRC3DShare::t_CheckFramePackingTableUsingRealVHzForGenoaAlone] (vHz:0) (bIsVHz23980:0)
    [212:105565][DEBUG][t_GetSizeInfo][2206] FOR PLAYER ID : 0
    [212:105865][DEBUG][t_GetResolutionInfo][11929] [HW] W[1280] H[720] FR[24000] PRG[0] RES[3]
    [212:105958][DEBUG][GetOutputArea][1035] RESOLUTION [1280x720]
    [212:106022][DEBUG][GetOutputArea][1040] DISPLAY AREA [0x0]
    [212:106066][DEBUG][t_GetSizeInfo][2229] CAPTURE[0/0/1280/720]  GEOMETRY[0/0/1920/1080]
    [TDaScaler][SetGeometry][ID:0]Geometry (0, 0, 1920, 1080)
    [TDaScaler][SetCapture][ID:0]Capture (0, 0, 1280, 720)
    [ERROR][hdiSetAudioDelay():644] EXTOUT AUDIO DELAY : Extout source type is error(18)
    	>>[ERR:TDsSamAudioProcessor.cpp] t_SetAudioSpeakerDelay():2514  - SDAL ERROR [-1] !!!
    t_GASFRC3D_SetAutoMotionPlus() : Motion Plus Demo OFF
    GetBluetoothDelayFor3DVideoSync() is not 50/60HZ source
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Turn Glass to OFF
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Glass Callback Registered, Run Callback. (3D : OFF, Param : 109122216)
    [BT_SS/Fatal] 299 : [Set3DOffsetBroadcastOnOff][line:2460] Set3DOffsetBroadcastOnOff : [Disable]
    [BT_SS/Fatal] 300 : [SetShutterInfoForBroadCast][line:2452] shutter info exceeds 65535. m_frame_period[60001], m_DutyForShuttering[125]
    [BT_SS/Fatal] 301 : [Set3DModeOffSetForBroadCast][line:2178] m_b3DOffsetBroadcast[0], m_frame_period[60001]... I would make 3DGS as open
    [BT_SS/Fatal] 302 : [Set3DSyncDetection][line:2475] Set3DSyncDetection : [Disable]
    Set3DMode() : Start, TD3dEffectMode_k = 0, iVideoPlane = 0 iBackendDevice:0
    t_Set3DModeForGenoaAlone(): Game/MJC Mode is same 
    SetStereoscopicScreenMode, 395, Not supported Screen
    212280 Set Panel mute Off 
    [TDsSamPanel::SetInverterForGenoaSPanelMute] Call bOnOff:1
    ------------ Inverter sw Real On Off:1
    [WINDOW_MAIN]#####Panel Mute OFF #####
    ##### Mute [OFF] In SetResolution Sequence~!!! #####
    [212:340908][DEBUG][SetResolutionDone][666] 
    [212:340992][DEBUG][SetResolutionDone][673] PLAYER 0 [0x78e3a58] IS DONE
    GetBluetoothDelayFor3DVideoSync() is not 50/60HZ source
    [BT_SS/Fatal] 303 : [SetShutterInfoForBroadCast][line:2452] shutter info exceeds 65535. m_frame_period[60001], m_DutyForShuttering[125]
    [BT_SS/Fatal] 304 : [Set3DModeOffSetForBroadCast][line:2178] m_b3DOffsetBroadcast[0], m_frame_period[60001]... I would make 3DGS as open
    [212:356222][DEBUG][setVideoMute][1780] SCALER MUTE [MAIN] : OFF
    [TDScaler][VidId:0][544] (Mute OnOff:0)
    [212:356730][DEBUG][setVideoMute][1780] SCALER MUTE [MAIN] : OFF
    CVideoRenderer::Mute Off
    *****************************
    *****************************
    *****************************
    VST: [19140390]
    *****************************
    *****************************
    *****************************
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300033]  MESSAGE[3]  CALLER[t_UpdateScreen]  LINE[3451]
    @@@@ send event of FLASHAPP_SET_MOVIEPLAY_ON
    *****************************
    *****************************
    *****************************
    MODIIED ID:(0)'s AST: [19140390]
    *****************************
    *****************************
    *****************************
    [212:357922][DEBUG][SetAudioMute][807] SOUND MUTE : OFF
    [t_HandleAudioMuteCallBack] bOn=0, PreState=PLAY_STATE_STOP
    [t_AudioThread][6574] ID:[78e3a58]	WARNNING: AUDIO FRAME EARLY BY MORE THAN 200000 MICRO SEC [D1811000] > [S23219]
     |> ROSE PTS(    1125) START PTS(       0) FLASH PTS(    1126) RUN TIME( 0: 1:12) STATUS(4) 	 BUFFER(2145 KBtyes) ooo 
     |> ROSE PTS(    2168) START PTS(       0) FLASH PTS(    2210) RUN TIME( 0: 2:21) STATUS(4) 	 BUFFER(3016 KBtyes) ooo 
     |> ROSE PTS(    3210) START PTS(       0) FLASH PTS(    3211) RUN TIME( 0: 3:21) STATUS(4) 	 BUFFER(3932 KBtyes) ooo 
     |> ROSE PTS(    4253) START PTS(       0) FLASH PTS(    4254) RUN TIME( 0: 4:25) STATUS(4) 	 BUFFER(3796 KBtyes) ooo 
     |> ROSE PTS(    5296) START PTS(       0) FLASH PTS(    5338) RUN TIME( 0: 5:33) STATUS(4) 	 BUFFER(3628 KBtyes) ooo 
     |> ROSE PTS(    6338) START PTS(       0) FLASH PTS(    6339) RUN TIME( 0: 6:33) STATUS(4) 	 BUFFER(3487 KBtyes) ooo 
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
     |> ROSE PTS(    7381) START PTS(       0) FLASH PTS(    7382) RUN TIME( 0: 7:38) STATUS(4) 	 BUFFER(3338 KBtyes) ooo 
     |> ROSE PTS(    8382) START PTS(       0) FLASH PTS(    8383) RUN TIME( 0: 8:38) STATUS(4) 	 BUFFER(3166 KBtyes) ooo 
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
     |> ROSE PTS(    9425) START PTS(       0) FLASH PTS(    9426) RUN TIME( 0: 9:42) STATUS(4) 	 BUFFER(2993 KBtyes) ooo 
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
    ThreadProc: cookies = /mtd_down/adobe/stagecraft/data/config/ssl/certs/cookies
     |> ROSE PTS(   10467) START PTS(       0) FLASH PTS(   10468) RUN TIME( 0:10:46) STATUS(4) 	 BUFFER(2698 KBtyes) ooo 
     |> ROSE PTS(   11510) START PTS(       0) FLASH PTS(   11511) RUN TIME( 0:11:51) STATUS(4) 	 BUFFER(2211 KBtyes) ooo 
     |> ROSE PTS(   12553) START PTS(       0) FLASH PTS(   12554) RUN TIME( 0:12:55) STATUS(4) 	 BUFFER(1874 KBtyes) ooo 
    [AP_SWU/Fatal] 305 : [IsDualBSP][line:1371] This is Dual BSP!!!!!!!!!!!!!!!!!!
     |> ROSE PTS(   13595) START PTS(       0) FLASH PTS(   13596) RUN TIME( 0:13:59) STATUS(4) 	 BUFFER(1671 KBtyes) ooo 
     |> ROSE PTS(   14638) START PTS(       0) FLASH PTS(   14639) RUN TIME( 0:14:63) STATUS(4) 	 BUFFER(1449 KBtyes) ooo 
    ## RunApp [CallThread=0x7696c460] App (72) runs App(InfoLink3:67), nRunData(0xffffffff), nRunOption(0x0) ##
    Terminate~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300033]  MESSAGE[6]  CALLER[Pause]  LINE[1515]
    @@@@ send event of FLASHAPP_SET_MOVIEPLAY_OFF
    [227:319229][DEBUG][UploadPlaybackInfo][2146] 
    #######################
    ### PLAY PAUSE !!!! ###
    #######################
    [227:352154][DEBUG][SetAudioMute][807] SOUND MUTE : ON
    [t_HandleAudioMuteCallBack] bOn=1, PreState=PLAY_STATE_START
    [227:372568][INFO][closeAudioOutput][689] AUDIO DISCONNECT SUCCESS
    [227:372783][ERROR][Render][226] AUDIO RENDERER WAS NOT OPENED
    [Stop][1252] ID:[78e3a58]	CALLED BY USER
    [t_SetPlaySpeed][1776] ID:[78e3a58]	CALLED!!! speed[ 1.000000 ]
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300033]  MESSAGE[3]  CALLER[t_SetPlaySpeed]  LINE[1855]
    @@@@ send event of FLASHAPP_SET_MOVIEPLAY_ON
    [227:437287][DEBUG][UploadPlaybackInfo][2146] 
    #######################
    ### PLAY START !!!! ###
    #######################
    [CSubtitleProcessor][Stop] CALLED
    [CSubtitleProcessor][Stop] FLAG START : 1
    [CSubtitleProcessor][Stop] TRY TO STOP OTHERS ....
    [CSubtitleProcessor][t_StopAll] WAITING FOR SUBTITLE THREAD TO BE TERMINATED.. SR[0]...
    [CPlayer][t_DisplayThread] DISPLAY THREAD TERMINATED .....
    [CPlayer][t_AudioPlayThread] ID:[126761560] AUDIO PLAY THREAD TERMINATED .....
    [t_StartPlayThread][9411] ID:[78e3a58]	WAITING FOR OTHER THREADS TO BE TERMINATED..  V[0] A[0] VR[1] AR[1]
    [CSubtitleProcessor][t_StopAll] WAITING FOR SUBTITLE THREAD TO BE TERMINATED.. SR[0]...
    [CSubtitleProcessor][t_StopAll] WAITING FOR SUBTITLE THREAD TO BE TERMINATED.. SR[0]...
    [CSubtitleProcessor][t_StopAll] WAITING FOR SUBTITLE THREAD TO BE TERMINATED.. SR[0]...
    [CSubtitleProcessor][t_StopAll] WAITING FOR SUBTITLE THREAD TO BE TERMINATED.. SR[0]...
    [CSubtitleProcessor][Stop] TRY TO DEINIT CAPTION ....
    [CSubtitleProcessor][Stop] STOPPING SUBTITLE THREADS DONE ....
    [CSubtitleProcessor][Stop] DENIED : 0
    [227:496635][ERROR][Close][150] AUDIO RENDERER WAS NOT OPENED
    [CPlayer][Stop] WAITING AUDIO[0] FLAGS [D(0), R(1), REDIRECT(1)]=[1, 1, 1] or [1, 1, 3] or [1, 0, 2]
    *************DEADLOCK PROBING RESULT*************
    	AUDIO HEADQUEUE:0
    	AUDIO DECODER:0
    	AUDIO RENDERER:0
    *************************************************
    [227:504190][DEBUG][closeAudioDecoder][1220] CLOSE AUDIO DECODER
    [227:504286][INFO][t_ReleaseResourceID][3283] _RESOURCE_ eResType[ 2 ], eResID[ 0 ]
    [t_AudioThread][6932] ID:[78e3a58]	AUDIO THREAD TERMINATED
    [227:505148][DEBUG][setVideoMute][1780] SCALER MUTE [MAIN] : ON
    [TDScaler][VidId:0][544] (Mute OnOff:1)
    CVideoRenderer::Mute On
    [227:505689][ERROR][t_Mute][248] VIDEO RENDERER WAS NOT OPENED
    [227:505794][DEBUG][UploadResolution][705] [MAIN][OFF] W[0] H[0] FR[0] PRG[0] RES[0] BR[0] CODEC[-1] FORMAT[4] EFFECT MODE[0], ASPECT_RATIO[0]
    [227:506244][DEBUG][setVideoQuality][1425] T[ 0 ]
    [CPlayer][t_CloseAllVideoResource] RESOLUTION SETTING IS NOT DONE!!! 
    [Check 3D Status...]
    3D Mode to Set: [0],
    [VSI] 3D Mode: [0],
    [DSP] 3D Mode: [0],
    [RES] 3D Mode: [0]
    Skip 3D Mode Last Memory Setting...[OFF] or Auto Detected 3D Mode!!!
    [TDScaler][VidId:0][544] (Mute OnOff:1)
    227510 Set Panel mute On 
    [CPlayer][Stop] WAITING VIDEO FLAGS [D(0), R(1), REDIRECT(1)]=[1, 1, 1] or [1, 1, 3] or [1, 0, 2]
    *************DEADLOCK PROBING RESULT*************
    	VIDEO HEADQUEUE:0
    	VIDEO DECODER:0
    	VIDEO RENDERER:0
    *************************************************
    [t_StartPlayThread][9411] ID:[78e3a58]	WAITING FOR OTHER THREADS TO BE TERMINATED..  V[0] A[1] VR[1] AR[1]
    [TDsSamPanel::SetInverterForGenoaSPanelMute] Call bOnOff:0
    ------------ Inverter sw Real On Off:0
    [WINDOW_MAIN]#####Panel Mute ON #####
    ##### Mute [ON] In SetResolution Sequence~!!! #####
    [Scaler]
     TDResolution_k : [24]
    TDResolutionInfo_t [1920], [1080], [0], [0], [2640], [1125], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [8192], [0], [4], [17], [0], [0]
    [BackEnd]
     TDResolution_k : [24]
    TDResolutionInfo_t [1920], [1080], [0], [0], [2640], [1125], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [8192], [0], [4], [17], [0], [0]
    [TDaScaler][SetCapture][ID:0]Capture (0, 0, 1920, 1080)
    [t_StartPlayThread][9411] ID:[78e3a58]	WAITING FOR OTHER THREADS TO BE TERMINATED..  V[0] A[1] VR[1] AR[1]
    [t_StartPlayThread][9411] ID:[78e3a58]	WAITING FOR OTHER THREADS TO BE TERMINATED..  V[0] A[1] VR[1] AR[1]
    [t_StartPlayThread][9411] ID:[78e3a58]	WAITING FOR OTHER THREADS TO BE TERMINATED..  V[0] A[1] VR[1] AR[1]
    [ERROR][hdiSetAudioDelay():644] EXTOUT AUDIO DELAY : Extout source type is error(18)
    	>>[ERR:TDsSamAudioProcessor.cpp] t_SetAudioSpeakerDelay():2514  - SDAL ERROR [-1] !!!
    [ERROR][hdiSetAudioDelay():644] EXTOUT AUDIO DELAY : Extout source type is error(18)
    	>>[ERR:TDsSamAudioProcessor.cpp] SetDelay():2027  - SDAL ERROR [-1] !!!
    t_GASFRC3D_SetAutoMotionPlus() : Motion Plus Demo OFF
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Turn Glass to OFF
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Glass Callback Registered, Run Callback. (3D : OFF, Param : 109122216)
    [BT_SS/Fatal] 306 : [Set3DOffsetBroadcastOnOff][line:2460] Set3DOffsetBroadcastOnOff : [Disable]
    [BT_SS/Fatal] 307 : [SetShutterInfoForBroadCast][line:2452] shutter info exceeds 65535. m_frame_period[60001], m_DutyForShuttering[125]
    [BT_SS/Fatal] 308 : [Set3DModeOffSetForBroadCast][line:2178] m_b3DOffsetBroadcast[0], m_frame_period[60001]... I would make 3DGS as open
    [BT_SS/Fatal] 309 : [Set3DSyncDetection][line:2475] Set3DSyncDetection : [Disable]
    [t_StartPlayThread][9411] ID:[78e3a58]	WAITING FOR OTHER THREADS TO BE TERMINATED..  V[0] A[1] VR[1] AR[1]
    Set3DMode() : Start, TD3dEffectMode_k = 0, iVideoPlane = 0 iBackendDevice:0
    t_Set3DModeForGenoaAlone(): Game/MJC Mode is same 
    SetStereoscopicScreenMode, 395, Not supported Screen
    227850 Set Panel mute Off 
    [TDsSamPanel::SetInverterForGenoaSPanelMute] Call bOnOff:1
    ------------ Inverter sw Real On Off:1
    [WINDOW_MAIN]#####Panel Mute OFF #####
    ##### Mute [OFF] In SetResolution Sequence~!!! #####
    [227:908781][DEBUG][SetResolutionDone][666] 
    [227:908864][DEBUG][SetResolutionDone][673] PLAYER 0 [0x78e3a58] IS DONE
    [BT_SS/Fatal] 310 : [SetShutterInfoForBroadCast][line:2452] shutter info exceeds 65535. m_frame_period[60001], m_DutyForShuttering[125]
    [BT_SS/Fatal] 311 : [Set3DModeOffSetForBroadCast][line:2178] m_b3DOffsetBroadcast[0], m_frame_period[60001]... I would make 3DGS as open
    	>>[ERR:TDiScaler.cpp] SetCurrentMediaType():234 Null Fuction Call !!!Must Check Implementation Code...
    [227:912222][DEBUG][setVideoMute][1780] SCALER MUTE [MAIN] : ON
    [TDScaler][Disconnect] (VideoId:0)
    [227:912672][INFO][t_ReleaseResourceID][3283] _RESOURCE_ eResType[ 1 ], eResID[ 0 ]
    [227:912739][INFO][Close][88] [CVideoRenderer][Close] DISPLAY CLOSED.. 
    UNINSTALL CALLBACK!!!!!!!
    [t_StartPlayThread][9411] ID:[78e3a58]	WAITING FOR OTHER THREADS TO BE TERMINATED..  V[0] A[1] VR[1] AR[1]
    [227:928154][INFO][t_ReleaseResourceID][3283] _RESOURCE_ eResType[ 0 ], eResID[ 0 ]
    [227:928279][DEBUG][UploadPlaybackInfo][2146] 
    ######################
    ### PLAY STOP !!!! ###
    ######################
    [227:928419][DEBUG][closeVideoDecoder][2300] CLOSE VIDEO DECODER
    [CPlayer][t_VideoThread] ID:[126761560] VIDEO THREAD TERMINATED .....
    [CPlayer][t_StartPlayThread] TERMINATE VIDEO RESOURCES
    [CPlayer][t_StartPlayThread] TERMINATE AUDIO RESOURCES
    [227:929925][ERROR][Close][150] AUDIO RENDERER WAS NOT OPENED
    [CPlayer][t_StartPlayThread] ID:[126761560] MAIN DEMUX THREAD TERMINATED .....
    [t_SendEventToApp][9714] ID:[78e3a58]	CALLBACK[0x913b2060] TYPE[300033]  MESSAGE[5]  CALLER[t_StartPlayThread]  LINE[9497]
    @@@@ send event of FLASHAPP_SET_MOVIEPLAY_OFF
    [Stop][1423] ID:[78e3a58]	STOPPING THREADS DONE
    [SetOutputICT][2086]
    [SetOutputICT][2091] m_CallBackICT == NULL
    [SetOutputMacrovision][2039]
    [SetOutputMacrovision][2044]
     m_CallBackMacroVision== NULL[SetOutputVBIData][2063]
    [SetOutputVBIData][2068] m_CallBackVBIData == NULL
    [227:930747][DEBUG][ReleasePlayer][535] 
    [227:930795][DEBUG][ReleasePlayer][541] PLAYER 0 [0x78e3a58]IS RELEASED
    ========================== ELAPSED TIME CHECKER ==========================
    TIME: 1-1. GET MEDIA 	(0 ms)
    TIME: 1-4. DELAY BTWN GETMEDIA TO PLAY 	(102 ms)
    TIME: 2-1. PLAY->BEFORE START DEMUX 	(6 ms)
    TIME: 2-2. START DEMUX -> BUFFERING ENDS 	(676 ms)
    TIME: 2-3. BUFFERING ENDS -> FIRST FRAME DECODED 	(25 ms)
    TIME: 2-4. FIRST FRAME DECODED -> BEFORE VIDEO QUALITY SETTING 	(315 ms)
    TIME: 2-5. VIDEO QUALITY SETTING -> FIRST FRAME DISPLAYED 	(520 ms)
    TIME: 3. TOTAL TIME FOR FIRST FRAME DISPLAY 	(1647 ms)
    TIME: 4-1. TRICK STOP 	(0 ms)
    TIME: 4-2. SUBTITLE STOP 	(59 ms)
    TIME: 4-3. AUDIO STOP 	(8 ms)
    TIME: 4-4. VIDEO STOP 	(425 ms)
    TIME: 4-5. 	VIDEO RENDERER STOP 	(407 ms)
    TIME: 4-6. 	VIDEO DECODER STOP 	(15 ms)
    TIME: 4-7. DEMUXER STOP 	(0 ms)
    TIME: 4-8. MACROVISION RESET 	(0 ms)
    TIME: 5. TOTAL TIME FOR STOP  	(494 ms)
    ==========================================================================
    [227:931777][ERROR][Close][600] [0x6c86540] MEDIA CLOSE FAIL
    [0;40;31m bye~ Player Destructor end
    ================================
    [~SamsungStreamPlayer(0, 0x79500f0)] DESTROYED...	END !!!
    ================================
    ~QueuedFrames: 
    ~QueuedFrames: 
    [FLASH_PLAYER/Fatal] 312 : @@@@ Delete General Render Plane
    ############################
    /home1/dblee/Genoa/GS_R_AP/AP_FlashPlayer/SC1.2/source/ae/kernel/platformloaders/linux/AELoader.cpp-UninitializeStagecraftLibrary_12
    ############################
    ############################
    /home1/dblee/Genoa/GS_R_AP/AP_FlashPlayer/SC1.2/source/ae/kernel/platformloaders/linux/AELoader.cpp-UninitializeAEKernel_12
    ############################
    Set3DEffectFunction Called...[true] Power Off Sequence [0])
    DynamicControl:5, FullOSD:false 
    [FLASH_APP/Fatal] 313 : no need to change source
    ####### Header = 12, 0
    Set3DEffectFunction Called...[false] Power Off Sequence [0])
    [AP_INFOLINK/Fatal] 314 : Call activateSmartSideBar
    (DbgMaple) [AP_BROWSER/Fatal] 315 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/ae/aeWidgetEngine.cpp:1223 in activateSmartSideBar() 
    (DbgMaple) [AP_BROWSER/Fatal] 316 : Enter activateSmartSideBar (id : 10110000001)
    (DbgMaple) [AP_BROWSER/Fatal] 317 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/am/amApplication.cpp:1302 in show() 
    (DbgMaple) [AP_BROWSER/Fatal] 318 : CApplication::show (app : 0x6b6c008, task : 0x6b6c0b0) (SCREEN NUMBER=1)
    (DbgMaple) [AP_BROWSER/Fatal] 319 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/am/amApplication.cpp:1304 in show() 
    (DbgMaple) [AP_BROWSER/Fatal] 320 : CApplication::show current screen resolution (1280x720), widget resolution (1280x720)
    (DbgMaple) [AP_BROWSER/Fatal] 321 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/am/amManagerWidget.cpp:457 in onActivateManagerWidget() 
    (DbgMaple) [AP_BROWSER/Fatal] 322 : onActivateManagerWidget
    (DbgAlert) [AP_WIDGET/Fatal] 323 : alert() : [Smart Hub Log] ########## Activate ##########
    (DbgAlert) [AP_WIDGET/Fatal] 324 : alert() : [Smart Hub Log] SmartHomeMain.setFocus() ==> UISmartHome.call
    Set3DEffectFunction Called...[false] Power Off Sequence [0])
    DynamicControl:5, FullOSD:true 
    (DbgMaple) [AP_BROWSER/Fatal] 325 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/ae/aeWidgetEngine.cpp:1253 in activateSmartSideBar() 
    (DbgMaple) [AP_BROWSER/Fatal] 326 : Exit activateSmartSideBar (id : 10110000001)
    [AP_INFOLINK/Fatal] 327 : CWidgetEngine::activateSmartSideBar returns TRUE
    [AP_INFOLINK/Fatal] 328 : Setting m_SafeAlarm->Reset(TIME_OUT_STOP, 0);
    [AP_INFOLINK/Fatal] 329 : ### MESSAGE_WEBSVC_ACTIVATE_READY_WM ###, m_bFirstStart [0]
    [AP_INFOLINK/Fatal] 330 : Update is False
    [AP_INFOLINK/Fatal] 331 : Setting m_SafeAlarm->Reset(TIME_OUT_STOP, 0);
    [AP_INFOLINK/Fatal] 332 : ### MESSAGE_WEBSVC_ACTIVATE_READY_WM ###, m_bFirstStart [0]
    [AP_INFOLINK/Fatal] 333 : Update is False
    (DbgAlert) [AP_WIDGET/Fatal] 334 : alert() : [Smart Hub Log]  @@@@@@@ SetPIG @@@@@@
    [DEFAULT/Debugging] 335 : CApp::SendEvent Event Receiver NULL-app[101]
    SetPreviousSource at 712 - 1
    SetPreviousSource at 717 - 2 Main Window
    SetPreviousSource at 724 - 4 
    SetPreviousSource at 726 - 5 
    SetPreviousSource at 741 - 8 
    [TPAWindow.cpp][DisconnectSource][WID:0][CALL]..
    [Check 3D Status...]
    3D Mode to Set: [0],
    [VSI] 3D Mode: [0],
    [DSP] 3D Mode: [0],
    [RES] 3D Mode: [0]
    Skip 3D Mode Last Memory Setting...[OFF] or Auto Detected 3D Mode!!!
    [Check 3D Status...]
    3D Mode to Set: [0],
    [VSI] 3D Mode: [0],
    [DSP] 3D Mode: [0],
    [RES] 3D Mode: [0]
    Skip 3D Mode Last Memory Setting...[OFF] or Auto Detected 3D Mode!!!
    [229:518124][DEBUG][UninstallVideoMuteCallback][1064] 
    [TDScaler][Disconnect] (VideoId:0)
    [ERROR][hdiSetAudioDelay():644] EXTOUT AUDIO DELAY : Extout source type is error(18)
    	>>[ERR:TDsSamAudioProcessor.cpp] SetDelay():2027  - SDAL ERROR [-1] !!!
    [229:518753][DEBUG][UninstallAudioMuteCallback][904] 
    [TPAWindow.cpp][DisconnectSource][WID:0][END]..
    [229:565694][DEBUG][UninstallResolutionCallback][794] 
    [UninstallResourceRequestCallback][822]
    [229:566084][DEBUG][UninstallAudioFormatCallback][947] 
    [TPAWindow.cpp][ConnectSource][WID:0][CALL]..
    (DbgAlert) [AP_WIDGET/Fatal] 336 : alert() : [Smart Hub Log] SET HIGHLIGHT....
    [DEFAULT/Debugging] 337 : CApp::SendEvent Event Receiver NULL-app[101]
    ####### Header = 12, 0
    [TDScaler][Connect]eOutVideoID = 0x0, eBackendId = 0x4, eWindowID = 0x0
    [TDScaler]eExtOutId = 0xd, eOutVideoId = 0x0
    [TDScaler]eSource = 0x901, m_ePipSourceMode = 0x0, m_ePreSrcMode:0x2001
    [TDScaler][VidId:0][3401] (CVBS OnOff:1)
    [Scaler]
     TDResolution_k : [15]
    TDResolutionInfo_t [720], [576], [0], [0], [864], [625], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [2305], [0], [4], [17], [0], [0]
    Source : 0x901, WindowType : 0 ExtInID : 0, BackEndID : 4, tdRet=0 
    ### eSrc 0x901, Audio Format [Not Support String 27], DDCompMode RF, Factory value -9, Real set value to SDAL 0
    [TPAWindow.cpp][ConnectSource][WID:0][END]..
    [TDScaler][VidId:2][770] (VideoOnOff:1)
    ============>TDaShare::m_StreamPath:1
    	>>[ERR:TDiDemux.cpp] SetInputType():208 Null Fuction Call !!!Must Check Implementation Code...
    [TPAWindow.cpp][ConnectSource][WID:4][CALL]..
    [TDScaler][Connect]eOutVideoID = 0x2, eBackendId = 0x0, eWindowID = 0x3
    [TDScaler]eExtOutId = 0x1, eOutVideoId = 0x2
    [TDScaler]eSource = 0x201, m_ePipSourceMode = 0x0, m_ePreSrcMode:0x901
    [Scaler]
     TDResolution_k : [21]
    TDResolutionInfo_t [720], [576], [0], [0], [864], [625], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [513], [1], [0], [17], [0], [0]
    Source : 0x201, WindowType : 4 ExtInID : 0, BackEndID : 7, tdRet=0 
    [ERROR][StopPcr():595] [WARN] PCR is already stopped!! 
    	>>[ERR:TDsSamAudioProcessor.cpp] Connect():672  - SDAL ERROR [-1] !!!
    [TPAWindow.cpp][ConnectSource][WID:4][END]..
    	>>[ERR:TDiDemux.cpp] SetInputType():208 Null Fuction Call !!!Must Check Implementation Code...
    [ERROR][StartAudio():304] PLAY ENGINE FAIL 
    	>>[ERR:TDsSamMpeg.cpp] StartAudioDecoding():1986  - SDAL ERROR [-2] !!!
    [ERROR][StopPcr():595] [WARN] PCR is already stopped!! 
    [Check 3D Status...]
    3D Mode to Set: [0],
    [VSI] 3D Mode: [0],
    [DSP] 3D Mode: [0],
    [RES] 3D Mode: [0]
    Skip 3D Mode Last Memory Setting...[OFF] or Auto Detected 3D Mode!!!
    [Scaler]
     TDResolution_k : [15]
    TDResolutionInfo_t [720], [576], [0], [0], [864], [625], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [2305], [0], [4], [17], [0], [0]
    [BackEnd]
     TDResolution_k : [15]
    TDResolutionInfo_t [720], [576], [0], [0], [864], [625], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [2305], [0], [4], [17], [0], [0]
    [TDaScaler][SetGeometry][ID:0]Geometry (60, 112, 482, 274)
    [TDaScaler][SetCapture][ID:0]Capture (26, 15, 668, 544)
    [ERROR][hdiSetAudioDelay():644] EXTOUT AUDIO DELAY : Extout source type is error(18)
    	>>[ERR:TDsSamAudioProcessor.cpp] t_SetAudioSpeakerDelay():2514  - SDAL ERROR [-1] !!!
    t_GASFRC3D_SetAutoMotionPlus() : Motion Plus Demo OFF
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Turn Glass to OFF
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Glass Callback Registered, Run Callback. (3D : OFF, Param : 109122216)
    [BT_SS/Fatal] 338 : [Set3DOffsetBroadcastOnOff][line:2460] Set3DOffsetBroadcastOnOff : [Disable]
    [BT_SS/Fatal] 339 : [SetShutterInfoForBroadCast][line:2452] shutter info exceeds 65535. m_frame_period[60001], m_DutyForShuttering[125]
    [BT_SS/Fatal] 340 : [Set3DModeOffSetForBroadCast][line:2178] m_b3DOffsetBroadcast[0], m_frame_period[60001]... I would make 3DGS as open
    [BT_SS/Fatal] 341 : [Set3DSyncDetection][line:2475] Set3DSyncDetection : [Disable]
    Set3DMode() : Start, TD3dEffectMode_k = 0, iVideoPlane = 0 iBackendDevice:0
    t_Set3DModeForGenoaAlone(): Game/MJC Mode is same 
    SetStereoscopicScreenMode, 395, Not supported Screen
    [TDScaler][VidId:0][544] (Mute OnOff:0)
    [BT_SS/Fatal] 342 : [SetShutterInfoForBroadCast][line:2452] shutter info exceeds 65535. m_frame_period[60001], m_DutyForShuttering[125]
    [BT_SS/Fatal] 343 : [Set3DModeOffSetForBroadCast][line:2178] m_b3DOffsetBroadcast[0], m_frame_period[60001]... I would make 3DGS as open
    GetServerType in plNNavi_pscomm.cpp . line 287
    [otn_parse_pdl_doc] errro pdl_get_value log_url
    [ERROR][StopPcr():595] [WARN] PCR is already stopped!! 
    [ERROR][StopPcr():595] [WARN] PCR is already stopped!! 
    [ERROR][StartAudio():304] PLAY ENGINE FAIL 
    	>>[ERR:TDsSamMpeg.cpp] StartAudioDecoding():1986  - SDAL ERROR [-2] !!!
    [Scaler]
     TDResolution_k : [21]
    TDResolutionInfo_t [720], [576], [0], [0], [864], [625], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [513], [1], [0], [17], [0], [0]
    [TDaScaler][SetGeometry][ID:2]Geometry (0, 0, 720, 576)
    [TDaScaler][SetCapture][ID:2]Capture (0, 0, 720, 576)
    GetServerType in plNNavi_pscomm.cpp . line 287
    (DbgAlert) [AP_WIDGET/Fatal] 344 : alert() : [Smart Hub Log] @@@@@ video mute ON @@@@@
    [TDScaler][VidId:0][544] (Mute OnOff:1)
    Hi there deliah wildweed 159
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 39848
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 45541
    [0m 
    (DbgMaple) [AP_BROWSER/Fatal] 345 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/am/amWidget.cpp:50 in onTaskCreate() 
    (DbgMaple) [AP_BROWSER/Fatal] 346 : Enter CWidget::onTaskCreate (widget : 0x6caf7d8[11091000000], task : 0x7326dd0) (SCREEN NUMBER=1)
    (DbgMaple) [AP_BROWSER/Fatal] 347 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/plProcess.c:767 in pl_InitStaticPLClass() 
    (DbgMaple) [AP_BROWSER/Fatal] 348 : [Maple Side Plugin] "Camera" plugin is not supported in this application.
    (DbgMaple) [AP_BROWSER/Fatal] 349 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/plProcess.c:767 in pl_InitStaticPLClass() 
    (DbgMaple) [AP_BROWSER/Fatal] 350 : [Maple Side Plugin] "Skype" plugin is not supported in this application.
    (DbgMaple) [AP_BROWSER/Fatal] 351 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/plProcess.c:767 in pl_InitStaticPLClass() 
    (DbgMaple) [AP_BROWSER/Fatal] 352 : [Maple Side Plugin] "Remote" plugin is not supported in this application.
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 36077
    [0m 
    Singletone emp is running. name:[AppCommon] Emp:[42328] , Client:[36077] ,  Option:[SINGLETON]  , Status:[2][CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 52821
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 45375
    [0m 
    [EmpMain::EmpMain(59)] <<< EmpMain start >>>
    [EmpMain::EmpMain(74)] EmpMain nPort = [45375] nLogParam = [-1]
    [CSEFDebug::SetDebugModule(46)] Log module = 2, onOff = 0
    [CheckVersion(45)] 
    [1;31;42m CheckVersion(strVersion=[2.000]), (m_strVersion=[2.301]) 
    [0m 
    [t9wrapper::InitIME(1144)]InitIME called with new xxt9oem
    [t9wrapper::SetLanguage(1299)]pLanguage is [69]
    [t9wrapper::ImportUDBData(954)]Error: no UDB file is on your device for import operation
    Hi there deliah wildweed 159
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 48184
    [0m 
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 60644
    [0m 
    [CEmpAppXT9(23)] 
    [1;31;42m EMP XT9 VERSION:[4.102]
    [0m 
    [EmpMain::EmpMain(59)] <<< EmpMain start >>>
    [EmpMain::EmpMain(74)] EmpMain nPort = [60644] nLogParam = [-1]
    [CSEFDebug::SetDebugModule(46)] Log module = 2, onOff = 0
    Thrift: Thu Jan  1 00:03:59 1970 TSocket::open() connect() <Host: localhost Port: 60644>errno = 111
    [CBrokerProxyEmp::Execute(148)] 
    [1;31;42m Execute call error [connect() failed: errno = 111]
    [0m 
    [CheckVersion(47)] 
    [1;31;42m CheckVersion(strVersion=[1.0]), (m_strVersion(real)=[4.102]) 
    [0m 
    XT9 VERSION 20110802.1626 NEW GREEK INCLUDED
    [SetLanguage](147)DO NOT need to set the same language again(non-Korea)
    Hi there deliah wildweed 159
    [CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 38049
    [0m 
    [t9wrapper::SetLanguage(1299)]pLanguage is [70]
    Singletone emp is running. name:[TV] Emp:[47969] , Client:[38049] ,  Option:[SINGLETON]  , Status:[2][CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 50024
    [0m 
    Singletone emp is running. name:[NNavi] Emp:[35490] , Client:[50024] ,  Option:[SINGLETON]  , Status:[2][CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 34887
    [0m 
    Singletone emp is running. name:[Network] Emp:[59603] , Client:[34887] ,  Option:[SINGLETON]  , Status:[2][CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 37935
    [0m 
    Singletone emp is running. name:[ExternalWidgetInterface] Emp:[41372] , Client:[37935] ,  Option:[SINGLETON]  , Status:[2][CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 56144
    [0m 
    Singletone emp is running. name:[TV] Emp:[47969] , Client:[56144] ,  Option:[SINGLETON]  , Status:[2][CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 48545
    [0m 
    Singletone emp is running. name:[TVMW] Emp:[45702] , Client:[48545] ,  Option:[SINGLETON]  , Status:[2][CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 40380
    [0m 
    Singletone emp is running. name:[Device] Emp:[39918] , Client:[40380] ,  Option:[SINGLETON]  , Status:[2][CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 38042
    [0m 
    Singletone emp is running. name:[AppCommon] Emp:[42328] , Client:[38042] ,  Option:[SINGLETON]  , Status:[2][CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 49679
    [0m 
    Singletone emp is running. name:[ExternalWidgetInterface] Emp:[41372] , Client:[49679] ,  Option:[SINGLETON]  , Status:[2][CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 45059
    [0m 
    Singletone emp is running. name:[Network] Emp:[59603] , Client:[45059] ,  Option:[SINGLETON]  , Status:[2][CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 49977
    [0m 
    Singletone emp is running. name:[FrontPanel] Emp:[52052] , Client:[49977] ,  Option:[SINGLETON]  , Status:[2][CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 51155
    [0m 
    Singletone emp is running. name:[TVMW] Emp:[45702] , Client:[51155] ,  Option:[SINGLETON]  , Status:[2][CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 37613
    [0m 
    Singletone emp is running. name:[Audio] Emp:[59471] , Client:[37613] ,  Option:[SINGLETON]  , Status:[2][CSocketPorts::GetPort(181)] 
    [1;31;42m Port Number: 39714
    [0m 
    Singletone emp is running. name:[NNavi] Emp:[35490] , Client:[39714] ,  Option:[SINGLETON]  , Status:[2][InstallResourceRequestCallback][811]
    [243:408840][DEBUG][InstallResourceRequestCallback][812] 
    @@@[SSSO SOURCE_TYPE_DTV1] [SsSourceBase.cpp] ControlAudioClip, ControlType[1]
    [TPAWindow.cpp][DisconnectSource][WID:4][CALL]..
    [TDScaler][Disconnect] (VideoId:2)
    [TPAWindow.cpp][DisconnectSource][WID:4][END]..
    	>>[ERR:TDiDemux.cpp] SetInputType():208 Null Fuction Call !!!Must Check Implementation Code...
    [ERROR][StopPcr():595] [WARN] PCR is already stopped!! 
    [ERROR][StopPcr():595] [WARN] PCR is already stopped!! 
    [UninstallResourceRequestCallback][822]
    [TDScaler][VidId:2][770] (VideoOnOff:0)
    [TPAWindow.cpp][DisconnectSource][WID:0][CALL]..
    [Check 3D Status...]
    3D Mode to Set: [0],
    [VSI] 3D Mode: [0],
    [DSP] 3D Mode: [0],
    [RES] 3D Mode: [0]
    Skip 3D Mode Last Memory Setting...[OFF] or Auto Detected 3D Mode!!!
    [TDScaler][Disconnect] (VideoId:0)
    [TPAWindow.cpp][DisconnectSource][WID:0][END]..
    [InstallResourceRequestCallback][811]
    [243:611322][DEBUG][InstallResourceRequestCallback][812] 
    [243:611397][DEBUG][InstallAudioFormatCallback][937] 
    [243:611649][DEBUG][InstallResolutionCallback][648] 
    [TPAWindow.cpp][ConnectSource][WID:0][CALL]..
    [TDScaler][Connect]eOutVideoID = 0x0, eBackendId = 0xb, eWindowID = 0x0
    [TDScaler]eExtOutId = 0xd, eOutVideoId = 0x0
    [TDScaler]eSource = 0x2000, m_ePipSourceMode = 0x0, m_ePreSrcMode:0x901
    [TDScaler][VidId:0][3401] (CVBS OnOff:1)
    [Scaler]
     TDResolution_k : [24]
    TDResolutionInfo_t [1920], [1080], [0], [0], [2640], [1125], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [8192], [0], [4], [17], [0], [0]
    [243:629784][DEBUG][InstallVideoMuteCallback][1037] 
    [InstallAudioMuteCallback][894]
    [Check 3D Status...]
    3D Mode to Set: [0],
    [VSI] 3D Mode: [0],
    [DSP] 3D Mode: [0],
    [RES] 3D Mode: [0]
    Skip 3D Mode Last Memory Setting...[OFF] or Auto Detected 3D Mode!!!
    [Scaler]
     TDResolution_k : [24]
    TDResolutionInfo_t [1920], [1080], [0], [0], [2640], [1125], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [8192], [0], [4], [17], [0], [0]
    [BackEnd]
     TDResolution_k : [24]
    TDResolutionInfo_t [1920], [1080], [0], [0], [2640], [1125], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [8192], [0], [4], [17], [0], [0]
    [TDaScaler][SetGeometry][ID:0]Geometry (0, 0, 1920, 1080)
    [TDaScaler][SetCapture][ID:0]Capture (0, 0, 1920, 1080)
    [ERROR][hdiSetAudioDelay():644] EXTOUT AUDIO DELAY : Extout source type is error(18)
    	>>[ERR:TDsSamAudioProcessor.cpp] t_SetAudioSpeakerDelay():2514  - SDAL ERROR [-1] !!!
    [ERROR][hdiSetAudioDelay():644] EXTOUT AUDIO DELAY : Extout source type is error(18)
    	>>[ERR:TDsSamAudioProcessor.cpp] SetDelay():2027  - SDAL ERROR [-1] !!!
    t_GASFRC3D_SetAutoMotionPlus() : Motion Plus Demo OFF
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Turn Glass to OFF
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Glass Callback Registered, Run Callback. (3D : OFF, Param : 109122216)
    [BT_SS/Fatal] 353 : [Set3DOffsetBroadcastOnOff][line:2460] Set3DOffsetBroadcastOnOff : [Disable]
    [BT_SS/Fatal] 354 : [SetShutterInfoForBroadCast][line:2452] shutter info exceeds 65535. m_frame_period[60001], m_DutyForShuttering[125]
    [BT_SS/Fatal] 355 : [Set3DModeOffSetForBroadCast][line:2178] m_b3DOffsetBroadcast[0], m_frame_period[60001]... I would make 3DGS as open
    [BT_SS/Fatal] 356 : [Set3DSyncDetection][line:2475] Set3DSyncDetection : [Disable]
    Set3DMode() : Start, TD3dEffectMode_k = 0, iVideoPlane = 0 iBackendDevice:0
    t_Set3DModeForGenoaAlone(): Game/MJC Mode is same 
    SetStereoscopicScreenMode, 395, Not supported Screen
    [244:202512][DEBUG][SetResolutionDone][666] 
    [TPAWindow.cpp][ConnectSource][WID:0][END]..
    [DEFAULT/Debugging] 357 :  [CMovieDemoAppBase::t_OnEvent - 427] EVENT_SET_MEDIA 
    GetServerType in plNNavi_pscomm.cpp . line 287
    ####### Header = 12, 0
    (DbgAlert) [AP_WIDGET/Fatal] 358 : alert() : [Smart Hub Log] SmartHomeMain.showWidget()
    (DbgAlert) [AP_WIDGET/Fatal] 359 : alert() : [Smart Hub Log] UISmartHome.hide()   pMoveOut true
    ####### Header = 12, 0
    (DbgAlert) [AP_WIDGET/Fatal] 360 : alert() : [Smart Hub Log] @@@@@ ReleasePIG @@@@@
    Task SetBannerState : [0] 
    Task SetBannerState : [0] 
    DynamicControl:5, FullOSD:true 
    (DbgMaple) [AP_BROWSER/Fatal] 361 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/am/amApplication.cpp:1386 in hide() 
    (DbgMaple) [AP_BROWSER/Fatal] 362 : CApplication::hide (app : 0x6b6c008, task : 0x6b6c0b0)
    (DbgMaple) [AP_BROWSER/Fatal] 363 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/am/amApplication.cpp:1302 in show() 
    (DbgMaple) [AP_BROWSER/Fatal] 364 : CApplication::show (app : 0x6caf7d8, task : 0x7326dd0) (SCREEN NUMBER=1)
    (DbgMaple) [AP_BROWSER/Fatal] 365 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/am/amApplication.cpp:1304 in show() 
    (DbgMaple) [AP_BROWSER/Fatal] 366 : CApplication::show current screen resolution (1280x720), widget resolution (960x540)
    (DbgMaple) [AP_BROWSER/Fatal] 367 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/am/amApplication.cpp:1323 in show() 
    (DbgMaple) [AP_BROWSER/Fatal] 368 : CApplication::show change resolution (SCREEN NUMBER=1) (SCREEN RESOLUTION[960x540])
    Task SendEventToDevice : [3] [7200] 
    Set3DEffectFunction Called...[true] Power Off Sequence [0])
    GetServerType in plNNavi_pscomm.cpp . line 287
    (DbgAlert) [AP_WIDGET/Fatal] 369 : alert() : [Facebook] 2011 DTV Model
    GetServerType in plNNavi_pscomm.cpp . line 287
    Task SetBannerState : [0] 
    (DbgMaple) [AP_BROWSER/Fatal] 370 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/ae/aeApplicationEngine.cpp:930 in destroyApplication() 
    (DbgMaple) [AP_BROWSER/Fatal] 371 : Enter destroyApplication (app : 0x6caf7d8)
    (DbgMaple) [AP_BROWSER/Fatal] 372 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/am/amApplication.cpp:864 in onEvent() 
    (DbgMaple) [AP_BROWSER/Fatal] 373 : Prepare to exit. (app : 0x6caf7d8)
    [TPAWindow.cpp][DisconnectSource][WID:0][CALL]..
    [Check 3D Status...]
    3D Mode to Set: [0],
    [VSI] 3D Mode: [0],
    [DSP] 3D Mode: [0],
    [RES] 3D Mode: [0]
    Skip 3D Mode Last Memory Setting...[OFF] or Auto Detected 3D Mode!!!
    [Check 3D Status...]
    3D Mode to Set: [0],
    [VSI] 3D Mode: [0],
    [DSP] 3D Mode: [0],
    [RES] 3D Mode: [0]
    Skip 3D Mode Last Memory Setting...[OFF] or Auto Detected 3D Mode!!!
    [257:301029][DEBUG][UninstallVideoMuteCallback][1064] 
    [TDScaler][Disconnect] (VideoId:0)
    [ERROR][hdiSetAudioDelay():644] EXTOUT AUDIO DELAY : Extout source type is error(18)
    	>>[ERR:TDsSamAudioProcessor.cpp] SetDelay():2027  - SDAL ERROR [-1] !!!
    [257:301786][DEBUG][UninstallAudioMuteCallback][904] 
    [TPAWindow.cpp][DisconnectSource][WID:0][END]..
    [257:302150][DEBUG][UninstallResolutionCallback][794] 
    [UninstallResourceRequestCallback][822]
    [257:302295][DEBUG][UninstallAudioFormatCallback][947] 
    (DbgMaple) [AP_BROWSER/Fatal] 374 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:212 in PL_SendShutdownEvent() 
    (DbgMaple) [AP_BROWSER/Fatal] 375 : [Maple Plugin Event] End PL_SHUTDOWN Event : AppCommon(0x6c98770) plugin app.
     @@@@@ IME Plugin OnShutdown @@@@@
    (DbgMaple) [AP_BROWSER/Fatal] 376 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:212 in PL_SendShutdownEvent() 
    (DbgMaple) [AP_BROWSER/Fatal] 377 : [Maple Plugin Event] End PL_SHUTDOWN Event : IME(0x78e1c08) plugin app.
    (DbgMaple) [AP_BROWSER/Fatal] 378 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:212 in PL_SendShutdownEvent() 
    (DbgMaple) [AP_BROWSER/Fatal] 379 : [Maple Plugin Event] End PL_SHUTDOWN Event : Sef(0x7393a78) plugin app.
    (DbgMaple) [AP_BROWSER/Fatal] 380 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:212 in PL_SendShutdownEvent() 
    (DbgMaple) [AP_BROWSER/Fatal] 381 : [Maple Plugin Event] End PL_SHUTDOWN Event : Sef(0x788d940) plugin app.
    (DbgMaple) [AP_BROWSER/Fatal] 382 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:212 in PL_SendShutdownEvent() 
    (DbgMaple) [AP_BROWSER/Fatal] 383 : [Maple Plugin Event] End PL_SHUTDOWN Event : NNavi(0x7a72900) plugin app.
    (DbgMaple) [AP_BROWSER/Fatal] 384 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:212 in PL_SendShutdownEvent() 
    [CEmpApp::StartServer(161)] 
    [1;31;42m The Server was gone with before port[45375], last port[45375]
    [0m 
    (DbgMaple) [AP_BROWSER/Fatal] 385 : [Maple Plugin Event] End PL_SHUTDOWN Event : Network(0x704f3a8) plugin app.
    (DbgMaple) [AP_BROWSER/Fatal] 386 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:212 in PL_SendShutdownEvent() 
    (DbgMaple) [AP_BROWSER/Fatal] 387 : [Maple Plugin Event] End PL_SHUTDOWN Event : ExternalWidgetInterface(0x7987bc8) plugin app.
    (DbgMaple) [AP_BROWSER/Fatal] 388 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:212 in PL_SendShutdownEvent() 
    (DbgMaple) [AP_BROWSER/Fatal] 389 : [Maple Plugin Event] End PL_SHUTDOWN Event : TV(0x79c8a20) plugin app.
    (DbgMaple) [AP_BROWSER/Fatal] 390 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:212 in PL_SendShutdownEvent() 
    (DbgMaple) [AP_BROWSER/Fatal] 391 : [Maple Plugin Event] End PL_SHUTDOWN Event : TVMW(0x7a70320) plugin app.
    (DbgMaple) [AP_BROWSER/Fatal] 392 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:212 in PL_SendShutdownEvent() 
    (DbgMaple) [AP_BROWSER/Fatal] 393 : [Maple Plugin Event] End PL_SHUTDOWN Event : Device(0x7a03d90) plugin app.
    (DbgMaple) [AP_BROWSER/Fatal] 394 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:212 in PL_SendShutdownEvent() 
    (DbgMaple) [AP_BROWSER/Fatal] 395 : [Maple Plugin Event] End PL_SHUTDOWN Event : AppCommon(0x7405878) plugin app.
    (DbgMaple) [AP_BROWSER/Fatal] 396 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:212 in PL_SendShutdownEvent() 
    (DbgMaple) [AP_BROWSER/Fatal] 397 : [Maple Plugin Event] End PL_SHUTDOWN Event : ExternalWidgetInterface(0x7a0a6c0) plugin app.
    [TPAWindow.cpp][ConnectSource][WID:0][CALL]..
    (DbgMaple) [AP_BROWSER/Fatal] 398 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:212 in PL_SendShutdownEvent() 
    (DbgMaple) [AP_BROWSER/Fatal] 399 : [Maple Plugin Event] End PL_SHUTDOWN Event : Network(0x719af98) plugin app.
    (DbgMaple) [AP_BROWSER/Fatal] 400 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:212 in PL_SendShutdownEvent() 
    (DbgMaple) [AP_BROWSER/Fatal] 401 : [Maple Plugin Event] End PL_SHUTDOWN Event : FrontPanel(0x7044460) plugin app.
    (DbgMaple) [AP_BROWSER/Fatal] 402 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:212 in PL_SendShutdownEvent() 
    (DbgMaple) [AP_BROWSER/Fatal] 403 : [Maple Plugin Event] End PL_SHUTDOWN Event : PowerInfolinkPlayer(0x7a0f9d8) plugin app.
    [CEmpApp::StartServer(161)] 
    [1;31;42m The Server was gone with before port[60644], last port[60644]
    [0m 
    (DbgMaple) [AP_BROWSER/Fatal] 404 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:212 in PL_SendShutdownEvent() 
    [TDScaler][Connect]eOutVideoID = 0x0, eBackendId = 0x4, eWindowID = 0x0
    [TDScaler]eExtOutId = 0xd, eOutVideoId = 0x0
    [TDScaler]eSource = 0x901, m_ePipSourceMode = 0x0, m_ePreSrcMode:0x2000
    (DbgMaple) [AP_BROWSER/Fatal] 405 : [Maple Plugin Event] End PL_SHUTDOWN Event : TVMW(0x787a3f8) plugin app.
    [TDScaler][VidId:0][3401] (CVBS OnOff:1)
    [Scaler]
     TDResolution_k : [15]
    TDResolutionInfo_t [720], [576], [0], [0], [864], [625], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [2305], [0], [4], [17], [0], [0]
    Source : 0x901, WindowType : 0 ExtInID : 0, BackEndID : 4, tdRet=0 
    ### eSrc 0x901, Audio Format [Not Support String 27], DDCompMode RF, Factory value -9, Real set value to SDAL 0
    [TPAWindow.cpp][ConnectSource][WID:0][END]..
    (DbgMaple) [AP_BROWSER/Fatal] 406 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:212 in PL_SendShutdownEvent() 
    (DbgMaple) [AP_BROWSER/Fatal] 407 : [Maple Plugin Event] End PL_SHUTDOWN Event : Audio(0x78a87d0) plugin app.
    (DbgMaple) [AP_BROWSER/Fatal] 408 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:212 in PL_SendShutdownEvent() 
    (DbgMaple) [AP_BROWSER/Fatal] 409 : [Maple Plugin Event] End PL_SHUTDOWN Event : NNavi(0x718bdc8) plugin app.
    (DbgMaple) [AP_BROWSER/Fatal] 410 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/am/amApplication.cpp:502 in onEvent() 
    (DbgMaple) [AP_BROWSER/Fatal] 411 : Received PHND stop ack (app : 0x6caf7d8)
    (DbgMaple) [AP_BROWSER/Fatal] 412 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:819 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 413 : [Maple Plugin Event] Destroy Plugin : IME(0x78e1c08) plugin app. (Decrease Ref Count of Application (0x6caf7d8 count 18 to 17)
    (DbgMaple) [AP_BROWSER/Fatal] 414 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:894 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 415 : [Maple Plugin Event] Plugin Task & Plugin Info(NPPluginObjInfo, NCPluginTaskInfo) were deleted.
    (DbgMaple) [AP_BROWSER/Fatal] 416 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:819 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 417 : [Maple Plugin Event] Destroy Plugin : AppCommon(0x6c98770) plugin app. (Decrease Ref Count of Application (0x6caf7d8 count 17 to 16)
    (DbgMaple) [AP_BROWSER/Fatal] 418 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:894 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 419 : [Maple Plugin Event] Plugin Task & Plugin Info(NPPluginObjInfo, NCPluginTaskInfo) were deleted.
    (DbgMaple) [AP_BROWSER/Fatal] 420 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/ae/aeApplicationEngine.cpp:956 in destroyApplication() 
    (DbgMaple) [AP_BROWSER/Fatal] 421 : Call PCTask::Destroy (app : 0x6caf7d8)
    (DbgMaple) [AP_BROWSER/Fatal] 422 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/wsal/shadow/cwsApplication.cpp:48 in finalizeTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 423 : Enter CWSApplication::finalizeTask (app : 0x6caf7d8)
    (DbgMaple) [AP_BROWSER/Fatal] 424 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:819 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 425 : [Maple Plugin Event] Destroy Plugin : Sef(0x7393a78) plugin app. (Decrease Ref Count of Application (0x6caf7d8 count 16 to 15)
    [TDScaler][VidId:2][770] (VideoOnOff:1)
    ============>TDaShare::m_StreamPath:1
    	>>[ERR:TDiDemux.cpp] SetInputType():208 Null Fuction Call !!!Must Check Implementation Code...
    [TPAWindow.cpp][ConnectSource][WID:4][CALL]..
    [TDScaler][Connect]eOutVideoID = 0x2, eBackendId = 0x0, eWindowID = 0x3
    [TDScaler]eExtOutId = 0x1, eOutVideoId = 0x2
    [TDScaler]eSource = 0x201, m_ePipSourceMode = 0x0, m_ePreSrcMode:0x901
    (DbgMaple) [AP_BROWSER/Fatal] 426 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:894 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 427 : [Maple Plugin Event] Plugin Task & Plugin Info(NPPluginObjInfo, NCPluginTaskInfo) were deleted.
    (DbgMaple) [AP_BROWSER/Fatal] 428 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:819 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 429 : [Maple Plugin Event] Destroy Plugin : Sef(0x788d940) plugin app. (Decrease Ref Count of Application (0x6caf7d8 count 15 to 14)
    (DbgMaple) [AP_BROWSER/Fatal] 430 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:894 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 431 : [Maple Plugin Event] Plugin Task & Plugin Info(NPPluginObjInfo, NCPluginTaskInfo) were deleted.
    (DbgMaple) [AP_BROWSER/Fatal] 432 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:819 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 433 : [Maple Plugin Event] Destroy Plugin : NNavi(0x7a72900) plugin app. (Decrease Ref Count of Application (0x6caf7d8 count 14 to 13)
    (DbgMaple) [AP_BROWSER/Fatal] 434 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:894 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 435 : [Maple Plugin Event] Plugin Task & Plugin Info(NPPluginObjInfo, NCPluginTaskInfo) were deleted.
    (DbgMaple) [AP_BROWSER/Fatal] 436 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:819 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 437 : [Maple Plugin Event] Destroy Plugin : Network(0x704f3a8) plugin app. (Decrease Ref Count of Application (0x6caf7d8 count 13 to 12)
    (DbgMaple) [AP_BROWSER/Fatal] 438 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:894 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 439 : [Maple Plugin Event] Plugin Task & Plugin Info(NPPluginObjInfo, NCPluginTaskInfo) were deleted.
    (DbgMaple) [AP_BROWSER/Fatal] 440 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:819 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 441 : [Maple Plugin Event] Destroy Plugin : ExternalWidgetInterface(0x7987bc8) plugin app. (Decrease Ref Count of Application (0x6caf7d8 count 12 to 11)
    [Scaler]
     TDResolution_k : [21]
    TDResolutionInfo_t [720], [576], [0], [0], [864], [625], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [513], [1], [0], [17], [0], [0]
    [Check 3D Status...]
    3D Mode to Set: [0],
    [VSI] 3D Mode: [0],
    [DSP] 3D Mode: [0],
    [RES] 3D Mode: [0]
    Skip 3D Mode Last Memory Setting...[OFF] or Auto Detected 3D Mode!!!
    (DbgMaple) [AP_BROWSER/Fatal] 442 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:894 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 443 : [Maple Plugin Event] Plugin Task & Plugin Info(NPPluginObjInfo, NCPluginTaskInfo) were deleted.
    (DbgMaple) [AP_BROWSER/Fatal] 444 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:819 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 445 : [Maple Plugin Event] Destroy Plugin : AppCommon(0x7405878) plugin app. (Decrease Ref Count of Application (0x6caf7d8 count 11 to 10)
    Source : 0x201, WindowType : 4 ExtInID : 0, BackEndID : 7, tdRet=0 
    [ERROR][StopPcr():595] [WARN] PCR is already stopped!! 
    	>>[ERR:TDsSamAudioProcessor.cpp] Connect():672  - SDAL ERROR [-1] !!!
    [TPAWindow.cpp][ConnectSource][WID:4][END]..
    [Scaler]
     TDResolution_k : [15]
    TDResolutionInfo_t [720], [576], [0], [0], [864], [625], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [2305], [0], [4], [17], [0], [0]
    [BackEnd]
     TDResolution_k : [15]
    TDResolutionInfo_t [720], [576], [0], [0], [864], [625], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [2305], [0], [4], [17], [0], [0]
    (DbgMaple) [AP_BROWSER/Fatal] 446 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:894 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 447 : [Maple Plugin Event] Plugin Task & Plugin Info(NPPluginObjInfo, NCPluginTaskInfo) were deleted.
    (DbgMaple) [AP_BROWSER/Fatal] 448 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:819 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 449 : [Maple Plugin Event] Destroy Plugin : Device(0x7a03d90) plugin app. (Decrease Ref Count of Application (0x6caf7d8 count 10 to 9)
    (DbgMaple) [AP_BROWSER/Fatal] 450 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:894 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 451 : [Maple Plugin Event] Plugin Task & Plugin Info(NPPluginObjInfo, NCPluginTaskInfo) were deleted.
    (DbgMaple) [AP_BROWSER/Fatal] 452 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:819 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 453 : [Maple Plugin Event] Destroy Plugin : TV(0x79c8a20) plugin app. (Decrease Ref Count of Application (0x6caf7d8 count 9 to 8)
    (DbgMaple) [AP_BROWSER/Fatal] 454 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:894 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 455 : [Maple Plugin Event] Plugin Task & Plugin Info(NPPluginObjInfo, NCPluginTaskInfo) were deleted.
    (DbgMaple) [AP_BROWSER/Fatal] 456 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:819 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 457 : [Maple Plugin Event] Destroy Plugin : TVMW(0x7a70320) plugin app. (Decrease Ref Count of Application (0x6caf7d8 count 8 to 7)
    (DbgMaple) [AP_BROWSER/Fatal] 458 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:894 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 459 : [Maple Plugin Event] Plugin Task & Plugin Info(NPPluginObjInfo, NCPluginTaskInfo) were deleted.
    (DbgMaple) [AP_BROWSER/Fatal] 460 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:819 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 461 : [Maple Plugin Event] Destroy Plugin : ExternalWidgetInterface(0x7a0a6c0) plugin app. (Decrease Ref Count of Application (0x6caf7d8 count 7 to 6)
    (DbgMaple) [AP_BROWSER/Fatal] 462 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:894 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 463 : [Maple Plugin Event] Plugin Task & Plugin Info(NPPluginObjInfo, NCPluginTaskInfo) were deleted.
    (DbgMaple) [AP_BROWSER/Fatal] 464 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:819 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 465 : [Maple Plugin Event] Destroy Plugin : Network(0x719af98) plugin app. (Decrease Ref Count of Application (0x6caf7d8 count 6 to 5)
    (DbgMaple) [AP_BROWSER/Fatal] 466 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:894 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 467 : [Maple Plugin Event] Plugin Task & Plugin Info(NPPluginObjInfo, NCPluginTaskInfo) were deleted.
    (DbgMaple) [AP_BROWSER/Fatal] 468 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:819 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 469 : [Maple Plugin Event] Destroy Plugin : FrontPanel(0x7044460) plugin app. (Decrease Ref Count of Application (0x6caf7d8 count 5 to 4)
    (DbgMaple) [AP_BROWSER/Fatal] 470 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:894 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 471 : [Maple Plugin Event] Plugin Task & Plugin Info(NPPluginObjInfo, NCPluginTaskInfo) were deleted.
    (DbgMaple) [AP_BROWSER/Fatal] 472 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:819 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 473 : [Maple Plugin Event] Destroy Plugin : PowerInfolinkPlayer(0x7a0f9d8) plugin app. (Decrease Ref Count of Application (0x6caf7d8 count 4 to 3)
    	>>[ERR:TDiDemux.cpp] SetInputType():208 [TDaScaler][SetGeometry][ID:0]Geometry (0, 0, 1920, 1080)
    [TDaScaler][SetCapture][ID:0]Capture (30, 17, 658, 540)
    Null Fuction Call !!!Must Check Implementation Code...
    [ERROR][StartAudio():304] PLAY ENGINE FAIL 
    	>>[ERR:TDsSamMpeg.cpp] StartAudioDecoding():1986  - SDAL ERROR [-2] !!!
    [ERROR][StopPcr():595] [WARN] PCR is already stopped!! 
    [ERROR][hdiSetAudioDelay():644] EXTOUT AUDIO DELAY : Extout source type is error(18)
    	>>[ERR:TDsSamAudioProcessor.cpp] t_SetAudioSpeakerDelay():2514  - SDAL ERROR [-1] !!!
    t_GASFRC3D_SetAutoMotionPlus() : Motion Plus Demo OFF
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Turn Glass to OFF
    TDa3dProcessor::Set3DMode(TD_3D_MODE_OFF) -> Glass Callback Registered, Run Callback. (3D : OFF, Param : 109122216)
    [BT_SS/Fatal] 474 : [Set3DOffsetBroadcastOnOff][line:2460] Set3DOffsetBroadcastOnOff : [Disable]
    [BT_SS/Fatal] 475 : [SetShutterInfoForBroadCast][line:2452] shutter info exceeds 65535. m_frame_period[60001], m_DutyForShuttering[125]
    [BT_SS/Fatal] 476 : [Set3DModeOffSetForBroadCast][line:2178] m_b3DOffsetBroadcast[0], m_frame_period[60001]... I would make 3DGS as open
    [BT_SS/Fatal] 477 : [Set3DSyncDetection][line:2475] Set3DSyncDetection : [Disable]
    Set3DMode() : Start, TD3dEffectMode_k = 0, iVideoPlane = 0 iBackendDevice:0
    t_Set3DModeForGenoaAlone(): Game/MJC Mode is same 
    SetStereoscopicScreenMode, 395, Not supported Screen
    [TDScaler][VidId:0][544] (Mute OnOff:0)
    [BT_SS/Fatal] 478 : [SetShutterInfoForBroadCast][line:2452] shutter info exceeds 65535. m_frame_period[60001], m_DutyForShuttering[125]
    [BT_SS/Fatal] 479 : [Set3DModeOffSetForBroadCast][line:2178] m_b3DOffsetBroadcast[0], m_frame_period[60001]... I would make 3DGS as open
    (DbgMaple) [AP_BROWSER/Fatal] 480 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:894 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 481 : [Maple Plugin Event] Plugin Task & Plugin Info(NPPluginObjInfo, NCPluginTaskInfo) were deleted.
    (DbgMaple) [AP_BROWSER/Fatal] 482 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:819 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 483 : [Maple Plugin Event] Destroy Plugin : NNavi(0x718bdc8) plugin app. (Decrease Ref Count of Application (0x6caf7d8 count 3 to 2)
    (DbgMaple) [AP_BROWSER/Fatal] 484 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:894 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 485 : [Maple Plugin Event] Plugin Task & Plugin Info(NPPluginObjInfo, NCPluginTaskInfo) were deleted.
    (DbgMaple) [AP_BROWSER/Fatal] 486 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:819 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 487 : [Maple Plugin Event] Destroy Plugin : TVMW(0x787a3f8) plugin app. (Decrease Ref Count of Application (0x6caf7d8 count 2 to 1)
    (DbgMaple) [AP_BROWSER/Fatal] 488 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:894 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 489 : [Maple Plugin Event] Plugin Task & Plugin Info(NPPluginObjInfo, NCPluginTaskInfo) were deleted.
    (DbgMaple) [AP_BROWSER/Fatal] 490 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:819 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 491 : [Maple Plugin Event] Destroy Plugin : Audio(0x78a87d0) plugin app. (Decrease Ref Count of Application (0x6caf7d8 count 1 to 0)
    (DbgMaple) [AP_BROWSER/Fatal] 492 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/pl/event/plEvent.c:894 in pl_DeletePluginTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 493 : [Maple Plugin Event] Plugin Task & Plugin Info(NPPluginObjInfo, NCPluginTaskInfo) were deleted.
    (DbgMaple) [AP_BROWSER/Fatal] 494 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/am/amApplication.cpp:265 in onTaskDestroy() 
    (DbgMaple) [AP_BROWSER/Fatal] 495 : Enter CApplication onTaskDestroy (app : 0x6caf7d8, task : 0x7326dd0)
    (DbgMaple) [AP_BROWSER/Fatal] 496 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/am/amApplication.cpp:303 in onTaskDestroy() 
    (DbgMaple) [AP_BROWSER/Fatal] 497 : Exit CApplication onTaskDestroy (app : 0x6caf7d8, task : 0x7326dd0)
    (DbgMaple) [AP_BROWSER/Fatal] 498 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/wsal/shadow/cwsApplication.cpp:59 in finalizeTask() 
    (DbgMaple) [AP_BROWSER/Fatal] 499 : Exit CWSApplication::finalizeTask (app : 0x6caf7d8)
    (DbgMaple) [AP_BROWSER/Fatal] 500 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/ae/aeApplicationEngine.cpp:970 in destroyApplication() 
    (DbgMaple) [AP_BROWSER/Fatal] 501 : Exit destroyApplication
    Task SendEventToDevice : [4] [0] 
    (DbgAlert) [AP_WIDGET/Fatal] 502 : alert() : [Smart Hub Log] @@@@@ video mute ON @@@@@
    [TDScaler][VidId:0][544] (Mute OnOff:1)
    ####### Header = 12, 0
    (DbgAlert) [AP_WIDGET/Fatal] 503 : alert() : [Smart Hub Log] @@@@@ video mute ON @@@@@
    (DbgAlert) [AP_WIDGET/Fatal] 504 : alert() : [Smart Hub Log] SmartHomeMain.setFocus() ==> UISmartHome.call
    ####### Header = 12, 0
    [AP_INFOLINK/Fatal] 505 : Setting m_SafeAlarm->Reset(TIME_OUT_STOP, 0);
    [AP_INFOLINK/Fatal] 506 : ### MESSAGE_WEBSVC_ACTIVATE_READY_WM ###, m_bFirstStart [0]
    [AP_INFOLINK/Fatal] 507 : Update is False
    Set3DEffectFunction Called...[false] Power Off Sequence [0])
    DynamicControl:5, FullOSD:true 
    (DbgMaple) [AP_BROWSER/Fatal] 508 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/am/amApplication.cpp:1302 in show() 
    (DbgMaple) [AP_BROWSER/Fatal] 509 : CApplication::show (app : 0x6b6c008, task : 0x6b6c0b0) (SCREEN NUMBER=1)
    (DbgMaple) [AP_BROWSER/Fatal] 510 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/am/amApplication.cpp:1304 in show() 
    (DbgMaple) [AP_BROWSER/Fatal] 511 : CApplication::show current screen resolution (960x540), widget resolution (1280x720)
    (DbgMaple) [AP_BROWSER/Fatal] 512 : [FATAL] /home1/dblee/Genoa/GS_R_AP/AP_Browser/Maple2011/src/core/am/amApplication.cpp:1323 in show() 
    (DbgMaple) [AP_BROWSER/Fatal] 513 : CApplication::show change resolution (SCREEN NUMBER=1) (SCREEN RESOLUTION[1280x720])
    [ERROR][StopPcr():595] [WARN] PCR is already stopped!! 
    [ERROR][StopPcr():595] [WARN] PCR is already stopped!! 
    [ERROR][StartAudio():304] PLAY ENGINE FAIL 
    	>>[ERR:TDsSamMpeg.cpp] StartAudioDecoding():1986  - SDAL ERROR [-2] !!!
    [Scaler]
     TDResolution_k : [21]
    TDResolutionInfo_t [720], [576], [0], [0], [864], [625], [0], [50000], [1], [0], [0], [0], [0], [0], [0], [0], [513], [1], [0], [17], [0], [0]
    [TDaScaler][SetGeometry][ID:2]Geometry (0, 0, 720, 576)
    [TDaScaler][SetCapture][ID:2]Capture (0, 0, 720, 576)
    (DbgAlert) [AP_WIDGET/Fatal] 514 : alert() : [Smart Hub Log]  @@@@@@@ SetPIG @@@@@@
    [TDaScaler][SetGeometry][ID:0]Geometry (60, 112, 482, 274)
    [TDaScaler][SetCapture][ID:0]Capture (26, 15, 668, 544)
    Task SetBannerState : [2] 
    [DEFAULT/Debugging] 515 : CApp::SendEvent Event Receiver NULL-app[101]
    (DbgAlert) [AP_WIDGET/Fatal] 516 : alert() : [Smart Hub Log] @@@@@ video mute OFF @@@@@
    [TDScaler][VidId:0][544] (Mute OnOff:0)


# Links


* <http://forum.samygo.tv/viewtopic.php?f=22&t=2701#p22009>  