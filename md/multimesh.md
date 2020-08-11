# Objective


Create a wireless mesh network using OLSR or any other routing protocol at layer 3, which is able to do not reuse the channel channel at each hop.

# Problem


In most mesh networks such as Freifunk, packets are routed through the network by reusing the same frequency. Since WiFi cards are half-duplex, each card cannot receive and transmit at the same time, **thus dividing the bandwidth by a factor of 2 at each hop**.

# Solution


Use at least 2 channels to obtain full duplex links, and higher throughput.

# Testbed


For this tested, I used 10 foneras flashed with OpenWRT Kamikaze, and I have installed olsrd 0.5.3.

I used 2 foneras per node, one on channel 1 with the BSSID fixed on ca:fe:ca:fe:ca:fe and ESSID bombolong1:

> root@zoomesh08$ cat /etc/config/wireless 
> config wifi-device  wifi0
>         option type     atheros
>         **option channel  1**
>         option agmode   11g
>         option diversity 0
>         option txantenna 1
>         option rxantenna 1
> 
> config wifi-iface
>         option device   wifi0
>         option network  wlan
>         option mode     adhoc
>         **option ssid     bombolong1**
>         option hidden   0
>         option txpower  16
>         option encryption none
>         **option bssid ca:fe:ca:fe:ca:fe**

And the other one on channel 11 with the BSSID fixed on 00:11:00:11:00:11 and ESSID bombolong11:

> root@zoomesh07$ cat /etc/config/wireless 
> config wifi-device  wifi0
>         option type     atheros
>         **option channel  11**
>         option agmode   11g
>         option diversity 0
>         option txantenna 1
>         option rxantenna 1
> 
> config wifi-iface
>         option device   wifi0
>         option network  wlan
>         option mode     adhoc
>         **option ssid     bombolong11**
>         option hidden   0
>         option txpower  16
>         option encryption none
>         **option bssid 00:11:00:11:00:11**

The 2 foneras are linked with an ethernet cable.

The first fonera has an olsrd.conf config file with a default weight of 0.10:

> h
> h
> h

While the second fonera has an olsrd.conf config file with a default weight of 0.20:

> h
> h
> h
> h

Here are the routes:

# Simulator


Test with some 20 [openvz instances](http://www.openvz.org) and [ebtables](http://ebtables.sf.net) in order to simulate the behaviour of the network. Also try with [ Uml-wifi](http://folk.uio.no/paalee/referencing_publications/ref-nr-guffens-presentation05.pdf), as [explained here](http://www.metz.supelec.fr/metz/personnel/galtier/PagesPerso/TutorielUML/Wifi_for_UML/index.html).

# Improvements


Negative weights with [Bellman-Ford](http://en.wikipedia.org/wiki/Bellman-Ford_algorithm) instead of [Dijkstra](http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)?