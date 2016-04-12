brctl addbr br0
brctl addif br0 em1
dhclient br0
iptables -A FORWARD --in-interface em1 --out-interface br0 -p tcp -d 192.168.1.0/255.255.255.0 --destination-port ssh -j ACCEPT
iptables-save
