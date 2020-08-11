# About


I needed a quick and easy way to serve a directory, more powerful and stronger then python:


    python -m SimpleHTTPServer


Lighttpd came to the rescue, except that I spend too much time removing all the unnecessary variables.

Here are the 3 lines which I came to, the server.pid-file is optional, but required by the gentoo init script.

# cat /etc/lighttpd/lighttpd.conf



    server.document-root =          "/home/girona/zoobab/www/root" 
    dir-listing.activate =          "enable"
    server.pid-file      =          "/var/run/lighttpd.pid"
    server.max-worker =               "3"
