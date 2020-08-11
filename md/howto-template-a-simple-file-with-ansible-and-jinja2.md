# About


How to template a simple file with Ansible and Jinja2.

# Template


Let's consider a simple template file named "myfile.txt.j2" in jinja2 format, where a variable named "secondword" will be replaced:


    $ cat myfile.txt.j2
    Lorem {{ secondword }} dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.


You should put this file in a directory called "templates":


    $ mkdir -pv templates
    $ mv myfile.txt.j2


Go back to the upper directory, the directory structure should look like:


    $ cd ..
    $ find ./
    ./
    ./templates
    ./templates/myfile.txt.j2


Let's launch ansible to do the templating job to an output file located in "/tmp/myfile.txt":


    $ ansible all -i "localhost," -c local -m template -a "src=myfile.txt.j2 dest=/tmp/myfile.txt" --extra-vars='{"secondword": "ipsum"}'
    localhost | SUCCESS => {
        "changed": true,
        "checksum": "4518012e1b365e504001dbc94120624f15b8bbd5",
        "dest": "/tmp/myfile.txt",
        "gid": 1000,
        "group": "centos",
        "md5sum": "edc715389af2498a623134608ba0a55b",
        "mode": "0664",
        "owner": "centos",
        "secontext": "unconfined_u:object_r:user_home_t:s0",
        "size": 446,
        "src": "/home/centos/.ansible/tmp/ansible-tmp-1537774107.54-44748629310806/source",
        "state": "file",
        "uid": 1000
    }


It should generate a file:


    $ cat /tmp/myfile.txt
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


If you don't provide the right arguments, it should fail and give you an error exit code:


    $ ansible all -i "localhost," -c local -m template -a "src=myfile.txt.j2 dest=/tmp/myfile.txt" --extra-vars='{}'
    localhost | FAILED! => {
        "changed": false,
        "msg": "AnsibleUndefinedVariable: 'secondword' is undefined"
    }
    $ echo $?
    2


# Use environment variables as extra vars


You can also use environment variables as extra vars:


    $ ansible-playbook -i "localhost," ldap.yaml --extra-vars="LDAP_HOST={{ lookup('env', 'LDAP_HOST') }} clustername=mycluster env=dev LDAP_USERNAME={{ lookup('env', 'LDAP_USERNAME') }} LDAP_PASSWORD={{ lookup('env', 'LDAP_PASSWORD') }}"


You need to set the variables LDAP_HOST, LDAP_USERNAME, LDAP_PASSWORD with export:


    $ export LDAP_HOST=127.0.0.1
    $ export LDAP_USERNAME=myuser
    $ export LDAP_PASSWORD=mypass
