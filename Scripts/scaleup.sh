sudo qemu-img resize /home/images/$1.qcow2 +$2G
qemu-img info /home/images/$1.qcow2
virt-filesystems --long -h --all -a /home/images/$1.qcow2
