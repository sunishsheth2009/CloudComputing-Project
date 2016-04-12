virt-install --virt-type kvm --name centos-6.4 --ram 1024 \
--cdrom=/data/CentOS-6.4-x86_64-netinstall.iso \
--disk path=/home/images/centos7.0.qcow2,size=10,format=qcow2 \
--network network=default \
--graphics vnc,listen=0.0.0.0 --noautoconsole \
--os-type=linux --os-variant=rhel6
 
qemu-img create -f qcow2 /home/images/node0_virt1.qcow2 12G

sudo virt-install --connect qemu:///system -n node0_virt2 -r 512 -f /home/images/centos7.1.qcow2 -s 12 -c /home/node0/Downloads/CentOS-7-x86_64-Everything-1503-01.iso --vnc --noautoconsole --os-type linux --os-variant linux