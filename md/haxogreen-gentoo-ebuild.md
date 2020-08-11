# Hello world


<http://www.zoobab.com/local--files/haxogreen-gentoo-ebuild/hellozoo-0.1.tar.gz>  

# Ebuild example: hellozoo-0.1.ebuild



    # Copyright 1999-2012 Gentoo Foundation
    # Distributed under the terms of the GNU General Public License v2
    # $Header: $
    
    EAPI=4
    
    inherit eutils
    
    DESCRIPTION="zoobab hello world for haxogreen"
    HOMEPAGE="http://www.zoobab.com/haxogreen-gentoo-ebuild"
    SRC_URI="http://www.zoobab.com/local--files/haxogreen-gentoo-ebuild/hellozoo-0.1.tar.gz"
    
    LICENSE="BSD"
    SLOT="0"
    KEYWORDS="amd64"
    IUSE=""
    
    DEPEND=""
    RDEPEND="${DEPEND}"
    src_compile() {
    		emake || die
    }
    
    src_install() {
    	exeinto /usr/sbin
    		doexe hellozoo || die
    }


# Emerge


    root@gentoo3 /var/lib/layman/zoobab/app-misc/hellozoo [330]# emerge -1 hellozoo
    
     * IMPORTANT: 2 news items need reading for repository 'gentoo'.
     * Use eselect news to read news items.
    
    Calculating dependencies... done!
    
    >>> Verifying ebuild manifests
    
    >>> Emerging (1 of 1) app-misc/hellozoo-0.1 from x-zoobab
     * hellozoo-0.1.tar.gz RMD160 SHA1 SHA256 size ;-) ...                                                                                                                                                       [ ok ]
    >>> Unpacking source...
    >>> Unpacking hellozoo-0.1.tar.gz to /var/tmp/portage/app-misc/hellozoo-0.1/work
    >>> Source unpacked in /var/tmp/portage/app-misc/hellozoo-0.1/work
    >>> Preparing source in /var/tmp/portage/app-misc/hellozoo-0.1/work/hellozoo-0.1 ...
    >>> Source prepared.
    >>> Configuring source in /var/tmp/portage/app-misc/hellozoo-0.1/work/hellozoo-0.1 ...
    >>> Source configured.
    >>> Compiling source in /var/tmp/portage/app-misc/hellozoo-0.1/work/hellozoo-0.1 ...
     * Compilation started ...
    make 
    gcc -o hellozoo hellozoo.c                                                                                                                                                                                   [ ok ]
    >>> Source compiled.
    >>> Test phase [not enabled]: app-misc/hellozoo-0.1
    
    >>> Install hellozoo-0.1 into /var/tmp/portage/app-misc/hellozoo-0.1/image/ category app-misc
     * Installing in /usr/sbin ...                                                                                                                                                                               [ ok ]
    >>> Completed installing hellozoo-0.1 into /var/tmp/portage/app-misc/hellozoo-0.1/image/
    
    strip: x86_64-pc-linux-gnu-strip --strip-unneeded -R .comment -R .GCC.command.line
       usr/sbin/hellozoo
    
    >>> Installing (1 of 1) app-misc/hellozoo-0.1
    >>> Auto-cleaning packages...
    
    >>> No outdated packages were found on your system.
    
     * GNU info directory index is up-to-date.
    
     * IMPORTANT: 2 news items need reading for repository 'gentoo'.
     * Use eselect news to read news items.
    
    root@gentoo3 /var/lib/layman/zoobab/app-misc/hellozoo [331]#


# Uwfirmforce example


<http://www.zoobab.com/local--files/haxogreen-gentoo-ebuild/uwfirmforce-0.0.7.tar.gz>  