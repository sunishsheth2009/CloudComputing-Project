ssh node0
virsh destroy $1
qemu-img resize /home/images/$1.qcow2 +$2G
virsh start $1
sleep 60
ssh $1
<PASSWORD>
fdisk /dev/vda
n
p
3


t
3
8e
w
reboot
sleep 60 or ssh node0
ssh $1
<password>
pvcreate /dev/vda3
vgextend centos /dev/vda3
lvextend /dev/centos/root /dev/vda3
xfs_growfs /dev/centos/root
