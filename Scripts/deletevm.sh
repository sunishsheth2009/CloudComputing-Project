virsh destroy $1
virsh undefine $1
rm /home/images/$1.qcow2
