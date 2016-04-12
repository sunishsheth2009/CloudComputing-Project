sleep 60
pvcreate /dev/vda3
vgextend centos /dev/vda3
lvextend /dev/centos/root /dev/vda3
xfs_growfs /dev/centos/root
