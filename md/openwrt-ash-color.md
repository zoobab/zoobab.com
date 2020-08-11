I just found out that replacing .profile on OpenWRT gives you a better shell invite (you can also replace /etc/profile, /root/.profile does not always work for me):


    root@OpenWrt /root [#]# cat .profile 
    PS1='\[\033[35;1m\]\u\[\033[0m\]@\[\033[31;1m\]\h \[\033[32;1m\]$PWD\[\033[0m\] [\[\033[35m\]\#\[\033[0m\]]\[\033[31m\]\$\[\033[0m\] '
    alias u="cd .."
    alias l="ls -lA --color=yes"
    alias p="ping -c 3 130.104.1.1"


And you will have this:

[[=image openwrt-ash-colored.png]]