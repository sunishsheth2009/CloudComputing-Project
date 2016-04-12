virsh destroy $1
cd /etc/libvirt/qemu/
sed -i -r "s/<vcpu.*>/<vcpu placement='static'>$2<\\/vcpu>'/g" $1.xml
sed -i -r "s/<topology.*>/<topology sockets='1' cores='$3' threads='$4'\\/>'/g" $1.xml
virsh create /etc/libvirt/qemu/$1.xml
