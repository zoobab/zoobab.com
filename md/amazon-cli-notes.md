Amazon has a nice CLI but complex, but it took me while to figure out how to get a decent table output, it is crazzy there is no shorter version for humans:


    $ aws ec2 describe-instances  --query "Reservations[*].Instances[*].{name: Tags[?Key=='Name'] | [0].Value, instance_id: InstanceId, ip_address: PrivateIpAddress, state: State.Name}" --output table
    -------------------------------------------------------------------------
    |                           DescribeInstances                           |
    +----------------------+----------------+--------------------+----------+
    |      instance_id     |  ip_address    |       name         |  state   |
    +----------------------+----------------+--------------------+----------+
    |  i-01792bad6fe501f21 |  172.16.4.33   |  openshift-node    |  running |
    |  i-00737320c29b05758 |  172.16.4.31   |  openshift-master  |  running |
    |  i-06542424c7ceffdf7 |  172.16.5.239  |  openshift-node    |  running |
    |  i-00dcbc35c4386e2e2 |  172.31.34.172 |  bhenrion5         |  running |
    |  i-09ec084ed1a74a5de |  172.16.6.121  |  openshift-node    |  running |
    |  i-032812c51b79062f1 |  10.68.3.79    |  None              |  running |
    +----------------------+----------------+--------------------+----------+


AWS for humans!