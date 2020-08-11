I wanted to backup files between 2 machines without the overhead of SSH encryption, so I setuped an Rsyncd server on one machine:


    root@buzek /tmp [27]# cat /etc/rsyncd.conf 
    motd file = /etc/rsyncd.motd
    log file = /var/log/rsyncd.log
    pid file = /var/run/rsyncd.pid
    lock file = /var/run/rsync.lock
    
    [home]
       path = /home
       comment = homedir
       uid = root
       gid = root
       read only = yes
       list = yes


On client side, just do:


    rsync -av --partial --progress buzek::home /home/buzek/
