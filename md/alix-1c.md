

# Pictures


[[=image <http://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Alix.1C_board_with_AMD_Geode_LX_800_%28PC_Engines%29.jpg/609px-Alix.1C_board_with_AMD_Geode_LX_800_%28PC_Engines%29.jpg>  ]]

# JTAG


Find out howto JTAG the board and install Comboot on it, together with gPXE, and load an installer over the internet.

# Flash


SST 49LF040B 33-4C-NHE 0647008-CA (512KB)

# Coreboot


* <http://qa.coreboot.org/binaries/abuild-coreboot-v2-3749/pcengines_alix1c/coreboot.rom>  
* [../files/alix-1c/coreboot.rom](coreboot.rom) (md5sum: 54b2c8aa61f0d9cfe1d63ae94ba2f827)
* [[File flashrom-static]]

# Problems


Once I flashed the coreboot.rom with the flashrom-static binary, I did not get any VGA at boot time, but messages on the serial console:


    $ screen -L /dev/ttyUSB0 115200
    coreboot-4.0-r6474 Sat Apr  9 19:13:09 CEST 2011 starting...
    MSR GLCP_SYS_RSTPLL (4c000014) value is 0000059c:0000182e
    Configuring PLL.
    coreboot-4.0-r6474 Sat Apr  9 19:13:09 CEST 2011 starting...
    MSR GLCP_SYS_RSTPLL (4c000014) value is 0000059c:07de002e
    PLL configured.
    Castle 2.0 BTM periodic sync period.
    Enable Quack for fewer re-RAS on the MC
     GLIU port active enable
    Set the Delay Control in GLCP
    spd_read_byte dev 50 addr 0d returns 08
    spd_read_byte dev 50 addr 05 returns 01
    spd_read_byte dev 51 returns 0xff
    Enable RSDC
    FPU imprecise exceptions bit
    Enable Suspend on HLT & PAUSE instructions
    Enable SUSP and allow TSC to run in Suspend
    Setup throttling delays to proper mode
    Done cpuRegInit
    Ram1.00
    Ram2.00
     * sdram_set_spd_register
    spd_read_byte dev 50 addr 15 returns ff
     * Check DIMM 0
     * Check DIMM 1
    spd_read_byte dev 51 returns 0xff
     * Check DDR MAX
    spd_read_byte dev 50 addr 09 returns 0a
    spd_read_byte dev 51 returns 0xff
     * AUTOSIZE DIMM 0
     * Check present
    spd_read_byte dev 50 addr 02 returns 07
     * MODBANKS
    spd_read_byte dev 50 addr 05 returns 01
     * FIELDBANKS
    spd_read_byte dev 50 addr 11 returns 04
     * SPDNUMROWS
    spd_read_byte dev 50 addr 03 returns 03
    spd_read_byte dev 50 addr 04 returns 0a
     * SPDBANKDENSITY
    spd_read_byte dev 50 addr 1f returns 40
     * DIMMSIZE
     * BEFORT CTZ
     * TEST DIMM SIZE>8
     * PAGESIZE
    spd_read_byte dev 50 addr 04 returns 0a
     * MAXCOLADDR
     * >12address test
     * RDMSR CF07
     * WRMSR CF07
     * ALL DONE
     * AUTOSIZE DIMM 1
     * Check present
    spd_read_byte dev 51 returns 0xff
     * set cas latency
    spd_read_byte dev 50 addr 12 returns 10
    spd_read_byte dev 50 addr 17 returns 3c
    spd_read_byte dev 50 addr 19 returns 4b
    spd_read_byte dev 51 returns 0xff
     * set all latency
    spd_read_byte dev 50 addr 1e returns 28
    spd_read_byte dev 51 returns 0xff
    spd_read_byte dev 50 addr 1b returns 0f
    spd_read_byte dev 51 returns 0xff
    spd_read_byte dev 50 addr 1d returns 0f
    spd_read_byte dev 51 returns 0xff
    spd_read_byte dev 50 addr 1c returns 0a
    spd_read_byte dev 51 returns 0xff
    spd_read_byte dev 50 addr 2a returns 46
    spd_read_byte dev 51 returns 0xff
     * set emrs
    spd_read_byte dev 50 addr 16 returns ff
    spd_read_byte dev 51 returns 0xff
     * set ref rate
    spd_read_byte dev 50 addr 0c returns 3a
    spd_read_byte dev 51 returns 0xff
    Ram3
     * DRAM controller init done.
    RAM DLL lock
    Ram4
    POST 02
    Past wbinvd
    Loading image.
    Check CBFS header at fffeffe0
    magic is 4f524243
    Found CBFS header at fffeffe0
    Check fallback/coreboot_ram
    Stage: loading fallback/coreboot_ram @ 0x100000 (114688 bytes), entry @ 0x100000
    Stage: done loading.
    Jumping to image.
    coreboot-4.0-r6474 Sat Apr  9 19:13:09 CEST 2011 booting...
    clocks_per_usec: 499
    Enumerating buses...
    Show all devs...Before device enumeration.
    Root Device: enabled 1
    PCI_DOMAIN: 0000: enabled 1
    PCI: 00:01.0: enabled 1
    PCI: 00:01.1: enabled 1
    PCI: 00:0f.0: enabled 1
    PNP: 002e.0: enabled 0
    PNP: 002e.1: enabled 1
    PNP: 002e.2: enabled 1
    PNP: 002e.3: enabled 1
    PNP: 002e.5: enabled 1
    PNP: 002e.6: enabled 0
    PNP: 002e.7: enabled 0
    PNP: 002e.8: enabled 1
    PNP: 002e.9: enabled 1
    PNP: 002e.a: enabled 1
    PNP: 002e.b: enabled 1
    PCI: 00:0f.1: enabled 1
    PCI: 00:0f.2: enabled 1
    PCI: 00:0f.3: enabled 1
    PCI: 00:0f.4: enabled 1
    PCI: 00:0f.5: enabled 1
    APIC_CLUSTER: 0: enabled 1
    APIC: 00: enabled 1
    Compare with tree...
    Root Device: enabled 1
     PCI_DOMAIN: 0000: enabled 1
      PCI: 00:01.0: enabled 1
      PCI: 00:01.1: enabled 1
      PCI: 00:0f.0: enabled 1
       PNP: 002e.0: enabled 0
       PNP: 002e.1: enabled 1
       PNP: 002e.2: enabled 1
       PNP: 002e.3: enabled 1
       PNP: 002e.5: enabled 1
       PNP: 002e.6: enabled 0
       PNP: 002e.7: enabled 0
       PNP: 002e.8: enabled 1
       PNP: 002e.9: enabled 1
       PNP: 002e.a: enabled 1
       PNP: 002e.b: enabled 1
      PCI: 00:0f.1: enabled 1
      PCI: 00:0f.2: enabled 1
      PCI: 00:0f.3: enabled 1
      PCI: 00:0f.4: enabled 1
      PCI: 00:0f.5: enabled 1
     APIC_CLUSTER: 0: enabled 1
      APIC: 00: enabled 1
    scan_static_bus for Root Device
    >> Entering northbridge.c: enable_dev with path 6
    >> Entering northbridge.c: pci_domain_enable
    Enter northbridge_init_early
    writeglmsr: MSR 0x10000020, val 0x20000000:0x000fff80
    writeglmsr: MSR 0x10000021, val 0x20000000:0x080fffe0
    sizeram: _MSR MC_CF07_DATA: 10076013:00061a40
    sizeram: sizem 0x100MB
    SysmemInit: enable for 256MBytes
    usable RAM: 268304383 bytes
    SysmemInit: MSR 0x10000028, val 0x2000000f:0xfdf00100
    sizeram: _MSR MC_CF07_DATA: 10076013:00061a40
    sizeram: sizem 0x100MB
    SMMGL0Init: 268304384 bytes
    SMMGL0Init: offset is 0x80400000
    SMMGL0Init: MSR 0x10000026, val 0x28fbe080:0x400fffe0
    writeglmsr: MSR 0x10000080, val 0x00000000:0x00000003
    writeglmsr: MSR 0x40000020, val 0x20000000:0x000fff80
    writeglmsr: MSR 0x40000021, val 0x20000000:0x080fffe0
    sizeram: _MSR MC_CF07_DATA: 10076013:00061a40
    sizeram: sizem 0x100MB
    SysmemInit: enable for 256MBytes
    usable RAM: 268304383 bytes
    SysmemInit: MSR 0x4000002a, val 0x2000000f:0xfdf00100
    SMMGL1Init:
    SMMGL1Init: MSR 0x40000023, val 0x20000080:0x400fffe0
    writeglmsr: MSR 0x40000080, val 0x00000000:0x00000001
    writeglmsr: MSR 0x400000e3, val 0x60000000:0x033000f0
    CPU_RCONF_DEFAULT (1808): 0x25FFFC02:0x10FFDF00
    CPU_RCONF_BYPASS (180A): 0x00000000 : 0x00000000
    L2 cache enabled
    Enabling cache
    GLPCI R1: system msr.lo 0x00100130 msr.hi 0x0ffdf000
    GLPCI R2: system msr.lo 0x80400120 msr.hi 0x8041f000
    Exit northbridge_init_early
    Done cpubug fixes 
    Not Doing ChipsetFlashSetup()
    Preparing for VSA...
    VSA: Real mode stub @00000600: 606 bytes
    Check CBFS header at fffeffe0
    magic is 4f524243
    Found CBFS header at fffeffe0
    Check fallback/coreboot_ram
    CBFS: follow chain: fff80000 + 38 + 7949 + align -> fff879c0
    Check fallback/payload
    CBFS: follow chain: fff879c0 + 38 + 17a78 + align -> fff9f480
    Check 
    CBFS: follow chain: fff9f480 + 28 + 50b38 + align -> ffff0000
    CBFS:  Could not find file vsa
    Failed to load VSA.
    Graphics init...
    VRC_VG value: 0xffff
    Finding PCI configuration type.
    PCI: Sanity check failed
    pci_check_direct failed


I am now trying to compile coreboot with a VSA image:

[[=image coreboot-alix1c-vsa.png]]

It then complains:


    MAKE       SeaBIOS 1efb10b9ea30c45a8c9c6230234fefa10d2886ed
      Build Kconfig config file
    /home/zoobab/soft/alix1c/coreboot/payloads/external/SeaBIOS/seabios/.config:75:warning: override: reasso symbol COREBOOT
    /home/zoobab/soft/alix1c/coreboot/payloads/external/SeaBIOS/seabios/.config:76:warning: override: reasso symbol DEBUG_SERIAL
    #
    # configuration written to /home/zoobab/soft/alix1c/coreboot/payloads/external/SeaBIOS/seabios/.config
    #
      Compiling whole program out/ccode.16.s
      Compiling to assembler out/asm-offsets.s
      Generating offset file out/asm-offsets.h
      Compiling (16bit) out/code16.o
      Compiling whole program out/ccode32flat.o
      Compiling whole program out/code32seg.o
      Building ld scripts (version "pre-0.6.2-20110417_115851-buzek")
    Fixed space: 0xe05b-0x10000  total: 8101  slack: 2  Percent slack: 0.0%
    16bit size:           39424
    32bit segmented size: 2416
    32bit flat size:      14000
    32bit flat init size: 39600
      Linking out/rom16.o
      Stripping out/rom16.strip.o
      Linking out/rom32seg.o
      Stripping out/rom32seg.strip.o
      Linking out/rom.o
      Prepping out/bios.bin
    Total size: 96832  Fixed: 55848  Free: 34240 (used 73.9% of 128KiB rom)
    make: *** No rule to make target `gpl_vsa_lx_102.bin', needed by `build/coreboot.rom'.  Stop.


[[=image coreboot-alix1c-missinggplvsa.png]]

I now downloaded the missing file to the root directory of coreboot:


    zoobab@buzek /home/zoobab/soft/alix1c/coreboot [39]$ wget http://marcjonesconsulting.com/gplvsa/gpl_vsa_lx_102.bin.gz
    --2011-04-17 12:14:51--  http://marcjonesconsulting.com/gplvsa/gpl_vsa_lx_102.bin.gz
    Resolving marcjonesconsulting.com... 209.169.7.5
    Connecting to marcjonesconsulting.com|209.169.7.5|:80... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 32756 (32K) [application/x-gzip]
    Saving to: `gpl_vsa_lx_102.bin.gz'
    
    100%[=====================================================================>] 32,756      38.8K/s   in 0.8s    
    
    2011-04-17 12:14:52 (38.8 KB/s) - `gpl_vsa_lx_102.bin.gz' saved [32756/32756]
    
    zoobab@buzek /home/zoobab/soft/alix1c/coreboot [40]$ gunzip gpl_vsa_lx_102.bin.gz 
    zoobab@buzek /home/zoobab/soft/alix1c/coreboot [41]$ l
    total 124
    drwxr-xr-x 14 zoobab zoobab  4096 2011-04-17 12:12 build
    -rw-r--r--  1 zoobab zoobab 17987 2011-04-03 20:36 COPYING
    drwxr-xr-x  4 zoobab zoobab  4096 2011-04-03 20:36 documentation
    -rw-r--r--  1 zoobab zoobab 57504 2009-08-18 21:32 gpl_vsa_lx_102.bin
    -rw-r--r--  1 zoobab zoobab  7988 2011-04-03 20:36 Makefile
    -rw-r--r--  1 zoobab zoobab  9595 2011-04-03 20:36 Makefile.inc
    drwxr-xr-x  7 zoobab zoobab  4096 2011-04-03 20:36 payloads
    -rw-r--r--  1 zoobab zoobab  2576 2011-04-03 20:36 README
    drwxr-xr-x 18 zoobab zoobab  4096 2011-04-03 20:36 src
    drwxr-xr-x 29 zoobab zoobab  4096 2011-04-03 20:36 util
    zoobab@buzek /home/zoobab/soft/alix1c/coreboot [42]$


A make then succeeds in making a coreboot.rom file:


    [...]
    
      Building ld scripts (version "pre-0.6.2-20110417_121613-buzek")
    Fixed space: 0xe05b-0x10000  total: 8101  slack: 2  Percent slack: 0.0%
    16bit size:           39424
    32bit segmented size: 2416
    32bit flat size:      14000
    32bit flat init size: 39600
      Linking out/rom16.o
      Stripping out/rom16.strip.o
      Linking out/rom32seg.o
      Stripping out/rom32seg.strip.o
      Linking out/rom.o
      Prepping out/bios.bin
    Total size: 96832  Fixed: 55848  Free: 34240 (used 73.9% of 128KiB rom)
        CBFS       coreboot.rom
        PAYLOAD    SeaBIOS (internal, compression: none)
        VSA        gpl_vsa_lx_102.bin
        CBFSPRINT  coreboot.rom
    
    coreboot.rom: 512 kB, bootblocksize 65536, romsize 524288, offset 0x0
    Alignment: 64 bytes
    
    Name                           Offset     Type         Size
    fallback/coreboot_ram          0x0        stage        31047
    fallback/payload               0x7980     payload      96888
    vsa                            0x1f440    stage        57532
    (empty)                        0x2d540    null         273016


I obtain a new rom image, that I renamed [[File corebootwithvsa.rom]] (md5: 3b6b387f2e9e0c8a2645d4ac4e9c37b7).

Now I have to figure out how to flash it (I am trying to get the LPC working with an arduino and serprog), but for now I have a bricked box.
