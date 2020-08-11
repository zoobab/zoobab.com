

# How to use the Asus EEEPC as a Desktop machine with an external screen


You have to connect a USB keyboard and mouses, and an external screen. The default Xandros application:

[[=image eeepc-external-screen.png]]

does not support resolutions other then 800x600 and 1024x768. My external LCD screen nevertheless supports 1280x1024. Just change the file (in root mode) /etc/X11/xorg.conf like this (basically I replaced 1024 768 in the XXX section by 1280 1024):


    Section "Screen"
            Identifier "Screen1"
            Device     "Device1"
            Monitor    "Monitor1"
            DefaultDepth     16
            SubSection "Display"
                    Depth     8
                    Virtual  1280 1024
            EndSubSection
            SubSection "Display"
                    Depth     15
                    Virtual  1280 1024
            EndSubSection
            SubSection "Display"
                    Depth     16
                    Virtual  1280 1024
            EndSubSection
            SubSection "Display"
                    Depth     24
                    Virtual  1280 1024
            EndSubSection
    EndSection


First, obtain a shell by typing ctrl+alt+t.
Second, be root by typing "sudo bash":

>  /home/user> sudo bash
> asus-1439342445:/home/user>
> asus-1439342445:/home/user> whoami
> root
> asus-1439342445:/home/user>

Third, make a backup of your original xorg.conf config file:

> asus-1439342445:/home/user> cp /etc/X11/xorg.conf /etc/X11/xorg.conf.bak

Fourth, assure you have a root shell on the machine via SSH on another machine in case it fails ():

Fifth, copy my config file (Warning: this config file is for an EEEPC 900 with a 9 inches screen) to your machine:

> asus-1439342445:/home/user> wget <http://zoobab.wikidot.com/file>   -O out.conf

Next step is to install eeeXubuntu on a SD card only as a live distribution. And maybe port OpenWRT and see how to optimise the kernel and other apps for an embedded in order to save battery.

# How to burn the content of a directory on a CD


> mkisofs -joliet -volid volumename /home/zoobab/2burn | cdrecord -v -eject dev=ATAPI:/dev/cdrom speed=20 -data -;

# Howto tunnel when email port 25 is blocked by your ISP


You have to use port 2525 on your localhost 127.0.0.1:

> ssh -N -L2525:vic.ffii.org:25 zoobab@vic.ffii.org

Works for me:

> zoobab@freeman /home/zoobab [1]$ telnet 127.0.0.1 2525
> Trying 127.0.0.1...
> Connected to 127.0.0.1.
> Escape character is '^]'.
> 220 vic.ffii.org ESMTP Exim 4.63 Fri, 18 Apr 2008 15:11:41 +0200

Point your email client to 2525 and it is done. You can also use port 25 on localhost if you don't have any MTA like Exim or postfix running:

> ssh -N -L25:vic.ffii.org:25 zoobab@vic.ffii.org

# How to backup a Palm Zire 31 with pilot-link


> root@freeman /home/zoobab [30]# lsusb
> Bus 003 Device 001: ID 0000:0000
> Bus 002 Device 001: ID 0000:0000
> Bus 001 Device 016: ID 0830:0061 Palm, Inc.

Then install pilot-link:

> root@freeman /home/zoobab [31]# apt-get install pilot-link

Then backup your files, and push the HostSync button:

> pilot-xfer -p usb:0830:0061 -b pilot/
>    Listening for incoming connection on usb:0830:0061... connected!
> 
>    [+][1   ][PAdd] Backing up 'ContactsDB-PAdd', 4666 bytes, 4 KiB...
>    [+][2   ][PDat] Backing up 'CalendarDB-PDat', 378 bytes, 4 KiB...
>    [+][3   ][PMem] Backing up 'MemosDB-PMem', 1727 bytes, 6 KiB...
>    [+][4   ][PTod] Backing up 'TasksDB-PTod', 820 bytes, 7 KiB...
>    [+][5   ][QRYS] Backing up 'Queries', 746 bytes, 8 KiB...
>    [+][6   ][addr] Backing up 'AddressDB', 1870 bytes, 9 KiB...
>    [+][7   ][date] Backing up 'DatebookDB', 360 bytes, 10 KiB...
>    [+][8   ][locL] Backing up 'locLDefLocationDB', 2990 bytes, 13 KiB...
>    [+][9   ][memo] Backing up 'MemoDB', 1709 bytes, 14 KiB...
>    [-][skip][modm] Skipping OS file 'ConnectionMgr50DB'.
>    [+][10  ][netw] Backing up 'NetworkDB', 441 bytes, 15 KiB...
>    [+][11  ][npad] Backing up 'npadDB', 3066 bytes, 18 KiB...
>    [+][12  ][pdmE] Backing up 'PIMsSupportStatus-pdmE'
>    [-][fail][pdmE] Failed, unable to retrieve 'PIMsSupportStatus-pdmE' from the Palm.
>    [+][13  ][todo] Backing up 'ToDoDB', 799 bytes, 19 KiB...
>    [+][14  ][locL] Backing up 'locLCusLocationDB', 301 bytes, 19 KiB...
>    [-][skip][a68k] Skipping OS file 'DynDevInfo-DDIR_appl_a68k'.
>    [-][skip][a68k] Skipping OS file 'Display-Dply_appl_a68k'.
>    [+][15  ][Foto] Backing up '4.jpg', 6486 bytes, 25 KiB...
>    [+][16  ][Foto] Backing up '3.jpg', 6531 bytes, 32 KiB...
>    [+][17  ][Foto] Backing up '2.jpg', 6066 bytes, 38 KiB...
>    [+][18  ][Foto] Backing up '1.jpg', 1818 bytes, 39 KiB...
>    [+][19  ][Foto] Backing up 'PhotosDB-Foto', 11304 bytes, 50 KiB...
>    [-][skip][a68k] Skipping OS file 'Photos-Foto_appl_a68k'.
>    [-][skip][a68k] Skipping OS file 'GoLCD-GAny_panl_a68k'.
>    [-][skip][a68k] Skipping OS file 'Keylock_KEYL_panl_a68k'.
>    [-][skip][a68k] Skipping OS file 'Contacts-PAdd_appl_a68k'.
>    [-][skip][a68k] Skipping OS file 'Calendar-PDat_appl_a68k'.
>    [-][skip][a68k] Skipping OS file 'Memos-PMem_appl_a68k'.
>    [-][skip][a68k] Skipping OS file 'Tasks-PTod_appl_a68k'.
>    [-][skip][a68k] Skipping OS file 'Clock-PcLK_appl_a68k'.
>    [-][skip][a68k] Skipping OS file 'Power_Powr_panl_a68k'.
>    [-][skip][a68k] Skipping OS file 'Quick Tour_QKTR_appl_a68k'.
>    [-][skip][a68k] Skipping OS file 'QueriesApp_QRYS_appl_a68k'.
>    [-][skip][a68k] Skipping OS file 'RealOne_RNWK_appl_a68k'.
>    [-][skip][a68k] Skipping OS file 'SoundsAlert_SdAl_panl_a68k'.
>    [-][skip][a68k] Skipping OS file 'TattooArtist_TTOO_appl_a68k'.
>    [-][skip][a68k] Skipping OS file 'PACE Data Store Reserve'.
>    [-][skip][a68k] Skipping OS file 'Address Book_addr_appl_a68k'.
>    [+][20  ][PAdd] Backing up 'ContactsBDIndex-PAdd', 4472 bytes, 55 KiB...
>    [-][skip][a68k] Skipping OS file 'Buttons_bttn_panl_a68k'.
>    [-][skip][a68k] Skipping OS file 'Calculator_calc_appl_a68k'.
>    [-][skip][a68k] Skipping OS file 'Card Info_cinf_appl_a68k'.
>    [+][21  ][addr] Backing up 'AddressCitiesDB', 80 bytes, 55 KiB...
>    [+][22  ][addr] Backing up 'AddressCompaniesDB', 80 bytes, 55 KiB...
>    [+][23  ][addr] Backing up 'AddressCountriesDB', 80 bytes, 55 KiB...
>    [-][skip][a68k] Skipping OS file 'ColorTheme-colP_panl_a68k'.
>    [-][skip][a68k] Skipping OS file 'Date Book_date_appl_a68k'.
>    [-][skip][a68k] Skipping OS file 'Digitizer_digi_panl_a68k'.
>    [-][skip][a68k] Skipping OS file 'Date & Time_dttm_panl_a68k'.
>    [-][skip][a68k] Skipping OS file 'Expense_exps_appl_a68k'.
>    [-][skip][a68k] Skipping OS file 'Formats_frmt_panl_a68k'.
>    [-][skip][a68k] Skipping OS file 'Graffiti 2 Prefs_grfp_panl_a68k'.
>    [-][skip][a68k] Skipping OS file 'Launcher_lnch_appl_a68k'.
>    [+][24  ][psys] Backing up 'psysLaunchDB', 69792 bytes, 123 KiB...
>    [-][skip][a68k] Skipping OS file 'Language Picker_lpkr_appl_a68k'.
>    [+][25  ][graf] Backing up 'Graffiti ShortCuts', 462 bytes, 124 KiB...
>    [-][skip][a68k] Skipping OS file 'Memo Pad_memo_appl_a68k'.
>    [-][skip][a68k] Skipping OS file 'Connection_modm_panl_a68k'.
>    [-][skip][a68k] Skipping OS file 'Network_netw_panl_a68k'.
>    [-][skip][a68k] Skipping OS file 'Note Pad_npad_appl_a68k'.
>    [-][skip][a68k] Skipping OS file 'Owner_ownr_panl_a68k'.
>    [-][skip][a68k] Skipping OS file 'HiddenPIMsSupport-pdmE_appl_a68'.
>    [-][skip][a68k] Skipping OS file 'Preferences_pref_appl_a68k'.
>    [-][unsv] Skipping 'Unsaved Preferences'
>    [+][26  ][netl] Backing up 'Net Prefs', 1068 bytes, 125 KiB...
>    [-][skip][a68k] Skipping OS file 'Security_scrt_panl_a68k'.
>    [-][skip][a68k] Skipping OS file 'Setup_setp_appl_a68k'.
>    [-][skip][a68k] Skipping OS file 'ShortCuts_shct_panl_a68k'.
>    [+][27  ][psys] Backing up 'MIDI-Systemsignale', 990 bytes, 126 KiB...
>    [-][skip][a68k] Skipping OS file 'Splash-splZ_appl_a68k'.
>    [+][28  ][psys] Backing up 'Saved Preferences', 1485 bytes, 127 KiB...
>    [+][29  ][addr] Backing up 'AddressStatesDB', 80 bytes, 127 KiB...
>    [+][30  ][addr] Backing up 'AddressTitlesDB', 80 bytes, 127 KiB...
>    [-][skip][a68k] Skipping OS file 'To Do List_todo_appl_a68k'.
> 
>    RAM backup complete. 30 files backed up, 0 skipped, 1 file failed.
> 
>    Thank you for using pilot-link.