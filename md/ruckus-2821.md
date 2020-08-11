[[=image ruckus-2821.jpg]]

# SoC


Seems to be based on ar531x.

# About


The board seems to be very close to the Fonera, which is also based on the ar531x. There is probably a way to compile a decent redboot bootloader for it.

# Reboot sources


See [[[file:]]].

# Serial port


There is a serial port on the board:


    # screen /dev/ttyUSB0 9600


It runs Vxworks:


    ar531xPlus rev 0x00000086 firmware startup...
    CTL Reg: 0x01060014
    CTL Reg: 0x01160014
    flash page write circuit present !!!
    GD6-5 version 4.0.0.167
    auto-booting...
    Attaching to TFFS... done.
    Loading /fl/apv54...1101040
    Starting at 0x804846e0...
    flash page write circuit present !!!
                                                                    
    /fl/  - Volume is OK 
    Reading Configuration File "/fl/apcfg".
    apCfgOpModeSet(0, 0)
    apcfg:0 set OpMode to Access Point
    apCfgOpModeSet(1, 0)
    apcfg:1 set OpMode to Access Point
    Configuration file checksum: 5e36b is good
    Setting MV Port 5 to 100 Full
    Please check the ethernet cable on port 0!
    apInit call ar5hwcCreatePhy(0)
    v54_antinfo_init: 6C: using max 3 of 6 = 41 states
    v54_hwantctrl_init: 2316
    Pinot+ Adaptive Control Algorithm, Copyright (C) 2003-2005, Video54 Technologies, Inc. All Rights Reserved.
    Pinot+ Adaptive Control Algorithm, Copyright (C) 2003-2005, Video54 Technologies, Inc. All Rights Reserved.
    apInit call ar5hwcCreatePhy(1)
    Attaching interface lo0...done
    Adding 5209 symbols for standalone.
                    VxWorks
    Copyright 1984-2001  Wind River Systems, Inc.
                CPU: GD6-5
       Runtime Name: VxWorks
    Runtime Version: 5.4.20x
    81fffdf0     (BSP version: 1.0
    t        Created: RooJul 17 2006, 17:48:5tTask8): 
     netLibIni            WDB: tneReadytTaskSemId = 0x.
    8038ee10
    Video54 Ac
    cess Point Rev 3.3.0x1.1481
    81fffdf0v54 (AP software tRootTask3.3.1.1481): Cntlsizeof(ATHEROS_DESC)=
    160 1.2 Copyright  CACHE_LINE_SIZE=p4b32uild
    (C) 2005 Vide0x@81fffdf0o54 Techn (BULLETtRootTaskolo): :wireless access point starting...
    h:/atheros/ap/ap/os/vxworks/target/proj/ap-ar5315-productiongi
    es Inc.Jul 17 2006, 17:48:58
    wlan0 -> Auto Channel Scan selected 2472 MHz, channel 13
    0x81fffdf0 (tRootTask):  wlan0 Ready
    0x81fffdf0 (tRootTask):  Ready
    ar531xPlus rev 0x00000086 firmware startup...
    CTL Reg: 0x01060014
    CTL Reg: 0x01160014
    flash page write circuit present !!!
    GD6-5 version 4.0.0.167
    auto-booting...
    Attaching to TFFS... done.
    Loading /fl/apv54...1101040
    Starting at 0x804846e0...
    flash page write circuit present !!!
                                                                    
    /fl/  - Volume is OK 
    Reading Configuration File "/fl/apcfg".
    apCfgOpModeSet(0, 0)
    apcfg:0 set OpMode to Access Point
    apCfgOpModeSet(1, 0)
    apcfg:1 set OpMode to Access Point
    Configuration file checksum: 5e36b is good
    Setting MV Port 5 to 100 Full
    Please check the ethernet cable on port 0!
    apInit call ar5hwcCreatePhy(0)
    v54_antinfo_init: 6C: using max 3 of 6 = 41 states
    v54_hwantctrl_init: 2316
    Pinot+ Adaptive Control Algorithm, Copyright (C) 2003-2005, Video54 Technologies, Inc. All Rights Reserved.
    Pinot+ Adaptive Control Algorithm, Copyright (C) 2003-2005, Video54 Technologies, Inc. All Rights Reserved.
    apInit call ar5hwcCreatePhy(1)
    Attaching interface lo0...done
    Adding 5209 symbols for standalone.
                    VxWorks
    Copyright 1984-2001  Wind River Systems, Inc.
                CPU: GD6-5
       Runtime Name: VxWorks
    Runtime Version: 5.4.20x
    81fffdf0     (BSP version: 1.0
    t        Created: RooJul 17 2006, 17:48:5tTask8): 
     netLibIni            WDB: tneReadytTaskSemId = 0x.
    8038ee10
    Video54 Ac
    cess Point Rev 3.3.0x1.1481
    81fffdf0v54 (AP software tRootTask3.3.1.1481): Cntlsizeof(ATHEROS_DESC)=
    160 1.2 Copyright  CACHE_LINE_SIZE=p4b32uild
    (C) 2005 Vide0x@81fffdf0o54 Techn (BULLETtRootTaskolo): :wireless access point starting...
    h:/atheros/ap/ap/os/vxworks/target/proj/ap-ar5315-productiongie
    s Inc.Jul 17 2006, 17:48:58
    wlan0 -> Auto Channel Scan selected 2472 MHz, channel 13
    0x81fffdf0 (tRootTask):  wlan0 Ready
    0x81fffdf0 (tRootTask):  Ready
    wlan0 -> 
    wlan0 -> 
    wlan0 -> 
    wlan0 -> 
    wlan0 -> 
    wlan0 -> ls
    apcfg          4793
    apv54        995860
    apcfg.bak      4788
    bootromM.sys 263440
    6240256 bytes free
    wlan0 -> ls
    Invalid input characters!
    wlan0 -> ps
    Unknown command: ps
    Type "help" for a list of valid commands.
    wlan0 -> ifconfig
    Unknown command: ifconfig
    Type "help" for a list of valid commands.
    wlan0 -> help
    List of Access Point CLI commands:
     ?                                  -- Display CLI Command List
     arp add                            -- create or modify ARP table entry
     arp delete                         -- remove ARP table entry
     arp flush                          -- flush all entries in the ARP table
     arp show                           -- Display firmware information
     board change                       -- Change Board Data
     board dump                         -- Dump Board Data
     add remoteWbr                      -- Add a remote Wireless Bridge
     admin                              -- Temporary factory admin
     boot flash                         -- Boot from flash
     boot ethernet                      -- Boot from network
     boot dump                          -- dump boot line data
     cat                                -- list file
     cp                                 -- Copy file
     config wlan                        -- config wlanX
     connect bss                        -- connect to bssX
     del acl                            -- Delete Access Control List
     del key                            -- Delete Encryption key
     del remoteWbr                      -- Delete a remote Wireless Bridge
     del seed                           -- Delete Random Seed
     dis                                -- Dis-associate an End Station
     eeprom                             -- dump eeprom data
     find bss                           -- Find BSS
     find channel                       -- Find Available Channel
     find all                           -- Find All BSS
     format                             -- Format flash filesytem
     bootrom                            -- Update boot rom image
     ftp                                -- Software update via FTP
     get 11gonly                        -- Display 11g Only Allowed
     get 11goptimize                    -- Display 11g Optimization Level
     get 11goverlapbss                  -- Display Overlapping BSS Protection
     get abolt                          -- 
     get acl                            -- Display Access Control List
     get aging                          -- Display Aging Interval
     get antenna                        -- Display Antenna Diversity
     get arp                            -- Display arp Table
     get if                             -- Display attached network interfaces
     get routes                         -- Display routing table 
     get association                    -- Display Association Table
     get authentication                 -- Display Authentication Type
     get autoProvision                  -- Display Auto-Provision Mode
     get autochannelselect              -- Display Auto Channel Select
     get basic11b                       -- Display Basic 11b Rates
     get basic11g                       -- Display Basic 11g Rates
     get beaconinterval                 -- Display Beacon Interval
     get bridgeTable                    -- Display internal SW bridge table
     get burstSeqThreshold              -- Display Max Number of frames in a Burst
     get burstTime                      -- Display Burst Time
     get cacheperf                      -- Display the cache performance counters
     get calibration                    -- Display Noise And Offset Calibration Mode
     get cckTrigHigh                    -- Display Higher Trigger Threshold for CCK Phy Errors for ANI Control
     get cckTrigLow                     -- Display Lower Trigger Threshold for CCK Phy Errors for ANI Control
     get cckWeakSigThr                  -- Display ANI Parameter for CCK Weak Signal Detection Threshold
     get channel                        -- Display Radio Channel
     get cipher                         -- Display Encryption cipher
     get compproc                       -- Display Compression scheme
     get compwinsize                    -- Display Compression Window Size
     get config                         -- Display Current AP Configuration
     get countrycode                    -- Display Country Code
     get ctsmode                        -- Display CTS mode
     get ctsrate                        -- Display CTS rate
     get ctstype                        -- Display CTS type
     get domainsuffix                   -- Display Domain Name Server suffix
     get dtim                           -- Display Data Beacon Rate (DTIM)
     get dhcp                           -- Display DHCP Client Mode
     get enableANI                      -- Display Adaptive Noise Immunity Control On/Off
     get encryption                     -- Display Encryption Mode
     get eth                            -- Display Ethernet Statistics
     get extendedchanmode               -- Display Extended Channel Mode
     get firStepLvl                     -- Display ANI Parameter for FirStepLevel
     get fragmentthreshold              -- Display Fragment Threshold
     get frequency                      -- Display Radio Frequency (MHz)
     get gateway                        -- Display Gateway IP Address
     get gbeaconrate                    -- Display 11g Beacon Rate
     get gdraft5                        -- Display 11g Draft 5.0 compatibility
     get groupkeyupdate                 -- Display Group Key Update Interval (in Seconds)
     get hardware                       -- Display Hardware Revisions
     get hostipaddr                     -- Display Host IP Address
     get ipaddr                         -- Display IP Address
     get ipmask                         -- Display IP Subnet Mask
     get jsw                            -- Display Jumpstart Mode
     get jsP2PassPhrase                 -- Display JS-P2 passphrase
     get key                            -- Display Encryption Key
     get keyentrymethod                 -- Display Encyrption Key Entry Method
     get keysource                      -- Display Source Of Encryption Keys
     get ledStatus                      -- Display current LED status
     get login                          -- Display Login User Name
     get minimumrate                    -- Display Minimum Rate
     get nameaddr                       -- Display IP address of name server
     get nf                             -- Display Noise Floor
     get noiseImmunityLvl               -- Display ANI Parameter for Noise Immunity Level
     get ofdmTrigHigh                   -- Display Higher Trigger Threshold for OFDM Phy Errors for ANI Control
     get ofdmTrigLow                    -- Display Lower Trigger Threshold for OFDM Phy Errors for ANI Control
     get ofdmWeakSigDet                 -- Display ANI Parameter for OFDM Weak Signal Detection
     get overRidetxpower                -- Display Tx power override
     get operationMode                  -- Display Operation Mode
     get passphrase                     -- Display Passphrase
     get passphrasekey                  -- Display Passphrase Key
     get perfstats                      -- Dump system performance stats
     get pnetmon                        -- NetTask profile information
     get pktLogEnable                   -- Display Packet Logging Mode
     get power                          -- Display Transmit Power Setting
     get quietAckCtsAllow               -- Display if Ack/Cts frames are allowed during quiet period
     get quietDuration                  -- Display Duration of quiet period
     get quietOffset                    -- Display Offset of quiet period into the beacon period
     get radiusname                     -- Display RADIUS server name or IP address
     get radiusport                     -- Display RADIUS port number
     get rate                           -- Display Data Rate
     get reg                            -- Display the register contents at the given offset
     get remoteAp                       -- Display Remote Ap's Mac Address
     get reset                          -- Display # of resets
     get remoteWbr                      -- Display configured Remote Wireless bridges
     get hwtxretries                    -- Display HW Transmit Retry Limit
     get swtxretries                    -- Display SW Transmit Retry Limit
     get rtsthreshold                   -- Display RTS/CTS Threshold
     get seed                           -- Display Random Seed
     get shortpreamble                  -- Display Short Preamble Usage
     get shortslottime                  -- Display Short Slot Time Usage
     get sib                            -- Display Station Information
     get sntpserver                     -- Display SNTP/NTP Server IP Address
     get softwareretry                  -- Display Software Retry
     get spurImmunityLvl                -- Display ANI Parameter for Spur Immunity Level
     get ssid                           -- Display Service Set ID
     get ssidsuppress                   -- Display SSID Suppress Mode
     get station                        -- Display Station Status
     get SuperG                         -- Display SuperG Feature Status
     get systemname                     -- Display Access Point System Name
     get telnet                         -- Display Telnet Mode
     get timeout                        -- Display Telnet Timeout
     get times                          -- Display startup times
     get tzone                          -- Display Time Zone Setting
     get updateparam                    -- Display Vendor Default Firmware Update Params
     get uptime                         -- Display UpTime
     get vlan                           -- Display VLAN Mode
     get watchdog                       -- Display Watchdog Mode
     get wds                            -- Display WDS Mode
     get webUI                          -- Display WebUI Mode
     get wep                            -- Display Encryption Mode
     get wirelessmode                   -- Display Wireless LAN Mode
     get wmm                            -- Display WMM Mode
     get wmmParamBss                    -- Display WMM parameters used by STA in this BSS
     get wmmParam                       -- Display WMM parameters used by this AP
     get wlanstate                      -- Display wlan state
     help                               -- Display CLI Command List
     Lebradeb                           -- Disable reboot during radar detection
     ls                                 -- list directory
     logoff                             -- Logoff
     mem                                -- system memory statistics
     mv                                 -- Move file
     np                                 -- Network Performance
     ns                                 -- Network Performance Server
     ping                               -- Ping
     pktLog                             -- Packet Log
     radar!                             -- Simulate radar detection on current channel
     reboot                             -- Reboot Access Point
     rm                                 -- Remove file
     run                                -- Run command file
     task priority                      -- Set task priority
     task show                          -- Set task info
     task stack                         -- Set task stack info
     task resume                        -- resume task
     task suspend                       -- suspend task
     tftp                               -- Software update via TFTP
     quit                               -- Logoff
     set 11gonly                        -- Set 11g Only Allowed
     set 11goptimize                    -- Set 11g Optimization Level
     set 11goverlapbss                  -- Set Overlapping BSS Protection
     set abolt                          -- 
     set acl                            -- Set Access Control List
     set aging                          -- Set Aging Interval
     set antenna                        -- Set Antenna
     set authentication                 -- Set Authentication Type
     set autoProvision                  -- Set Auto-Provision Mode
     set autochannelselect              -- Set Auto Channel Selection
     set basic11b                       -- Set Use of Basic 11b Rates
     set basic11g                       -- Set Use of Basic 11g Rates
     set beaconinterval                 -- Modify Beacon Interval
     set burstSeqThreshold              -- Set Max Number of frames in a Burst
     set burstTime                      -- Set Burst Time
     set cachePerf                      -- Begin cache performance monitoring
     set calibration                    -- Set Calibration Period
     set cckTrigHigh                    -- Set Higher Trigger Threshold for CCK Phy Errors For ANI Control
     set cckTrigLow                     -- Set Lower Trigger Threshold for CCK Phy Errors For ANI Control
     set cckWeakSigThr                  -- Set ANI Parameter for CCK Weak Signal Detection Threshold
     set channel                        -- Set Radio Channel
     set cipher                         -- Set Cipher
     set compproc                       -- Set Compression Scheme
     set compwinsize                    -- Set Compression Window Size
     set countrycode                    -- Set Country Code
     set ctsmode                        -- Set CTS Mode
     set ctsrate                        -- Set CTS Rate
     set ctstype                        -- Set CTS Type
     set domainsuffix                   -- Set Domain Name Server Suffix
     set dtim                           -- Set Data Beacon Rate (DTIM)
     set dhcp                           -- Set DHCP Mode
     set enableANI                      -- Turn Adaptive Noise Immunity Control On/Off
     set encryption                     -- Set Encryption Mode
     set extendedchanmode               -- Set Extended Channel Mode
     set factorydefault                 -- Restore to Default Factory Settings
     set firStepLvl                     -- Set ANI Parameter for FirStepLevel
     set fragmentthreshold              -- Set Fragment Threshold
     set frequency                      -- Set Radio Frequency (MHz)
     set gateway                        -- Set Gateway IP Address
     set gbeaconrate                    -- Set 11g Beacon Rate
     set groupkeyupdate                 -- Set Group Key Update Interval (in Seconds)
     set gdraft5                        -- Set 11g Draft 5.0 compatibility
     set hostipaddr                     -- Set Host IP address
     set ipaddr                         -- Set IP Address
     set ipmask                         -- Set IP Subnet Mask
     set jsw                            -- Set Jumpstart Mode
     set jsp2Passwd                     -- Set JS-P2 password
     set key                            -- Set Encryption Key
     set keyentrymethod                 -- Select Encryption Key Entry Method
     set keysource                      -- Select Source Of Encryption Keys
     set login                          -- Modify Login User Name
     set minimumrate                    -- Set Minimum Rate
     set minimumrate                    -- Set Minimum Rate
     set minimumrate                    -- Set Minimum Rate
     set minimumrate                    -- Set Minimum Rate
     set minimumrate                    -- Set Minimum Rate
     set nameaddress                    -- Set Name Server IP address
     set noiseImmunityLvl               -- Set ANI Parameter for Noise Immunity Level
     set ofdmTrigHigh                   -- Set Higher Trigger Threshold for OFDM Phy Errors for ANI Control
     set ofdmTrigLow                    -- Set Lower Trigger Threshold for OFDM Phy Errors for ANI Control
     set ofdmWeakSigDet                 -- Set ANI Parameter for OFDM Weak Signal Detection
     set overRidetxpower                -- Set Tx power override
     set operationMode                  -- Set operation Mode
     set password                       -- Modify Password
     set passphrase                     -- Modify Passphrase
     set pktLogEnable                   -- Enable Packet Logging
     set power                          -- Set Transmit Power
     set quietAckCtsAllow               -- Allow Ack/Cts frames during quiet period
     set quietDuration                  -- Duration of quiet period
     set quietOffset                    -- Offset of quiet period into the beacon period
     set radiusname                     -- Set RADIUS name or IP address
     set radiusport                     -- Set RADIUS port number
     set radiussecret                   -- Set RADIUS shared secret
     set rate                           -- Set Data Rate
     set rate                           -- Set Data Rate
     set rate                           -- Set Data Rate
     set rate                           -- Set Data Rate
     set rate                           -- Set Data Rate
     set reg                            -- Set Register Value
     set regulatorydomain               -- Set Regulatory Domain
     set remoteAP                       -- Set Remote AP's Mac Address
     set hwtxretries                    -- Set HW Transmit Retry Limit
     set swtxretries                    -- Set SW Transmit Retry Limit
     set rtsthreshold                   -- Set RTS/CTS Threshold
     set shortpreamble                  -- Set Short Preamble
     set shortslottime                  -- Set Short Slot Time
     set sntpserver                     -- Set SNTP/NTP Server IP Address
     set softwareretry                  -- Set Software Retry
     set spurImmunityLvl                -- Set ANI Parameter for Spur Immunity Level
     set ssid                           -- Set Service Set ID
     set ssidsuppress                   -- Set SSID Suppress Mode
     set SuperG                         -- Super G Features 
     set systemname                     -- Set Access Point System Name
     set telnet                         -- Set Telnet Mode
     set timeout                        -- Set Telnet Timeout
     set tzone                          -- Set Time Zone Setting
     set updateparam                    -- Set Vendor Default Firmware Update Params
     set vlan                           -- Set VLAN Mode
     set watchdog                       -- Set Watchdog Mode
     set wds                            -- Set WDS Mode
     set webUI                          -- Set Web UI Mode
     set wep                            -- Set Encryption Mode
     set wlanstate                      -- Set wlan state
     set wirelessmode                   -- Set Wireless LAN Mode
     set wmm                            -- Set WMM Mode
     set wmmParamBss                    -- Set WMM parameters used by STAs in this BSS
     set wmmParam                       -- Set WMM parameters used by this AP
     spy report                         -- Print spy report
     spy show                           -- Print debug info
     spy start                          -- Start spy
     spy stop                           -- Stop spy
     start wlan                         -- Start the current wlan
     stop wlan                          -- Stop the current wlan
     support                            -- Print support information
     timeofday                          -- Display Current Time of Day
     v54 alg                            -- Set/show the antenna algorithm
     v54 ant                            -- Video54 Antenna Config
     v54 antreset                       -- Reset V54 TxCtrl State
     v54 rtt                            -- Real-time Telemetry output
     v54 fchan                          -- Fast Channel Change
     v54 emon                           -- Environmental Monitoring
     v54 learn                          -- Send V54 learning packets
     v54 queue                          -- Video54 Queuing Debug Info
     v54 reset                          -- Reset V54 TxCtrl State
     v54 staQueue                       -- Per-Station-Queue scheduling
     v54 staticant                      -- Configure a static antenna
     v54 staticant                      -- Configure a static antenna
     version                            -- Software version
     video classifier                   -- Classify
     video qos                          -- Quality Of Service
     video pcap                         -- Packet capture
    wlan0 -> version
    AP software 3.3.1.1481
    p4build@BULLET:h:/atheros/ap/ap/os/vxworks/target/proj/ap-ar5315-production
    Jul 17 2006, 17:48:58
    wlan0 -> reboot
    Rebooting AP...
    flash page write circuit present !!!
    ar531xPlus rev 0x00000086 firmware startup...
    CTL Reg: 0x01060014
    CTL Reg: 0x01160014
    flash page write circuit present !!!
     Ple
    GD6-5 version 4.0.0.167
         1
    auto-booting...
    Attaching to TFFS... done.
    Loading /fl/apv54...1101040
    Starting at 0x804846e0...
    flash page write circuit present !!!
                                                                    
    /fl/  - Volume is OK 
    Reading Configuration File "/fl/apcfg".
    apCfgOpModeSet(0, 0)
    apcfg:0 set OpMode to Access Point
    apCfgOpModeSet(1, 0)
    apcfg:1 set OpMode to Access Point
    Configuration file checksum: 5e36b is good
    Setting MV Port 5 to 100 Full
    ^C^C^CPlease check the ethernet cable on port 0!
    apInit call ar5hwcCreatePhy(0)
    v54_antinfo_init: 6C: using max 3 of 6 = 41 states
    v54_hwantctrl_init: 2316
    Pinot+ Adaptive Control Algorithm, Copyright (C) 2003-2005, Video54 Technologies, Inc. All Rights Reserved.
    Pinot+ Adaptive Control Algorithm, Copyright (C) 2003-2005, Video54 Technologies, Inc. All Rights Reserved.
    apInit call ar5hwcCreatePhy(1)
    Attaching interface lo0...done
    Adding 5209 symbols for standalone.
                    VxWorks
    Copyright 1984-2001  Wind River Systems, Inc.
                CPU: GD6-5
       Runtime Name: VxWorks
    Runtime Version: 5.4.20x
    81fffdf0     (BSP version: 1.0
    t        Created: RooJul 17 2006, 17:48:5tTask8): 
     netLibIni            WDB: tneReadytTaskSemId = 0x.
    8038ee10
    Video54 Ac
    cess Point Rev 3.3.0x1.1481
    81fffdf0v54 (AP software tRootTask3.3.1.1481): Cntlsizeof(ATHEROS_DESC)=
    160 1.2 Copyright  CACHE_LINE_SIZE=p4b32uild
    (C) 2005 Vide0x@81fffdf0o54 Techn (BULLETtRootTaskolo): :wireless access point starting...
    h:/atheros/ap/ap/os/vxworks/target/proj/ap-ar5315-productiongi
    es Inc.Jul 17 2006, 17:48:58
    wlan0 -> Auto Channel Scan selected 2472 MHz, channel 13
    0x81fffdf0 (tRootTask):  wlan0 Ready
    0x81fffdf0 (tRootTask):  Ready
    Invalid input characters!
    wlan0 -> 
    wlan0 -> 
    wlan0 -> 
    wlan0 -> help
    List of Access Point CLI commands:
     ?                                  -- Display CLI Command List
     arp add                            -- create or modify ARP table entry
     arp delete                         -- remove ARP table entry
     arp flush                          -- flush all entries in the ARP table
     arp show                           -- Display firmware information
     board change                       -- Change Board Data
     board dump                         -- Dump Board Data
     add remoteWbr                      -- Add a remote Wireless Bridge
     admin                              -- Temporary factory admin
     boot flash                         -- Boot from flash
     boot ethernet                      -- Boot from network
     boot dump                          -- dump boot line data
     cat                                -- list file
     cp                                 -- Copy file
     config wlan                        -- config wlanX
     connect bss                        -- connect to bssX
     del acl                            -- Delete Access Control List
     del key                            -- Delete Encryption key
     del remoteWbr                      -- Delete a remote Wireless Bridge
     del seed                           -- Delete Random Seed
     dis                                -- Dis-associate an End Station
     eeprom                             -- dump eeprom data
     find bss                           -- Find BSS
     find channel                       -- Find Available Channel
     find all                           -- Find All BSS
     format                             -- Format flash filesytem
     bootrom                            -- Update boot rom image
     ftp                                -- Software update via FTP
     get 11gonly                        -- Display 11g Only Allowed
     get 11goptimize                    -- Display 11g Optimization Level
     get 11goverlapbss                  -- Display Overlapping BSS Protection
     get abolt                          -- 
     get acl                            -- Display Access Control List
     get aging                          -- Display Aging Interval
     get antenna                        -- Display Antenna Diversity
     get arp                            -- Display arp Table
     get if                             -- Display attached network interfaces
     get routes                         -- Display routing table 
     get association                    -- Display Association Table
     get authentication                 -- Display Authentication Type
     get autoProvision                  -- Display Auto-Provision Mode
     get autochannelselect              -- Display Auto Channel Select
     get basic11b                       -- Display Basic 11b Rates
     get basic11g                       -- Display Basic 11g Rates
     get beaconinterval                 -- Display Beacon Interval
     get bridgeTable                    -- Display internal SW bridge table
     get burstSeqThreshold              -- Display Max Number of frames in a Burst
     get burstTime                      -- Display Burst Time
     get cacheperf                      -- Display the cache performance counters
     get calibration                    -- Display Noise And Offset Calibration Mode
     get cckTrigHigh                    -- Display Higher Trigger Threshold for CCK Phy Errors for ANI Control
     get cckTrigLow                     -- Display Lower Trigger Threshold for CCK Phy Errors for ANI Control
     get cckWeakSigThr                  -- Display ANI Parameter for CCK Weak Signal Detection Threshold
     get channel                        -- Display Radio Channel
     get cipher                         -- Display Encryption cipher
     get compproc                       -- Display Compression scheme
     get compwinsize                    -- Display Compression Window Size
     get config                         -- Display Current AP Configuration
     get countrycode                    -- Display Country Code
     get ctsmode                        -- Display CTS mode
     get ctsrate                        -- Display CTS rate
     get ctstype                        -- Display CTS type
     get domainsuffix                   -- Display Domain Name Server suffix
     get dtim                           -- Display Data Beacon Rate (DTIM)
     get dhcp                           -- Display DHCP Client Mode
     get enableANI                      -- Display Adaptive Noise Immunity Control On/Off
     get encryption                     -- Display Encryption Mode
     get eth                            -- Display Ethernet Statistics
     get extendedchanmode               -- Display Extended Channel Mode
     get firStepLvl                     -- Display ANI Parameter for FirStepLevel
     get fragmentthreshold              -- Display Fragment Threshold
     get frequency                      -- Display Radio Frequency (MHz)
     get gateway                        -- Display Gateway IP Address
     get gbeaconrate                    -- Display 11g Beacon Rate
     get gdraft5                        -- Display 11g Draft 5.0 compatibility
     get groupkeyupdate                 -- Display Group Key Update Interval (in Seconds)
     get hardware                       -- Display Hardware Revisions
     get hostipaddr                     -- Display Host IP Address
     get ipaddr                         -- Display IP Address
     get ipmask                         -- Display IP Subnet Mask
     get jsw                            -- Display Jumpstart Mode
     get jsP2PassPhrase                 -- Display JS-P2 passphrase
     get key                            -- Display Encryption Key
     get keyentrymethod                 -- Display Encyrption Key Entry Method
     get keysource                      -- Display Source Of Encryption Keys
     get ledStatus                      -- Display current LED status
     get login                          -- Display Login User Name
     get minimumrate                    -- Display Minimum Rate
     get nameaddr                       -- Display IP address of name server
     get nf                             -- Display Noise Floor
     get noiseImmunityLvl               -- Display ANI Parameter for Noise Immunity Level
     get ofdmTrigHigh                   -- Display Higher Trigger Threshold for OFDM Phy Errors for ANI Control
     get ofdmTrigLow                    -- Display Lower Trigger Threshold for OFDM Phy Errors for ANI Control
     get ofdmWeakSigDet                 -- Display ANI Parameter for OFDM Weak Signal Detection
     get overRidetxpower                -- Display Tx power override
     get operationMode                  -- Display Operation Mode
     get passphrase                     -- Display Passphrase
     get passphrasekey                  -- Display Passphrase Key
     get perfstats                      -- Dump system performance stats
     get pnetmon                        -- NetTask profile information
     get pktLogEnable                   -- Display Packet Logging Mode
     get power                          -- Display Transmit Power Setting
     get quietAckCtsAllow               -- Display if Ack/Cts frames are allowed during quiet period
     get quietDuration                  -- Display Duration of quiet period
     get quietOffset                    -- Display Offset of quiet period into the beacon period
     get radiusname                     -- Display RADIUS server name or IP address
     get radiusport                     -- Display RADIUS port number
     get rate                           -- Display Data Rate
     get reg                            -- Display the register contents at the given offset
     get remoteAp                       -- Display Remote Ap's Mac Address
     get reset                          -- Display # of resets
     get remoteWbr                      -- Display configured Remote Wireless bridges
     get hwtxretries                    -- Display HW Transmit Retry Limit
     get swtxretries                    -- Display SW Transmit Retry Limit
     get rtsthreshold                   -- Display RTS/CTS Threshold
     get seed                           -- Display Random Seed
     get shortpreamble                  -- Display Short Preamble Usage
     get shortslottime                  -- Display Short Slot Time Usage
     get sib                            -- Display Station Information
     get sntpserver                     -- Display SNTP/NTP Server IP Address
     get softwareretry                  -- Display Software Retry
     get spurImmunityLvl                -- Display ANI Parameter for Spur Immunity Level
     get ssid                           -- Display Service Set ID
     get ssidsuppress                   -- Display SSID Suppress Mode
     get station                        -- Display Station Status
     get SuperG                         -- Display SuperG Feature Status
     get systemname                     -- Display Access Point System Name
     get telnet                         -- Display Telnet Mode
     get timeout                        -- Display Telnet Timeout
     get times                          -- Display startup times
     get tzone                          -- Display Time Zone Setting
     get updateparam                    -- Display Vendor Default Firmware Update Params
     get uptime                         -- Display UpTime
     get vlan                           -- Display VLAN Mode
     get watchdog                       -- Display Watchdog Mode
     get wds                            -- Display WDS Mode
     get webUI                          -- Display WebUI Mode
     get wep                            -- Display Encryption Mode
     get wirelessmode                   -- Display Wireless LAN Mode
     get wmm                            -- Display WMM Mode
     get wmmParamBss                    -- Display WMM parameters used by STA in this BSS
     get wmmParam                       -- Display WMM parameters used by this AP
     get wlanstate                      -- Display wlan state
     help                               -- Display CLI Command List
     Lebradeb                           -- Disable reboot during radar detection
     ls                                 -- list directory
     logoff                             -- Logoff
     mem                                -- system memory statistics
     mv                                 -- Move file
     np                                 -- Network Performance
     ns                                 -- Network Performance Server
     ping                               -- Ping
     pktLog                             -- Packet Log
     radar!                             -- Simulate radar detection on current channel
     reboot                             -- Reboot Access Point
     rm                                 -- Remove file
     run                                -- Run command file
     task priority                      -- Set task priority
     task show                          -- Set task info
     task stack                         -- Set task stack info
     task resume                        -- resume task
     task suspend                       -- suspend task
     tftp                               -- Software update via TFTP
     quit                               -- Logoff
     set 11gonly                        -- Set 11g Only Allowed
     set 11goptimize                    -- Set 11g Optimization Level
     set 11goverlapbss                  -- Set Overlapping BSS Protection
     set abolt                          -- 
     set acl                            -- Set Access Control List
     set aging                          -- Set Aging Interval
     set antenna                        -- Set Antenna
     set authentication                 -- Set Authentication Type
     set autoProvision                  -- Set Auto-Provision Mode
     set autochannelselect              -- Set Auto Channel Selection
     set basic11b                       -- Set Use of Basic 11b Rates
     set basic11g                       -- Set Use of Basic 11g Rates
     set beaconinterval                 -- Modify Beacon Interval
     set burstSeqThreshold              -- Set Max Number of frames in a Burst
     set burstTime                      -- Set Burst Time
     set cachePerf                      -- Begin cache performance monitoring
     set calibration                    -- Set Calibration Period
     set cckTrigHigh                    -- Set Higher Trigger Threshold for CCK Phy Errors For ANI Control
     set cckTrigLow                     -- Set Lower Trigger Threshold for CCK Phy Errors For ANI Control
     set cckWeakSigThr                  -- Set ANI Parameter for CCK Weak Signal Detection Threshold
     set channel                        -- Set Radio Channel
     set cipher                         -- Set Cipher
     set compproc                       -- Set Compression Scheme
     set compwinsize                    -- Set Compression Window Size
     set countrycode                    -- Set Country Code
     set ctsmode                        -- Set CTS Mode
     set ctsrate                        -- Set CTS Rate
     set ctstype                        -- Set CTS Type
     set domainsuffix                   -- Set Domain Name Server Suffix
     set dtim                           -- Set Data Beacon Rate (DTIM)
     set dhcp                           -- Set DHCP Mode
     set enableANI                      -- Turn Adaptive Noise Immunity Control On/Off
     set encryption                     -- Set Encryption Mode
     set extendedchanmode               -- Set Extended Channel Mode
     set factorydefault                 -- Restore to Default Factory Settings
     set firStepLvl                     -- Set ANI Parameter for FirStepLevel
     set fragmentthreshold              -- Set Fragment Threshold
     set frequency                      -- Set Radio Frequency (MHz)
     set gateway                        -- Set Gateway IP Address
     set gbeaconrate                    -- Set 11g Beacon Rate
     set groupkeyupdate                 -- Set Group Key Update Interval (in Seconds)
     set gdraft5                        -- Set 11g Draft 5.0 compatibility
     set hostipaddr                     -- Set Host IP address
     set ipaddr                         -- Set IP Address
     set ipmask                         -- Set IP Subnet Mask
     set jsw                            -- Set Jumpstart Mode
     set jsp2Passwd                     -- Set JS-P2 password
     set key                            -- Set Encryption Key
     set keyentrymethod                 -- Select Encryption Key Entry Method
     set keysource                      -- Select Source Of Encryption Keys
     set login                          -- Modify Login User Name
     set minimumrate                    -- Set Minimum Rate
     set minimumrate                    -- Set Minimum Rate
     set minimumrate                    -- Set Minimum Rate
     set minimumrate                    -- Set Minimum Rate
     set minimumrate                    -- Set Minimum Rate
     set nameaddress                    -- Set Name Server IP address
     set noiseImmunityLvl               -- Set ANI Parameter for Noise Immunity Level
     set ofdmTrigHigh                   -- Set Higher Trigger Threshold for OFDM Phy Errors for ANI Control
     set ofdmTrigLow                    -- Set Lower Trigger Threshold for OFDM Phy Errors for ANI Control
     set ofdmWeakSigDet                 -- Set ANI Parameter for OFDM Weak Signal Detection
     set overRidetxpower                -- Set Tx power override
     set operationMode                  -- Set operation Mode
     set password                       -- Modify Password
     set passphrase                     -- Modify Passphrase
     set pktLogEnable                   -- Enable Packet Logging
     set power                          -- Set Transmit Power
     set quietAckCtsAllow               -- Allow Ack/Cts frames during quiet period
     set quietDuration                  -- Duration of quiet period
     set quietOffset                    -- Offset of quiet period into the beacon period
     set radiusname                     -- Set RADIUS name or IP address
     set radiusport                     -- Set RADIUS port number
     set radiussecret                   -- Set RADIUS shared secret
     set rate                           -- Set Data Rate
     set rate                           -- Set Data Rate
     set rate                           -- Set Data Rate
     set rate                           -- Set Data Rate
     set rate                           -- Set Data Rate
     set reg                            -- Set Register Value
     set regulatorydomain               -- Set Regulatory Domain
     set remoteAP                       -- Set Remote AP's Mac Address
     set hwtxretries                    -- Set HW Transmit Retry Limit
     set swtxretries                    -- Set SW Transmit Retry Limit
     set rtsthreshold                   -- Set RTS/CTS Threshold
     set shortpreamble                  -- Set Short Preamble
     set shortslottime                  -- Set Short Slot Time
     set sntpserver                     -- Set SNTP/NTP Server IP Address
     set softwareretry                  -- Set Software Retry
     set spurImmunityLvl                -- Set ANI Parameter for Spur Immunity Level
     set ssid                           -- Set Service Set ID
     set ssidsuppress                   -- Set SSID Suppress Mode
     set SuperG                         -- Super G Features 
     set systemname                     -- Set Access Point System Name
     set telnet                         -- Set Telnet Mode
     set timeout                        -- Set Telnet Timeout
     set tzone                          -- Set Time Zone Setting
     set updateparam                    -- Set Vendor Default Firmware Update Params
     set vlan                           -- Set VLAN Mode
     set watchdog                       -- Set Watchdog Mode
     set wds                            -- Set WDS Mode
     set webUI                          -- Set Web UI Mode
     set wep                            -- Set Encryption Mode
     set wlanstate                      -- Set wlan state
     set wirelessmode                   -- Set Wireless LAN Mode
     set wmm                            -- Set WMM Mode
     set wmmParamBss                    -- Set WMM parameters used by STAs in this BSS
     set wmmParam                       -- Set WMM parameters used by this AP
     spy report                         -- Print spy report
     spy show                           -- Print debug info
     spy start                          -- Start spy
     spy stop                           -- Stop spy
     start wlan                         -- Start the current wlan
     stop wlan                          -- Stop the current wlan
     support                            -- Print support information
     timeofday                          -- Display Current Time of Day
     v54 alg                            -- Set/show the antenna algorithm
     v54 ant                            -- Video54 Antenna Config
     v54 antreset                       -- Reset V54 TxCtrl State
     v54 rtt                            -- Real-time Telemetry output
     v54 fchan                          -- Fast Channel Change
     v54 emon                           -- Environmental Monitoring
     v54 learn                          -- Send V54 learning packets
     v54 queue                          -- Video54 Queuing Debug Info
     v54 reset                          -- Reset V54 TxCtrl State
     v54 staQueue                       -- Per-Station-Queue scheduling
     v54 staticant                      -- Configure a static antenna
     v54 staticant                      -- Configure a static antenna
     version                            -- Software version
     video classifier                   -- Classify
     video qos                          -- Quality Of Service
     video pcap                         -- Packet capture
    wlan0 -> bootrom
    Not enough parameters!
    wlan0 -> ^[[A
    Invalid input characters!
    wlan0 -> 
    wlan0 -> help
    List of Access Point CLI commands:
     ?                                  -- Display CLI Command List
     arp add                            -- create or modify ARP table entry
     arp delete                         -- remove ARP table entry
     arp flush                          -- flush all entries in the ARP table
     arp show                           -- Display firmware information
     board change                       -- Change Board Data
     board dump                         -- Dump Board Data
     add remoteWbr                      -- Add a remote Wireless Bridge
     admin                              -- Temporary factory admin
     boot flash                         -- Boot from flash
     boot ethernet                      -- Boot from network
     boot dump                          -- dump boot line data
     cat                                -- list file
     cp                                 -- Copy file
     config wlan                        -- config wlanX
     connect bss                        -- connect to bssX
     del acl                            -- Delete Access Control List
     del key                            -- Delete Encryption key
     del remoteWbr                      -- Delete a remote Wireless Bridge
     del seed                           -- Delete Random Seed
     dis                                -- Dis-associate an End Station
     eeprom                             -- dump eeprom data
     find bss                           -- Find BSS
     find channel                       -- Find Available Channel
     find all                           -- Find All BSS
     format                             -- Format flash filesytem
     bootrom                            -- Update boot rom image
     ftp                                -- Software update via FTP
     get 11gonly                        -- Display 11g Only Allowed
     get 11goptimize                    -- Display 11g Optimization Level
     get 11goverlapbss                  -- Display Overlapping BSS Protection
     get abolt                          -- 
     get acl                            -- Display Access Control List
     get aging                          -- Display Aging Interval
     get antenna                        -- Display Antenna Diversity
     get arp                            -- Display arp Table
     get if                             -- Display attached network interfaces
     get routes                         -- Display routing table 
     get association                    -- Display Association Table
     get authentication                 -- Display Authentication Type
     get autoProvision                  -- Display Auto-Provision Mode
     get autochannelselect              -- Display Auto Channel Select
     get basic11b                       -- Display Basic 11b Rates
     get basic11g                       -- Display Basic 11g Rates
     get beaconinterval                 -- Display Beacon Interval
     get bridgeTable                    -- Display internal SW bridge table
     get burstSeqThreshold              -- Display Max Number of frames in a Burst
     get burstTime                      -- Display Burst Time
     get cacheperf                      -- Display the cache performance counters
     get calibration                    -- Display Noise And Offset Calibration Mode
     get cckTrigHigh                    -- Display Higher Trigger Threshold for CCK Phy Errors for ANI Control
     get cckTrigLow                     -- Display Lower Trigger Threshold for CCK Phy Errors for ANI Control
     get cckWeakSigThr                  -- Display ANI Parameter for CCK Weak Signal Detection Threshold
     get channel                        -- Display Radio Channel
     get cipher                         -- Display Encryption cipher
     get compproc                       -- Display Compression scheme
     get compwinsize                    -- Display Compression Window Size
     get config                         -- Display Current AP Configuration
     get countrycode                    -- Display Country Code
     get ctsmode                        -- Display CTS mode
     get ctsrate                        -- Display CTS rate
     get ctstype                        -- Display CTS type
     get domainsuffix                   -- Display Domain Name Server suffix
     get dtim                           -- Display Data Beacon Rate (DTIM)
     get dhcp                           -- Display DHCP Client Mode
     get enableANI                      -- Display Adaptive Noise Immunity Control On/Off
     get encryption                     -- Display Encryption Mode
     get eth                            -- Display Ethernet Statistics
     get extendedchanmode               -- Display Extended Channel Mode
     get firStepLvl                     -- Display ANI Parameter for FirStepLevel
     get fragmentthreshold              -- Display Fragment Threshold
     get frequency                      -- Display Radio Frequency (MHz)
     get gateway                        -- Display Gateway IP Address
     get gbeaconrate                    -- Display 11g Beacon Rate
     get gdraft5                        -- Display 11g Draft 5.0 compatibility
     get groupkeyupdate                 -- Display Group Key Update Interval (in Seconds)
     get hardware                       -- Display Hardware Revisions
     get hostipaddr                     -- Display Host IP Address
     get ipaddr                         -- Display IP Address
     get ipmask                         -- Display IP Subnet Mask
     get jsw                            -- Display Jumpstart Mode
     get jsP2PassPhrase                 -- Display JS-P2 passphrase
     get key                            -- Display Encryption Key
     get keyentrymethod                 -- Display Encyrption Key Entry Method
     get keysource                      -- Display Source Of Encryption Keys
     get ledStatus                      -- Display current LED status
     get login                          -- Display Login User Name
     get minimumrate                    -- Display Minimum Rate
     get nameaddr                       -- Display IP address of name server
     get nf                             -- Display Noise Floor
     get noiseImmunityLvl               -- Display ANI Parameter for Noise Immunity Level
     get ofdmTrigHigh                   -- Display Higher Trigger Threshold for OFDM Phy Errors for ANI Control
     get ofdmTrigLow                    -- Display Lower Trigger Threshold for OFDM Phy Errors for ANI Control
     get ofdmWeakSigDet                 -- Display ANI Parameter for OFDM Weak Signal Detection
     get overRidetxpower                -- Display Tx power override
     get operationMode                  -- Display Operation Mode
     get passphrase                     -- Display Passphrase
     get passphrasekey                  -- Display Passphrase Key
     get perfstats                      -- Dump system performance stats
     get pnetmon                        -- NetTask profile information
     get pktLogEnable                   -- Display Packet Logging Mode
     get power                          -- Display Transmit Power Setting
     get quietAckCtsAllow               -- Display if Ack/Cts frames are allowed during quiet period
     get quietDuration                  -- Display Duration of quiet period
     get quietOffset                    -- Display Offset of quiet period into the beacon period
     get radiusname                     -- Display RADIUS server name or IP address
     get radiusport                     -- Display RADIUS port number
     get rate                           -- Display Data Rate
     get reg                            -- Display the register contents at the given offset
     get remoteAp                       -- Display Remote Ap's Mac Address
     get reset                          -- Display # of resets
     get remoteWbr                      -- Display configured Remote Wireless bridges
     get hwtxretries                    -- Display HW Transmit Retry Limit
     get swtxretries                    -- Display SW Transmit Retry Limit
     get rtsthreshold                   -- Display RTS/CTS Threshold
     get seed                           -- Display Random Seed
     get shortpreamble                  -- Display Short Preamble Usage
     get shortslottime                  -- Display Short Slot Time Usage
     get sib                            -- Display Station Information
     get sntpserver                     -- Display SNTP/NTP Server IP Address
     get softwareretry                  -- Display Software Retry
     get spurImmunityLvl                -- Display ANI Parameter for Spur Immunity Level
     get ssid                           -- Display Service Set ID
     get ssidsuppress                   -- Display SSID Suppress Mode
     get station                        -- Display Station Status
     get SuperG                         -- Display SuperG Feature Status
     get systemname                     -- Display Access Point System Name
     get telnet                         -- Display Telnet Mode
     get timeout                        -- Display Telnet Timeout
     get times                          -- Display startup times
     get tzone                          -- Display Time Zone Setting
     get updateparam                    -- Display Vendor Default Firmware Update Params
     get uptime                         -- Display UpTime
     get vlan                           -- Display VLAN Mode
     get watchdog                       -- Display Watchdog Mode
     get wds                            -- Display WDS Mode
     get webUI                          -- Display WebUI Mode
     get wep                            -- Display Encryption Mode
     get wirelessmode                   -- Display Wireless LAN Mode
     get wmm                            -- Display WMM Mode
     get wmmParamBss                    -- Display WMM parameters used by STA in this BSS
     get wmmParam                       -- Display WMM parameters used by this AP
     get wlanstate                      -- Display wlan state
     help                               -- Display CLI Command List
     Lebradeb                           -- Disable reboot during radar detection
     ls                                 -- list directory
     logoff                             -- Logoff
     mem                                -- system memory statistics
     mv                                 -- Move file
     np                                 -- Network Performance
     ns                                 -- Network Performance Server
     ping                               -- Ping
     pktLog                             -- Packet Log
     radar!                             -- Simulate radar detection on current channel
     reboot                             -- Reboot Access Point
     rm                                 -- Remove file
     run                                -- Run command file
     task priority                      -- Set task priority
     task show                          -- Set task info
     task stack                         -- Set task stack info
     task resume                        -- resume task
     task suspend                       -- suspend task
     tftp                               -- Software update via TFTP
     quit                               -- Logoff
     set 11gonly                        -- Set 11g Only Allowed
     set 11goptimize                    -- Set 11g Optimization Level
     set 11goverlapbss                  -- Set Overlapping BSS Protection
     set abolt                          -- 
     set acl                            -- Set Access Control List
     set aging                          -- Set Aging Interval
     set antenna                        -- Set Antenna
     set authentication                 -- Set Authentication Type
     set autoProvision                  -- Set Auto-Provision Mode
     set autochannelselect              -- Set Auto Channel Selection
     set basic11b                       -- Set Use of Basic 11b Rates
     set basic11g                       -- Set Use of Basic 11g Rates
     set beaconinterval                 -- Modify Beacon Interval
     set burstSeqThreshold              -- Set Max Number of frames in a Burst
     set burstTime                      -- Set Burst Time
     set cachePerf                      -- Begin cache performance monitoring
     set calibration                    -- Set Calibration Period
     set cckTrigHigh                    -- Set Higher Trigger Threshold for CCK Phy Errors For ANI Control
     set cckTrigLow                     -- Set Lower Trigger Threshold for CCK Phy Errors For ANI Control
     set cckWeakSigThr                  -- Set ANI Parameter for CCK Weak Signal Detection Threshold
     set channel                        -- Set Radio Channel
     set cipher                         -- Set Cipher
     set compproc                       -- Set Compression Scheme
     set compwinsize                    -- Set Compression Window Size
     set countrycode                    -- Set Country Code
     set ctsmode                        -- Set CTS Mode
     set ctsrate                        -- Set CTS Rate
     set ctstype                        -- Set CTS Type
     set domainsuffix                   -- Set Domain Name Server Suffix
     set dtim                           -- Set Data Beacon Rate (DTIM)
     set dhcp                           -- Set DHCP Mode
     set enableANI                      -- Turn Adaptive Noise Immunity Control On/Off
     set encryption                     -- Set Encryption Mode
     set extendedchanmode               -- Set Extended Channel Mode
     set factorydefault                 -- Restore to Default Factory Settings
     set firStepLvl                     -- Set ANI Parameter for FirStepLevel
     set fragmentthreshold              -- Set Fragment Threshold
     set frequency                      -- Set Radio Frequency (MHz)
     set gateway                        -- Set Gateway IP Address
     set gbeaconrate                    -- Set 11g Beacon Rate
     set groupkeyupdate                 -- Set Group Key Update Interval (in Seconds)
     set gdraft5                        -- Set 11g Draft 5.0 compatibility
     set hostipaddr                     -- Set Host IP address
     set ipaddr                         -- Set IP Address
     set ipmask                         -- Set IP Subnet Mask
     set jsw                            -- Set Jumpstart Mode
     set jsp2Passwd                     -- Set JS-P2 password
     set key                            -- Set Encryption Key
     set keyentrymethod                 -- Select Encryption Key Entry Method
     set keysource                      -- Select Source Of Encryption Keys
     set login                          -- Modify Login User Name
     set minimumrate                    -- Set Minimum Rate
     set minimumrate                    -- Set Minimum Rate
     set minimumrate                    -- Set Minimum Rate
     set minimumrate                    -- Set Minimum Rate
     set minimumrate                    -- Set Minimum Rate
     set nameaddress                    -- Set Name Server IP address
     set noiseImmunityLvl               -- Set ANI Parameter for Noise Immunity Level
     set ofdmTrigHigh                   -- Set Higher Trigger Threshold for OFDM Phy Errors for ANI Control
     set ofdmTrigLow                    -- Set Lower Trigger Threshold for OFDM Phy Errors for ANI Control
     set ofdmWeakSigDet                 -- Set ANI Parameter for OFDM Weak Signal Detection
     set overRidetxpower                -- Set Tx power override
     set operationMode                  -- Set operation Mode
     set password                       -- Modify Password
     set passphrase                     -- Modify Passphrase
     set pktLogEnable                   -- Enable Packet Logging
     set power                          -- Set Transmit Power
     set quietAckCtsAllow               -- Allow Ack/Cts frames during quiet period
     set quietDuration                  -- Duration of quiet period
     set quietOffset                    -- Offset of quiet period into the beacon period
     set radiusname                     -- Set RADIUS name or IP address
     set radiusport                     -- Set RADIUS port number
     set radiussecret                   -- Set RADIUS shared secret
     set rate                           -- Set Data Rate
     set rate                           -- Set Data Rate
     set rate                           -- Set Data Rate
     set rate                           -- Set Data Rate
     set rate                           -- Set Data Rate
     set reg                            -- Set Register Value
     set regulatorydomain               -- Set Regulatory Domain
     set remoteAP                       -- Set Remote AP's Mac Address
     set hwtxretries                    -- Set HW Transmit Retry Limit
     set swtxretries                    -- Set SW Transmit Retry Limit
     set rtsthreshold                   -- Set RTS/CTS Threshold
     set shortpreamble                  -- Set Short Preamble
     set shortslottime                  -- Set Short Slot Time
     set sntpserver                     -- Set SNTP/NTP Server IP Address
     set softwareretry                  -- Set Software Retry
     set spurImmunityLvl                -- Set ANI Parameter for Spur Immunity Level
     set ssid                           -- Set Service Set ID
     set ssidsuppress                   -- Set SSID Suppress Mode
     set SuperG                         -- Super G Features 
     set systemname                     -- Set Access Point System Name
     set telnet                         -- Set Telnet Mode
     set timeout                        -- Set Telnet Timeout
     set tzone                          -- Set Time Zone Setting
     set updateparam                    -- Set Vendor Default Firmware Update Params
     set vlan                           -- Set VLAN Mode
     set watchdog                       -- Set Watchdog Mode
     set wds                            -- Set WDS Mode
     set webUI                          -- Set Web UI Mode
     set wep                            -- Set Encryption Mode
     set wlanstate                      -- Set wlan state
     set wirelessmode                   -- Set Wireless LAN Mode
     set wmm                            -- Set WMM Mode
     set wmmParamBss                    -- Set WMM parameters used by STAs in this BSS
     set wmmParam                       -- Set WMM parameters used by this AP
     spy report                         -- Print spy report
     spy show                           -- Print debug info
     spy start                          -- Start spy
     spy stop                           -- Stop spy
     start wlan                         -- Start the current wlan
     stop wlan                          -- Stop the current wlan
     support                            -- Print support information
     timeofday                          -- Display Current Time of Day
     v54 alg                            -- Set/show the antenna algorithm
     v54 ant                            -- Video54 Antenna Config
     v54 antreset                       -- Reset V54 TxCtrl State
     v54 rtt                            -- Real-time Telemetry output
     v54 fchan                          -- Fast Channel Change
     v54 emon                           -- Environmental Monitoring
     v54 learn                          -- Send V54 learning packets
     v54 queue                          -- Video54 Queuing Debug Info
     v54 reset                          -- Reset V54 TxCtrl State
     v54 staQueue                       -- Per-Station-Queue scheduling
     v54 staticant                      -- Configure a static antenna
     v54 staticant                      -- Configure a static antenna
     version                            -- Software version
     video classifier                   -- Classify
     video qos                          -- Quality Of Service
     video pcap                         -- Packet capture
    wlan0 -> boot ethernet
    Invalid input characters!
    wlan0 -> boot
    Invalid input characters!
    wlan0 -> help boot
    List of Access Point CLI commands:
     ?                                  -- Display CLI Command List
     arp add                            -- create or modify ARP table entry
     arp delete                         -- remove ARP table entry
     arp flush                          -- flush all entries in the ARP table
     arp show                           -- Display firmware information
     board change                       -- Change Board Data
     board dump                         -- Dump Board Data
     add remoteWbr                      -- Add a remote Wireless Bridge
     admin                              -- Temporary factory admin
     boot flash                         -- Boot from flash
     boot ethernet                      -- Boot from network
     boot dump                          -- dump boot line data
     cat                                -- list file
     cp                                 -- Copy file
     config wlan                        -- config wlanX
     connect bss                        -- connect to bssX
     del acl                            -- Delete Access Control List
     del key                            -- Delete Encryption key
     del remoteWbr                      -- Delete a remote Wireless Bridge
     del seed                           -- Delete Random Seed
     dis                                -- Dis-associate an End Station
     eeprom                             -- dump eeprom data
     find bss                           -- Find BSS
     find channel                       -- Find Available Channel
     find all                           -- Find All BSS
     format                             -- Format flash filesytem
     bootrom                            -- Update boot rom image
     ftp                                -- Software update via FTP
     get 11gonly                        -- Display 11g Only Allowed
     get 11goptimize                    -- Display 11g Optimization Level
     get 11goverlapbss                  -- Display Overlapping BSS Protection
     get abolt                          -- 
     get acl                            -- Display Access Control List
     get aging                          -- Display Aging Interval
     get antenna                        -- Display Antenna Diversity
     get arp                            -- Display arp Table
     get if                             -- Display attached network interfaces
     get routes                         -- Display routing table 
     get association                    -- Display Association Table
     get authentication                 -- Display Authentication Type
     get autoProvision                  -- Display Auto-Provision Mode
     get autochannelselect              -- Display Auto Channel Select
     get basic11b                       -- Display Basic 11b Rates
     get basic11g                       -- Display Basic 11g Rates
     get beaconinterval                 -- Display Beacon Interval
     get bridgeTable                    -- Display internal SW bridge table
     get burstSeqThreshold              -- Display Max Number of frames in a Burst
     get burstTime                      -- Display Burst Time
     get cacheperf                      -- Display the cache performance counters
     get calibration                    -- Display Noise And Offset Calibration Mode
     get cckTrigHigh                    -- Display Higher Trigger Threshold for CCK Phy Errors for ANI Control
     get cckTrigLow                     -- Display Lower Trigger Threshold for CCK Phy Errors for ANI Control
     get cckWeakSigThr                  -- Display ANI Parameter for CCK Weak Signal Detection Threshold
     get channel                        -- Display Radio Channel
     get cipher                         -- Display Encryption cipher
     get compproc                       -- Display Compression scheme
     get compwinsize                    -- Display Compression Window Size
     get config                         -- Display Current AP Configuration
     get countrycode                    -- Display Country Code
     get ctsmode                        -- Display CTS mode
     get ctsrate                        -- Display CTS rate
     get ctstype                        -- Display CTS type
     get domainsuffix                   -- Display Domain Name Server suffix
     get dtim                           -- Display Data Beacon Rate (DTIM)
     get dhcp                           -- Display DHCP Client Mode
     get enableANI                      -- Display Adaptive Noise Immunity Control On/Off
     get encryption                     -- Display Encryption Mode
     get eth                            -- Display Ethernet Statistics
     get extendedchanmode               -- Display Extended Channel Mode
     get firStepLvl                     -- Display ANI Parameter for FirStepLevel
     get fragmentthreshold              -- Display Fragment Threshold
     get frequency                      -- Display Radio Frequency (MHz)
     get gateway                        -- Display Gateway IP Address
     get gbeaconrate                    -- Display 11g Beacon Rate
     get gdraft5                        -- Display 11g Draft 5.0 compatibility
     get groupkeyupdate                 -- Display Group Key Update Interval (in Seconds)
     get hardware                       -- Display Hardware Revisions
     get hostipaddr                     -- Display Host IP Address
     get ipaddr                         -- Display IP Address
     get ipmask                         -- Display IP Subnet Mask
     get jsw                            -- Display Jumpstart Mode
     get jsP2PassPhrase                 -- Display JS-P2 passphrase
     get key                            -- Display Encryption Key
     get keyentrymethod                 -- Display Encyrption Key Entry Method
     get keysource                      -- Display Source Of Encryption Keys
     get ledStatus                      -- Display current LED status
     get login                          -- Display Login User Name
     get minimumrate                    -- Display Minimum Rate
     get nameaddr                       -- Display IP address of name server
     get nf                             -- Display Noise Floor
     get noiseImmunityLvl               -- Display ANI Parameter for Noise Immunity Level
     get ofdmTrigHigh                   -- Display Higher Trigger Threshold for OFDM Phy Errors for ANI Control
     get ofdmTrigLow                    -- Display Lower Trigger Threshold for OFDM Phy Errors for ANI Control
     get ofdmWeakSigDet                 -- Display ANI Parameter for OFDM Weak Signal Detection
     get overRidetxpower                -- Display Tx power override
     get operationMode                  -- Display Operation Mode
     get passphrase                     -- Display Passphrase
     get passphrasekey                  -- Display Passphrase Key
     get perfstats                      -- Dump system performance stats
     get pnetmon                        -- NetTask profile information
     get pktLogEnable                   -- Display Packet Logging Mode
     get power                          -- Display Transmit Power Setting
     get quietAckCtsAllow               -- Display if Ack/Cts frames are allowed during quiet period
     get quietDuration                  -- Display Duration of quiet period
     get quietOffset                    -- Display Offset of quiet period into the beacon period
     get radiusname                     -- Display RADIUS server name or IP address
     get radiusport                     -- Display RADIUS port number
     get rate                           -- Display Data Rate
     get reg                            -- Display the register contents at the given offset
     get remoteAp                       -- Display Remote Ap's Mac Address
     get reset                          -- Display # of resets
     get remoteWbr                      -- Display configured Remote Wireless bridges
     get hwtxretries                    -- Display HW Transmit Retry Limit
     get swtxretries                    -- Display SW Transmit Retry Limit
     get rtsthreshold                   -- Display RTS/CTS Threshold
     get seed                           -- Display Random Seed
     get shortpreamble                  -- Display Short Preamble Usage
     get shortslottime                  -- Display Short Slot Time Usage
     get sib                            -- Display Station Information
     get sntpserver                     -- Display SNTP/NTP Server IP Address
     get softwareretry                  -- Display Software Retry
     get spurImmunityLvl                -- Display ANI Parameter for Spur Immunity Level
     get ssid                           -- Display Service Set ID
     get ssidsuppress                   -- Display SSID Suppress Mode
     get station                        -- Display Station Status
     get SuperG                         -- Display SuperG Feature Status
     get systemname                     -- Display Access Point System Name
     get telnet                         -- Display Telnet Mode
     get timeout                        -- Display Telnet Timeout
     get times                          -- Display startup times
     get tzone                          -- Display Time Zone Setting
     get updateparam                    -- Display Vendor Default Firmware Update Params
     get uptime                         -- Display UpTime
     get vlan                           -- Display VLAN Mode
     get watchdog                       -- Display Watchdog Mode
     get wds                            -- Display WDS Mode
     get webUI                          -- Display WebUI Mode
     get wep                            -- Display Encryption Mode
     get wirelessmode                   -- Display Wireless LAN Mode
     get wmm                            -- Display WMM Mode
     get wmmParamBss ac                 -- Get EDCA values for this access class
     get wmmParam ac                    -- Get EDCA values for this access class
     get wmmParam queue                 -- Get EDCA values for this HW queue
     get wlanstate                      -- Display wlan state
     help                               -- Display CLI Command List
     Lebradeb                           -- Disable reboot during radar detection
     ls                                 -- list directory
     logoff                             -- Logoff
     mem                                -- system memory statistics
     mv                                 -- Move file
     np                                 -- Network Performance
     ns                                 -- Network Performance Server
     ping                               -- Ping
     pktLog                             -- Packet Log
     radar!                             -- Simulate radar detection on current channel
     reboot                             -- Reboot Access Point
     rm                                 -- Remove file
     run                                -- Run command file
     task priority                      -- Set task priority
     task show                          -- Set task info
     task stack                         -- Set task stack info
     task resume                        -- resume task
     task suspend                       -- suspend task
     tftp                               -- Software update via TFTP
     quit                               -- Logoff
     set 11gonly disable                -- Disable 11g only allowed
     set 11gonly enable                 -- Enable 11g only allowed
     set 11goptimize                    -- Set 11g Optimization Level
     set 11goverlapbss disable          -- Disable Overlapping BSS protection
     set 11goverlapbss enable           -- Enable Overlapping BSS protection
     set abolt                          -- 
     set acl allow                      -- Add MAC address to the ACL
     set acl enable                     -- Select Restricted Access
     set acl deny                       -- Add MAC address to the disabled ACL
     set acl disable                    -- Select Unrestrict Access
     set acl keymap                     -- Add Encryption key mapping for MAC address
     set acl strict                     -- Select Restricted (w/ACL match) Access
     set aging                          -- Set Aging Interval
     set antenna best                   -- Enable antenna diversity
     set antenna 1                      -- Select antenna 1
     set antenna 2                      -- Select antenna 2
     set authentication open-system     -- Select Open-System Authentication Type
     set authentication shared-key      -- Select Shared-Key Authentication Type
     set authentication auto            -- Select auto Authentication Type
     set authentication WPA             -- Select Authentication WPA Type
     set authentication WPA-PSK         -- Select Authentication WPA-PSK Type
     set authentication WPA2            -- Select WPA2 for Authentication Type
     set authentication WPA2-PSK        -- Select WPA2-PSK for Authentication Type
     set authentication WPA-AUTO        -- Allow WPAv1 or WPAv2 for Authentication Type
     set authentication WPA-AUTO-PSK    -- Allow WPAv1-PSK or WPAv2-PSK for Authentication Type
     set autoProvision disable          -- Disable Auto-Provisioning by AP
     set autoProvision enable           -- Enable Auto-Provisioning by AP
     set autochannelselect disable      -- Disable Automatic Channel Selection
     set autochannelselect enable       -- Enable Automatic Channel Selection
     set basic11b disable               -- Disable only basic 11b rates - use all rates
     set basic11b enable                -- Enable only basic 11b rates (1, 2)
     set basic11g 11                    -- Basic Rates (1, 2)
     set basic11g 11b                   -- Basic Rates (1, 2, 5.5, 11)
     set basic11g 11g                   -- Basic Rates (1, 2, 5.5, 11, 6, 12, 24)
     set basic11g ofdm                  -- Basic Rates (6, 12, 24)
     set beaconinterval                 -- Modify Beacon Interval
     set burstSeqThreshold              -- Set Max Number of frames in a Burst
     set burstTime                      -- Set Burst Time
     set cachePerf ic                   -- i-cache performance counters
     set cachePerf dc                   -- d-cache performance counters
     set cachePerf cm                   -- i and d-cache miss  counters
     set cachePerf ch                   -- i and d-cache hit   counters
     set calibration                    -- Set Calibration Period
     set cckTrigHigh                    -- Set Higher Trigger Threshold for CCK Phy Errors For ANI Control
     set cckTrigLow                     -- Set Lower Trigger Threshold for CCK Phy Errors For ANI Control
     set cckWeakSigThr                  -- Set ANI Parameter for CCK Weak Signal Detection Threshold
     set channel                        -- Set Radio Channel
     set cipher wep                     -- Select wep
     set cipher aes                     -- Select aes
     set cipher tkip                    -- Select tkip
     set cipher auto                    -- Select cipher through negotiation
     set compproc                       -- Set Compression Scheme
     set compwinsize                    -- Set Compression Window Size
     set countrycode                    -- Set Country Code
     set ctsmode                        -- Set CTS Mode
     set ctsrate                        -- Set CTS Rate
     set ctstype                        -- Set CTS Type
     set domainsuffix                   -- Set Domain Name Server Suffix
     set dtim                           -- Set Data Beacon Rate (DTIM)
     set dhcp disable                   -- Disable DHCP
     set dhcp enable                    -- Enable DHCP
     set enableANI                      -- Turn Adaptive Noise Immunity Control On/Off
     set encryption disable             -- Disable Encryption
     set encryption enable              -- Enable Encryption
     set extendedchanmode disable       -- Disable Extended Channel Mode
     set extendedchanmode enable        -- Enable Extended Channel Mode
     set factorydefault                 -- Restore to Default Factory Settings
     set firStepLvl                     -- Set ANI Parameter for FirStepLevel
     set fragmentthreshold              -- Set Fragment Threshold
     set frequency                      -- Set Radio Frequency (MHz)
     set gateway                        -- Set Gateway IP Address
     set gbeaconrate                    -- Set 11g Beacon Rate
     set groupkeyupdate                 -- Set Group Key Update Interval (in Seconds)
     set gdraft5 disable                -- Disable 11g Draft 5.0 compatibility
     set gdraft5 enable                 -- Enable 11g Draft 5.0 compatibility
     set hostipaddr                     -- Set Host IP address
     set ipaddr                         -- Set IP Address
     set ipmask                         -- Set IP Subnet Mask
     set jsw enable                     -- Enable  Jumpstart
     set jsw disable                    -- Disable  Jumpstart
     set jsp2Passwd                     -- Set JS-P2 password
     set key default                    -- Set Default Encryption Key
     set key 40                         -- Set 40-bit Encryption Key
     set key 104                        -- Set 104-bit Encryption Key
     set key 128                        -- Set 128-bit Encryption Key
     set keyentrymethod hexadecimal     -- Key contains (0 - 9, A - F)
     set keyentrymethod asciitext       -- Key contains keyboard characters
     set keysource flash                -- All keys will be read from flash (no key derivation)
     set keysource server               -- All keys will be derived from authentication server
     set keysource mixed                -- Keys read from flash or derived from authentication server
     set login                          -- Modify Login User Name
     set minimumrate 0.25               -- Select 0.25 Mbps
     set minimumrate 0.5                -- Select 0.5 Mbps
     set minimumrate 1                  -- Select 1 Mbps
     set minimumrate 2                  -- Select 2 Mbps
     set minimumrate 3                  -- Select 3 Mbps
     set minimumrate 6                  -- Select 6 Mbps
     set minimumrate 9                  -- Select 9 Mbps
     set minimumrate 12                 -- Select 12 Mbps
     set minimumrate 18                 -- Select 18 Mbps
     set minimumrate 24                 -- Select 24 Mbps
     set minimumrate 36                 -- Select 36 Mbps
     set minimumrate 48                 -- Select 48 Mbps
     set minimumrate 54                 -- Select 54 Mbps
     set minimumrate 12                 -- Select 12 Mbps
     set minimumrate 18                 -- Select 18 Mbps
     set minimumrate 24                 -- Select 24 Mbps
     set minimumrate 36                 -- Select 36 Mbps
     set minimumrate 48                 -- Select 48 Mbps
     set minimumrate 72                 -- Select 72 Mbps
     set minimumrate 96                 -- Select 96 Mbps
     set minimumrate 108                -- Select 108 Mbps
     set minimumrate 1                  -- Select 1 Mbps
     set minimumrate 2                  -- Select 2 Mbps
     set minimumrate 5.5                -- Select 5.5 Mbps
     set minimumrate 11                 -- Select 11 Mbps
     set minimumrate 0.25               -- Select 0.25 Mbps
     set minimumrate 0.5                -- Select 0.5 Mbps
     set minimumrate 1                  -- Select 1 Mbps
     set minimumrate 2                  -- Select 2 Mbps
     set minimumrate 1x                 -- Select XR 1 Mbps
     set minimumrate 2x                 -- Select XR 2 Mbps
     set minimumrate 3                  -- Select 3 Mbps
     set minimumrate 5.5                -- Select 5.5 Mbps
     set minimumrate 11                 -- Select 11 Mbps
     set minimumrate 6                  -- Select 6 Mbps
     set minimumrate 9                  -- Select 9 Mbps
     set minimumrate 12                 -- Select 12 Mbps
     set minimumrate 18                 -- Select 18 Mbps
     set minimumrate 24                 -- Select 24 Mbps
     set minimumrate 36                 -- Select 36 Mbps
     set minimumrate 48                 -- Select 48 Mbps
     set minimumrate 54                 -- Select 54 Mbps
     set minimumrate 12                 -- Select 12 Mbps
     set minimumrate 18                 -- Select 18 Mbps
     set minimumrate 24                 -- Select 24 Mbps
     set minimumrate 36                 -- Select 36 Mbps
     set minimumrate 48                 -- Select 48 Mbps
     set minimumrate 72                 -- Select 72 Mbps
     set minimumrate 96                 -- Select 96 Mbps
     set minimumrate 108                -- Select 108 Mbps
     set nameaddress                    -- Set Name Server IP address
     set noiseImmunityLvl               -- Set ANI Parameter for Noise Immunity Level
     set ofdmTrigHigh                   -- Set Higher Trigger Threshold for OFDM Phy Errors for ANI Control
     set ofdmTrigLow                    -- Set Lower Trigger Threshold for OFDM Phy Errors for ANI Control
     set ofdmWeakSigDet                 -- Set ANI Parameter for OFDM Weak Signal Detection
     set overRidetxpower                -- Set Tx power override
     set operationMode ap               -- Operating as Access Point
     set operationMode sta              -- Operating as Wireless Client
     set operationMode wbr              -- Operating as Wireless Bridge
     set operationMode repeater         -- Operating as Wireless Repeater
     set password                       -- Modify Password
     set passphrase                     -- Modify Passphrase
     set pktLogEnable                   -- Enable Packet Logging
     set power full                     -- Set maximum (normal) transmit power
     set power half                     -- Set fractional (1/2) transmit power
     set power quarter                  -- Set fractional (1/4) transmit power
     set power eighth                   -- Set fractional (1/8) transmit power
     set power min                      -- Set minimum transmit power
     set quietAckCtsAllow               -- Allow Ack/Cts frames during quiet period
     set quietDuration                  -- Duration of quiet period
     set quietOffset                    -- Offset of quiet period into the beacon period
     set radiusname                     -- Set RADIUS name or IP address
     set radiusport                     -- Set RADIUS port number
     set radiussecret                   -- Set RADIUS shared secret
     set rate best                      -- Select best data rate
     set rate 6                         -- Select 6 Mbps
     set rate 9                         -- Select 9 Mbps
     set rate 12                        -- Select 12 Mbps
     set rate 18                        -- Select 18 Mbps
     set rate 24                        -- Select 24 Mbps
     set rate 36                        -- Select 36 Mbps
     set rate 48                        -- Select 48 Mbps
     set rate 54                        -- Select 54 Mbps
     set rate best                      -- Select best data rate
     set rate 12                        -- Select 12 Mbps
     set rate 18                        -- Select 18 Mbps
     set rate 24                        -- Select 24 Mbps
     set rate 36                        -- Select 36 Mbps
     set rate 48                        -- Select 48 Mbps
     set rate 72                        -- Select 72 Mbps
     set rate 96                        -- Select 96 Mbps
     set rate 108                       -- Select 108 Mbps
     set rate best                      -- Select best data rate
     set rate 1                         -- Select 1 Mbps
     set rate 2                         -- Select 2 Mbps
     set rate 5.5                       -- Select 5.5 Mbps
     set rate 11                        -- Select 11 Mbps
     set rate best                      -- Select best data rate
     set rate 1                         -- Select 1 Mbps
     set rate 2                         -- Select 2 Mbps
     set rate 5.5                       -- Select 5.5 Mbps
     set rate 11                        -- Select 11 Mbps
     set rate 6                         -- Select 6 Mbps
     set rate 9                         -- Select 9 Mbps
     set rate 12                        -- Select 12 Mbps
     set rate 18                        -- Select 18 Mbps
     set rate 24                        -- Select 24 Mbps
     set rate 36                        -- Select 36 Mbps
     set rate 48                        -- Select 48 Mbps
     set rate 54                        -- Select 54 Mbps
     set rate best                      -- Select best data rate
     set rate 12                        -- Select 12 Mbps
     set rate 18                        -- Select 18 Mbps
     set rate 24                        -- Select 24 Mbps
     set rate 36                        -- Select 36 Mbps
     set rate 48                        -- Select 48 Mbps
     set rate 72                        -- Select 72 Mbps
     set rate 96                        -- Select 96 Mbps
     set rate 108                       -- Select 108 Mbps
     set reg                            -- Set Register Value
     set regulatorydomain               -- Set Regulatory Domain
     set remoteAP                       -- Set Remote AP's Mac Address
     set hwtxretries                    -- Set HW Transmit Retry Limit
     set swtxretries                    -- Set SW Transmit Retry Limit
     set rtsthreshold                   -- Set RTS/CTS Threshold
     set shortpreamble disable          -- Disable Short Preamble (use only long)
     set shortpreamble enable           -- Enable Short and Long Preamble
     set shortslottime disable          -- Disable Short Slot Time (use only long)
     set shortslottime enable           -- Enable Short Slot Time
     set sntpserver                     -- Set SNTP/NTP Server IP Address
     set softwareretry enable           -- Enable Software Retry
     set softwareretry disable          -- Disable Software Retry
     set spurImmunityLvl                -- Set ANI Parameter for Spur Immunity Level
     set ssid                           -- Set Service Set ID
     set ssidsuppress enable            -- Enable SSID suppress mode
     set ssidsuppress disable           -- Disable SSID suppress mode
     set SuperG enable                  -- Enable SuperG Features
     set SuperG disable                 -- Disable SuperG Features
     set systemname                     -- Set Access Point System Name
     set telnet disable                 -- Disable Telnet access
     set telnet enable                  -- Enable Telnet access
     set timeout                        -- Set Telnet Timeout
     set tzone                          -- Set Time Zone Setting
     set updateparam                    -- Set Vendor Default Firmware Update Params
     set vlan disable                   -- Disable VLAN
     set vlan enable                    -- Enable VLAN
     set watchdog disable               -- Disable Watchdog
     set watchdog enable                -- Enable Watchdog
     set wds disable                    -- Disable WDS support
     set wds enable                     -- Enable WDS support
     set webUI disable                  -- Disable Web UI
     set webUI enable                   -- Enable Web UI
     set wep disable                    -- Disable Encryption
     set wep enable                     -- Enable Encryption
     set wlanstate disable              -- Disable wlan
     set wlanstate enable               -- Enable wlan
     set wirelessmode 11a               -- 802.11a
     set wirelessmode 11b               -- 802.11b
     set wirelessmode 11g               -- 802.11g
     set wirelessmode 108g static       -- 802.11g Static Turbo
     set wirelessmode 108g dynamic      -- 802.11g Dynamic Turbo
     set wirelessmode turbo static      -- 802.11a Static Turbo
     set wirelessmode turbo dynamic     -- 802.11a Dynamic Turbo
     set wmm disable                    -- Disable WMM
     set wmm enable                     -- Enable WMM
     set wmmParamBss ac                 -- Set EDCA values for all access classes
     set wmmParam ac                    -- Set EDCA values for all access classes
     set wmmParam queue                 -- Set EDCA values for all HW queues
     spy report                         -- Print spy report
     spy show                           -- Print debug info
     spy start                          -- Start spy
     spy stop                           -- Stop spy
     start wlan                         -- Start the current wlan
     stop wlan                          -- Stop the current wlan
     support                            -- Print support information
     timeofday                          -- Display Current Time of Day
     v54 alg                            -- Set/show the antenna algorithm
     v54 ant                            -- Video54 Antenna Config
     v54 antreset                       -- Reset V54 TxCtrl State
     v54 rtt                            -- Real-time Telemetry output
     v54 fchan                          -- Fast Channel Change
     v54 emon rx disable                -- Disable Rx stats gathering
     v54 emon rx enable                 -- Enable  Rx stats gathering
     v54 emon tx disable                -- Disable Tx stats gathering
     v54 emon tx enable                 -- Enable  Tx stats gathering
     v54 emon output disable            -- Disable emon periodic output
     v54 emon output enable             -- Enable  emon periodic output
     v54 emon dump second               -- Dump per-second stats history
     v54 emon dump minute               -- Dump per-minute stats history
     v54 emon dump hour                 -- Dump per-hour   stats history
     v54 learn                          -- Send V54 learning packets
     v54 queue                          -- Video54 Queuing Debug Info
     v54 reset                          -- Reset V54 TxCtrl State
     v54 staQueue clear                 -- Reset PSQ statistics counters
     v54 staQueue disable               -- Disable Per-Station-Queue scheduling
     v54 staQueue enable                -- Enable Per-Station-Queue scheduling
     v54 staQueue hires disable         -- Disable using Hi-Res Clock
     v54 staQueue hires enable          -- Enable using Hi-Res Clock
     v54 staQueue priorityAdjust        -- PSQ priority-adjust factor
     v54 staQueue queueLimit            -- PSQ per-station max queue size
     v54 staQueue show                  -- Display PSQ statistics
     v54 staticant                      -- Configure a static antenna
     v54 staticant                      -- Configure a static antenna
     version                            -- Software version
     video classifier actions tos disable -- Disable TOS marking
     video classifier actions tos enable -- Enable TOS marking
     video classifier actions tos video -- Set Video TOS value
     video classifier actions tos voIP  -- Set VoIP TOS value
     video classifier both dbmcast disable -- Disable Directed Bcast/Mcast Feature
     video classifier both dbmcast enable -- Enable Directed Bcast/Mcast Feature
     video classifier both disable      -- Disable Classification on Interface
     video classifier both enable       -- Enable Classification on Interface
     video classifier both igmp disable -- Disable IGMP Snooping
     video classifier both igmp enable  -- Enable IGMP Snooping
     video classifier both port add tcp dest tos video -- Mark TOS with video value
     video classifier both port add tcp dest tos voice -- Mark TOS with voice value
     video classifier both port add tcp dest drop -- Drop packet
     video classifier both port add tcp dest pcap -- Capture packet
     video classifier both port add tcp dst tos video -- Mark TOS with video value
     video classifier both port add tcp dst tos voice -- Mark TOS with voice value
     video classifier both port add tcp dst drop -- Drop packet
     video classifier both port add tcp dst pcap -- Capture packet
     video classifier both port add tcp src tos video -- Mark TOS with video value
     video classifier both port add tcp src tos voice -- Mark TOS with voice value
     video classifier both port add tcp src drop -- Drop packet
     video classifier both port add tcp src pcap -- Capture packet
     video classifier both port add udp dest tos video -- Mark TOS with video value
     video classifier both port add udp dest tos voice -- Mark TOS with voice value
     video classifier both port add udp dest drop -- Drop packet
     video classifier both port add udp dest pcap -- Capture packet
     video classifier both port add udp dst tos video -- Mark TOS with video value
     video classifier both port add udp dst tos voice -- Mark TOS with voice value
     video classifier both port add udp dst drop -- Drop packet
     video classifier both port add udp dst pcap -- Capture packet
     video classifier both port add udp src tos video -- Mark TOS with video value
     video classifier both port add udp src tos voice -- Mark TOS with voice value
     video classifier both port add udp src drop -- Drop packet
     video classifier both port add udp src pcap -- Capture packet
     video classifier both port delete tcp dest tos video -- Mark TOS with video value
     video classifier both port delete tcp dest tos voice -- Mark TOS with voice value
     video classifier both port delete tcp dest drop -- Drop packet
     video classifier both port delete tcp dest pcap -- Capture packet
     video classifier both port delete tcp dst tos video -- Mark TOS with video value
     video classifier both port delete tcp dst tos voice -- Mark TOS with voice value
     video classifier both port delete tcp dst drop -- Drop packet
     video classifier both port delete tcp dst pcap -- Capture packet
     video classifier both port delete tcp src tos video -- Mark TOS with video value
     video classifier both port delete tcp src tos voice -- Mark TOS with voice value
     video classifier both port delete tcp src drop -- Drop packet
     video classifier both port delete tcp src pcap -- Capture packet
     video classifier both port delete udp dest tos video -- Mark TOS with video value
     video classifier both port delete udp dest tos voice -- Mark TOS with voice value
     video classifier both port delete udp dest drop -- Drop packet
     video classifier both port delete udp dest pcap -- Capture packet
     video classifier both port delete udp dst tos video -- Mark TOS with video value
     video classifier both port delete udp dst tos voice -- Mark TOS with voice value
     video classifier both port delete udp dst drop -- Drop packet
     video classifier both port delete udp dst pcap -- Capture packet
     video classifier both port delete udp src tos video -- Mark TOS with video value
     video classifier both port delete udp src tos voice -- Mark TOS with voice value
     video classifier both port delete udp src drop -- Drop packet
     video classifier both port delete udp src pcap -- Capture packet
     video classifier both port disable -- Disable port classification Mode
     video classifier both port enable  -- Enable port classification Mode
     video classifier both port show    -- Show current L4 port filters
     video classifier both show         -- Show Classification Info
     video classifier both nonzero disable -- Disable Non-zero TOS marking
     video classifier both nonzero enable -- Enable Non-zero TOS marking
     video classifier both unkMcast disable -- Disable Unknown Mcast Drop
     video classifier both unkMcast enable -- Enable Unknown Mcast Drop
     video classifier both upnp disable -- Disable UPnP Processing
     video classifier both upnp enable  -- Enable UPnP Processing
     video classifier ethernet dbmcast disable -- Disable Directed Bcast/Mcast Feature
     video classifier ethernet dbmcast enable -- Enable Directed Bcast/Mcast Feature
     video classifier ethernet disable  -- Disable Classification on Interface
     video classifier ethernet enable   -- Enable Classification on Interface
     video classifier ethernet igmp disable -- Disable IGMP Snooping
     video classifier ethernet igmp enable -- Enable IGMP Snooping
     video classifier ethernet port add tcp dest tos video -- Mark TOS with video value
     video classifier ethernet port add tcp dest tos voice -- Mark TOS with voice value
     video classifier ethernet port add tcp dest drop -- Drop packet
     video classifier ethernet port add tcp dest pcap -- Capture packet
     video classifier ethernet port add tcp dst tos video -- Mark TOS with video value
     video classifier ethernet port add tcp dst tos voice -- Mark TOS with voice value
     video classifier ethernet port add tcp dst drop -- Drop packet
     video classifier ethernet port add tcp dst pcap -- Capture packet
     video classifier ethernet port add tcp src tos video -- Mark TOS with video value
     video classifier ethernet port add tcp src tos voice -- Mark TOS with voice value
     video classifier ethernet port add tcp src drop -- Drop packet
     video classifier ethernet port add tcp src pcap -- Capture packet
     video classifier ethernet port add udp dest tos video -- Mark TOS with video value
     video classifier ethernet port add udp dest tos voice -- Mark TOS with voice value
     video classifier ethernet port add udp dest drop -- Drop packet
     video classifier ethernet port add udp dest pcap -- Capture packet
     video classifier ethernet port add udp dst tos video -- Mark TOS with video value
     video classifier ethernet port add udp dst tos voice -- Mark TOS with voice value
     video classifier ethernet port add udp dst drop -- Drop packet
     video classifier ethernet port add udp dst pcap -- Capture packet
     video classifier ethernet port add udp src tos video -- Mark TOS with video value
     video classifier ethernet port add udp src tos voice -- Mark TOS with voice value
     video classifier ethernet port add udp src drop -- Drop packet
     video classifier ethernet port add udp src pcap -- Capture packet
     video classifier ethernet port delete tcp dest tos video -- Mark TOS with video value
     video classifier ethernet port delete tcp dest tos voice -- Mark TOS with voice value
     video classifier ethernet port delete tcp dest drop -- Drop packet
     video classifier ethernet port delete tcp dest pcap -- Capture packet
     video classifier ethernet port delete tcp dst tos video -- Mark TOS with video value
     video classifier ethernet port delete tcp dst tos voice -- Mark TOS with voice value
     video classifier ethernet port delete tcp dst drop -- Drop packet
     video classifier ethernet port delete tcp dst pcap -- Capture packet
     video classifier ethernet port delete tcp src tos video -- Mark TOS with video value
     video classifier ethernet port delete tcp src tos voice -- Mark TOS with voice value
     video classifier ethernet port delete tcp src drop -- Drop packet
     video classifier ethernet port delete tcp src pcap -- Capture packet
     video classifier ethernet port delete udp dest tos video -- Mark TOS with video value
     video classifier ethernet port delete udp dest tos voice -- Mark TOS with voice value
     video classifier ethernet port delete udp dest drop -- Drop packet
     video classifier ethernet port delete udp dest pcap -- Capture packet
     video classifier ethernet port delete udp dst tos video -- Mark TOS with video value
     video classifier ethernet port delete udp dst tos voice -- Mark TOS with voice value
     video classifier ethernet port delete udp dst drop -- Drop packet
     video classifier ethernet port delete udp dst pcap -- Capture packet
     video classifier ethernet port delete udp src tos video -- Mark TOS with video value
     video classifier ethernet port delete udp src tos voice -- Mark TOS with voice value
     video classifier ethernet port delete udp src drop -- Drop packet
     video classifier ethernet port delete udp src pcap -- Capture packet
     video classifier ethernet port disable -- Disable port classification Mode
     video classifier ethernet port enable -- Enable port classification Mode
     video classifier ethernet port show -- Show current L4 port filters
     video classifier ethernet show     -- Show Classification Info
     video classifier ethernet nonzero disable -- Disable Non-zero TOS marking
     video classifier ethernet nonzero enable -- Enable Non-zero TOS marking
     video classifier ethernet unkMcast disable -- Disable Unknown Mcast Drop
     video classifier ethernet unkMcast enable -- Enable Unknown Mcast Drop
     video classifier ethernet upnp disable -- Disable UPnP Processing
     video classifier ethernet upnp enable -- Enable UPnP Processing
     video classifier wireless dbmcast disable -- Disable Directed Bcast/Mcast Feature
     video classifier wireless dbmcast enable -- Enable Directed Bcast/Mcast Feature
     video classifier wireless disable  -- Disable Classification on Interface
     video classifier wireless enable   -- Enable Classification on Interface
     video classifier wireless igmp disable -- Disable IGMP Snooping
     video classifier wireless igmp enable -- Enable IGMP Snooping
     video classifier wireless port add tcp dest tos video -- Mark TOS with video value
     video classifier wireless port add tcp dest tos voice -- Mark TOS with voice value
     video classifier wireless port add tcp dest drop -- Drop packet
     video classifier wireless port add tcp dest pcap -- Capture packet
     video classifier wireless port add tcp dst tos video -- Mark TOS with video value
     video classifier wireless port add tcp dst tos voice -- Mark TOS with voice value
     video classifier wireless port add tcp dst drop -- Drop packet
     video classifier wireless port add tcp dst pcap -- Capture packet
     video classifier wireless port add tcp src tos video -- Mark TOS with video value
     video classifier wireless port add tcp src tos voice -- Mark TOS with voice value
     video classifier wireless port add tcp src drop -- Drop packet
     video classifier wireless port add tcp src pcap -- Capture packet
     video classifier wireless port add udp dest tos video -- Mark TOS with video value
     video classifier wireless port add udp dest tos voice -- Mark TOS with voice value
     video classifier wireless port add udp dest drop -- Drop packet
     video classifier wireless port add udp dest pcap -- Capture packet
     video classifier wireless port add udp dst tos video -- Mark TOS with video value
     video classifier wireless port add udp dst tos voice -- Mark TOS with voice value
     video classifier wireless port add udp dst drop -- Drop packet
     video classifier wireless port add udp dst pcap -- Capture packet
     video classifier wireless port add udp src tos video -- Mark TOS with video value
     video classifier wireless port add udp src tos voice -- Mark TOS with voice value
     video classifier wireless port add udp src drop -- Drop packet
     video classifier wireless port add udp src pcap -- Capture packet
     video classifier wireless port delete tcp dest tos video -- Mark TOS with video value
     video classifier wireless port delete tcp dest tos voice -- Mark TOS with voice value
     video classifier wireless port delete tcp dest drop -- Drop packet
     video classifier wireless port delete tcp dest pcap -- Capture packet
     video classifier wireless port delete tcp dst tos video -- Mark TOS with video value
     video classifier wireless port delete tcp dst tos voice -- Mark TOS with voice value
     video classifier wireless port delete tcp dst drop -- Drop packet
     video classifier wireless port delete tcp dst pcap -- Capture packet
     video classifier wireless port delete tcp src tos video -- Mark TOS with video value
     video classifier wireless port delete tcp src tos voice -- Mark TOS with voice value
     video classifier wireless port delete tcp src drop -- Drop packet
     video classifier wireless port delete tcp src pcap -- Capture packet
     video classifier wireless port delete udp dest tos video -- Mark TOS with video value
     video classifier wireless port delete udp dest tos voice -- Mark TOS with voice value
     video classifier wireless port delete udp dest drop -- Drop packet
     video classifier wireless port delete udp dest pcap -- Capture packet
     video classifier wireless port delete udp dst tos video -- Mark TOS with video value
     video classifier wireless port delete udp dst tos voice -- Mark TOS with voice value
     video classifier wireless port delete udp dst drop -- Drop packet
     video classifier wireless port delete udp dst pcap -- Capture packet
     video classifier wireless port delete udp src tos video -- Mark TOS with video value
     video classifier wireless port delete udp src tos voice -- Mark TOS with voice value
     video classifier wireless port delete udp src drop -- Drop packet
     video classifier wireless port delete udp src pcap -- Capture packet
     video classifier wireless port disable -- Disable port classification Mode
     video classifier wireless port enable -- Enable port classification Mode
     video classifier wireless port show -- Show current L4 port filters
     video classifier wireless show     -- Show Classification Info
     video classifier wireless nonzero disable -- Disable Non-zero TOS marking
     video classifier wireless nonzero enable -- Enable Non-zero TOS marking
     video classifier wireless unkMcast disable -- Disable Unknown Mcast Drop
     video classifier wireless unkMcast enable -- Enable Unknown Mcast Drop
     video classifier wireless upnp disable -- Disable UPnP Processing
     video classifier wireless upnp enable -- Enable UPnP Processing
     video qos disable                  -- Disable QOS Features
     video qos enable                   -- Enable QOS Features
     video qos mgtAcl disable           -- Disable MgtACL Feature
     video qos mgtAcl enable            -- Enable MgtACL Feature
     video qos show                     -- Display QOS state
     video qos txFail                   -- Set Tx Failure Threshold
     video pcap start                   -- Start capture
     video pcap continue                -- continue capture
     video pcap stop                    -- Stop capture
     video pcap save                    -- Save capture
     video pcap set                     -- Set options
     video pcap show                    -- Display capture status
    wlan0 -> boot etherner
    Invalid parameter: etherner
    Type "help" for a list of valid commands.
    wlan0 -> boot ethernet
    BOOT PARAM           : bootline
    IP Addrress          : 192.168.0.1:ffffff00
    Host                 : 
    Gateway              : 
    Startup script       : 
    other                : AP
    boot device          : ae
    unit number          : 1 
    processor number     : 0 
    file name            : /fl/apv54
    inet on ethernet (e) : 192.168.0.1:ffffff00
    flags (f)            : 0x80 
    other (o)            : AP
    wlan0 -> hel
    BOOT PARAM           : bootline
    IP Addrress          : 192.168.0.1:ffffff00
    Host                 : 
    Gateway              : 
    Startup script       : 
    other                : AP
    List of Access Point CLI commands:
     ?                                  -- Display CLI Command List
     arp add                            -- create or modify ARP table entry
     arp delete                         -- remove ARP table entry
     arp flush                          -- flush all entries in the ARP table
     arp show                           -- Display firmware information
     board change                       -- Change Board Data
     board dump                         -- Dump Board Data
     add remoteWbr                      -- Add a remote Wireless Bridge
     admin                              -- Temporary factory admin
     boot flash                         -- Boot from flash
     boot ethernet                      -- Boot from network
     boot dump                          -- dump boot line data
     cat                                -- list file
     cp                                 -- Copy file
     config wlan                        -- config wlanX
     connect bss                        -- connect to bssX
     del acl                            -- Delete Access Control List
     del key                            -- Delete Encryption key
     del remoteWbr                      -- Delete a remote Wireless Bridge
     del seed                           -- Delete Random Seed
     dis                                -- Dis-associate an End Station
     eeprom                             -- dump eeprom data
     find bss                           -- Find BSS
     find channel                       -- Find Available Channel
     find all                           -- Find All BSS
     format                             -- Format flash filesytem
     bootrom                            -- Update boot rom image
     ftp                                -- Software update via FTP
     get 11gonly                        -- Display 11g Only Allowed
     get 11goptimize                    -- Display 11g Optimization Level
     get 11goverlapbss                  -- Display Overlapping BSS Protection
     get abolt                          -- 
     get acl                            -- Display Access Control List
     get aging                          -- Display Aging Interval
     get antenna                        -- Display Antenna Diversity
     get arp                            -- Display arp Table
     get if                             -- Display attached network interfaces
     get routes                         -- Display routing table 
     get association                    -- Display Association Table
     get authentication                 -- Display Authentication Type
     get autoProvision                  -- Display Auto-Provision Mode
     get autochannelselect              -- Display Auto Channel Select
     get basic11b                       -- Display Basic 11b Rates
     get basic11g                       -- Display Basic 11g Rates
     get beaconinterval                 -- Display Beacon Interval
     get bridgeTable                    -- Display internal SW bridge table
     get burstSeqThreshold              -- Display Max Number of frames in a Burst
     get burstTime                      -- Display Burst Time
     get cacheperf                      -- Display the cache performance counters
     get calibration                    -- Display Noise And Offset Calibration Mode
     get cckTrigHigh                    -- Display Higher Trigger Threshold for CCK Phy Errors for ANI Control
     get cckTrigLow                     -- Display Lower Trigger Threshold for CCK Phy Errors for ANI Control
     get cckWeakSigThr                  -- Display ANI Parameter for CCK Weak Signal Detection Threshold
     get channel                        -- Display Radio Channel
     get cipher                         -- Display Encryption cipher
     get compproc                       -- Display Compression scheme
     get compwinsize                    -- Display Compression Window Size
     get config                         -- Display Current AP Configuration
     get countrycode                    -- Display Country Code
     get ctsmode                        -- Display CTS mode
     get ctsrate                        -- Display CTS rate
     get ctstype                        -- Display CTS type
     get domainsuffix                   -- Display Domain Name Server suffix
     get dtim                           -- Display Data Beacon Rate (DTIM)
     get dhcp                           -- Display DHCP Client Mode
     get enableANI                      -- Display Adaptive Noise Immu^Cnity Control On/Off
     get encryption                     -- Display Encryption Mode
     get eth                            -- Display Ethernet Statistics
     get extendedchanmode               -- Display Ext^ended Channel Mode
     get firStepLvl                     -- Display ANI Parameter for FirStepLevel
     get fragmentthreshold              -- Display Fragment Thresho^ld
     get frequency                      -- Display Radio Frequency (MHz)
     get gateway                        -- Display G
    ateway IP Address
     get gbeaconrate                    -- Display 11g Beacon Rate
     get gdraft5                        -- Display 11g Draft 5.0 compatibility
     get groupkeyupdate     
                -- Display Group Key Update Interval (in Seconds)
     get hardware                       -- Display Hardware Revisions
     get hostipaddr                     -- Display Host IP Address
     get ipaddr                         -- Display IP Address
     get ipmask                         -- Display IP Subnet Mask
     get jsw                     
           -- Display Jumpstart Mode
     get jsP2PassPhrase                 -- Display JS-P2 passphrase
     get key               
                 -- Display Encryption Key
     get keyentrymethod                 -- Display Encyrption Key Entry Method
     get k
    eysource                      -- Display Source Of Encryption Keys
     get ledStatus                      -- Display current LED status
     get login                          -- Display Login User Name
     get minimumrate                    -- Display Minimum Rate
     get nameaddr                       -- Display IP address of name server
     get nf                             -- Display Noise Floor
     get noiseImmunityLvl               -- Display ANI Parameter for Noise Immunity Level
     get ofdmTrigHigh                   -- Display Higher Trigger Threshold for OFDM Phy Errors for ANI Control
     get ofdmTrigLow                    -- Display Lower Trigger Threshold for OFDM Phy Errors for ANI Control
     get ofdmWeakSigDet                 -- Display ANI Parameter for OFDM Weak Signal Detection
     get overRidetxpower                -- Display Tx power override
     get operationMode                  -- Display Operation Mode
     get passphrase                     -- Display Passphrase
     get passphrasekey                  -- Display Passphrase Key
     get perfstats                      -- Dump system performance stats
     get pnetmon                        -- NetTask profile information
     get pktLogEnable                   -- Display Packet Logging Mode
     get power                          -- Display Transmit Power Setting
     get quietAckCtsAllow               -- Display if Ack/Cts frames are allowed during quiet period
     get quietDuration                  -- Display Duration of quiet period
     get quietOffset                    -- Display Offset of quiet period into the beacon period
     get radiusname                     -- Display RADIUS server name or IP address
     get radiusport                     -- Display RADIUS port number
     get rate                           -- Display Data Rate
     get reg                            -- Display the register contents at the given offset
     get remoteAp                       -- Display Remote Ap's Mac Address
     get reset                          -- Display # of resets
     get remoteWbr                      -- Display configured Remote Wireless bridges
     get hwtxretries                    -- Display HW Transmit Retry Limit
     get swtxretries                    -- Display SW Transmit Retry Limit
     get rtsthreshold                   -- Display RTS/CTS Threshold
     get seed                           -- Display Random Seed
     get shortpreamble                  -- Display Short Preamble Usage
     get shortslottime                  -- Display Short Slot Time Usage
     get sib                            -- Display Station Information
     get sntpserver                     -- Display SNTP/NTP Server IP Address
     get softwareretry                  -- Display Software Retry
     get spurImmunityLvl                -- Display ANI Parameter for Spur Immunity Level
     get ssid                           -- Display Service Set ID
     get ssidsuppress                   -- Display SSID Suppress Mode
     get station                        -- Display Station Status
     get SuperG                         -- Display SuperG Feature Status
     get systemname                     -- Display Access Point System Name
     get telnet                         -- Display Telnet Mode
     get timeout                        -- Display Telnet Timeout
     get times                          -- Display startup times
     get tzone                          -- Display Time Zone Setting
     get updateparam                    -- Display Vendor Default Firmware Update Params
     get uptime                         -- Display UpTime
     get vlan                           -- Display VLAN Mode
     get watchdog                       -- Display Watchdog Mode
     get wds                            -- Display WDS Mode
     get webUI                          -- Display WebUI Mode
     get wep                            -- Display Encryption Mode
     get wirelessmode                   -- Display Wireless LAN Mode
     get wmm                            -- Display WMM Mode
     get wmmParamBss                    -- Display WMM parameters used by STA in this BSS
     get wmmParam                       -- Display WMM parameters used by this AP
     get wlanstate                      -- Display wlan state
     help                               -- Display CLI Command List
     Lebradeb                           -- Disable reboot during radar detection
     ls                                 -- list directory
     logoff                             -- Logoff
     mem                                -- system memory statistics
     mv                                 -- Move file
     np                                 -- Network Performance
     ns                                 -- Network Performance Server
     ping                               -- Ping
     pktLog                             -- Packet Log
     radar!                             -- Simulate radar detection on current channel
     reboot                             -- Reboot Access Point
     rm                                 -- Remove file
     run                                -- Run command file
     task priority                      -- Set task priority
     task show                          -- Set task info
     task stack                         -- Set task stack info
     task resume                        -- resume task
     task suspend                       -- suspend task
     tftp                               -- Software update via TFTP
     quit                               -- Logoff
     set 11gonly                        -- Set 11g Only Allowed
     set 11goptimize                    -- Set 11g Optimization Level
     set 11goverlapbss                  -- Set Overlapping BSS Protection
     set abolt                          -- 
     set acl                            -- Set Access Control List
     set aging                          -- Set Aging Interval
     set antenna                        -- Set Antenna
     set authentication                 -- Set Authentication Type
     set autoProvision                  -- Set Auto-Provision Mode
     set autochannelselect              -- Set Auto Channel Selection
     set basic11b                       -- Set Use of Basic 11b Rates
     set basic11g                       -- Set Use of Basic 11g Rates
     set beaconinterval                 -- Modify Beacon Interval
     set burstSeqThreshold              -- Set Max Number of frames in a Burst
     set burstTime                      -- Set Burst Time
     set cachePerf                      -- Begin cache performance monitoring
     set calibration                    -- Set Calibration Period
     set cckTrigHigh                    -- Set Higher Trigger Threshold for CCK Phy Errors For ANI Control
     set cckTrigLow                     -- Set Lower Trigger Threshold for CCK Phy Errors For ANI Control
     set cckWeakSigThr                  -- Set ANI Parameter for CCK Weak Signal Detection Threshold
     set channel                        -- Set Radio Channel
     set cipher                         -- Set Cipher
     set compproc                       -- Set Compression Scheme
     set compwinsize                    -- Set Compression Window Size
     set countrycode                    -- Set Country Code
     set ctsmode                        -- Set CTS Mode
     set ctsrate                        -- Set CTS Rate
     set ctstype                        -- Set CTS Type
     set domainsuffix                   -- Set Domain Name Server Suffix
     set dtim                           -- Set Data Beacon Rate (DTIM)
     set dhcp                           -- Set DHCP Mode
     set enableANI                      -- Turn Adaptive Noise Immunity Control On/Off
     set encryption                     -- Set Encryption Mode
     set extendedchanmode               -- Set Extended Channel Mode
     set factorydefault                 -- Restore to Default Factory Settings
     set firStepLvl                     -- Set ANI Parameter for FirStepLevel
     set fragmentthreshold              -- Set Fragment Threshold
     set frequency                      -- Set Radio Frequency (MHz)
     set gateway                        -- Set Gateway IP Address
     set gbeaconrate                    -- Set 11g Beacon Rate
     set groupkeyupdate                 -- Set Group Key Update Interval (in Seconds)
     set gdraft5                        -- Set 11g Draft 5.0 compatibility
     set hostipaddr                     -- Set Host IP address
     set ipaddr                         -- Set IP Address
     set ipmask                         -- Set IP Subnet Mask
     set jsw                            -- Set Jumpstart Mode
     set jsp2Passwd                     -- Set JS-P2 password
     set key                            -- Set Encryption Key
     set keyentrymethod                 -- Select Encryption Key Entry Method
     set keysource                      -- Select Source Of Encryption Keys
     set login                          -- Modify Login User Name
     set minimumrate                    -- Set Minimum Rate
     set minimumrate                    -- Set Minimum Rate
     set minimumrate                    -- Set Minimum Rate
     set minimumrate                    -- Set Minimum Rate
     set minimumrate                    -- Set Minimum Rate
     set nameaddress                    -- Set Name Server IP address
     set noiseImmunityLvl               -- Set ANI Parameter for Noise Immunity Level
     set ofdmTrigHigh                   -- Set Higher Trigger Threshold for OFDM Phy Errors for ANI Control
     set ofdmTrigLow                    -- Set Lower Trigger Threshold for OFDM Phy Errors for ANI Control
     set ofdmWeakSigDet                 -- Set ANI Parameter for OFDM Weak Signal Detection
     set overRidetxpower                -- Set Tx power override
     set operationMode                  -- Set operation Mode
     set password                       -- Modify Password
     set passphrase                     -- Modify Passphrase
     set pktLogEnable                   -- Enable Packet Logging
     set power                          -- Set Transmit Power
     set quietAckCtsAllow               -- Allow Ack/Cts frames during quiet period
     set quietDuration                  -- Duration of quiet period
     set quietOffset                    -- Offset of quiet period into the beacon period
     set radiusname                     -- Set RADIUS name or IP address
     set radiusport                     -- Set RADIUS port number
     set radiussecret                   -- Set RADIUS shared secret
     set rate                           -- Set Data Rate
     set rate                           -- Set Data Rate
     set rate                           -- Set Data Rate
     set rate                           -- Set Data Rate
     set rate                           -- Set Data Rate
     set reg                            -- Set Register Value
     set regulatorydomain               -- Set Regulatory Domain
     set remoteAP                       -- Set Remote AP's Mac Address
     set hwtxretries                    -- Set HW Transmit Retry Limit
     set swtxretries                    -- Set SW Transmit Retry Limit
     set rtsthreshold                   -- Set RTS/CTS Threshold
     set shortpreamble                  -- Set Short Preamble
     set shortslottime                  -- Set Short Slot Time
     set sntpserver                     -- Set SNTP/NTP Server IP Address
     set softwareretry                  -- Set Software Retry
     set spurImmunityLvl                -- Set ANI Parameter for Spur Immunity Level
     set ssid                           -- Set Service Set ID
     set ssidsuppress                   -- Set SSID Suppress Mode
     set SuperG                         -- Super G Features 
     set systemname                     -- Set Access Point System Name
     set telnet                         -- Set Telnet Mode
     set timeout                        -- Set Telnet Timeout
     set tzone                          -- Set Time Zone Setting
     set updateparam                    -- Set Vendor Default Firmware Update Params
     set vlan                           -- Set VLAN Mode
     set watchdog                       -- Set Watchdog Mode
     set wds                            -- Set WDS Mode
     set webUI                          -- Set Web UI Mode
     set wep                            -- Set Encryption Mode
     set wlanstate                      -- Set wlan state
     set wirelessmode                   -- Set Wireless LAN Mode
     set wmm                            -- Set WMM Mode
     set wmmParamBss                    -- Set WMM parameters used by STAs in this BSS
     set wmmParam                       -- Set WMM parameters used by this AP
     spy report                         -- Print spy report
     spy show                           -- Print debug info
     spy start                          -- Start spy
     spy stop                           -- Stop spy
     start wlan                         -- Start the current wlan
     stop wlan                          -- Stop the current wlan
     support                            -- Print support information
     timeofday                          -- Display Current Time of Day
     v54 alg                            -- Set/show the antenna algorithm
     v54 ant                            -- Video54 Antenna Config
     v54 antreset                       -- Reset V54 TxCtrl State
     v54 rtt                            -- Real-time Telemetry output
     v54 fchan                          -- Fast Channel Change
     v54 emon                           -- Environmental Monitoring
     v54 learn                          -- Send V54 learning packets
     v54 queue                          -- Video54 Queuing Debug Info
     v54 reset                          -- Reset V54 TxCtrl State
     v54 staQueue                       -- Per-Station-Queue scheduling
     v54 staticant                      -- Configure a static antenna
     v54 staticant                      -- Configure a static antenna
     version                            -- Software version
     video classifier                   -- Classify
     video qos                          -- Quality Of Service
     video pcap                         -- Packet capture
    wlan0 -> Invalid input characters!
    wlan0 -> wlan0 -> wlan0 -> wlan0 -> wlan0 -> boot 
    Invalid input characters!
    wlan0 -> boot 
    Invalid input characters!
    wlan0 -> boot flash
    BOOT PARAM           : bootline
    IP Addrress          : 192.168.0.1:ffffff00
    Host                 : 
    Gateway              : 
    Startup script       : 
    other                : AP
    boot device          : tffs:
    unit number          : 1 
    processor number     : 0 
    file name            : /fl/apv54
    inet on ethernet (e) : 192.168.0.1:ffffff00
    flags (f)            : 0x80 
    other (o)            : AP
    wlan0 -> boot 
    Invalid input characters!
    wlan0 -> boor
    Invalid input characters!
    wlan0 -> bootrom
    Not enough parameters!
    wlan0 -> bootrom
    Not enough parameters!
    wlan0 -> help bootrom
    List of Access Point CLI commands:
     ?                                  -- Display CLI Command List
     arp add                            -- create or modify ARP table entry
     arp delete                         -- remove ARP table entry
     arp flush                          -- flush all entries in the ARP table
     arp show                           -- Display firmware information
     board change                       -- Change Board Data
     board dump                         -- Dump Board Data
     add remoteWbr                      -- Add a remote Wireless Bridge
     admin                              -- Temporary factory admin
     boot flash                         -- Boot from flash
     boot ethernet                      -- Boot from network
     boot dump                          -- dump boot line data
     cat                                -- list file
     cp                                 -- Copy file
     config wlan                        -- config wlanX
     connect bss                        -- connect to bssX
     del acl                            -- Delete Access Control List
     del key                            -- Delete Encryption key
     del remoteWbr                      -- Delete a remote Wireless Bridge
     del seed                           -- Delete Random Seed
     dis                                -- Dis-associate an End Station
     eeprom                             -- dump eeprom data
     find bss                           -- Find BSS
     find channel                       -- Find Available Channel
     find all                           -- Find All BSS
     format                             -- Format flash filesytem
     bootrom                            -- Update boot rom image
     ftp                                -- Software update via FTP
     get 11gonly                        -- Display 11g Only Allowed
     get 11goptimize                    -- Display 11g Optimization Level
     get 11goverlapbss                  -- Display Overlapping BSS Protection
     get abolt                          -- 
     get acl                            -- Display Access Control List
     get aging     ^C                     -- Display Aging Interval
     get antenna                        -- Display Antenna Diversity
     get arp                            -- Display arp Table
     get if                             -- Display attached network interfaces
     get routes     
                        -- Display routing table 
     get association                    -- Display Association Table
     get authentication          
           -- Display Authentication Type
     get autoProvision                  -- Display Auto-Provision 
    Mode
     get autochannelselect              -- Display Auto Channel Select
     get basic11b                       -- Display Basic 11b Rates
     get 
    basic11g                       -- Display Basic 11g Rates
     get beaconinterval                 -- Display Beacon Interval
     get bridgeTable                    -- Display internal SW bridge table
     get burstSeqThreshold              -- Display Max Number of frames in a Burst
     get burstTime                      -- Display Burst Time
     get cacheperf                      -- Display the cache performance counters
     get calibration                    -- Display Noise And Offset Calibration Mode
     get cckTrigHigh                    -- Display Higher Trigger Threshold for CCK Phy Errors for ANI Control
     get cckTrigLow                     -- Display Lower Trigger Threshold for CCK Phy Errors for ANI Control
     get cckWeakSigThr                  -- Display ANI Parameter for CCK Weak Signal Detection Threshold
     get channel                        -- Display Radio Channel
     get cipher                         -- Display Encryption cipher
     get compproc                       -- Display Compression scheme
     get compwinsize                    -- Display Compression Window Size
     get config                         -- Display Current AP Configuration
     get countrycode                    -- Display Country Code
     get ctsmode                        -- Display CTS mode
     get ctsrate                        -- Display CTS rate
     get ctstype                        -- Display CTS type
     get domainsuffix                   -- Display Domain Name Server suffix
     get dtim                           -- Display Data Beacon Rate (DTIM)
     get dhcp                           -- Display DHCP Client Mode
     get enableANI                      -- Display Adaptive Noise Immunity Control On/Off
     get encryption                     -- Display Encryption Mode
     get eth                            -- Display Ethernet Statistics
     get extendedchanmode               -- Display Extended Channel Mode
     get firStepLvl                     -- Display ANI Parameter for FirStepLevel
     get fragmentthreshold              -- Display Fragment Threshold
     get frequency                      -- Display Radio Frequency (MHz)
     get gateway                        -- Display Gateway IP Address
     get gbeaconrate                    -- Display 11g Beacon Rate
     get gdraft5                        -- Display 11g Draft 5.0 compatibility
     get groupkeyupdate                 -- Display Group Key Update Interval (in Seconds)
     get hardware                       -- Display Hardware Revisions
     get hostipaddr                     -- Display Host IP Address
     get ipaddr                         -- Display IP Address
     get ipmask                         -- Display IP Subnet Mask
     get jsw                            -- Display Jumpstart Mode
     get jsP2PassPhrase                 -- Display JS-P2 passphrase
     get key                            -- Display Encryption Key
     get keyentrymethod                 -- Display Encyrption Key Entry Method
     get keysource                      -- Display Source Of Encryption Keys
     get ledStatus                      -- Display current LED status
     get login                          -- Display Login User Name
     get minimumrate                    -- Display Minimum Rate
     get nameaddr                       -- Display IP address of name server
     get nf                             -- Display Noise Floor
     get noiseImmunityLvl               -- Display ANI Parameter for Noise Immunity Level
     get ofdmTrigHigh                   -- Display Higher Trigger Threshold for OFDM Phy Errors for ANI Control
     get ofdmTrigLow                    -- Display Lower Trigger Threshold for OFDM Phy Errors for ANI Control
     get ofdmWeakSigDet                 -- Display ANI Parameter for OFDM Weak Signal Detection
     get overRidetxpower                -- Display Tx power override
     get operationMode                  -- Display Operation Mode
     get passphrase                     -- Display Passphrase
     get passphrasekey                  -- Display Passphrase Key
     get perfstats                      -- Dump system performance stats
     get pnetmon                        -- NetTask profile information
     get pktLogEnable                   -- Display Packet Logging Mode
     get power                          -- Display Transmit Power Setting
     get quietAckCtsAllow               -- Display if Ack/Cts frames are allowed during quiet period
     get quietDuration                  -- Display Duration of quiet period
     get quietOffset                    -- Display Offset of quiet period into the beacon period
     get radiusname                     -- Display RADIUS server name or IP address
     get radiusport                     -- Display RADIUS port number
     get rate                           -- Display Data Rate
     get reg                            -- Display the register contents at the given offset
     get remoteAp                       -- Display Remote Ap's Mac Address
     get reset                          -- Display # of resets
     get remoteWbr                      -- Display configured Remote Wireless bridges
     get hwtxretries                    -- Display HW Transmit Retry Limit
     get swtxretries                    -- Display SW Transmit Retry Limit
     get rtsthreshold                   -- Display RTS/CTS Threshold
     get seed                           -- Display Random Seed
     get shortpreamble                  -- Display Short Preamble Usage
     get shortslottime                  -- Display Short Slot Time Usage
     get sib                            -- Display Station Information
     get sntpserver                     -- Display SNTP/NTP Server IP Address
     get softwareretry                  -- Display Software Retry
     get spurImmunityLvl                -- Display ANI Parameter for Spur Immunity Level
     get ssid                           -- Display Service Set ID
     get ssidsuppress                   -- Display SSID Suppress Mode
     get station                        -- Display Station Status
     get SuperG                         -- Display SuperG Feature Status
     get systemname                     -- Display Access Point System Name
     get telnet                         -- Display Telnet Mode
     get timeout                        -- Display Telnet Timeout
     get times                          -- Display startup times
     get tzone                          -- Display Time Zone Setting
     get updateparam                    -- Display Vendor Default Firmware Update Params
     get uptime                         -- Display UpTime
     get vlan                           -- Display VLAN Mode
     get watchdog                       -- Display Watchdog Mode
     get wds                            -- Display WDS Mode
     get webUI                          -- Display WebUI Mode
     get wep                            -- Display Encryption Mode
     get wirelessmode                   -- Display Wireless LAN Mode
     get wmm                            -- Display WMM Mode
     get wmmParamBss ac                 -- Get EDCA values for this access class
     get wmmParam ac                    -- Get EDCA values for this access class
     get wmmParam queue                 -- Get EDCA values for this HW queue
     get wlanstate                      -- Display wlan state
     help                               -- Display CLI Command List
     Lebradeb                           -- Disable reboot during radar detection
     ls                                 -- list directory
     logoff                             -- Logoff
     mem                                -- system memory statistics
     mv                                 -- Move file
     np                                 -- Network Performance
     ns                                 -- Network Performance Server
     ping                               -- Ping
     pktLog                             -- Packet Log
     radar!                             -- Simulate radar detection on current channel
     reboot                             -- Reboot Access Point
     rm                                 -- Remove file
     run                                -- Run command file
     task priority                      -- Set task priority
     task show                          -- Set task info
     task stack                         -- Set task stack info
     task resume                        -- resume task
     task suspend                       -- suspend task
     tftp                               -- Software update via TFTP
     quit                               -- Logoff
     set 11gonly disable                -- Disable 11g only allowed
     set 11gonly enable                 -- Enable 11g only allowed
     set 11goptimize                    -- Set 11g Optimization Level
     set 11goverlapbss disable          -- Disable Overlapping BSS protection
     set 11goverlapbss enable           -- Enable Overlapping BSS protection
     set abolt                          -- 
     set acl allow                      -- Add MAC address to the ACL
     set acl enable                     -- Select Restricted Access
     set acl deny                       -- Add MAC address to the disabled ACL
     set acl disable                    -- Select Unrestrict Access
     set acl keymap                     -- Add Encryption key mapping for MAC address
     set acl strict                     -- Select Restricted (w/ACL match) Access
     set aging                          -- Set Aging Interval
     set antenna best                   -- Enable antenna diversity
     set antenna 1                      -- Select antenna 1
     set antenna 2                      -- Select antenna 2
     set authentication open-system     -- Select Open-System Authentication Type
     set authentication shared-key      -- Select Shared-Key Authentication Type
     set authentication auto            -- Select auto Authentication Type
     set authentication WPA             -- Select Authentication WPA Type
     set authentication WPA-PSK         -- Select Authentication WPA-PSK Type
     set authentication WPA2            -- Select WPA2 for Authentication Type
     set authentication WPA2-PSK        -- Select WPA2-PSK for Authentication Type
     set authentication WPA-AUTO        -- Allow WPAv1 or WPAv2 for Authentication Type
     set authentication WPA-AUTO-PSK    -- Allow WPAv1-PSK or WPAv2-PSK for Authentication Type
     set autoProvision disable          -- Disable Auto-Provisioning by AP
     set autoProvision enable           -- Enable Auto-Provisioning by AP
     set autochannelselect disable      -- Disable Automatic Channel Selection
     set autochannelselect enable       -- Enable Automatic Channel Selection
     set basic11b disable               -- Disable only basic 11b rates - use all rates
     set basic11b enable                -- Enable only basic 11b rates (1, 2)
     set basic11g 11                    -- Basic Rates (1, 2)
     set basic11g 11b                   -- Basic Rates (1, 2, 5.5, 11)
     set basic11g 11g                   -- Basic Rates (1, 2, 5.5, 11, 6, 12, 24)
     set basic11g ofdm                  -- Basic Rates (6, 12, 24)
     set beaconinterval                 -- Modify Beacon Interval
     set burstSeqThreshold              -- Set Max Number of frames in a Burst
     set burstTime                      -- Set Burst Time
     set cachePerf ic                   -- i-cache performance counters
     set cachePerf dc                   -- d-cache performance counters
     set cachePerf cm                   -- i and d-cache miss  counters
     set cachePerf ch                   -- i and d-cache hit   counters
     set calibration                    -- Set Calibration Period
     set cckTrigHigh                    -- Set Higher Trigger Threshold for CCK Phy Errors For ANI Control
     set cckTrigLow                     -- Set Lower Trigger Threshold for CCK Phy Errors For ANI Control
     set cckWeakSigThr                  -- Set ANI Parameter for CCK Weak Signal Detection Threshold
     set channel                        -- Set Radio Channel
     set cipher wep                     -- Select wep
     set cipher aes                     -- Select aes
     set cipher tkip                    -- Select tkip
     set cipher auto                    -- Select cipher through negotiation
     set compproc                       -- Set Compression Scheme
     set compwinsize                    -- Set Compression Window Size
     set countrycode                    -- Set Country Code
     set ctsmode                        -- Set CTS Mode
     set ctsrate                        -- Set CTS Rate
     set ctstype                        -- Set CTS Type
     set domainsuffix                   -- Set Domain Name Server Suffix
     set dtim                           -- Set Data Beacon Rate (DTIM)
     set dhcp disable                   -- Disable DHCP
     set dhcp enable                    -- Enable DHCP
     set enableANI                      -- Turn Adaptive Noise Immunity Control On/Off
     set encryption disable             -- Disable Encryption
     set encryption enable              -- Enable Encryption
     set extendedchanmode disable       -- Disable Extended Channel Mode
     set extendedchanmode enable        -- Enable Extended Channel Mode
     set factorydefault                 -- Restore to Default Factory Settings
     set firStepLvl                     -- Set ANI Parameter for FirStepLevel
     set fragmentthreshold              -- Set Fragment Threshold
     set frequency                      -- Set Radio Frequency (MHz)
     set gateway                        -- Set Gateway IP Address
     set gbeaconrate                    -- Set 11g Beacon Rate
     set groupkeyupdate                 -- Set Group Key Update Interval (in Seconds)
     set gdraft5 disable                -- Disable 11g Draft 5.0 compatibility
     set gdraft5 enable                 -- Enable 11g Draft 5.0 compatibility
     set hostipaddr                     -- Set Host IP address
     set ipaddr                         -- Set IP Address
     set ipmask                         -- Set IP Subnet Mask
     set jsw enable                     -- Enable  Jumpstart
     set jsw disable                    -- Disable  Jumpstart
     set jsp2Passwd                     -- Set JS-P2 password
     set key default                    -- Set Default Encryption Key
     set key 40                         -- Set 40-bit Encryption Key
     set key 104                        -- Set 104-bit Encryption Key
     set key 128                        -- Set 128-bit Encryption Key
     set keyentrymethod hexadecimal     -- Key contains (0 - 9, A - F)
     set keyentrymethod asciitext       -- Key contains keyboard characters
     set keysource flash                -- All keys will be read from flash (no key derivation)
     set keysource server               -- All keys will be derived from authentication server
     set keysource mixed                -- Keys read from flash or derived from authentication server
     set login                          -- Modify Login User Name
     set minimumrate 0.25               -- Select 0.25 Mbps
     set minimumrate 0.5                -- Select 0.5 Mbps
     set minimumrate 1                  -- Select 1 Mbps
     set minimumrate 2                  -- Select 2 Mbps
     set minimumrate 3                  -- Select 3 Mbps
     set minimumrate 6                  -- Select 6 Mbps
     set minimumrate 9                  -- Select 9 Mbps
     set minimumrate 12                 -- Select 12 Mbps
     set minimumrate 18                 -- Select 18 Mbps
     set minimumrate 24                 -- Select 24 Mbps
     set minimumrate 36                 -- Select 36 Mbps
     set minimumrate 48                 -- Select 48 Mbps
     set minimumrate 54                 -- Select 54 Mbps
     set minimumrate 12                 -- Select 12 Mbps
     set minimumrate 18                 -- Select 18 Mbps
     set minimumrate 24                 -- Select 24 Mbps
     set minimumrate 36                 -- Select 36 Mbps
     set minimumrate 48                 -- Select 48 Mbps
     set minimumrate 72                 -- Select 72 Mbps
     set minimumrate 96                 -- Select 96 Mbps
     set minimumrate 108                -- Select 108 Mbps
     set minimumrate 1                  -- Select 1 Mbps
     set minimumrate 2                  -- Select 2 Mbps
     set minimumrate 5.5                -- Select 5.5 Mbps
     set minimumrate 11                 -- Select 11 Mbps
     set minimumrate 0.25               -- Select 0.25 Mbps
     set minimumrate 0.5                -- Select 0.5 Mbps
     set minimumrate 1                  -- Select 1 Mbps
     set minimumrate 2                  -- Select 2 Mbps
     set minimumrate 1x                 -- Select XR 1 Mbps
     set minimumrate 2x                 -- Select XR 2 Mbps
     set minimumrate 3                  -- Select 3 Mbps
     set minimumrate 5.5                -- Select 5.5 Mbps
     set minimumrate 11                 -- Select 11 Mbps
     set minimumrate 6                  -- Select 6 Mbps
     set minimumrate 9                  -- Select 9 Mbps
     set minimumrate 12                 -- Select 12 Mbps
     set minimumrate 18                 -- Select 18 Mbps
     set minimumrate 24                 -- Select 24 Mbps
     set minimumrate 36                 -- Select 36 Mbps
     set minimumrate 48                 -- Select 48 Mbps
     set minimumrate 54                 -- Select 54 Mbps
     set minimumrate 12                 -- Select 12 Mbps
     set minimumrate 18                 -- Select 18 Mbps
     set minimumrate 24                 -- Select 24 Mbps
     set minimumrate 36                 -- Select 36 Mbps
     set minimumrate 48                 -- Select 48 Mbps
     set minimumrate 72                 -- Select 72 Mbps
     set minimumrate 96                 -- Select 96 Mbps
     set minimumrate 108                -- Select 108 Mbps
     set nameaddress                    -- Set Name Server IP address
     set noiseImmunityLvl               -- Set ANI Parameter for Noise Immunity Level
     set ofdmTrigHigh                   -- Set Higher Trigger Threshold for OFDM Phy Errors for ANI Control
     set ofdmTrigLow                    -- Set Lower Trigger Threshold for OFDM Phy Errors for ANI Control
     set ofdmWeakSigDet                 -- Set ANI Parameter for OFDM Weak Signal Detection
     set overRidetxpower                -- Set Tx power override
     set operationMode ap               -- Operating as Access Point
     set operationMode sta              -- Operating as Wireless Client
     set operationMode wbr              -- Operating as Wireless Bridge
     set operationMode repeater         -- Operating as Wireless Repeater
     set password                       -- Modify Password
     set passphrase                     -- Modify Passphrase
     set pktLogEnable                   -- Enable Packet Logging
     set power full                     -- Set maximum (normal) transmit power
     set power half                     -- Set fractional (1/2) transmit power
     set power quarter                  -- Set fractional (1/4) transmit power
     set power eighth                   -- Set fractional (1/8) transmit power
     set power min                      -- Set minimum transmit power
     set quietAckCtsAllow               -- Allow Ack/Cts frames during quiet period
     set quietDuration                  -- Duration of quiet period
     set quietOffset                    -- Offset of quiet period into the beacon period
     set radiusname                     -- Set RADIUS name or IP address
     set radiusport                     -- Set RADIUS port number
     set radiussecret                   -- Set RADIUS shared secret
     set rate best                      -- Select best data rate
     set rate 6                         -- Select 6 Mbps
     set rate 9                         -- Select 9 Mbps
     set rate 12                        -- Select 12 Mbps
     set rate 18                        -- Select 18 Mbps
     set rate 24                        -- Select 24 Mbps
     set rate 36                        -- Select 36 Mbps
     set rate 48                        -- Select 48 Mbps
     set rate 54                        -- Select 54 Mbps
     set rate best                      -- Select best data rate
     set rate 12                        -- Select 12 Mbps
     set rate 18                        -- Select 18 Mbps
     set rate 24                        -- Select 24 Mbps
     set rate 36                        -- Select 36 Mbps
     set rate 48                        -- Select 48 Mbps
     set rate 72                        -- Select 72 Mbps
     set rate 96                        -- Select 96 Mbps
     set rate 108                       -- Select 108 Mbps
     set rate best                      -- Select best data rate
     set rate 1                         -- Select 1 Mbps
     set rate 2                         -- Select 2 Mbps
     set rate 5.5                       -- Select 5.5 Mbps
     set rate 11                        -- Select 11 Mbps
     set rate best                      -- Select best data rate
     set rate 1                         -- Select 1 Mbps
     set rate 2                         -- Select 2 Mbps
     set rate 5.5                       -- Select 5.5 Mbps
     set rate 11                        -- Select 11 Mbps
     set rate 6                         -- Select 6 Mbps
     set rate 9                         -- Select 9 Mbps
     set rate 12                        -- Select 12 Mbps
     set rate 18                        -- Select 18 Mbps
     set rate 24                        -- Select 24 Mbps
     set rate 36                        -- Select 36 Mbps
     set rate 48                        -- Select 48 Mbps
     set rate 54                        -- Select 54 Mbps
     set rate best                      -- Select best data rate
     set rate 12                        -- Select 12 Mbps
     set rate 18                        -- Select 18 Mbps
     set rate 24                        -- Select 24 Mbps
     set rate 36                        -- Select 36 Mbps
     set rate 48                        -- Select 48 Mbps
     set rate 72                        -- Select 72 Mbps
     set rate 96                        -- Select 96 Mbps
     set rate 108                       -- Select 108 Mbps
     set reg                            -- Set Register Value
     set regulatorydomain               -- Set Regulatory Domain
     set remoteAP                       -- Set Remote AP's Mac Address
     set hwtxretries                    -- Set HW Transmit Retry Limit
     set swtxretries                    -- Set SW Transmit Retry Limit
     set rtsthreshold                   -- Set RTS/CTS Threshold
     set shortpreamble disable          -- Disable Short Preamble (use only long)
     set shortpreamble enable           -- Enable Short and Long Preamble
     set shortslottime disable          -- Disable Short Slot Time (use only long)
     set shortslottime enable           -- Enable Short Slot Time
     set sntpserver                     -- Set SNTP/NTP Server IP Address
     set softwareretry enable           -- Enable Software Retry
     set softwareretry disable          -- Disable Software Retry
     set spurImmunityLvl                -- Set ANI Parameter for Spur Immunity Level
     set ssid                           -- Set Service Set ID
     set ssidsuppress enable            -- Enable SSID suppress mode
     set ssidsuppress disable           -- Disable SSID suppress mode
     set SuperG enable                  -- Enable SuperG Features
     set SuperG disable                 -- Disable SuperG Features
     set systemname                     -- Set Access Point System Name
     set telnet disable                 -- Disable Telnet access
     set telnet enable                  -- Enable Telnet access
     set timeout                        -- Set Telnet Timeout
     set tzone                          -- Set Time Zone Setting
     set updateparam                    -- Set Vendor Default Firmware Update Params
     set vlan disable                   -- Disable VLAN
     set vlan enable                    -- Enable VLAN
     set watchdog disable               -- Disable Watchdog
     set watchdog enable                -- Enable Watchdog
     set wds disable                    -- Disable WDS support
     set wds enable                     -- Enable WDS support
     set webUI disable                  -- Disable Web UI
     set webUI enable                   -- Enable Web UI
     set wep disable                    -- Disable Encryption
     set wep enable                     -- Enable Encryption
     set wlanstate disable              -- Disable wlan
     set wlanstate enable               -- Enable wlan
     set wirelessmode 11a               -- 802.11a
     set wirelessmode 11b               -- 802.11b
     set wirelessmode 11g               -- 802.11g
     set wirelessmode 108g static       -- 802.11g Static Turbo
     set wirelessmode 108g dynamic      -- 802.11g Dynamic Turbo
     set wirelessmode turbo static      -- 802.11a Static Turbo
     set wirelessmode turbo dynamic     -- 802.11a Dynamic Turbo
     set wmm disable                    -- Disable WMM
     set wmm enable                     -- Enable WMM
     set wmmParamBss ac                 -- Set EDCA values for all access classes
     set wmmParam ac                    -- Set EDCA values for all access classes
     set wmmParam queue                 -- Set EDCA values for all HW queues
     spy report                         -- Print spy report
     spy show                           -- Print debug info
     spy start                          -- Start spy
     spy stop                           -- Stop spy
     start wlan                         -- Start the current wlan
     stop wlan                          -- Stop the current wlan
     support                            -- Print support information
     timeofday                          -- Display Current Time of Day
     v54 alg                            -- Set/show the antenna algorithm
     v54 ant                            -- Video54 Antenna Config
     v54 antreset                       -- Reset V54 TxCtrl State
     v54 rtt                            -- Real-time Telemetry output
     v54 fchan                          -- Fast Channel Change
     v54 emon rx disable                -- Disable Rx stats gathering
     v54 emon rx enable                 -- Enable  Rx stats gathering
     v54 emon tx disable                -- Disable Tx stats gathering
     v54 emon tx enable                 -- Enable  Tx stats gathering
     v54 emon output disable            -- Disable emon periodic output
     v54 emon output enable             -- Enable  emon periodic output
     v54 emon dump second               -- Dump per-second stats history
     v54 emon dump minute               -- Dump per-minute stats history
     v54 emon dump hour                 -- Dump per-hour   stats history
     v54 learn                          -- Send V54 learning packets
     v54 queue                          -- Video54 Queuing Debug Info
     v54 reset                          -- Reset V54 TxCtrl State
     v54 staQueue clear                 -- Reset PSQ statistics counters
     v54 staQueue disable               -- Disable Per-Station-Queue scheduling
     v54 staQueue enable                -- Enable Per-Station-Queue scheduling
     v54 staQueue hires disable         -- Disable using Hi-Res Clock
     v54 staQueue hires enable          -- Enable using Hi-Res Clock
     v54 staQueue priorityAdjust        -- PSQ priority-adjust factor
     v54 staQueue queueLimit            -- PSQ per-station max queue size
     v54 staQueue show                  -- Display PSQ statistics
     v54 staticant                      -- Configure a static antenna
     v54 staticant                      -- Configure a static antenna
     version                            -- Software version
     video classifier actions tos disable -- Disable TOS marking
     video classifier actions tos enable -- Enable TOS marking
     video classifier actions tos video -- Set Video TOS value
     video classifier actions tos voIP  -- Set VoIP TOS value
     video classifier both dbmcast disable -- Disable Directed Bcast/Mcast Feature
     video classifier both dbmcast enable -- Enable Directed Bcast/Mcast Feature
     video classifier both disable      -- Disable Classification on Interface
     video classifier both enable       -- Enable Classification on Interface
     video classifier both igmp disable -- Disable IGMP Snooping
     video classifier both igmp enable  -- Enable IGMP Snooping
     video classifier both port add tcp dest tos video -- Mark TOS with video value
     video classifier both port add tcp dest tos voice -- Mark TOS with voice value
     video classifier both port add tcp dest drop -- Drop packet
     video classifier both port add tcp dest pcap -- Capture packet
     video classifier both port add tcp dst tos video -- Mark TOS with video value
     video classifier both port add tcp dst tos voice -- Mark TOS with voice value
     video classifier both port add tcp dst drop -- Drop packet
     video classifier both port add tcp dst pcap -- Capture packet
     video classifier both port add tcp src tos video -- Mark TOS with video value
     video classifier both port add tcp src tos voice -- Mark TOS with voice value
     video classifier both port add tcp src drop -- Drop packet
     video classifier both port add tcp src pcap -- Capture packet
     video classifier both port add udp dest tos video -- Mark TOS with video value
     video classifier both port add udp dest tos voice -- Mark TOS with voice value
     video classifier both port add udp dest drop -- Drop packet
     video classifier both port add udp dest pcap -- Capture packet
     video classifier both port add udp dst tos video -- Mark TOS with video value
     video classifier both port add udp dst tos voice -- Mark TOS with voice value
     video classifier both port add udp dst drop -- Drop packet
     video classifier both port add udp dst pcap -- Capture packet
     video classifier both port add udp src tos video -- Mark TOS with video value
     video classifier both port add udp src tos voice -- Mark TOS with voice value
     video classifier both port add udp src drop -- Drop packet
     video classifier both port add udp src pcap -- Capture packet
     video classifier both port delete tcp dest tos video -- Mark TOS with video value
     video classifier both port delete tcp dest tos voice -- Mark TOS with voice value
     video classifier both port delete tcp dest drop -- Drop packet
     video classifier both port delete tcp dest pcap -- Capture packet
     video classifier both port delete tcp dst tos video -- Mark TOS with video value
     video classifier both port delete tcp dst tos voice -- Mark TOS with voice value
     video classifier both port delete tcp dst drop -- Drop packet
     video classifier both port delete tcp dst pcap -- Capture packet
     video classifier both port delete tcp src tos video -- Mark TOS with video value
     video classifier both port delete tcp src tos voice -- Mark TOS with voice value
     video classifier both port delete tcp src drop -- Drop packet
     video classifier both port delete tcp src pcap -- Capture packet
     video classifier both port delete udp dest tos video -- Mark TOS with video value
     video classifier both port delete udp dest tos voice -- Mark TOS with voice value
     video classifier both port delete udp dest drop -- Drop packet
     video classifier both port delete udp dest pcap -- Capture packet
     video classifier both port delete udp dst tos video -- Mark TOS with video value
     video classifier both port delete udp dst tos voice -- Mark TOS with voice value
     video classifier both port delete udp dst drop -- Drop packet
     video classifier both port delete udp dst pcap -- Capture packet
     video classifier both port delete udp src tos video -- Mark TOS with video value
     video classifier both port delete udp src tos voice -- Mark TOS with voice value
     video classifier both port delete udp src drop -- Drop packet
     video classifier both port delete udp src pcap -- Capture packet
     video classifier both port disable -- Disable port classification Mode
     video classifier both port enable  -- Enable port classification Mode
     video classifier both port show    -- Show current L4 port filters
     video classifier both show         -- Show Classification Info
     video classifier both nonzero disable -- Disable Non-zero TOS marking
     video classifier both nonzero enable -- Enable Non-zero TOS marking
     video classifier both unkMcast disable -- Disable Unknown Mcast Drop
     video classifier both unkMcast enable -- Enable Unknown Mcast Drop
     video classifier both upnp disable -- Disable UPnP Processing
     video classifier both upnp enable  -- Enable UPnP Processing
     video classifier ethernet dbmcast disable -- Disable Directed Bcast/Mcast Feature
     video classifier ethernet dbmcast enable -- Enable Directed Bcast/Mcast Feature
     video classifier ethernet disable  -- Disable Classification on Interface
     video classifier ethernet enable   -- Enable Classification on Interface
     video classifier ethernet igmp disable -- Disable IGMP Snooping
     video classifier ethernet igmp enable -- Enable IGMP Snooping
     video classifier ethernet port add tcp dest tos video -- Mark TOS with video value
     video classifier ethernet port add tcp dest tos voice -- Mark TOS with voice value
     video classifier ethernet port add tcp dest drop -- Drop packet
     video classifier ethernet port add tcp dest pcap -- Capture packet
     video classifier ethernet port add tcp dst tos video -- Mark TOS with video value
     video classifier ethernet port add tcp dst tos voice -- Mark TOS with voice value
     video classifier ethernet port add tcp dst drop -- Drop packet
     video classifier ethernet port add tcp dst pcap -- Capture packet
     video classifier ethernet port add tcp src tos video -- Mark TOS with video value
     video classifier ethernet port add tcp src tos voice -- Mark TOS with voice value
     video classifier ethernet port add tcp src drop -- Drop packet
     video classifier ethernet port add tcp src pcap -- Capture packet
     video classifier ethernet port add udp dest tos video -- Mark TOS with video value
     video classifier ethernet port add udp dest tos voice -- Mark TOS with voice value
     video classifier ethernet port add udp dest drop -- Drop packet
     video classifier ethernet port add udp dest pcap -- Capture packet
     video classifier ethernet port add udp dst tos video -- Mark TOS with video value
     video classifier ethernet port add udp dst tos voice -- Mark TOS with voice value
     video classifier ethernet port add udp dst drop -- Drop packet
     video classifier ethernet port add udp dst pcap -- Capture packet
     video classifier ethernet port add udp src tos video -- Mark TOS with video value
     video classifier ethernet port add udp src tos voice -- Mark TOS with voice value
     video classifier ethernet port add udp src drop -- Drop packet
     video classifier ethernet port add udp src pcap -- Capture packet
     video classifier ethernet port delete tcp dest tos video -- Mark TOS with video value
     video classifier ethernet port delete tcp dest tos voice -- Mark TOS with voice value
     video classifier ethernet port delete tcp dest drop -- Drop packet
     video classifier ethernet port delete tcp dest pcap -- Capture packet
     video classifier ethernet port delete tcp dst tos video -- Mark TOS with video value
     video classifier ethernet port delete tcp dst tos voice -- Mark TOS with voice value
     video classifier ethernet port delete tcp dst drop -- Drop packet
     video classifier ethernet port delete tcp dst pcap -- Capture packet
     video classifier ethernet port delete tcp src tos video -- Mark TOS with video value
     video classifier ethernet port delete tcp src tos voice -- Mark TOS with voice value
     video classifier ethernet port delete tcp src drop -- Drop packet
     video classifier ethernet port delete tcp src pcap -- Capture packet
     video classifier ethernet port delete udp dest tos video -- Mark TOS with video value
     video classifier ethernet port delete udp dest tos voice -- Mark TOS with voice value
     video classifier ethernet port delete udp dest drop -- Drop packet
     video classifier ethernet port delete udp dest pcap -- Capture packet
     video classifier ethernet port delete udp dst tos video -- Mark TOS with video value
     video classifier ethernet port delete udp dst tos voice -- Mark TOS with voice value
     video classifier ethernet port delete udp dst drop -- Drop packet
     video classifier ethernet port delete udp dst pcap -- Capture packet
     video classifier ethernet port delete udp src tos video -- Mark TOS with video value
     video classifier ethernet port delete udp src tos voice -- Mark TOS with voice value
     video classifier ethernet port delete udp src drop -- Drop packet
     video classifier ethernet port delete udp src pcap -- Capture packet
     video classifier ethernet port disable -- Disable port classification Mode
     video classifier ethernet port enable -- Enable port classification Mode
     video classifier ethernet port show -- Show current L4 port filters
     video classifier ethernet show     -- Show Classification Info
     video classifier ethernet nonzero disable -- Disable Non-zero TOS marking
     video classifier ethernet nonzero enable -- Enable Non-zero TOS marking
     video classifier ethernet unkMcast disable -- Disable Unknown Mcast Drop
     video classifier ethernet unkMcast enable -- Enable Unknown Mcast Drop
     video classifier ethernet upnp disable -- Disable UPnP Processing
     video classifier ethernet upnp enable -- Enable UPnP Processing
     video classifier wireless dbmcast disable -- Disable Directed Bcast/Mcast Feature
     video classifier wireless dbmcast enable -- Enable Directed Bcast/Mcast Feature
     video classifier wireless disable  -- Disable Classification on Interface
     video classifier wireless enable   -- Enable Classification on Interface
     video classifier wireless igmp disable -- Disable IGMP Snooping
     video classifier wireless igmp enable -- Enable IGMP Snooping
     video classifier wireless port add tcp dest tos video -- Mark TOS with video value
     video classifier wireless port add tcp dest tos voice -- Mark TOS with voice value
     video classifier wireless port add tcp dest drop -- Drop packet
     video classifier wireless port add tcp dest pcap -- Capture packet
     video classifier wireless port add tcp dst tos video -- Mark TOS with video value
     video classifier wireless port add tcp dst tos voice -- Mark TOS with voice value
     video classifier wireless port add tcp dst drop -- Drop packet
     video classifier wireless port add tcp dst pcap -- Capture packet
     video classifier wireless port add tcp src tos video -- Mark TOS with video value
     video classifier wireless port add tcp src tos voice -- Mark TOS with voice value
     video classifier wireless port add tcp src drop -- Drop packet
     video classifier wireless port add tcp src pcap -- Capture packet
     video classifier wireless port add udp dest tos video -- Mark TOS with video value
     video classifier wireless port add udp dest tos voice -- Mark TOS with voice value
     video classifier wireless port add udp dest drop -- Drop packet
     video classifier wireless port add udp dest pcap -- Capture packet
     video classifier wireless port add udp dst tos video -- Mark TOS with video value
     video classifier wireless port add udp dst tos voice -- Mark TOS with voice value
     video classifier wireless port add udp dst drop -- Drop packet
     video classifier wireless port add udp dst pcap -- Capture packet
     video classifier wireless port add udp src tos video -- Mark TOS with video value
     video classifier wireless port add udp src tos voice -- Mark TOS with voice value
     video classifier wireless port add udp src drop -- Drop packet
     video classifier wireless port add udp src pcap -- Capture packet
     video classifier wireless port delete tcp dest tos video -- Mark TOS with video value
     video classifier wireless port delete tcp dest tos voice -- Mark TOS with voice value
     video classifier wireless port delete tcp dest drop -- Drop packet
     video classifier wireless port delete tcp dest pcap -- Capture packet
     video classifier wireless port delete tcp dst tos video -- Mark TOS with video value
     video classifier wireless port delete tcp dst tos voice -- Mark TOS with voice value
     video classifier wireless port delete tcp dst drop -- Drop packet
     video classifier wireless port delete tcp dst pcap -- Capture packet
     video classifier wireless port delete tcp src tos video -- Mark TOS with video value
     video classifier wireless port delete tcp src tos voice -- Mark TOS with voice value
     video classifier wireless port delete tcp src drop -- Drop packet
     video classifier wireless port delete tcp src pcap -- Capture packet
     video classifier wireless port delete udp dest tos video -- Mark TOS with video value
     video classifier wireless port delete udp dest tos voice -- Mark TOS with voice value
     video classifier wireless port delete udp dest drop -- Drop packet
     video classifier wireless port delete udp dest pcap -- Capture packet
     video classifier wireless port delete udp dst tos video -- Mark TOS with video value
     video classifier wireless port delete udp dst tos voice -- Mark TOS with voice value
     video classifier wireless port delete udp dst drop -- Drop packet
     video classifier wireless port delete udp dst pcap -- Capture packet
     video classifier wireless port delete udp src tos video -- Mark TOS with video value
     video classifier wireless port delete udp src tos voice -- Mark TOS with voice value
     video classifier wireless port delete udp src drop -- Drop packet
     video classifier wireless port delete udp src pcap -- Capture packet
     video classifier wireless port disable -- Disable port classification Mode
     video classifier wireless port enable -- Enable port classification Mode
     video classifier wireless port show -- Show current L4 port filters
     video classifier wireless show     -- Show Classification Info
     video classifier wireless nonzero disable -- Disable Non-zero TOS marking
     video classifier wireless nonzero enable -- Enable Non-zero TOS marking
     video classifier wireless unkMcast disable -- Disable Unknown Mcast Drop
     video classifier wireless unkMcast enable -- Enable Unknown Mcast Drop
     video classifier wireless upnp disable -- Disable UPnP Processing
     video classifier wireless upnp enable -- Enable UPnP Processing
     video qos disable                  -- Disable QOS Features
     video qos enable                   -- Enable QOS Features
     video qos mgtAcl disable           -- Disable MgtACL Feature
     video qos mgtAcl enable            -- Enable MgtACL Feature
     video qos show                     -- Display QOS state
     video qos txFail                   -- Set Tx Failure Threshold
     video pcap start                   -- Start capture
     video pcap continue                -- continue capture
     video pcap stop                    -- Stop capture
     video pcap save                    -- Save capture
     video pcap set                     -- Set options
     video pcap show                    -- Display capture status
    wlan0 -> Invalid input characters!
    wlan0 -> wlan0 -> wlan0 -> wlan0 -> wlan0 ->
