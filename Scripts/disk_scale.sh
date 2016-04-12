#!/usr/bin/expect -f
virsh destroy $1
qemu-img resize /home/images/$1.qcow2 +$2
virsh start $1
sleep 60

