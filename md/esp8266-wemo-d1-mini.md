# ESPEasy


## Flashing


Inside ESPEasy_R78.zip (<http://www.esp8266.nu/downloads/ESPEasy_R78.zip>  ), there is some Windows CMD script to flash the device:


    zoobab@sabayonx86-64 /home/zoobab/soft/espeasy [153]$ l
    total 2192
    -rw-r--r-- 1 zoobab users 1061028 Feb 13 10:12 ESPEasy_R78.zip
    -rw-r--r-- 1 zoobab users  375904 Feb  6 13:07 ESPEasy_R78_1024.bin
    -rw-r--r-- 1 zoobab users  375904 Feb  6 13:09 ESPEasy_R78_4096.bin
    -rw-r--r-- 1 zoobab users  375904 Feb  6 13:03 ESPEasy_R78_512.bin
    drwxr-xr-x 4 zoobab users    4096 Mar 23 15:20 Source
    -rw-r--r-- 1 zoobab users   38926 Aug  1  2015 esptool.exe
    -rw-r--r-- 1 zoobab users     373 Jan 24 13:54 flash.cmd
    zoobab@sabayonx86-64 /home/zoobab/soft/espeasy [154]$ cat flash.cmd 
    @echo off
    set /p comport= Comport (example 3, 4, ..)           :
    set /p fsize= Flash Size (example 512, 1024, 4096) :
    set /p build= Build (example 71, 72, ..)           :
    
    echo Using com port: %comport%
    echo Using bin file: ESPEasy_R%build%_%fsize%.bin
    
    esptool.exe -vv -cd nodemcu -cb 115200 -cp COM%comport% -ca 0x00000 -cf ESPEasy_R%build%_%fsize%.bin
    
    pause
    zoobab@sabayonx86-64 /home/zoobab/soft/espeasy [155]$


I then try to flash it with the python version of it on Linux:


    zoobab@sabayonx86-64 /home/zoobab/soft/espeasy [138]$ sudo esptool.py --port /dev/ttyUSB0 --baud 460880 write_flash 0x00000 ESPEasy_R78_4096.bin 
    Connecting...
    Erasing flash...
    Wrote 376832 bytes at 0x00000000 in 10.8 seconds (278.6 kbit/s)...
    
    Leaving...
    zoobab@sabayonx86-64 /home/zoobab/soft/espeasy [139]$


Then I got those errors:


    ets Jan  8 2013,rst cause:2, boot mode:(3,7)
    
    load 0x4010f000, len 1264, room 16 
    tail 0
    chksum 0x42
    csum 0x42
    ~ld
       ªU
         PID:1396788294
    Version:1394621000
    INIT : Incorrect PID or version!
    RESET: Reboot count: 3
    FLASH: Erase Sector: 92
    FLASH: Erase Sector: 93
    FLASH: Erase Sector: 94
    FLASH: Erase Sector: 95
    FLASH: Erase Sector: 96
    FLASH: Erase Sector: 97
    FLASH: Erase Sector: 98
    FLASH: Erase Sector: 99
    FLASH: Erase Sector: 100
    FLASH: Erase Sector: 101
    FLASH: Erase Sector: 102
    FLASH: Erase Sector: 103
    FLASH: Erase Sector: 104
    FLASH: Erase Sector: 105
    FLASH: Erase Sector: 106
    FLASH: Erase Sector: 107
    FLASH: Erase Sector: 108
    FLASH: Erase Sector: 109
    FLASH: Erase Sector: 110
    FLASH: Erase Sector: 111
    FLASH: Erase Sector: 112
    FLASH: Erase Sector: 113
    FLASH: Erase Sector: 114
    FLASH: Erase Sector: 115
    FLASH: Erase Sector: 116
    FLASH: Erase Sector: 117
    FLASH: Erase Sector: 118
    FLASH: Erase Sector: 119
    FLASH: Erase Sector: 120
    FLASH: Erase Sector: 121
    FLASH: Erase Sector: 122
    FLASH: Erase Sector: 123
    FLASH: Erase Sector: 124
    FLASH: Erase Sector: 125
    FLASH: Erase Sector: 126
    FLASH: Erase Sector: 127
    FLASH: Settings saved
    FLASH: Settings saved
    
     ets Jan  8 2013,rst cause:2, boot mode:(3,7)
    
    load 0x4010f000, len 1264, room 16 
    tail 0
    chksum 0x42
    csum 0x42
    ~ld
       ªU
         PID:1396788294
    Version:1394621000
    INIT : Incorrect PID or version!
    RESET: Reboot count: 4
    RESET: To many reset attempts
    Entered Rescue mode!


And then this one:


    Version:1073696274
    INIT : Incorrect PID or version!
    RESET: Reboot count: 4
    RESET: To many reset attempts
    Entered Rescue mode!
    {dl|
        là|däc|ìsc
                  b
                   ûoolggãìbp
                             lsd{dxògà$cnã|$cónnçd
                                                  l`o
                                                     l`gsol`snl`ügªU
                                                                    PID:0
    Version:1073696274
    INIT : Incorrect PID or version!
    RESET: Reboot count: 4
    RESET: To many reset attempts
    Entered Rescue mode!
