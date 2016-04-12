#!/usr/bin/expect

service nfs stop

service nfs start

exportfs -a

ssh node1 mount node0:/var/lib/libvirt/images /var/lib/libvirt/images	

ssh node2 mount node0:/var/lib/libvirt/images /var/lib/libvirt/images

iptables -F


