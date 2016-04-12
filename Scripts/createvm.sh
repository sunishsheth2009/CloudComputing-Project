cp /home/images/vanilla.qcow2 /home/images/$2.qcow2
cp /etc/libvirt/qemu/vanilla.xml /etc/libvirt/qemu/$2.xml
UUID=$('uuidgen')
cd /etc/libvirt/qemu/
sed -i -r "s/<name>.*>/<name>$2<\\/name>/g" $2.xml
sed -i -r "s/<uuid>.*>/<uuid>$UUID<\\/uuid>/g" $2.xml
sed -i -r "s/<source file=.*>/<source file='\\/home\\/images\\/$2.qcow2'\\/>/g" $2.xml
sed -i -r "s/<memory.*>/<memory unit='KiB'>$3<\\/memory>'/g" $2.xml
sed -i -r "s/<currentMemory.*>/<currentMemory unit='KiB'>$3<\\/currentMemory>'/g" $2.xml
sed -i -r "s/<vcpu.*>/<vcpu placement='static'>$4<\\/vcpu>'/g" $2.xml
sed -i -r "s/<topology.*>/<topology sockets='1' cores='$5' threads='$6'\\/>'/g" $2.xml
virsh define $2.xml
virsh create $2.xml

sleep 30
virsh destroy $2
sed -i -r "s/IPADDR=192.*'/IPADDR=$7'/g" /home/images/network_config.sh
virt-sysprep --run /home/images/network_config.sh -d $2
virsh start $2

#virsh setmaxmem $2 $3 --config
#<maxMemory slots='16' unit='KiB'>1524288</maxMemory>
#spawn ssh root@node$1
#expect "password"
#send "cloud123\r"
#interact
#exit
#sed -i -r 's/IPADDRESS=[0-9].+/IPADDRESS=192.168.1.15/g' $2.xml

#virsh snapshot-create-as $1 $2 "Vm Migration" --diskspec vda,file=/home/images/$3 --disk-only --atomic
#cd /etc/libvirt/qemu/
#cp $1.xml $2.xml

#<source file='/home/images/snap2-testvm.qcow2'/>
#sed -i -r 's/<source file=\\'[a-z]\\/+\\'/<source file=\\'/home/images/testvm.qcow2\\'/g' test.sh
#sed -i -r 's/<source file=\\'/<source file=\\'123/g' test.sh
#sed -i -r "s/<source file=.*$>/hello/g" test.sh
