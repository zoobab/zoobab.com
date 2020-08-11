# Installing Pubuntu


# Resizing the filesystem


# Speed problems



    root@pubuntu /mnt/C [34]# time dd if=/dev/zero of=10M count=10 bs=1M
    10+0 records in
    10+0 records out
    10485760 bytes (10 MB) copied, 6.13009 s, 1.7 MB/s
    
    real	0m6.180s
    user	0m0.090s
    sys	0m6.050s
    root@pubuntu /mnt/C [35]# cd
    root@pubuntu /home/pubuntu [36]# time dd if=/dev/zero of=10M count=10 bs=1M
    10+0 records in
    10+0 records out
    10485760 bytes (10 MB) copied, 0.160002 s, 65.5 MB/s
    
    real	0m0.230s
    user	0m0.020s
    sys	0m0.190s
    root@pubuntu /home/pubuntu [37]#
