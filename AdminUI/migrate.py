import subprocess

from subprocess import call


node0_virt_id_list = []

node0_string = subprocess.check_output("virsh list",shell=True)

stringss = node0_string.split();

text_file = open("Output.txt", "w")

i=0

for s in stringss:
	if i==5 or i==8 or i==11 or i==14 or i==17:
		text_file.write(s)
		text_file.write('\n')
		print s
	i+=1


text_file.close()



