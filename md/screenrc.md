Put this in your .screenrc, it will produce logs in the directory where you are in the format of "screenlog-20100824-10:05:27":


    # cat ~/.screenrc
    logfile screenlog-%Y%m%d-%c:%s


Or this screenrc to produce logs in your Home directory:


    # cat ~/.screenrc
    logfile $HOME/screenlog-%Y%m%d-%c:%s


This feature is not documented in the screen manpage, I have emailed the author several times, but the man page still does not document this feature.

Screen does not log in real time, you have to pass it some more config to tell it to "logfile flush 0" to avoid any delay in file logging:

<http://unix.stackexchange.com/questions/114206/log-output-of-gnu-screen-in-real-time>  


    # cat ~/.screenrc
    logfile /tmp/screenlog-%Y%m%d-%c:%s
    logfile flush 0
