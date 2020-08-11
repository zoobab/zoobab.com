[[f>toc]]

# Goals


# Setup some services (ex: ssh) behind on a computer that is running behind firewall, without the need of a internet server of which you have a root password.
# Anonymous Bittorrent over multiple VPN interfaces
# etc...

# Step 1: install the stuff needed


In Ubuntu or Debian, type:


    sudo apt-get install tor onioncat


# Step 2: enable hidden services


Edit your /etc/tor/torrc in order to have:


    HiddenServiceDir /var/lib/tor/hidden_service/
    HiddenServicePort 80 127.0.0.1:80


You can also specify another location, for example /var/lib/tor/hidden_service_n120/.

Restart tor (/etc/init.d/tor restart), and you will see two files in /var/lib/tor/hidden_service/:


    root@gierek /var/lib/tor/hidden_service [4]# l
    total 8
    -rw------- 1 debian-tor debian-tor  23 2009-05-14 02:03 hostname
    -rw------- 1 debian-tor debian-tor 887 2009-05-13 23:50 private_key
    root@gierek /var/lib/tor/hidden_service [5]# cat hostname 
    ze3xqosv5mviyktl.onion


# Step 3: Get onioncat running


Simply type:


    root@gierek /var/lib/tor/hidden_service [7]# ocat ze3xqosv5mviyktl
    Fri, 15 May 2009 13:18:29.115 +0200 [0:main      :  info] Bernhard R. Fischer (c) onioncat 0.1.10-471M -- compiled Feb 21 2009 11:44:00
    Fri, 15 May 2009 13:18:29.116 +0200 [0:main      :  info] MAC address 0:0:6c:8c:2a:6b
    Fri, 15 May 2009 13:18:29.320 +0200 [0:main      :  info] configuring tun IP: "ifconfig tun0 add fd87:d87e:eb43:c937:783a:55eb:2a8c:2a6b/48 up"
    Fri, 15 May 2009 13:18:29.332 +0200 [0:main      :  info] IPv6 address fd87:d87e:eb43:c937:783a:55eb:2a8c:2a6b
    Fri, 15 May 2009 13:18:29.332 +0200 [0:main      :  info] TUN/TAP device tun0
    Fri, 15 May 2009 13:18:29.333 +0200 [0:main      :  info] process backgrounded, pid = 16855
    Fri, 15 May 2009 13:18:29.338 +0200 [0:main      :  info] running as root, changing uid/gid to tor (uid 1002/gid 1002)
    Fri, 15 May 2009 13:18:29.338 +0200 [3:cleaner   :  info] stats: ... (not implemented yet)
    Fri, 15 May 2009 13:18:29.338 +0200 [2:receiver  :   err] select encountered error: "Interrupted system call", restarting
    Fri, 15 May 2009 13:18:29.338 +0200 [2:receiver  :   err] select encountered error: "Interrupted system call", restarting


And then you should have a tun0 with an IPv6 address running:


    root@gierek /var/lib/tor/hidden_service [8]# ifconfig -a
    eth0      Link encap:Ethernet  HWaddr 00:23:54:f3:00:ee  
              BROADCAST MULTICAST  MTU:1500  Metric:1
              RX packets:0 errors:0 dropped:0 overruns:0 frame:0
              TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000 
              RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
              Interrupt:17 
    
    lo        Link encap:Local Loopback  
              inet addr:127.0.0.1  Mask:255.0.0.0
              inet6 addr: ::1/128 Scope:Host
              UP LOOPBACK RUNNING  MTU:16436  Metric:1
              RX packets:1109 errors:0 dropped:0 overruns:0 frame:0
              TX packets:1109 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:0 
              RX bytes:96835 (96.8 KB)  TX bytes:96835 (96.8 KB)
    
    ra0       Link encap:Ethernet  HWaddr 00:22:43:5e:d8:53  
              inet addr:192.168.50.110  Bcast:255.255.255.255  Mask:255.255.255.0
              UP BROADCAST RUNNING MULTICAST  MTU:576  Metric:1
              RX packets:310580 errors:0 dropped:0 overruns:0 frame:0
              TX packets:126686 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000 
              RX bytes:102538459 (102.5 MB)  TX bytes:18669870 (18.6 MB)
              Interrupt:19 
    
    tun0      Link encap:UNSPEC  HWaddr 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  
              inet6 addr: fd87:d87e:eb43:c937:783a:55eb:2a8c:2a6b/48 Scope:Global
              UP POINTOPOINT RUNNING NOARP MULTICAST  MTU:1500  Metric:1
              RX packets:0 errors:0 dropped:0 overruns:0 frame:0
              TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:500 
              RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)


After that, try to ping one host (beware it takes one minute to create the route):


    root@gierek /var/lib/tor/hidden_service [8]# ping6 fd87:d87e:eb43:f947:ad24:ec81:8abe:753e
    
    PING fd87:d87e:eb43:f947:ad24:ec81:8abe:753e(fd87:d87e:eb43:f947:ad24:ec81:8abe:753e) 56 data bytes
    64 bytes from fd87:d87e:eb43:f947:ad24:ec81:8abe:753e: icmp_seq=149 ttl=64 time=3387 ms
    64 bytes from fd87:d87e:eb43:f947:ad24:ec81:8abe:753e: icmp_seq=150 ttl=64 time=4418 ms
    64 bytes from fd87:d87e:eb43:f947:ad24:ec81:8abe:753e: icmp_seq=151 ttl=64 time=3669 ms
    64 bytes from fd87:d87e:eb43:f947:ad24:ec81:8abe:753e: icmp_seq=152 ttl=64 time=5650 ms


# Next steps


1. Modify onioncat in order to support other network prefixes (and have multiple tun0, tun1, ..., tunx with different network prefixes);
2. Try ctorrent over multiple interfaces to see if it can send and receive streams over multiple interfaces.
3. Make the config permanent in case of reboot.
4. Configure Tor in order to have only 2 hops and not 3.

# Bugs


When I try to ping a machine on the onioncat network, /var/log/tor/log gives me some error messages:


    May 15 16:24:17.655 [warn] Failed to fetch rendezvous descriptor.
    May 15 16:24:17.655 [notice] Closing stream for '[scrubbed].onion': hidden service is unavailable (try again later).
