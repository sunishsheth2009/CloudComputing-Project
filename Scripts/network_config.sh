UUID=$('uuidgen')

echo 'TYPE="Ethernet"
BOOTPROTO="static"
DEFROUTE="yes"
IPV4_FAILURE_FATAL="no"
IPV6INIT=no
NAME="eth0"
UUID='$UUID'
DEVICE="eth0"
ONBOOT="yes"
PEERDNS=yes
PEERROUTES=yes
GATEWAY=192.168.1.1
NETWORK=192.168.1.0
DNS1=8.8.8.8
DNS2=8.8.4.4
IPADDR=192.168.1.15' > /etc/sysconfig/network-scripts/ifcfg-eth0
