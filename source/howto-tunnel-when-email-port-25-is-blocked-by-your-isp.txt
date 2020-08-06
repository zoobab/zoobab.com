You have to use port 2525 on your localhost 127.0.0.1:

> ssh -N -L2525:vic.ffii.org:25 zoobab@vic.ffii.org

Works for me:

> zoobab@freeman /home/zoobab [1]$ telnet 127.0.0.1 2525
> Trying 127.0.0.1...
> Connected to 127.0.0.1.
> Escape character is '^]'.
> 220 vic.ffii.org ESMTP Exim 4.63 Fri, 18 Apr 2008 15:11:41 +0200

Point your email client to 2525 and it is done. You can also use port 25 on localhost if you don't have any MTA like Exim or postfix running:

> ssh -N -L25:vic.ffii.org:25 zoobab@vic.ffii.org