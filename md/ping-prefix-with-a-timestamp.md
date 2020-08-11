A bit of awk to add some timestamp to ping:


    zoobab@chuchu /home/zoobab [11]$ ping 192.168.100.3 | awk '{ print strftime("%Y-%m-%d %H:%M:%S"), $0; fflush(); }'
    2016-01-13 10:08:07 PING 192.168.100.3 (192.168.100.3) 56(84) bytes of data.
    2016-01-13 10:08:07 64 bytes from 192.168.100.3: icmp_seq=1 ttl=64 time=0.585 ms
    2016-01-13 10:08:08 64 bytes from 192.168.100.3: icmp_seq=2 ttl=64 time=0.268 ms
    2016-01-13 10:08:09 64 bytes from 192.168.100.3: icmp_seq=3 ttl=64 time=0.270 ms
    2016-01-13 10:08:10 64 bytes from 192.168.100.3: icmp_seq=4 ttl=64 time=0.238 ms
    2016-01-13 10:08:11 64 bytes from 192.168.100.3: icmp_seq=5 ttl=64 time=0.272 ms
    2016-01-13 10:08:19 64 bytes from 192.168.100.3: icmp_seq=12 ttl=64 time=1003 ms
    2016-01-13 10:08:19 64 bytes from 192.168.100.3: icmp_seq=13 ttl=64 time=3.77 ms
    2016-01-13 10:08:20 64 bytes from 192.168.100.3: icmp_seq=14 ttl=64 time=0.297 ms
    2016-01-13 10:08:21 64 bytes from 192.168.100.3: icmp_seq=15 ttl=64 time=0.346 ms
    2016-01-13 10:08:22 64 bytes from 192.168.100.3: icmp_seq=16 ttl=64 time=0.261 ms
    2016-01-13 10:08:23 64 bytes from 192.168.100.3: icmp_seq=17 ttl=64 time=0.216 ms
    2016-01-13 10:08:24 64 bytes from 192.168.100.3: icmp_seq=18 ttl=64 time=0.329 ms
    2016-01-13 10:08:25 64 bytes from 192.168.100.3: icmp_seq=19 ttl=64 time=0.438 ms
    2016-01-13 10:08:26 64 bytes from 192.168.100.3: icmp_seq=20 ttl=64 time=0.257 ms
    2016-01-13 10:09:10 64 bytes from 192.168.100.3: icmp_seq=64 ttl=64 time=0.834 ms
    2016-01-13 10:09:11 64 bytes from 192.168.100.3: icmp_seq=65 ttl=64 time=0.239 ms
    2016-01-13 10:09:12 64 bytes from 192.168.100.3: icmp_seq=66 ttl=64 time=0.239 ms
