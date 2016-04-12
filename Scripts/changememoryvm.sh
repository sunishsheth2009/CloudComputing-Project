virsh destroy $1
cd /etc/libvirt/qemu/
virsh setmaxmem $1 $2 --config
sed -i -r "s/<currentMemory.*>/<currentMemory unit='KiB'>$2<\\/currentMemory>'/g" $1.xml
virsh create /etc/libvirt/qemu/$1.xml
