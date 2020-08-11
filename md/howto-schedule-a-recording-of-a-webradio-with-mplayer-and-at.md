# Introduction


I wanted to record a friend who was talking on a radio, but I was unable to be on time in front of my radio to listen to him, so I wanted to schedule a recording of it. Here is how I did it with mplayer and at.

# Step1: Install mplayer, at and a shell


Be sure you have mplayer and at installed on your system, as well as a shell like bash.

# Step2: create a shell script


Create a shell script that will dump the content of the streaming on a file. Use an argument to dump it in a name that contain the time when the dump started (you need the date command for that):


    zoobab@vic /home/zoobab [4]$ vim radiopanikstart.sh
    #!/bin/sh
    mplayer -v -dumpstream -dumpfile radiopanik-`date +%T` http://streaming.domainepublic.net:8000/radiopanik.ogg


Put this code in a file with your favourite text editor, save it as "radiopanik.sh", and make it executable with:


    zoobab@vic /home/zoobab [5]$ chmod +x radiopanikstart.sh


# Step 3: Use the AT scheduler to launch the script


Let's say you want to schedule the start of the recording at 22:00 today:


    zoobab@vic /home/zoobab [6]$ at -f radiopanikstart.sh 22:00
    warning: commands will be executed using /bin/sh
    job 4 at Wed Feb 11 22:00:00 2009


# Step 4: Use the AT scheduler to stop the dumping


There is a need to specify an end to the recording dumping process. You can schedule the end of the recording at 23:00 :


    zoobab@vic /home/zoobab [4]$ vim radiopanikstop.sh
    #!/bin/sh
    killall mplayer


This is a bit rude to kill all mplayer processes, but it is simple enough in my case.

Now let's schedule it:


    zoobab@vic /home/zoobab [6]$ at -f radiopanikstop.sh 23:00
    warning: commands will be executed using /bin/sh
    job 5 at Wed Feb 11 23:00:00 2009
