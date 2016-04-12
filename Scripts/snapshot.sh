virsh snapshot-list node1_virt1
cd /var/lib/libvirt/qemu/snapshot/$2
virsh snapshot-delete node1_virt1 --metadata 1445112750
