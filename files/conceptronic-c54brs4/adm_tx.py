#!/usr/bin/env python
"""
   Upload firmware to ADM5120 router.

   biffer@yahoo.co.uk  2007
"""
import fdpexpect, os, sys, tempfile, struct, termios
from optparse import OptionParser


g_usage = "%prog [options] <filename>"

g_description = """
Waits for the ADM5120 to power up, then transfers the specified
kernel image to the DRAM/FLASH.  %prog will try to remind you if you're
writing to FLASH ram and you've forgotten the CSYS header.  It can
also create a temporary file adding/removing the CSYS header as it
does so.  You need to 1) Switch off the router, 2) Run this program then
3) Switch on the router.
"""

opt = OptionParser(version="%prog v2.1", usage=g_usage, 
                   description=g_description)
opt.add_option("-i","--image", dest="image", default="vmlinuz",
               help="Image to send (default: %default)")
opt.add_option("-d","--device", dest="device", default="/dev/tts/USB0",
               help="Communication device (default: %default)")
opt.add_option("-b","--burn", dest="burn", action="store_true", 
               help="'Burn' to flash (default: load to SDRAM)")
opt.add_option("-f","--force", dest="force", action="store_true", 
               help="Try to fix the image so it matches the action, i.e. "
                    "add/remove CSYS header as necessary. (default: No)")
(opts, args) = opt.parse_args()

if not os.path.isfile(opts.image) or args :
	opt.print_help()
	sys.exit(0)


def SetupSerial(device) :
  print "Setting device '%s' to 112500, 8N1" % device
  fd = os.open(device, os.O_RDWR)
  params = termios.tcgetattr(fd)
  params[0] = termios.IGNBRK        # iflag, 1
  params[1] = 0                     # oflag, 0
  # cflag:  0x18b2
  params[2] = (termios.CS8 |     # 0x30    8-bit data
              termios.CLOCAL |   # 0x800   ignore modem ctrl lines.
              termios.CBAUDEX |  # 0x1000
              termios.CREAD |    # 0x80
              params[2] & 2)     # leave bit 2 as-is.
  params[3] = 0                  # lflag
  params[4] = termios.B115200   # ispeed
  params[5] = termios.B115200   # ospeed
  # leave cc flags as-is.
  termios.tcsetattr(fd, termios.TCSANOW, params)


def Upload(image, device, burn) :

  print "Connecting to serial device...",
  fd = os.open(device, os.O_RDWR|os.O_NONBLOCK|os.O_NOCTTY)
  print fd
  m = fdpexpect.fdspawn(fd)

  print "Waiting for device to be switched on...."

  # Wait for device to power up
  m.expect("ADM5120 Boot:")

  # Three spaces to interrupt the boot
  m.send("   ")
  m.expect("Please enter your key : ")

  # Download to sdram...
  if burn :
    print "Writing image to flash..."
    m.send("a")
  else :
    print "Writing image to SDRAM..."
    m.send("b")

  m.expect("Downloading........")
  # type some random garbage to make the transfer work.
  m.send("sdfgdshh")

  # Done with expect, close the device
  del m

  # Open the xmodem program to send the file.  We don't use
  # 'sx' here, but instead 'lsz -X' because 'sx' doesn't work on 
  # Slackware 11.0
  os.system("lsz -X -vv %s > %s < %s" % (image, device, device) )

  # re-connect to serial device
  fd = os.open(device, os.O_RDWR|os.O_NONBLOCK|os.O_NOCTTY)
  m = fdpexpect.fdspawn(fd)

  # Connect to the terminal
  m.interact()


g_magic = "CSYS\x00\x00\x50\x80"


def Check(burn, data, fname) :
  print "Checking image '%s' matches intended destination..." % fname
  if data.startswith(g_magic) :
    if not burn :
      print "'%s' has CSYS header but you're trying to write it to SDRAM." % fname
      sys.exit(-1)
  else :
    if burn :
      print "'%s' has no CSYS header but you're trying to write it to FLASH." % fname
      sys.exit(-1)


def Fixup(burn, data, fname) :
  print "Fixing up image '%s' for intended destination..." % fname
  if burn :
    if not data.startswith(g_magic) :
      print "Adding CSYS header."
      fd,oname = tempfile.mkstemp(".bin","kernel_image","./")
      os.close(fd)
      print "Creating temporary image file '%s'" % oname
      odata = g_magic + struct.pack("l",len(data)) + data
      file(oname,"wb").write(odata)
      return oname
  else :
    if data.startswith(g_magic) :
      print "Removing CSYS header."
      odata = data[12:]
      file(oname,"wb").write(data)
      return oname
  return fname

  

data = file(opts.image,"rb").read()
if opts.force :
  tosend = Fixup(opts.burn, data, opts.image)
else :
  Check(opts.burn, data, opts.image)
  tosend = opts.image
SetupSerial(opts.device)
Upload(tosend, opts.device, opts.burn)
if opts.force :
  os.unlink(tosend)



