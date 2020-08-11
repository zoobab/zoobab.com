# Man page amq_client.1



    .TH AMQ_CLIENT 1 "June 2009" "Version 1.4b3"
    .SH NAME
    amq_client - a client for the OpenAMQ messaging server
    .SH SYNOPSIS
    .B amq_client
    [options]
    .SH DESCRIPTION
    .BI amq_client
    a client for the OpenAMQ messaging server
    .SH OPTIONS
    .TP
    .I -s <server>:<port>
    Name or address, port of server (default = localhost)
    .TP
    .I -n <number>
    Number of messages to send/receive (default = 1)
    .TP
    .I -x <size>
    Size of each message (default = 1024)
    .TP
    .I -r <repeat>
    Repeat test N times (default = 1)
    .TP
    .I -t <level>
    Set trace level (default = 0)
    .TP
    .I -e <exchange>
    Exchange name (amq.direct) (0=none, 1=low, 2=medium, 3=high)
    .TP
    .I -d
    Use Direct Mode
    .TP
    .I -v
    Show version information
    .TP
    .I -h
    Show summary of command-line options
    .SH EXAMPLES
    amq_client \-n 10000 \-x 500 \-r 0
    .SH AUTHOR
    This manual page was written by Benjamin Henrion <bh@udev.org> for the Debian systems.
    .SH SEE ALSO
    .br
    .B amq_server(1)
    .br
    .B amq_server.cfg(1)
    .br
    .B amq_shell(1)
    .br
    .B zyre(1)


# Man page amq_server.1



    .TH AMQ_SERVER 1 "June 2009" "Version 1.4b3"
    .SH NAME
    amq_server - the OpenAMQ messaging server
    .SH SYNOPSIS
    .B amq_server
    [options]
    .SH DESCRIPTION
    .BI amq_client
    the OpenAMQ messaging server
    .SH OPTIONS
    .TP
    .I -w <directory>
    Working directory for server (default = current)
    .TP
    .I -s <filename>
    Load custom settings from file (default = amq_server.cfg)
    .TP
    .I -S <filename>
    Snapshot server settings to file
    .TP
    .I -X <comment>
    Comment, has no effect
    .TP
    .I -q
    Quiet mode: no messages (default = no)
    .TP
    .I -b
    Run as background server process (default = no)
    .TP
    .I -f
    Run as foreground console process (default = yes)
    .TP
    .I -i
    Show program statistics when ending (default = no)
    .TP
    .I -v
    Show version information
    .TP
    .I -h
    Show summary of command-line options
    .TP
    .I --help
    Show detailed configuration help
    .TP
    .I --port <portnumber>
    Server port for clients
    .TP
    .I --listen <ipadress>
    Address (local network interface) to listen on
    .TP
    .I --queue_timeout <numberofsecs>
    Timeout for auto-deleted queues, in seconds
    .SH EXAMPLES
    amq_server \-n 10000 \-x 500 \-r 0
    .SH AUTHOR
    This manual page was written by Benjamin Henrion <bh@udev.org>
    .SH SEE ALSO
    .br
    .B amq_server(1)
    .br
    .B amq_server.cfg(1)
    .br
    .B amq_shell(1)
    .br
    .B zyre(1)
