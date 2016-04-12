#!/bin/sh
cp /home/images/$5.qcow2 /home/images/$2.qcow2
cp /etc/libvirt/qemu/vanilla.xml /etc/libvirt/qemu/$2.xml
if [ $6 == 'yes' ]
then
   virsh destroy $5
   virsh undefine $5
   rm /home/images/$5.qcow2
fi
UUID=$('uuidgen')
cd /etc/libvirt/qemu/
sed -i -r "s/<name>.*>/<name>$2<\\/name>/g" $2.xml
sed -i -r "s/<uuid>.*>/<uuid>$UUID<\\/uuid>/g" $2.xml
sed -i -r "s/<source file=.*>/<source file='\\/home\\/images\\/$2.qcow2'\\/>/g" $2.xml
sed -i -r "s/<memory.*>/<memory unit='KiB'>$3<\\/memory>'/g" $2.xml
sed -i -r "s/<currentMemory.*>/<currentMemory unit='KiB'>$3<\\/currentMemory>'/g" $2.xml
sed -i -r "s/<vcpu.*>/<vcpu placement='static'>$4<\\/vcpu>'/g" $2.xml
sed -i -r "s/<topology.*>/<topology sockets='1' cores='$7' threads='$8'\\/>'/g" $2.xml
virsh define $2.xml
virsh create $2.xml

sleep 30
virsh destroy $2
sed -i -r "s/IPADDR=192.*'/IPADDR=$7'/g" /home/images/network_config.sh
virt-sysprep --run /home/images/network_config.sh -d $2
virsh start $2
