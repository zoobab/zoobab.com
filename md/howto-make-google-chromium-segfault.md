

# Introduction


I recently read on Slashdot that [Google was offering 500 US dollars to find bugs](http://it.slashdot.org/story/10/01/29/171208/Google-To-Pay-500-For-Bugs-Found-In-Chromium) in its Chromium browser. I remembered I attended a presentation at [HSF2008](http://caca.zoy.org/raw-attachment/wiki/zzuf/zzuf-20080621.odp) on a fuzzer [zzuf](http://caca.zoy.org/wiki/zzuf) that made your browser crash.

# How to make Chromium crash


Here it a step by step procedure on howto make Chromium crash:

## Step 1: Download hello.jpg


Download [[file hello.jpg]].

[[=image hello.jpg]]

## Step 2: Install zzuf



    zoobab@buzek /home/zoobab/Downloads $ apt-get install zzuf


## Step 3: Generate an hello.html file



    zoobab@buzek /home/zoobab/Downloads $ seq -f '<img src="hello.jpg#%g">' 0 500 > hello.html


## Step 4: Use Zzuf with some variations in hello.jpg



    zoobab@buzek /home/zoobab/Downloads $ zzuf -I 'hello[.]jpg' -r0.1 chromium-browser hello.html
    Corrupt JPEG data: 138 extraneous bytes before marker 0xc0
    Corrupt JPEG data: 138 extraneous bytes before marker 0xc0
    Corrupt JPEG data: 138 extraneous bytes before marker 0xc0
    Corrupt JPEG data: 138 extraneous bytes before marker 0xc0
    Corrupt JPEG data: 138 extraneous bytes before marker 0xc0
    Corrupt JPEG data: 138 extraneous bytes before marker 0xc0
    Corrupt JPEG data: 138 extraneous bytes before marker 0xc0
    Corrupt JPEG data: 138 extraneous bytes before marker 0xc0
    Corrupt JPEG data: 138 extraneous bytes before marker 0xc0
    Corrupt JPEG data: 138 extraneous bytes before marker 0xc0
    Corrupt JPEG data: 138 extraneous bytes before marker 0xc0
    Corrupt JPEG data: 138 extraneous bytes before marker 0xc0
    Corrupt JPEG data: 138 extraneous bytes before marker 0xc0
    Corrupt JPEG data: 138 extraneous bytes before marker 0xc0
    Corrupt JPEG data: 138 extraneous bytes before marker 0xc0
    zzuf[s=0,r=0.1]: signal 11 (SIGSEGV)


Chromium is crashing. Now it should be possible to generate the correct JPEG image that makes the browser crash.

It seems to crash faster with the -r0.01 option:


    zoobab@buzek /home/zoobab/test [346]$ zzuf -I 'hello[.]jpg' -r0.01 chromium-browser hello.html 
    zzuf[s=0,r=0.01]: signal 11 (SIGSEGV)


Reducing the number of seq:


    zoobab@buzek /home/zoobab/test [477]$ seq -f '<img src="hello.jpg#%g">' 0 300 > hello300.html
    zoobab@buzek /home/zoobab/test [477]$ zzuf -A -I "hello.jpg" -r0.01 chromium-browser  hello300.html


I can hardly make it crash with 200, but with 250 and 300 it crashes most of time.

# Versions


I used the Chromium version of today 29 January 2010 from the PPA:

> deb <<http://ppa.launchpad.net/ts.sch.gr/ppa/ubuntu>  >   karmic main 
> deb-src http://ppa.launchpad.net/ts.sch.gr/ppa/ubuntu karmic main

# Bug submitted


<http://code.google.com/p/chromium/issues/detail?id=33654>  

# Video


[[embedvideo]]
<object width="425" height="344"><param name="movie" value="<<http://www.youtube.com/v/ZO4BgfnIumA&hl=en_US&fs=1&>  >  "></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/ZO4BgfnIumA&hl=en_US&fs=1&" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="425" height="344"></embed></object>
[[/embedvideo]]

# Comments


[[module Comments]]