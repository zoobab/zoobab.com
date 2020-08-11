Here is a typical [[file network | /etc/config/network]] config file to setup a fonera as a bridge between the wired (eth0) and wireless (ath0) interfaces:


    # Loopback
    config interface loopback
    	option ifname   "lo"
    	option proto    static
    	option ipaddr   127.0.0.1
    	option netmask  255.0.0.0
    
    # LAN
    config interface lan
    	option type     bridge
    	option ifname   "eth0"
    	option proto    static
    	option ipaddr   192.168.1.1
    	option netmask  255.255.255.0
    
    # WiFi
    config interface wifi
    	option ifname   "ath0"
    	option proto    static
    	option ipaddr   192.168.40.199
    	option netmask  255.255.255.0
