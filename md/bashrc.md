# .bashrc


Put this [[file bashrc | .bashrc]] in your home directory:


    PS1='\[\033[35;1m\]\u\[\033[0m\]@\[\033[31;1m\]\h \[\033[32;1m\]$PWD\[\033[0m\] [\[\033[35m\]\#\[\033[0m\]]\[\033[31m\]\$\[\033[0m\] '
    alias u="cd .."
    alias ll="ls -lA --color=yes | less -r -E -X"
    alias l="ls -l --color=yes "
    alias p="ping -c 3 google.com"


# .bashrc with git prompt


If you want the GIT branch in your prompt, you can change the PS1 to be (you need to have git installed):


    parse_git_branch() {
          git rev-parse --abbrev-ref HEAD 2> /dev/null
    }
    PS1='\[\033[35;1m\]\u\[\033[0m\]@\[\033[31;1m\]\h \[\033[32;1m\]$PWD\[\033[0m\] [$(parse_git_branch)] $ '
    alias u="cd .."
    alias ll="ls -lA --color=yes | less -r -E -X"
    alias l="ls -l --color=yes "
    alias p="ping -c 3 google.com"


# Shell prompt


It will give you a shell prompt like this:

[[=image bashrc.png]]

# Other examples


## Red prompt


With a red shell (this [[file bashrc-red | .bashrc]]), similar to the gentoo's bash prompt:


    export PS1='\[\033[01;31m\]\u@\h\[\033[01;34m\] $PWD \[\033[00m\]$ '
    alias l='ls --color=auto'
    alias grep='grep --color=auto'
    alias ll='ls -lA --color=yes'


Screenshot:

[[=image bashrc-red.png]]

## Green prompt


With a green shell (this [[file bashrc-green | .bashrc]]):


    export PS1='\[\033[01;32m\]\u@\h\[\033[01;34m\] $PWD \[\033[00m\]$ '
    alias l='ls --color=auto'
    alias grep='grep --color=auto'
    alias ll='ls -lA --color=yes'


Screenshot:

[[=image bashrc-green.png]]

## Yellow prompt


With a yellow shell (this [[file bashrc-yellow | .bashrc]]):


    export PS1='\[\033[01;33m\]\u@\h\[\033[01;34m\] $PWD \[\033[00m\]$ '
    alias l='ls --color=auto'
    alias grep='grep --color=auto'
    alias ll='ls -lA --color=yes'


Screenshot:

[[=image bashrc-yellow.png]]