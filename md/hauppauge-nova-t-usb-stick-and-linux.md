

# Kernel messages



    zoobab@gierek /home/zoobab [11]$ cat /proc/version
    Linux version 2.6.28-11-generic (buildd@palmer) (gcc version 4.3.3 (Ubuntu 4.3.3-5ubuntu4) ) #42-Ubuntu SMP Fri Apr 17 01:57:59 UTC 2009



    [   61.717082] usb 1-2: new high speed USB device using ehci_hcd and address 4
    [   61.851285] usb 1-2: configuration #1 chosen from 1 choice
    [   62.251445] dib0700: loaded with support for 8 different device-types
    [   62.251704] dvb-usb: found a 'Hauppauge Nova-T Stick' in cold state, will try to load a firmware
    [   62.251713] usb 1-2: firmware: requesting dvb-usb-dib0700-1.20.fw
    [   62.327298] dvb-usb: downloading firmware from file 'dvb-usb-dib0700-1.20.fw'
    [   62.567950] dib0700: firmware started successfully.
    [   63.069133] dvb-usb: found a 'Hauppauge Nova-T Stick' in warm state.
    [   63.069288] dvb-usb: will pass the complete MPEG2 transport stream to the software demuxer.
    [   63.069786] DVB: registering new adapter (Hauppauge Nova-T Stick)
    [   63.325100] DVB: registering adapter 0 frontend 0 (DiBcom 7000PC)...
    [   63.509002] DiB0070: successfully identified
    [   63.509282] input: IR-receiver inside an USB DVB receiver as /devices/pci0000:00/0000:00:1d.7/usb1/1-2/input/input11
    [   63.525308] dvb-usb: schedule remote query interval to 50 msecs.
    [   63.525330] dvb-usb: Hauppauge Nova-T Stick successfully initialized and connected.
    [   63.525690] usbcore: registered new interface driver dvb_usb_dib0700
    [   79.870879] Process accounting paused
    [  124.637302] DVB: adapter 0 frontend 0 frequency 0 out of range (45000000..860000000)
    [  144.745222] ATL1E 0000:03:00.0: ATL1E: eth0 NIC Link is Up<100 Mbps Full Duplex>
    [  144.745921] ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready
    [  146.095230] ATL1E 0000:03:00.0: ATL1E: eth0 NIC Link is Down
    [  147.636244] ATL1E 0000:03:00.0: ATL1E: eth0 NIC Link is Up<100 Mbps Full Duplex>
    [  155.232061] eth0: no IPv6 routers present
    [  926.415492] DVB: adapter 0 frontend 0 frequency 0 out of range (45000000..860000000)
    [  961.824016] DVB: adapter 0 frontend 0 frequency 0 out of range (45000000..860000000)


# Channels.conf for Brussels (Belgium)



    Klara continuo:482000:I999B8C12D12M64T8G4Y0:T:27500:0:4241:0:0:4240:8248:1:0
    MNM:482000:I999B8C12D12M64T8G4Y0:T:27500:0:4225:0:0:4224:8248:1:0
    Studio Brussel:482000:I999B8C12D12M64T8G4Y0:T:27500:0:4209:0:0:4208:8248:1:0
    Klara:482000:I999B8C12D12M64T8G4Y0:T:27500:0:4193:0:0:4192:8248:1:0
    Radio 1:482000:I999B8C12D12M64T8G4Y0:T:27500:0:4161:0:0:4160:8248:1:0
    Radio 2:482000:I999B8C12D12M64T8G4Y0:T:27500:0:4177:0:0:4176:8248:1:0
    EEN:482000:I999B8C12D12M64T8G4Y0:T:27500:4113:4114:4115:0:4112:8248:1:0
    Canvas/Ketnet:482000:I999B8C12D12M64T8G4Y0:T:27500:4129:4130:4131:0:4128:8248:1:0
    Canvas+/Ketnet+:482000:I999B8C12D12M64T8G4Y0:T:27500:4273:4274:0:0:4272:8248:1:0
    Sporza:482000:I999B8C12D12M64T8G4Y0:T:27500:0:4257:0:0:4256:8248:1:0
    Nieuws+:482000:I999B8C12D12M64T8G4Y0:T:27500:0:4289:0:0:4288:8248:1:0
    MNM hits:482000:I999B8C12D12M64T8G4Y0:T:27500:0:4305:0:0:4304:8248:1:0
    [0001]:594000:I999B8C999D999M999T999G999Y999:T:27500:300+302:301:0:0:1:0:0:0
    la une:754000:I999B8C999D999M999T999G999Y999:T:27500:33:34:38:0:1:0:0:0
    la deux:754000:I999B8C999D999M999T999G999Y999:T:27500:500:501:504:0:2:0:0:0
    la trois:754000:I999B8C999D999M999T999G999Y999:T:27500:2081:2082:2084:0:3:0:0:0
    EURONEWS:754000:I999B8C999D999M999T999G999Y999:T:27500:2201:2202:0:0:4:0:0:0
    La Prem1ere:754000:I999B8C999D999M999T999G999Y999:T:27500:0:51:0:0:11:0:0:0
    Musiq3:754000:I999B8C999D999M999T999G999Y999:T:27500:0:53:0:0:12:0:0:0
    Classic 21:754000:I999B8C999D999M999T999G999Y999:T:27500:0:55:0:0:13:0:0:0
    VivaCite:754000:I999B8C999D999M999T999G999Y999:T:27500:0:57:0:0:14:0:0:0
    brf:754000:I999B8C999D999M999T999G999Y999:T:27500:0:59:0:0:15:0:0:0
    Pure FM:754000:I999B8C999D999M999T999G999Y999:T:27500:0:61:0:0:16:0:0:0
