# Testing hard


[[=image babel-hackaton-ptr-working-hard.jpg size="medium"]]

# Gentoo ebuilds for Babeld


If you want to install babeld on Gentoo, you can add my overlay by adding an entry to /etc/layman/layman.cfg:


    #-----------------------------------------------------------
    # URLs of the remote lists of overlays (one per line) or
    # local overlay definitions
    #
    #overlays: http://www.gentoo.org/proj/en/overlays/repositories.xml
    #            http://dev.gentoo.org/~wrobel/layman/global-overlays.xml
    #            http://mydomain.org/my-layman-list.xml
    #            file:///var/lib/layman/my-list.xml
    
    overlays: http://www.gentoo.org/proj/en/overlays/repositories.xml
                      http://filez.zoobab.com/gentoo/overlay.xml


Then do:


    # layman -L
    # layman -a zoobab
    # eix-update


You should be able to find the babeld package:


    # eix babeld
    [I] net-misc/babeld [1]
         Available versions:  1.2.0 1.3.4
         Installed versions:  1.3.4[?](12:28:21 PM 07/21/2013)
         Homepage:            Babel a loop-avoiding distance-vector routing protocol
         Description:         Babeld routing daemon
    
    [1] /var/lib/layman/zoobab


You can then install babel with:


    # emerge -1 babeld


# Missing 


There is a need of a good default babeld.conf explaining all the options.

# Links 


* <http://wiki.leloop.org/index.php/Babel_hackathon>  
* <http://blog.freifunk.net/2013/babel-wireless-mesh-hackathon-paris-192021-july-2013>  

# Configs



    root@lambda:~# ifconfig
    eth1      Link encap:Ethernet  HWaddr 02:15:6D:C8:03:BF  
              inet addr:192.168.100.35  Bcast:192.168.100.255  Mask:255.255.255.0
              inet6 addr: fe80::15:6dff:fec8:3bf/64 Scope:Link
              inet6 addr: 2001:41d0:1:f19f:21b:b1ff:fe83:8d00/128 Scope:Global
              UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
              RX packets:767 errors:0 dropped:0 overruns:0 frame:0
              TX packets:747 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000 
              RX bytes:146196 (142.7 KiB)  TX bytes:76822 (75.0 KiB)
              Interrupt:5 
    
    lo        Link encap:Local Loopback  
              inet addr:127.0.0.1  Mask:255.0.0.0
              inet6 addr: ::1/128 Scope:Host
              UP LOOPBACK RUNNING  MTU:16436  Metric:1
              RX packets:8052 errors:0 dropped:0 overruns:0 frame:0
              TX packets:8052 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:0 
              RX bytes:661254 (645.7 KiB)  TX bytes:661254 (645.7 KiB)
    
    wlan0     Link encap:Ethernet  HWaddr 00:1B:B1:83:8D:3B  
              inet addr:192.168.101.35  Bcast:192.168.101.255  Mask:255.255.255.0
              inet6 addr: 2001:41d0:1:f19f:21b:b1ff:fe83:8d01/128 Scope:Global
              inet6 addr: fe80::21b:b1ff:fe83:8d3b/64 Scope:Link
              UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
              RX packets:83 errors:0 dropped:0 overruns:0 frame:0
              TX packets:89 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:32 
              RX bytes:10762 (10.5 KiB)  TX bytes:12597 (12.3 KiB)
    
    wlan2     Link encap:Ethernet  HWaddr 00:1B:B1:83:8D:38  
              inet addr:192.168.105.35  Bcast:192.168.105.255  Mask:255.255.255.0
              inet6 addr: fe80::21b:b1ff:fe83:8d38/64 Scope:Link
              inet6 addr: 2001:41d0:1:f19f:21b:b1ff:fe83:8d05/128 Scope:Global
              UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
              RX packets:88 errors:0 dropped:0 overruns:0 frame:0
              TX packets:93 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:32 
              RX bytes:10868 (10.6 KiB)  TX bytes:12552 (12.2 KiB)
    
    root@lambda:~#


## Network



    root@lambda:~# cat /etc/config/network
    config interface 'loopback'
            option ifname 'lo'
            option proto 'static'
            option ipaddr '127.0.0.1'
            option netmask '255.0.0.0'
    
    config interface 'lan'
            option ifname 'eth1'
            option proto 'static'
            option ipaddr '192.168.100.35/24'
            option ip6addr '2001:41d0:1:f19f:21b:b1ff:fe83:8d00/128'
    
    config switch
            option name 'switch0'
            option reset '1'
            option enable_vlan '1'
    
    config switch_vlan
            option device 'switch0'
            option vlan '1'
            option ports '0 2 3 4'
    
    config interface 'wifi0'
            option ifname 'wlan0'
            option proto 'static'
            option ipaddr '192.168.101.35/24'
            option ip6addr '2001:41d0:1:f19f:21b:b1ff:fe83:8d01/128'
    
    config interface 'wifi2'
            option ifname 'wlan2'
            option proto 'static'
            option ipaddr '192.168.105.35/24'
            option ip6addr '2001:41d0:1:f19f:21b:b1ff:fe83:8d05/128'


## Wireless



    config wifi-device  radio0
    	option type     mac80211
    	option channel  1
    	option macaddr	00:1b:b1:83:8d:3b
    	option hwmode	11ng
    	option htmode	HT20
    	list ht_capab	SHORT-GI-40
    	list ht_capab	TX-STBC
    	list ht_capab	RX-STBC1
    	list ht_capab	DSSS_CCK-40
    
    config wifi-iface
    	option device   radio0
    	option network  wifi0
    	option mode     adhoc
    	option ssid     pps1
    	option encryption none
    
    config wifi-device  radio1
    	option type     mac80211
    	option channel  6
    	option macaddr	00:1b:b1:83:8d:39
    	option hwmode	11ng
    	option htmode	HT20
    	list ht_capab	SHORT-GI-40
    	list ht_capab	TX-STBC
    	list ht_capab	RX-STBC1
    	list ht_capab	DSSS_CCK-40
    	option disabled 1
    
    config wifi-iface
    	option device   radio1
    	option network  wifi1
    	option mode     adhoc
    	option ssid     pps
    	option encryption none
    
    config wifi-device  radio2
    	option type     mac80211
    	option channel  36
    	option macaddr	00:1b:b1:83:8d:38
    	option hwmode	11na
    	option htmode	HT20
    	list ht_capab	SHORT-GI-40
    	list ht_capab	TX-STBC
    	list ht_capab	RX-STBC1
    	list ht_capab	DSSS_CCK-40
    
    config wifi-iface
    	option device   radio2
    	option network  wifi2
    	option mode     adhoc
    	option ssid     pps5
    	option encryption none


## Laptop1



    # iwconfig wlan0 mode ad-hoc essid pps1 enc off channel 1


The configure the ip addr:


    # ifconfig wlan0 192.168.101.199/24


Then launch babeld:


    # babeld -d 1 -z 3 wlan0



## To ignore one machine


How to ignore babel messages from one machine:


    # ip6tables -A INPUT --proto udp --source <machine_ipv6_addr> --dport 6696  -j DROP


## Channels


You can see the channels used (here ch36 and ch1) in the babel debug messages ('-d 1' option), search for  chan (36,1):


    # babeld -d 1 -z 3 eth1
    [...]
    My id 02:80:00:ff:fe:00:80:24 seqno 33929
    Neighbour fe80::15:6dff:fec8:3bf dev eth1 reach ff00 rxcost 96 txcost 96 chan -2.
    192.168.0.179/32 metric 0 (exported)
    192.168.11.2/32 metric 0 (exported)
    192.168.101.199/32 metric 0 (exported)
    192.168.100.135/32 metric 0 (exported)
    192.168.0.242/32 metric 395 refmetric 299 id 02:26:c6:ff:fe:7b:5e:00 seqno 13471 chan (36,1) age 8 via eth1 neigh fe80::15:6dff:fec8:3bf nexthop 192.168.100.35 (installed)
    192.168.101.199/32 metric 395 refmetric 299 id 02:26:c6:ff:fe:7b:5e:00 seqno 13471 chan (36,1) age 8 via eth1 neigh fe80::15:6dff:fec8:3bf nexthop 192.168.100.35 (feasible)
    2001:41d0:1:f19f:21b:b1ff:fe83:8d00/128 metric 96 refmetric 0 id 02:1b:b1:ff:fe:83:8d:3b seqno 9058 age 8 via eth1 neigh fe80::15:6dff:fec8:3bf (installed)


## Lambda (35)



    root@lambda:/# ifconfig
    eth1      Link encap:Ethernet  HWaddr 02:15:6D:C8:03:BF  
              inet addr:192.168.100.35  Bcast:192.168.100.255  Mask:255.255.255.0
              inet6 addr: fe80::15:6dff:fec8:3bf/64 Scope:Link
              inet6 addr: 2001:41d0:1:f19f:21b:b1ff:fe83:8d00/128 Scope:Global
              UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
              RX packets:3951 errors:0 dropped:0 overruns:0 frame:0
              TX packets:4160 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000 
              RX bytes:502644 (490.8 KiB)  TX bytes:482575 (471.2 KiB)
              Interrupt:5 
    
    lo        Link encap:Local Loopback  
              inet addr:127.0.0.1  Mask:255.0.0.0
              inet6 addr: ::1/128 Scope:Host
              UP LOOPBACK RUNNING  MTU:16436  Metric:1
              RX packets:78430 errors:0 dropped:0 overruns:0 frame:0
              TX packets:78430 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:0 
              RX bytes:6434078 (6.1 MiB)  TX bytes:6434078 (6.1 MiB)
    
    wlan0     Link encap:Ethernet  HWaddr 00:1B:B1:83:8D:3B  
              inet addr:192.168.101.35  Bcast:192.168.101.255  Mask:255.255.255.0
              inet6 addr: 2001:41d0:1:f19f:21b:b1ff:fe83:8d01/128 Scope:Global
              inet6 addr: fe80::21b:b1ff:fe83:8d3b/64 Scope:Link
              UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
              RX packets:3388 errors:0 dropped:0 overruns:0 frame:0
              TX packets:1622 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:32 
              RX bytes:464204 (453.3 KiB)  TX bytes:265856 (259.6 KiB)
    
    wlan2     Link encap:Ethernet  HWaddr 00:1B:B1:83:8D:38  
              inet addr:192.168.105.35  Bcast:192.168.105.255  Mask:255.255.255.0
              inet6 addr: fe80::21b:b1ff:fe83:8d38/64 Scope:Link
              inet6 addr: 2001:41d0:1:f19f:21b:b1ff:fe83:8d05/128 Scope:Global
              UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
              RX packets:1720 errors:0 dropped:0 overruns:0 frame:0
              TX packets:2395 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:32 
              RX bytes:213592 (208.5 KiB)  TX bytes:327484 (319.8 KiB)
    
    root@lambda:/#
