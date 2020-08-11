
    vlc -I dummy -vvv Jun2909-171424.mp4 --sout #transcode{vcodec=theora,vb=1024,scale=1,acodec=vorb,ab=64,channels=2}:std{access=file,mux=ogg,dst='/tmp/Jun2909-171424.ogm'} vlc://quit
