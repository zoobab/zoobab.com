

# Availability of the kernel sources


The website [Livebox Opensource](http://www.livebox-opensource.com) has released the sources of the kernel for the version 2.6.15. Note that there are 2 tar.bz2 files available, one for the platform [vFAST3XXX_6813E2](http://www.livebox-opensource.com/Products/LiveBox/LiveBox2/vFAST3XXX_6813E2/linux-2.6.15.tar.bz2) and the other for the [vFAST3XXX_6813E4](http://www.livebox-opensource.com/Products/LiveBox/LiveBox2/vFAST3XXX_6813E4/linux-2.6.15.tar.bz2).

I have requested Belgacom to provide the sources of the Linux kernel and uboot, without any answer so far.

# Download the kernel sources


First download the sources of [linux-2.6.15.tar.bz2](http://www.livebox-opensource.com/Products/LiveBox/LiveBox2/vFAST3XXX_6813E4/linux-2.6.15.tar.bz2): 


    $ wget -c http://www.livebox-opensource.com/Products/LiveBox/LiveBox2/vFAST3XXX_6813E4/linux-2.6.15.tar.bz2
    --2010-10-24 16:01:31--  http://www.livebox-opensource.com/Products/LiveBox/LiveBox2/vFAST3XXX_6813E4/linux-2.6.15.tar.bz2
    Resolving www.livebox-opensource.com... 161.106.104.24, 161.106.104.127
    Connecting to www.livebox-opensource.com|161.106.104.24|:80... connected.
    HTTP request sent, awaiting response... 206 Partial Content
    Length: 33038873 (32M), 14452378 (14M) remaining [application/x-bzip2]
    Saving to: `linux-2.6.15.tar.bz2'
    
    100%[=====================================================>] 33,038,873   401K/s   in 30s     
    
    2010-10-24 16:02:02 (466 KB/s) - `linux-2.6.15.tar.bz2' saved [33038873/33038873]


Check that the md5sum is equal to "071169d6fc193d6227da60c6fde84937":


    $ md5sum linux-2.6.15.tar.bz2 
    071169d6fc193d6227da60c6fde84937  linux-2.6.15.tar.bz2


Decompress the archive:


    $ tar -xvjf linux-2.6.15.tar.bz2
    tar: Record size = 8 blocks
    linux-2.6.15/
    linux-2.6.15/fs/
    linux-2.6.15/fs/affs/
    linux-2.6.15/fs/affs/Changes
    linux-2.6.15/fs/affs/namei.c
    linux-2.6.15/fs/affs/affs.h
    linux-2.6.15/fs/affs/dir.c
    linux-2.6.15/fs/affs/Makefile
    linux-2.6.15/fs/affs/amigaffs.c
    linux-2.6.15/fs/affs/inode.c
    [...]


# Download the binary toolchain


You can download a [prebuilt toolchain](http://www.livebox-opensource.com/Products/LiveBox/LiveBox2/vFAST3XXX_6813E4/toolchain-mips-linux-uclibc-prebuilt.tar.bz2) for Intel x86 32-bits processors:


    $ wget -c http://www.livebox-opensource.com/Products/LiveBox/LiveBox2/vFAST3XXX_6813E4/toolchain-mips-linux-uclibc-prebuilt.tar.bz2
    --2010-10-24 16:07:49--  http://www.livebox-opensource.com/Products/LiveBox/LiveBox2/vFAST3XXX_6813E4/toolchain-mips-linux-uclibc-prebuilt.tar.bz2
    Resolving www.livebox-opensource.com... 161.106.104.127, 161.106.104.24
    Connecting to www.livebox-opensource.com|161.106.104.127|:80... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 24393650 (23M) [application/x-bzip2]
    Saving to: `toolchain-mips-linux-uclibc-prebuilt.tar.bz2'
    
    100%[===========================================================>] 24,393,650   508K/s   in 51s     
    
    2010-10-24 16:08:40 (469 KB/s) - `toolchain-mips-linux-uclibc-prebuilt.tar.bz2' saved [24393650/24393650]


And verify that the md5dum matches "8a62f9e4451c20f905cf69383c025c92":


    $ md5sum toolchain-mips-linux-uclibc-prebuilt.tar.bz2 
    8a62f9e4451c20f905cf69383c025c92  toolchain-mips-linux-uclibc-prebuilt.tar.bz2


Decompress the archive:


    $ tar -xvjf toolchain-mips-linux-uclibc-prebuilt.tar.bz2 
    tar: Record size = 8 blocks
    mips-linux-uclibc/
    mips-linux-uclibc/mips-linux-uclibc/
    mips-linux-uclibc/mips-linux-uclibc/sys-include
    mips-linux-uclibc/mips-linux-uclibc/bin/
    mips-linux-uclibc/mips-linux-uclibc/bin/g++
    mips-linux-uclibc/mips-linux-uclibc/bin/as
    mips-linux-uclibc/mips-linux-uclibc/bin/ld
    mips-linux-uclibc/mips-linux-uclibc/bin/ranlib
    mips-linux-uclibc/mips-linux-uclibc/bin/c++
    mips-linux-uclibc/mips-linux-uclibc/bin/gcc
    mips-linux-uclibc/mips-linux-uclibc/bin/strip
    mips-linux-uclibc/mips-linux-uclibc/bin/ar
    [...]


# Or build the toolchain yourself from sources


The sources of the toolchain are also available [here](http://www.livebox-opensource.com/Products/LiveBox/LiveBox2/vFAST3XXX_6813E4/toolchain-mips-linux-uclibc.tar.bz2). You can compile the toolchain yourself, for example if you are using a 64bits system.

# Change your PATH environment variable


You need to change your PATH variable in order to have the toolchain compilers in your available binaries:


    $ pwd
    /home/zoobab/soft/bbox2/soft
    $ ls
    linux-2.6.15  linux-2.6.15.tar.bz2  mips-linux-uclibc  toolchain-mips-linux-uclibc-prebuilt.tar.bz2
    $ export PATH="$PATH:$PWD/mips-linux-uclibc/bin"


If your PATH is correct, you should be able to use mips-linux-gcc:


    $ mips-linux-gcc -v
    Reading specs from /home/zoobab/soft/bbox2/soft/mips-linux-uclibc/bin/../lib/gcc/mips-linux-uclibc/3.4.3/specs
    Configured with: /home/floss/FLOSS/orange-floss/Products/LiveBox/LiveBox2/Sagem/FAST3XXX_6813E2/.tmp.13602/toolchain-mips-linux-uclibc/toolchain_build_mips_nofpu/gcc-3.4.3/configure --prefix=/home/floss/FLOSS/orange-floss/Products/LiveBox/LiveBox2/Sagem/FAST3XXX_6813E2/.tmp.13602/toolchain-mips-linux-uclibc/build_mips_nofpu/staging_dir --build=i386-pc-linux-gnu --host=i386-pc-linux-gnu --target=mips-linux-uclibc --enable-languages=c,c++ --enable-shared --disable-__cxa_atexit --enable-target-optspace --with-gnu-ld --disable-nls --enable-multilib --with-float=soft --with-arch=lx4189
    Thread model: posix
    gcc version 3.4.3


# Compile the kernel


Go to the kernel directory and launch the compilation with "make CROSS_COMPILE=mips-linux-":


    $ cd linux-2.6.15
    linux-2.6.15$ make CROSS_COMPILE=mips-linux-


It will then starts to compile the kernel:


    $ make CROSS_COMPILE=mips-linux-
    if test ! /home/zoobab/soft/bbox2/soft/linux-2.6.15 -ef /home/zoobab/soft/bbox2/soft/linux-2.6.15; then \
            /bin/bash /home/zoobab/soft/bbox2/soft/linux-2.6.15/scripts/mkmakefile              \
                /home/zoobab/soft/bbox2/soft/linux-2.6.15 /home/zoobab/soft/bbox2/soft/linux-2.6.15 2 6         \
                > /home/zoobab/soft/bbox2/soft/linux-2.6.15/Makefile;                                 \
                echo '  GEN    /home/zoobab/soft/bbox2/soft/linux-2.6.15/Makefile';                   \
            fi
    set -e; echo '  CHK     include/linux/version.h'; mkdir -p include/linux/;      if [ `echo -n "2.6.15" | wc -c ` -gt 64 ]; then echo '"2.6.15" exceeds 64 characters' >&2; exit 1; fi; (echo \#define UTS_RELEASE \"2.6.15\"; echo \#define LINUX_VERSION_CODE `expr 2 \\* 65536 + 6 \\* 256 + 15`; echo '#define KERNEL_VERSION(a,b,c) (((a) << 16) + ((b) << 8) + (c))'; ) < /home/zoobab/soft/bbox2/soft/linux-2.6.15/Makefile > include/linux/version.h.tmp; if [ -r include/linux/version.h ] && cmp -s include/linux/version.h include/linux/version.h.tmp; then rm -f include/linux/version.h.tmp; else echo '  UPD     include/linux/version.h'; mv -f include/linux/version.h.tmp include/linux/version.h; fi
      CHK     include/linux/version.h
    make -f scripts/Makefile.build obj=scripts/basic
    make[1]: Entering directory `/home/zoobab/soft/bbox2/soft/linux-2.6.15'
    make[1]: Leaving directory `/home/zoobab/soft/bbox2/soft/linux-2.6.15'
    rm -rf .tmp_versions
    mkdir -p .tmp_versions
    make -f scripts/Makefile.build obj=.
    make[1]: Entering directory `/home/zoobab/soft/bbox2/soft/linux-2.6.15'
    mkdir -p arch/mips/kernel/
    make[1]: Leaving directory `/home/zoobab/soft/bbox2/soft/linux-2.6.15'
    make -f scripts/Makefile.build obj=scripts
    make[1]: Entering directory `/home/zoobab/soft/bbox2/soft/linux-2.6.15'
    make -f scripts/Makefile.build obj=scripts/mod
    make[2]: Entering directory `/home/zoobab/soft/bbox2/soft/linux-2.6.15'
      gcc -DCONFIG_HAS_MMU -Wp,-MD,scripts/mod/.modpost.o.d -Wall -Wstrict-prototypes -O2 -fomit-frame-pointer       -c -o scripts/mod/modpost.o scripts/mod/modpost.c
      gcc -DCONFIG_HAS_MMU -Wp,-MD,scripts/mod/.sumversion.o.d -Wall -Wstrict-prototypes -O2 -fomit-frame-pointer       -c -o scripts/mod/sumversion.o scripts/mod/sumversion.c
      gcc -DCONFIG_HAS_MMU  -o scripts/mod/modpost scripts/mod/modpost.o scripts/mod/file2alias.o scripts/mod/sumversion.o  
    make[2]: Leaving directory `/home/zoobab/soft/bbox2/soft/linux-2.6.15'
      gcc -DCONFIG_HAS_MMU -Wp,-MD,scripts/.kallsyms.d -Wall -Wstrict-prototypes -O2 -fomit-frame-pointer       -o scripts/kallsyms scripts/kallsyms.c  
    scripts/kallsyms.c: In function ‘read_symbol’:
    scripts/kallsyms.c:83: warning: ignoring return value of ‘fgets’, declared with attribute warn_unused_result
      gcc -DCONFIG_HAS_MMU -Wp,-MD,scripts/.bin2c.d -Wall -Wstrict-prototypes -O2 -fomit-frame-pointer       -o scripts/bin2c scripts/bin2c.c  
    make[1]: Leaving directory `/home/zoobab/soft/bbox2/soft/linux-2.6.15'
    make -f scripts/Makefile.build obj=init
    make[1]: Entering directory `/home/zoobab/soft/bbox2/soft/linux-2.6.15'
      mips-linux-uclibc-gcc -Wp,-MD,init/.main.o.d  -nostdinc -isystem /home/zoobab/soft/bbox2/soft/mips-linux-uclibc/bin/../lib/gcc/mips-linux-uclibc/3.4.3/include -D__KERNEL__ -Iinclude  -include include/linux/autoconf.h -I../../pkg/include -I/home/zoobab/soft/bbox2/soft/linux-2.6.15/../../pkg/include -D__TARGET__ -Wall -Wundef -Wstrict-prototypes -Wno-trigraphs -fno-strict-aliasing -fno-common -ffreestanding -Os     -fomit-frame-pointer -g  -I /home/zoobab/soft/bbox2/soft/linux-2.6.15/include/asm/gcc -G 0 -mno-abicalls -fno-pic -pipe  -mabi=32 -march=lx4189 -Wa,-32 -Wa,-march=lx4189 -Wa,-mips1 -Iinclude/asm-mips/mach-adi_fusiv -Iinclude/asm-mips/mach-generic -Wdeclaration-after-statement     -DKBUILD_BASENAME=main -DKBUILD_MODNAME=main -c -o init/main.o init/main.c
    init/main.c: In function `init':
    init/main.c:775: warning: implicit declaration of function `rg_load_kernel_modules_initial'
    init/main.c:776: warning: implicit declaration of function `rg_load_kernel_modules'
      CHK     include/linux/compile.h
    /bin/bash /home/zoobab/soft/bbox2/soft/linux-2.6.15/scripts/mkcompile_h include/linux/compile.h \
            "mips" "" "" "mips-linux-uclibc-gcc -Wall -Wundef -Wstrict-prototypes -Wno-trigraphs -fno-strict-aliasing -fno-common -ffreestanding -Os     -fomit-frame-pointer -g  -I /home/zoobab/soft/bbox2/soft/linux-2.6.15/include/asm/gcc -G 0 -mno-abicalls -fno-pic -pipe  -mabi=32 -march=lx4189 -Wa,-32 -Wa,-march=lx4189 -Wa,-mips1 -Iinclude/asm-mips/mach-adi_fusiv -Iinclude/asm-mips/mach-generic -Wdeclaration-after-statement "
      UPD     include/linux/compile.h
    [...]


The full log output is [[file bbox2-kernel-compilation.txt | here]].

And the end of the process, you should have a kernel of 24MB:


    $ ls -lha vmlinux
    -rwxr-xr-x 1 zoobab zoobab 24M 2010-10-24 16:50 vmlinux


# Dotconfig


The [[file dotconfig.txt | .config file]] given with the tar.bz2 archive seems really modified compared to the vanilla kernel 2.6.15:


    ARCH=mips
    AR=mips-linux-uclibc-ar
    AS=mips-linux-uclibc-as
    BOARD=F@ST 3202
    CC=mips-linux-uclibc-gcc
    CONFIG_OPENRG=y
    CONFIG_RG_KOS_FEATURE=y
    CONFIG_RG_IGMP_PROXY=y
    CONFIG_32BIT=y
    CONFIG_ARCH_AD6834_FAST3202=y
    CONFIG_ATM_BR2684=y
    CONFIG_ATM_CLIP=m
    CONFIG_ATM=y
    CONFIG_BASE_SMALL=0
    CONFIG_BINFMT_ELF=y
    CONFIG_BLK_DEV_SD=y
    CONFIG_BOOT_ELF32=y
    CONFIG_BT_BNEP_MC_FILTER=y
    CONFIG_BT_BNEP_PROTO_FILTER=y
    CONFIG_BT_BNEP=y
    CONFIG_BT_L2CAP=y
    CONFIG_BT_RFCOMM=y
    CONFIG_BT_SCO=y
    CONFIG_BT=y
    CONFIG_BUG=y
    CONFIG_CC_OPTIMIZE_FOR_SIZE=y
    CONFIG_CMDLINE=console=ttyS0,57600 quiet
    CONFIG_CPU_BIG_ENDIAN=y
    CONFIG_CPU_LX4189=y
    CONFIG_CRAMFS_DYN_BLOCKSIZE=y
    CONFIG_CRAMFS=y
    CONFIG_CRC32=y
    CONFIG_CROSSCOMPILE=y
    CONFIG_CRYPTO_AES=y
    CONFIG_CRYPTO_HMAC=y
    CONFIG_CRYPTO_MD5=y
    CONFIG_CRYPTO_SHA1=y
    CONFIG_CRYPTO=y
    CONFIG_DEBUG_INFO=y
    CONFIG_DEFAULT_IOSCHED="anticipatory"
    CONFIG_DMA_NONCOHERENT=y
    CONFIG_ETH_SWITCH=y
    CONFIG_EXT2_FS=y
    CONFIG_EXT3_FS=y
    CONFIG_FAT_DEFAULT_CODEPAGE=437
    CONFIG_FAT_DEFAULT_IOCHARSET="iso8859-1"
    CONFIG_FAT_FS=y
    CONFIG_FLATMEM=y
    CONFIG_FLAT_NODE_MEM_MAP=y
    CONFIG_FORCE_RECOVERY=y
    CONFIG_GENERIC_CALIBRATE_DELAY=y
    CONFIG_GENERIC_HARDIRQS=y
    CONFIG_HOTPLUG=y
    CONFIG_HW_BLUETOOTH=y
    CONFIG_IKCONFIG_PROC=y
    CONFIG_IKCONFIG=y
    CONFIG_INET_AH=y
    CONFIG_INET=y
    CONFIG_INIT_ENV_ARG_LIMIT=32
    CONFIG_INITRAMFS_ROOT_GID=$(shell id -g)
    CONFIG_INITRAMFS_ROOT_UID=$(shell id -u)
    CONFIG_INITRAMFS_SOURCE=$(RAMDISK_MOUNT_POINT)
    CONFIG_INOTIFY=y
    CONFIG_IOSCHED_NOOP=y
    CONFIG_IP_ADVANCED_ROUTER=y
    CONFIG_IP_FIB_HASH=y
    CONFIG_IP_MULTICAST=y
    CONFIG_IP_MULTIPLE_TABLES=y
    CONFIG_IP_ROUTE_FWMARK=y
    CONFIG_IP_ROUTE_MULTIPATH=y
    CONFIG_IP_ROUTE_VERBOSE=y
    CONFIG_JBD=y
    CONFIG_JFFS2_FS=y
    CONFIG_KALLSYMS=y
    CONFIG_KMOD=y
    CONFIG_LEGACY_PTY_COUNT=256
    CONFIG_LEGACY_PTYS=y
    CONFIG_LOG_BUF_SHIFT=14
    CONFIG_MACH_ADI_FUSIV=y
    CONFIG_MAGIC_SYSRQ=y
    CONFIG_MIPS_L1_CACHE_SHIFT=5
    CONFIG_MIPS_PATENTFREE=y
    CONFIG_MIPS=y
    CONFIG_MMU=y
    CONFIG_MODULES=y
    CONFIG_MODULE_UNLOAD=y
    CONFIG_MSDOS_FS=y
    CONFIG_MSDOS_PARTITION=y
    CONFIG_MTD_BLOCK=y
    CONFIG_MTD_CFI_AMDSTD=y
    CONFIG_MTD_CFI_I1=y
    CONFIG_MTD_CFI_I2=y
    CONFIG_MTD_CFI_UTIL=y
    CONFIG_MTD_CFI=y
    CONFIG_MTD_GEN_PROBE=y
    CONFIG_MTD_MAP_BANK_WIDTH_1=y
    CONFIG_MTD_MAP_BANK_WIDTH_2=y
    CONFIG_MTD_MAP_BANK_WIDTH_4=y
    CONFIG_MTD_PARTITIONS=y
    CONFIG_MTD=y
    CONFIG_NET_CLS_FW=y
    CONFIG_NET_CLS_POLICE=y
    CONFIG_NET_CLS_RSVP6=y
    CONFIG_NET_CLS_RSVP=y
    CONFIG_NET_CLS_TCINDEX=y
    CONFIG_NET_CLS_U32=y
    CONFIG_NET_CLS=y
    CONFIG_NETDEVICES=y
    CONFIG_NET_ESTIMATOR=y
    CONFIG_NET_ETHERNET=y
    CONFIG_NETFILTER=y
    CONFIG_NET_RADIO=y
    CONFIG_NET_SCH_ATM=y
    CONFIG_NET_SCH_CLK_JIFFIES=y
    CONFIG_NET_SCH_DSMARK=y
    CONFIG_NET_SCHED=y
    CONFIG_NET_SCH_HTB=y
    CONFIG_NET_SCH_INGRESS=y
    CONFIG_NET_SCH_PRIO=y
    CONFIG_NET_SCH_RED=y
    CONFIG_NET_SCH_SFQ=y
    CONFIG_NET_SCH_TBF=y
    CONFIG_NET_WIRELESS=y
    CONFIG_NET=y
    CONFIG_NLS_CODEPAGE_437=y
    CONFIG_NLS_CODEPAGE_850=y
    CONFIG_NLS_DEFAULT="437"
    CONFIG_NLS_ISO8859_1=y
    CONFIG_NLS_UTF8=y
    CONFIG_NLS=y
    CONFIG_NTFS_FS=y
    CONFIG_OBSOLETE_MODPARM=y
    CONFIG_OPENRG=y
    CONFIG_PACKET=y
    CONFIG_PAGE_SIZE_4KB=y
    CONFIG_PCI=y
    CONFIG_PRINTK=y
    CONFIG_PROC_FS=y
    CONFIG_RAMFS=y
    CONFIG_RG_BLUETOOTH=y
    CONFIG_RG_INITFS_RAMFS=y
    CONFIG_RG_MAINFS=y
    CONFIG_RG_MAINFS_CRAMFS=y
    CONFIG_RWSEM_GENERIC_SPINLOCK=y
    CONFIG_SAGEM_FTTHV2=y
    CONFIG_SAGEM_GENERIC_CARD_SUPPORT=y
    CONFIG_SAGEM_LBV2ULT=y
    CONFIG_SAGEM_USB_HOST=y
    CONFIG_SCSI=y
    CONFIG_SERIAL_8250_CONSOLE=y
    CONFIG_SERIAL_8250_NR_UARTS=1
    CONFIG_SERIAL_8250=y
    CONFIG_SERIAL_CORE_CONSOLE=y
    CONFIG_SERIAL_CORE=y
    CONFIG_SOFTIRQ_THROTTLE=y
    CONFIG_SPLIT_PTLOCK_CPUS=4
    CONFIG_SYN_COOKIES=y
    CONFIG_SYSCTL=y
    CONFIG_SYSFS=y
    CONFIG_SYSVIPC=y
    CONFIG_TINY_SHMEM=y
    CONFIG_TOS_DSCP_RFC2474=y
    CONFIG_TRAD_SIGNALS=y
    CONFIG_UNIX=y
    CONFIG_USB_ARCH_HAS_HCD=y
    CONFIG_USB_ARCH_HAS_OHCI=y
    CONFIG_USB_DEVICEFS=y
    CONFIG_USB_EHCI_HCD=m
    CONFIG_USB_OHCI_HCD=m
    CONFIG_USB_PRINTER=y
    CONFIG_USB_SERIAL_CP2101=m
    CONFIG_USB_SERIAL=m
    CONFIG_USB_STORAGE=y
    CONFIG_USB=y
    CONFIG_VFAT_FS=y
    CONFIG_VLAN_8021Q=y
    CONFIG_XFRM=y
    CONFIG_ZLIB_DEFLATE=y
    CONFIG_ZLIB_INFLATE=y
    CROSS_COMPILE=mips-linux-uclibc-
    GCC_VERSION=3.4.3
    HOSTCC=gcc -DCONFIG_HAS_MMU
    LD=mips-linux-uclibc-ld
    NM=mips-linux-uclibc-nm
    NUM_PHYS=2
    OBJCOPY=mips-linux-uclibc-objcopy
    OBJDUMP=mips-linux-uclibc-objdump
    RANLIB=mips-linux-uclibc-ranlib
    SIZE=mips-linux-uclibc-size
    STRIP=mips-linux-uclibc-strip


# Todo


* Make a diff between the released kernels and the vanilla kernels of kernel.org
* Compile the toolchains
* Find a way to reduce the kernel size (remove symbols, etc...)
* Try to just compile a simple kernel module and load it on the bbox2

# Comments


[[module Comments]]