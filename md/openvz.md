# Install a debian kernel in Ubuntu 9.04


Add the following lines to your /etc/apt/sources.list:


    # echo "deb http://ftp.de.debian.org/debian sid main" >> /etc/apt/sources.list


Then do an update:


    # apt-get update


Then install the kernel:


    # apt-get install linux-image-2.6.32-5-openvz-686


It should add a kernel and update your grub bootloader out of the box. It should warn you if you have some firmware issues.

Then reboot the machine, and pick your openvz kernel in grub.

# Install debian containers


## Step 1: Download a debian 5.0 template



    # wget http://ftp.openvz.org/template/precreated/debian-5.0-x86.tar.gz -O /var/lib/vz/template/cache/debian-5.0-x86.tar.gz


## Step 2: Create a new container


The container will be named 101, avoid starting it with zeros (like for example 001):


    # vzctl create 101 --ostemplate debian-5.0-x86


## Step 3: Set an IP address



    # vzctl set 101 --ipadd 192.168.20.101 --save


## Step 4: Set the DNS server


I use OpenDNS here (208.67.222.222 and 208.67.220.220):


    # vzctl set 101 --nameserver 208.67.222.222 --save


# Kernel crash


#openvz channel on IRC
18:09 < zoobab> hi
18:09 < zoobab> I have my openvz kernel crashing
18:10 < zoobab>  cat /proc/version 
18:10 < zoobab> Linux version 2.6.32-5-openvz-686
18:10 < zoobab> it crashes the ext4 stack when I try to create a container with a template tar.gz file
18:10 < zoobab> vzctl create 105 --ostemplate debian-5.0-x86
18:11 < zoobab> but I have problems to log the kernel messages
18:11 < zoobab> I tried to log them on a USB key, does not work
18:11 < zoobab> any idea?

<http://wiki.openvz.org/Remote_console_setup>  

# Nodealloc ext4 crash


<http://bugzilla.openvz.org/show_bug.cgi?id=1509>  

Modify /etc/fstab

UUID=194ac6ea-bf68-4916-949b-2e2ad962e169 /               ext4    nodelalloc,errors=remount-ro 0       1

Does not seem to crash anymore.

# Swap problem


OpenVZ does not seem to support swapping inside the containers.

# Links


* <http://webcache.googleusercontent.com/search?q=cache>  :xSPhbj8Y-KIJ:www.linuxforu.com/how-to/containing-linux-instances-with-openvz/+vzctl+--ostemplate+debian-5.0-x86&cd=4&hl=nl&ct=clnk&gl=be