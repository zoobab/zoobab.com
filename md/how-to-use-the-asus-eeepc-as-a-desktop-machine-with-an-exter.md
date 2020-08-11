You have to connect a USB keyboard and mouses, and an external screen. The default Xandros application:

[[=image <http://zoobab.wikidot.com/local--files/tips/eeepc-external-screen.png>  ]]

does not support resolutions other then 800x600 and 1024x768. My external LCD screen nevertheless supports 1280x1024. Just change the file (in root mode) /etc/X11/xorg.conf like this (basically I replaced 1024 768 in the XXX section by 1280 1024):


    Section "ServerLayout"
    	Identifier     "Xandros"
    	Screen      0  "Screen1"
    	InputDevice    "keyboard"
    	InputDevice    "mouse"
    	InputDevice    "synaptics"
    EndSection
    
    Section "Files"
    	ModulePath   "/usr/lib/xorg/modules"
    	FontPath     "/usr/share/fonts/X11/misc"
    	FontPath     "/usr/share/fonts/X11/Type1"
    	FontPath     "/usr/share/fonts/X11/75dpi"
    	FontPath     "/usr/X11R6/lib/X11/fonts/Type1"
    EndSection
    
    Section "Module"
    	Load  "glx"
    	Load  "dri"
    	Load  "extmod"
    	Load  "synaptics"
    EndSection
    
    Section "ServerFlags"
    	Option		"AllowMouseOpenFail"
    	Option		"BlankTime" "5"
    	Option		"DontVTSwitch"	"true"
    	Option		"AIGLX"   "false"
    EndSection
    
    Section "InputDevice"
    	Identifier  "keyboard"
    	Driver      "kbd"
    	Option	    "CoreKeyboard"
    	Option	    "XkbRules" "xorg"
    	Option      "XkbModel" "pc105"
    	Option      "XkbLayout" "us"
    	Option      "XkbVariant" ""
    EndSection
    
    Section "InputDevice"
    	Identifier  "mouse"
    	Driver      "mouse"
    	Option	    "Device" "/dev/input/mice"
    	Option	    "Protocol" "IMPS/2"
    	Option	    "Emulate3Buttons" "yes"
    	Option	    "ZAxisMapping" "4 5"
    	Option	    "CorePointer"
    EndSection
    
    Section "InputDevice"
    	Identifier  "synaptics"
    	Driver      "synaptics"
    	Option      "Device"           "/dev/psaux"
    	Option      "Protocol"         "auto-dev"
    	Option      "LeftEdge"         "1400"
    	Option      "RightEdge"        "5400"
    	Option      "TopEdge"          "1400"
    	Option      "BottomEdge"       "4500"
    	Option      "PalmDetect"       "0"
    	Option      "SHMConfig"        "true"
    	Option      "SendCoreEvents"   "yes"
    	Option      "HorizScrollDelta" "0"
    	Option      "VertScrollDelta"  "155"
    	Option      "RBCornerButton"   "0"
    	Option      "RTCornerButton"   "0"
    	Option      "TapButton2"       "0"
    	Option      "MinSpeed"         "0.095"
    	Option      "MaxSpeed"         "0.38"
    	Option      "VertTwoFingerScroll" "1"
    EndSection
    
    Section "Monitor"
    	Identifier   "Monitor1"
    	VendorName   "ASUS"
    	ModelName    "Eee PC P900"
    	Modeline     "1024x600"  48.96  1024 1064 1168 1312  600 601 604 622  -HSync +Vsync
    EndSection
    
    Section "Device"
    	Identifier  "Device1"
    	Driver      "intel"
    	VendorName  "Intel Corporation"
    	BoardName   "Mobile 915GM/GMS/910GML Express Graphics Controller"
    	BusID       "PCI:0:2:0"
    EndSection
    
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
    
    Section "DRI"
    	Mode         0666
    EndSection
    
    Section "Extensions"
    	Option	    "Composite" "Disable"
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

> asus-1439342445:/home/user> wget <http://zoobab.wikidot.com/local--files/tips/xorg.conf>   -O /etc/X11/xorg.conf

Next step is to install eeeXubuntu on a SD card only as a live distribution. And maybe port OpenWRT and see how to optimise the kernel and other apps for an embedded in order to save battery.