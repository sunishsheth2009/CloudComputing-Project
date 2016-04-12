#!/usr/bin/python
import os, sys
import subprocess
from subprocess import call
from random import randint
import time

userDetails={}
nodeDetails={}
vmDetails={}
nodesAvailable=[]
vmAvailable=[]
#path = '/Users/Sunish/BitBucket/Iaas-cloud-project/Scripts/userdetails.txt'
path = '/home/node0/Documents/Scripts/userdetails.txt'
def main():

	if len(sys.argv) > 1 and len(sys.argv) < 13:

		if sys.argv[1] == 'loadbalance':
			if len(sys.argv) != 7:
				printUsage()
			else:
				loadBalancing(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])

		elif sys.argv[1] == 'migrate':
			if len(sys.argv) != 5:
				printUsage()
			else:
				executeMigration(sys.argv[2], sys.argv[3], sys.argv[4])

		elif sys.argv[1] == 'scaleup' or sys.argv[1] == 'scaledown':
			if len(sys.argv) != 5:
				printUsage()
			else:
				if sys.argv[1] == 'scaleup':
					executeScalingUp(sys.argv[2], sys.argv[3], sys.argv[4])
				else:
					executeScalingDown(sys.argv[2], sys.argv[3])

		elif sys.argv[1] == 'createvm':
			if len(sys.argv) != 10:
				printUsage()
			else:
				executeCreateVm(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9])

		elif sys.argv[1] == 'createexistingvm':
			if len(sys.argv) != 12:
				printUsage()
			else:
				executeCreateExistingVm(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10], sys.argv[11])

		elif sys.argv[1] == 'destroyvm':
			if len(sys.argv) != 3:
				printUsage()
			else:
				executeDestroyVm(sys.argv[2])

		elif sys.argv[1] == 'deletevm':
			if len(sys.argv) != 3:
				printUsage()
			else:
				executeDeleteVm(sys.argv[2])

		elif sys.argv[1] == 'pausevm':
			if len(sys.argv) != 3:
				printUsage()
			else:
				executePauseVm(sys.argv[2])

		elif sys.argv[1] == 'startvm':
			if len(sys.argv) != 3:
				printUsage()
			else:
				executeStartVm(sys.argv[2])


		elif sys.argv[1] == 'shutdownvm':
			if len(sys.argv) != 3:
				printUsage()
			else:
				executeShutDownVm(sys.argv[2])

		elif sys.argv[1] == 'rebootvm':
			if len(sys.argv) != 3:
				printUsage()
			else:
				executeRebootVm(sys.argv[2])

		elif sys.argv[1] == 'changememoryvm':
			if len(sys.argv) != 4:
				printUsage()
			else:
				executeChangeMemoryVm(sys.argv[2], sys.argv[3])

		elif sys.argv[1] == 'changecpuvm':
			if len(sys.argv) != 4:
				printUsage()
			else:
				executeChangeCpuVm(sys.argv[2], sys.argv[3])

		elif sys.argv[1] == 'clonevm':
			if len(sys.argv) != 4:
				printUsage()
			else:
				executeCloneVm(sys.argv[2], sys.argv[3])

		elif sys.argv[1] == 'getuserdetails':
			if len(sys.argv) != 2:
				printUsage()
			else:
				getUserDetails()


		elif sys.argv[1] == 'modifyuserdetails':
			if len(sys.argv) != 6:
				printUsage()
			else:
				modifyUserDetails(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])


		elif sys.argv[1] == 'deleteuserdetails':
			if len(sys.argv) != 4:
				printUsage()
			else:
				deleteUserDetails(sys.argv[2], sys.argv[3])


		elif sys.argv[1] == 'adduserdetails':
			if len(sys.argv) != 11:
				printUsage()
			else:
				addUserDetails(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10])


		elif sys.argv[1] == 'getnodedetails':
			if len(sys.argv) != 2:
				printUsage()
			else:
				getNodeDetails()


		elif sys.argv[1] == 'getvmdetails':
			if len(sys.argv) != 2:
				printUsage()
			else:
				getVmDetails()


		elif sys.argv[1] == 'getips':
			if len(sys.argv) != 3:
				printUsage()
			else:
				getIpAddress(sys.argv[2])

		elif sys.argv[1] == 'start_monitor':
			if len(sys.argv) != 2:
				printUsage()
			else:
				startMonitoring()

		else:
			printUsage()

	else:
		printUsage()

#CloneVM - Exact same. No change in UUID MAC Address or even IP address


def printUsage():
	print color.BOLD + 'NAME' + color.END
	print '\t cloud1 -- type of procedure'
	print color.BOLD + 'SYNOPSIS' + color.END
	print '\t cloud1 loadbalance vm_name i/o memory disk cpu'
	print '\t cloud1 migrate from_node to_node vm_name'
	print '\t cloud1 scaleup user_name vm_name size'
	print '\t cloud1 scaledown vm_name size'
	print '\t cloud1 createvm username vm_name memory disk os cpu io ip_address'
	print '\t cloud1 createexistingvm username vm_name memory disk os cpu io ip_address img_file job_type'
	print '\t cloud1 destroyvm vm_name'
	print '\t cloud1 deletevm vm_name'
	print '\t cloud1 pausevm vm_name'
	print '\t cloud1 startvm vm_name'
	print '\t cloud1 shutdownvm vm_name'
	print '\t cloud1 rebootvm vm_name'
	print '\t cloud1 changememoryvm vm_name size'
	print '\t cloud1 changecpuvm vm_name size'
	print '\t cloud1 clonevm vm_name new_vm_name'
	print '\t cloud1 getuserdetails'
	print '\t cloud1 getnodedetails'
	print '\t cloud1 getvmdetails'
	print '\t cloud1 modifyuserdetails user_name vm_name parameter new_value'
	print '\t cloud1 deleteuserdetails user_name vm_name'
	print '\t cloud1 adduserdetails user_name vm_name IP_address node_name CPU memory disk io snapshot'
	print '\t cloud1 getips number'
	print '\t cloud1 start_monitor'


def startMonitoring():
	global nodesAvailable
	global vmAvailable
	global nodeDetails
	global vmDetails
	subprocess.call("python generate-graphs.py", shell=True)
	start = time.time()
	time.clock()
	elapsed = 0

	while True:
		elapsed = time.time() - start
		if elapsed > 10:
			start = time.time()
			# keep this execution ""Live"" from here:
			#raw_input()
			getAvailableVmsAndNodes()
			print 'Length Node' , len(nodesAvailable)
			print 'Length Vm' , len(vmAvailable)
			print 'Data Node', nodesAvailable
			print 'Data VM', vmAvailable
			# Node Monitoring for Migration...
			for i in range(0, len(nodesAvailable)):
				nodeNumber = nodesAvailable[i]
				nodeDetailsFromScript = subprocess.check_output('python monitor.py --metric --all '+nodeNumber , shell=True)
				nodeDetailsData = nodeDetailsFromScript.split('\n')
				nodeDetailsData.pop()
				print 'Node Details for', nodeNumber, ' ', nodeDetailsData
				if float(nodeDetailsData[0]) > 80:
					if float(nodeDetailsData[0]) < 95:
						adminDecision = raw_input('Do you wanna migrate due to memory insufficient on '+str(nodeNumber)+' ? >yes/no --> ')
					else:
						print 'Threshold level 2 crossed.. Lets migrate..', float(nodeDetailsData[0])
						adminDecision = 'yes'

					if adminDecision == 'yes':
						getNodeDetails()
						if nodeNumber in nodeDetails:
							allVmsInNode = nodeDetails[nodeNumber]
							maxIndex = -1
							maxValue = -1
							for vmsId in range(0, len(allVmsInNode)):
								vmDetailsDataFromScript = subprocess.check_output('python monitor.py --metric --all '+allVmsInNode[vmsId] , shell=True)
								vmDetailsData = vmDetailsDataFromScript.split('\n')
								vmDetailsData.pop()
								if maxValue < float(vmDetailsData[0]):
									maxVmIndex = vmsId
									maxValue = float(vmDetailsData[0])

							getVmDetails()
							if allVmsInNode[maxVmIndex] in vmDetails:
								vmName = allVmsInNode[maxVmIndex]
								vmDetailsObtained = vmDetails[vmName]
								nodeToMigrate = loadBalancing(vmName, vmDetailsObtained[5], vmDetailsObtained[3], vmDetailsObtained[4], vmDetailsObtained[2])
								if nodeToMigrate == nodeNumber:
									print 'No migration possible.. All nodes are busy..'
								else:
									print 'Migration Starts here.... Migirate '+str(vmName)+' to '+ str(nodesAvailable[nodeToMigrate])
									subprocess.call("ssh root@"+vmDetailsObtained[1]+" 'bash -s' < ./migrate.sh "+str(vmNumber)+" "+str(nodesAvailable[nodeToMigrate]), shell=True)
									modifyUserDetails(vmDetailsObtained[7], vmName, 'node', nodesAvailable[nodeToMigrate])

							else:
								print 'VM does not exist'

						else:
							print 'Node Does not exist'
					else:
						print 'Admin says no... Sorry'


				if float(nodeDetailsData[1]) > 80:
					if float(nodeDetailsData[1]) < 95:
						adminDecision = raw_input('Do you wanna migrate due to Cpu I/o insufficient on '+str(nodeNumber)+' ? >yes/no --> ')
					else:
						print 'Threshold level 2 crossed.. Lets migrate..'
						adminDecision = 'yes'

					if adminDecision == 'yes':
						getNodeDetails()
						if nodeNumber in nodeDetails:
							allVmsInNode = nodeDetails[nodeNumber]
							maxIndex = -1
							maxValue = -1
							for vmsId in range(0, len(allVmsInNode)):
								vmDetailsDataFromScript = subprocess.check_output('python monitor.py --metric --all '+allVmsInNode[vmsId] , shell=True)
								vmDetailsData = vmDetailsDataFromScript.split('\n')
								vmDetailsData.pop()
								if maxValue < float(vmDetailsData[1]):
									maxVmIndex = vmsId
									maxValue = float(vmDetailsData[1])

							getVmDetails()
							if allVmsInNode[maxVmIndex] in vmDetails:
								vmName = allVmsInNode[maxVmIndex]
								vmDetailsObtained = vmDetails[vmName]
								nodeToMigrate = loadBalancing(vmName, vmDetailsObtained[5], vmDetailsObtained[3], vmDetailsObtained[4], vmDetailsObtained[2])
								if nodeToMigrate == nodeNumber:
									print 'No migration possible.. All nodes are busy..'
								else:
									print 'Migration Starts here.... Migirate '+str(vmName)+' to '+ str(nodesAvailable[nodeToMigrate])
									subprocess.call("ssh root@"+vmDetailsObtained[1]+" 'bash -s' < ./migrate.sh "+str(vmNumber)+" "+str(nodesAvailable[nodeToMigrate]), shell=True)
									modifyUserDetails(vmDetailsObtained[7], vmName, 'node', nodesAvailable[nodeToMigrate])

							else:
								print 'VM does not exist'

						else:
							print 'Node Does not exist'
					else:
						print 'Admin says no... Sorry'




				if float(nodeDetailsData[2]) > 80:
					if float(nodeDetailsData[2]) < 95:
						adminDecision = raw_input('Do you wanna migrate due to Cpu Processor insufficient on '+str(nodeNumber)+' ? >yes/no --> ')
					else:
						print 'Threshold level 2 crossed.. Lets migrate..'
						adminDecision = 'yes'

					if adminDecision == 'yes':
						getNodeDetails()
						if nodeNumber in nodeDetails:
							allVmsInNode = nodeDetails[nodeNumber]
							maxIndex = -1
							maxValue = -1
							for vmsId in range(0, len(allVmsInNode)):
								vmDetailsDataFromScript = subprocess.check_output('python monitor.py --metric --all '+allVmsInNode[vmsId] , shell=True)
								vmDetailsData = vmDetailsDataFromScript.split('\n')
								vmDetailsData.pop()
								if maxValue < float(vmDetailsData[2]):
									maxVmIndex = vmsId
									maxValue = float(vmDetailsData[2])

							getVmDetails()
							if allVmsInNode[maxVmIndex] in vmDetails:
								vmName = allVmsInNode[maxVmIndex]
								vmDetailsObtained = vmDetails[vmName]
								nodeToMigrate = loadBalancing(vmName, vmDetailsObtained[5], vmDetailsObtained[3], vmDetailsObtained[4], vmDetailsObtained[2])
								if nodeToMigrate == nodeNumber:
									print 'No migration possible.. All nodes are busy..'
								else:
									print 'Migration Starts here.... Migirate '+str(vmName)+' to '+ str(nodesAvailable[nodeToMigrate])
									subprocess.call("ssh root@"+vmDetailsObtained[1]+" 'bash -s' < ./migrate.sh "+str(vmNumber)+" "+str(nodesAvailable[nodeToMigrate]), shell=True)
									modifyUserDetails(vmDetailsObtained[7], vmName, 'node', nodesAvailable[nodeToMigrate])

							else:
								print 'VM does not exist'

						else:
							print 'Node Does not exist'
					else:
						print 'Admin says no... Sorry'



				if float(nodeDetailsData[3]) > 80:
					if float(nodeDetailsData[3]) < 95:
						adminDecision = raw_input('Do you wanna migrate due to Disk insufficient on '+str(nodeNumber)+' ? >yes/no --> ')
					else:
						print 'Threshold level 2 crossed.. Lets migrate..'
						adminDecision = 'yes'

					if adminDecision == 'yes':
						getNodeDetails()
						if nodeNumber in nodeDetails:
							allVmsInNode = nodeDetails[nodeNumber]
							maxIndex = -1
							maxValue = -1
							for vmsId in range(0, len(allVmsInNode)):
								vmDetailsDataFromScript = subprocess.check_output('python monitor.py --metric --all '+allVmsInNode[vmsId] , shell=True)
								vmDetailsData = vmDetailsDataFromScript.split('\n')
								vmDetailsData.pop()
								if maxValue < float(vmDetailsData[3]):
									maxVmIndex = vmsId
									maxValue = float(vmDetailsData[3])

							getVmDetails()
							if allVmsInNode[maxVmIndex] in vmDetails:
								vmName = allVmsInNode[maxVmIndex]
								vmDetailsObtained = vmDetails[vmName]
								nodeToMigrate = loadBalancing(vmName, vmDetailsObtained[5], vmDetailsObtained[3], vmDetailsObtained[4], vmDetailsObtained[2])
								if nodeToMigrate == nodeNumber:
									print 'No migration possible.. All nodes are busy..'
								else:
									print 'Migration Starts here.... Migirate '+str(vmName)+' to '+ str(nodesAvailable[nodeToMigrate])
									subprocess.call("ssh root@"+vmDetailsObtained[1]+" 'bash -s' < ./migrate.sh "+str(vmNumber)+" "+str(nodesAvailable[nodeToMigrate]), shell=True)
									modifyUserDetails(vmDetailsObtained[7], vmName, 'node', nodesAvailable[nodeToMigrate])

							else:
								print 'VM does not exist'

						else:
							print 'Node Does not exist'
					else:
						print 'Admin says no... Sorry'

			# Vm monitoring for Vm scalling..
			for i in range(0, len(vmAvailable)):
				vmNumber = vmAvailable[i]
				vmDetailsDataFromScript = subprocess.check_output('python monitor.py --metric --all '+vmNumber , shell=True)
				vmDetailsData = vmDetailsDataFromScript.split('\n')
				vmDetailsData.pop()
				print 'Cool', vmDetailsData
				if float(vmDetailsData[0]) > 80 or float(vmDetailsData[0]) < 5:
					if float(vmDetailsData[0]) < 95 and float(vmDetailsData[0]) > 80:
						userDecision = raw_input('Do you wanna scale up due to memory insufficient on '+str(vmNumber)+' ? >yes/no --> ')
					elif float(vmDetailsData[0]) >= 0 and float(vmDetailsData[0]) < 5:
						userDecision = raw_input('Do you wanna scale down due to memory not in use for '+str(vmNumber)+' ? >yes/no --> ')
					else:
						print 'Threshold level 2 crossed.. Lets Scale..'
						userDecision = 'yes'

					if userDecision == 'yes':
						getVmDetails()
						if vmNumber in vmDetails:
							vmDetailsObtained = vmDetails[vmNumber]
							newValue = raw_input('Change Memory for  '+str(vmNumber)+'from '+ vmDetailsObtained[3] +' to ? --> ')

							nodeData = subprocess.check_output('python monitor.py --metric --all '+vmDetailsObtained[1] , shell=True)
							nodeDataArray = nodeData.split('\n')
							nodeTotalData = subprocess.check_output('python monitor.py --metric --all-total '+vmDetailsObtained[1] , shell=True)
							nodeTotalDataArray = nodeTotalData.split('\n')
							if(nodeDataArray[0] < (newValue/nodeTotalDataArray[0] * 100)):
								print 'Screwed Up'
								nodeToMigrate = loadBalancing(vmNumber, vmDetailsObtained[5], newValue, vmDetailsObtained[4], vmDetailsObtained[2])
								if nodeToMigrate != vmDetailsObtained[1] and str(nodeToMigrate).isdigit():
									print 'Migration Starts here.... Migirate '+str(vmNumber)+' to '+ str(nodesAvailable[nodeToMigrate])
									subprocess.call("ssh root@"+vmDetailsObtained[1]+" 'bash -s' < ./migrate.sh "+str(vmNumber)+" "+str(nodesAvailable[nodeToMigrate]), shell=True)
									modifyUserDetails(vmDetailsObtained[7], vmNumber, 'node', nodesAvailable[nodeToMigrate])
									modifyUserDetails(vmDetailsObtained[7], vmNumber, 'memory', newValue)
								else:
									print 'No migration possible.. All nodes are busy..'
							else:
								modifyUserDetails(vmDetailsObtained[7], vmNumber, 'memory', newValue)
						else:
							print 'VM Error..'
					else:
						print 'User says no... Sorry'


				if float(vmDetailsData[2]) > 80 or float(vmDetailsData[2]) < 5:
					if float(vmDetailsData[2]) < 95 and float(vmDetailsData[2]) > 80:
						userDecision = raw_input('Do you wanna scale up due to cpu insufficient on '+str(vmNumber)+' ? >yes/no --> ')
					elif float(vmDetailsData[2]) >= 0 and float(vmDetailsData[2]) < 5:
						userDecision = raw_input('Do you wanna scale down due to cpu not in use for '+str(vmNumber)+' ? >yes/no --> ')
					else:
						print 'Threshold level 2 crossed.. Lets Scale..'
						userDecision = 'yes'

					if userDecision == 'yes':
						getVmDetails()
						if vmNumber in vmDetails:
							vmDetailsObtained = vmDetails[vmNumber]
							newValue = raw_input('Change Cpus for  '+str(vmNumber)+'from '+ vmDetailsObtained[2] +'  to ? --> ')

							nodeData = subprocess.check_output('python monitor.py --metric --all '+vmDetailsObtained[1] , shell=True)
							nodeDataArray = nodeData.split('\n')
							if(nodeDataArray[2] < 95):
								print 'Screwed Up'
								nodeToMigrate = loadBalancing(vmNumber, vmDetailsObtained[5], vmDetailsObtained[3], vmDetailsObtained[4], newValue)
								if nodeToMigrate != vmDetailsObtained[1] and str(nodeToMigrate).isdigit():
									print 'Migration Starts here.... Migirate '+str(vmNumber)+' to '+ str(nodesAvailable[nodeToMigrate])
									subprocess.call("ssh root@"+vmDetailsObtained[1]+" 'bash -s' < ./migrate.sh "+str(vmNumber)+" "+str(nodesAvailable[nodeToMigrate]), shell=True)
									modifyUserDetails(vmDetailsObtained[7], vmNumber, 'node', nodesAvailable[nodeToMigrate])
									modifyUserDetails(vmDetailsObtained[7], vmNumber, 'cpu', newValue)
								else:
									print 'No migration possible.. All nodes are busy..'
							else:
								modifyUserDetails(vmDetailsObtained[7], vmNumber, 'cpu', newValue)
						else:
							print 'VM Error..'
					else:
						print 'User says no... Sorry'


				if float(vmDetailsData[3]) > 80 or float(vmDetailsData[3]) < 5:
					if float(vmDetailsData[3]) < 95 and float(vmDetailsData[3]) > 80:
						userDecision = raw_input('Do you wanna scale up due to disk insufficient on '+str(vmNumber)+' ? >yes/no --> ')
					elif float(vmDetailsData[3]) >= 0 and float(vmDetailsData[3]) < 5:
						userDecision = raw_input('Do you wanna scale down due to disk not in use for '+str(vmNumber)+' ? >yes/no --> ')
					else:
						print 'Threshold level 2 crossed.. Lets Scale..'
						userDecision = 'yes'

					if userDecision == 'yes':
						getVmDetails()
						if vmNumber in vmDetails:
							vmDetailsObtained = vmDetails[vmNumber]
							newValue = raw_input('Change Disk for  '+str(vmNumber)+'from '+ vmDetailsObtained[4] +'  to ? --> ')

							nodeData = subprocess.check_output('python monitor.py --metric --all '+vmDetailsObtained[1] , shell=True)
							nodeDataArray = nodeData.split('\n')
							nodeTotalData = subprocess.check_output('python monitor.py --metric --all-total '+vmDetailsObtained[1] , shell=True)
							nodeTotalDataArray = nodeTotalData.split('\n')
							if(nodeDataArray[3] < (newValue/nodeTotalDataArray[2] * 100)):
								print 'Screwed Up'
								nodeToMigrate = loadBalancing(vmNumber, vmDetailsObtained[5], vmDetailsObtained[3], newValue, vmDetailsObtained[2])
								if nodeToMigrate != vmDetailsObtained[1] and str(nodeToMigrate).isdigit():
									print 'Migration Starts here.... Migirate '+str(vmNumber)+' to '+ str(nodesAvailable[nodeToMigrate])
									subprocess.call("ssh root@"+vmDetailsObtained[1]+" 'bash -s' < ./migrate.sh "+str(vmNumber)+" "+str(nodesAvailable[nodeToMigrate]), shell=True)
									modifyUserDetails(vmDetailsObtained[7], vmNumber, 'node', nodesAvailable[nodeToMigrate])
									modifyUserDetails(vmDetailsObtained[7], vmNumber, 'disk', newValue)
								else:
									print 'No migration possible.. All nodes are busy..'
							else:
								modifyUserDetails(vmDetailsObtained[7], vmNumber, 'disk', newValue)

						else:
							print 'VM Error..'
					else:
						print 'User says no... Sorry'




def executeMigration(from_node, to_node, vm_name):
	subprocess.call("ssh root@"+from_node+" 'bash -s' < ./migrate.sh "+str(vm_name)+" "+str(from_node), shell=True)
	print 'Migration Starts'


def executeScalingUp(username, vm_name, size):
	getVmDetails()
	vmDetailsObtained = vmDetails[vm_name]
	print 'Scaling up Starts'
	subprocess.call("ssh root@"+vmDetailsObtained[1]+" 'bash -s' < ./disk_scale.sh "+str(vm_name)+" "+str(size), shell=True)
	subprocess.call("sshpass -p 'admin' ssh -o StrictHostKeyChecking=no "+vm_name+" 'bash -s' < ./disk_scale1.sh ", shell=True)
	subprocess.call("sleep 60", shell=True)
	subprocess.call("sshpass -p 'admin' ssh -o StrictHostKeyChecking=no "+vm_name+" 'bash -s' < ./disk_scale2.sh ", shell=True)

def executeScalingDown(vm_name, size):
	print 'Scaling Down Starts'
	subprocess.call('./scaledown.sh', shell=True)


def executeCreateVm(username, vm_name, memory, disk, os, cpu, io, ipadd):
	print 'Create Vm Starts'
	node = loadBalancing(vm_name, io, memory, disk, cpu)
	print node
	getAvailableVmsAndNodes()
	if int(cpu) <= 8:
		cores = 1
		threads = int(cpu)
	else:
		cores = int(cpu)/8
		threads = 8
	if str(node).isdigit():
		subprocess.call("ssh root@"+nodesAvailable[node]+" 'bash -s' < ./createvm.sh "+str(node)+" "+str(vm_name)+" "+str(memory)+" "+str(cpu)+" "+str(cores)+" "+str(threads)+" "+str(ipadd), shell=True)
		subprocess.call("./addHost.sh "+str(ipadd)+" "+str(vm_name), shell=True)
		addUserDetails(username, vm_name, ipadd, nodesAvailable[node], cpu, memory, disk, io, 'no-snapshot')
	else:
		print 'Sorry Vm Creation Not possible.. Try again later..'


def executeCreateExistingVm(username, vm_name, memory, disk, os, cpu, io, ipadd, image_name, job_type):
	print 'Create Vm Starts'
	node = loadBalancing(vm_name, io, memory, disk, cpu)
	if int(cpu) <= 8:
		cores = 1
		threads = int(cpu)
	else:
		cores = int(cpu)/8
		threads = 8
	if str(node).isdigit():
		subprocess.call("ssh root@"+nodesAvailable[node]+" 'bash -s' < ./createexistingvm.sh "+str(node)+" "+str(vm_name)+" "+str(memory)+" "+str(cpu)+" "+str(image_name)+" "+str(job_type)+" "+str(cores)+" "+str(threads)+" "+str(ipadd), shell=True)
		subprocess.call("./addHost.sh "+str(ipadd)+" "+str(vm_name), shell=True)
		addUserDetails(username, vm_name, ipadd, nodesAvailable[node], cpu, memory, disk, io, 'no-snapshot')
	else:
		print 'Sorry Vm Creation Not possible.. Try again later..'

def executeDestroyVm(vm_name):
	print 'Destroy Vm Starts'
	getVmDetails()
	nodeName = vmDetails[vm_name][1]
	subprocess.call("ssh root@"+nodeName+" 'bash -s' < ./destroyvm.sh "+vm_name, shell=True)

def executeDeleteVm(vm_name):
	print 'Delete Vm Starts'
	getVmDetails()
	nodeName = vmDetails[vm_name][1]
	subprocess.call("ssh root@"+nodeName+" 'bash -s' < ./deletevm.sh "+vm_name, shell=True)

def executePauseVm(vm_name):
	print 'Pause Vm Starts'
	getVmDetails()
	nodeName = vmDetails[vm_name][1]
	subprocess.call("ssh root@"+nodeName+" 'bash -s' < ./pausevm.sh "+vm_name, shell=True)

def executeStartVm(vm_name):
	print 'Start Vm Starts'
	getVmDetails()
	nodeName = vmDetails[vm_name][1]
	subprocess.call("ssh root@"+nodeName+" 'bash -s' < ./startvm.sh "+vm_name, shell=True)

def executeShutDownVm(vm_name):
	print 'ShutDown Vm Starts'
	getVmDetails()
	nodeName = vmDetails[vm_name][1]
	subprocess.call("ssh root@"+nodeName+" 'bash -s' < ./shutdownvm.sh "+vm_name, shell=True)

def executeRebootVm(vm_name):
	print 'Reboot Vm Starts'
	getVmDetails()
	nodeName = vmDetails[vm_name][1]
	subprocess.call("ssh root@"+nodeName+" 'bash -s' < ./rebootvm.sh "+vm_name, shell=True)

def executeCloneVm(vm_name, new_vm_name):
	print 'Clone Vm Starts'
	getVmDetails()
	nodeName = vmDetails[vm_name][1]
	subprocess.call("ssh root@"+nodeName+" 'bash -s' < ./clonevm.sh", shell=True)


def executeChangeMemoryVm(vm_name, size):
	print 'Changing Memory of Vm Starts'
	getVmDetails()
	nodeName = vmDetails[vm_name][1]
	subprocess.call("ssh root@"+nodeName+" 'bash -s' < ./changememoryvm.sh "+vm_name+" "+size, shell=True)

def executeChangeCpuVm(vm_name, size):
	print 'Changing CPUs of Starts'
	getVmDetails()
	nodeName = vmDetails[vm_name][1]
	if int(size) <= 8:
		cores = 1
		threads = int(size)
	else:
		cores = int(size)/8
		threads = 8
	subprocess.call("ssh root@"+nodeName+" 'bash -s' < ./changecpuvm.sh "+vm_name+" "+size+" "+str(cores)+" "+str(threads), shell=True)

def getIpAddress(number):
	print 'Giving back Ips'
	ipadd = subprocess.check_output('./getip.sh '+number , shell=True)
	print ipadd
	return ipadd

def loadBalancing(vm_name, io, memory, disk, cpu):
	global nodesAvailable
	nodeInfo = getDataFromMonitoringSystem()
	print 'Before',nodeInfo
	for i in range(len(nodeInfo)):
		nodeNumber = nodesAvailable[i]
		nodeTotalData = subprocess.check_output('python monitor.py --metric --all-total '+nodeNumber , shell=True)
		nodeTotalDataArray = nodeTotalData.split('\n')
		nodeInfo[i][0] = nodeInfo[i][0] + ((float(memory)/float(nodeTotalDataArray[0])) * 100)
		nodeInfo[i][1] = nodeInfo[i][1] + float(io)
		nodeInfo[i][2] = nodeInfo[i][2]
		nodeInfo[i][3] = nodeInfo[i][3] + ((float(disk)/float(nodeTotalDataArray[2])) * 100)

	print 'After',nodeInfo

	tbTable = []
	# Low = 0, Medium = 5, High = 20, HeavyLoad = 100
	for eachNode in range(len(nodeInfo)):
		tbTable.append([])
		for eachDataPoint in range(len(nodeInfo[eachNode])):
			if(nodeInfo[eachNode][eachDataPoint] <= 30):
				tbTable[eachNode].append(0)
			elif(nodeInfo[eachNode][eachDataPoint] > 30 and nodeInfo[eachNode][eachDataPoint] <= 70):
				tbTable[eachNode].append(5)
			elif(nodeInfo[eachNode][eachDataPoint] > 70 and nodeInfo[eachNode][eachDataPoint] <= 95):
				tbTable[eachNode].append(20)
			elif(nodeInfo[eachNode][eachDataPoint] > 95 and nodeInfo[eachNode][eachDataPoint] <= 100):
				tbTable[eachNode].append(100)
			elif(nodeInfo[eachNode][eachDataPoint] > 100):
				tbTable[eachNode].append(200)

	priorityQueue = []
	for i in range(len(tbTable)):
		priorityQueue.append(0)
 		for j in range(len(tbTable[i])):
 			priorityQueue[i] = priorityQueue[i] + tbTable[i][j]

 	nodeNumber = priorityQueue[0]
 	minIndex = 0
 	for i in range(len(priorityQueue)):
 		if(priorityQueue[i] < nodeNumber):
 			minIndex = i
 			nodeNumber = priorityQueue[i]

 	if(nodeNumber > 200):
 		print 'No Node Perfect for placing VM',vm_name
 	else:
 		print nodesAvailable[minIndex],'is best suited for VM',vm_name
	return minIndex


def getDataFromMonitoringSystem():
	global nodesAvailable
	global vmAvailable
	nodesAvailable = []
	vmAvailable = []
	systemLive = subprocess.check_output('python monitor.py --live-nodes', shell=True)
	systemLiveArray = systemLive.split('\n')
	for i in range(0,len(systemLiveArray)):
		if systemLiveArray[i] == 'node0' or systemLiveArray[i] == 'node1' or systemLiveArray[i] == 'node2' or systemLiveArray[i] == 'node3' or systemLiveArray[i] == 'node4' or systemLiveArray[i] == 'node5':
			nodesAvailable.append(systemLiveArray[i])
		elif systemLiveArray[i] != '':
			vmAvailable.append(systemLiveArray[i])
	nodeInfo = []
	print nodesAvailable
	for eachNode in range(0,len(nodesAvailable)):
		nodeData = subprocess.check_output('python monitor.py --metric --all '+nodesAvailable[eachNode] , shell=True)
		nodeDataArray = nodeData.split('\n')
		print 'NodeData-',nodeDataArray
		nodeInfo.append([])
		for eachDataPoint in range(0,4):
			nodeInfo[eachNode].append(float(nodeDataArray[eachDataPoint]))

	return nodeInfo

def getAvailableVmsAndNodes():
	global nodesAvailable
	global vmAvailable
	nodesAvailable = []
	vmAvailable = []
	systemLive = subprocess.check_output('python monitor.py --live-nodes', shell=True)
	systemLiveArray = systemLive.split('\n')
	for i in range(0,len(systemLiveArray)):
		if systemLiveArray[i] == 'node0' or systemLiveArray[i] == 'node1' or systemLiveArray[i] == 'node2' or systemLiveArray[i] == 'node3' or systemLiveArray[i] == 'node4' or systemLiveArray[i] == 'node5':
			nodesAvailable.append(systemLiveArray[i])
		elif systemLiveArray[i] != '':
			vmAvailable.append(systemLiveArray[i])
	nodeInfo = []
	print nodesAvailable


def getVmDetails():
	global userDetails
	global vmDetails
	vmDetails = {}
	getUserDetails()
	display = -1
	for eachUser in userDetails:
	    eachUserDetail = userDetails[eachUser]
	    for i in range(0,len(eachUserDetail)):
	        dataFields = []
	        for j in range(1,(len(eachUserDetail[i]))):
				dataFields.append(eachUserDetail[i][j])

	        dataFields.append(eachUser)
	        if eachUserDetail[i][0] in vmDetails:
				print 'VM with Same name'
				display = 0
	        else:
				vmDetails[eachUserDetail[i][0]] = dataFields

	if display != 0:
		print vmDetails
	return vmDetails


def getNodeDetails():
	global userDetails
	global nodeDetails
	nodeDetails = {}
	getUserDetails()
	for eachUser in userDetails:
	    eachUserDetail = userDetails[eachUser]
	    for i in range(0,len(eachUserDetail)):
			if eachUserDetail[i][2] in nodeDetails:
				nodeDetails[eachUserDetail[i][2]].append(eachUserDetail[i][0])
			else:
				nodeDetails[eachUserDetail[i][2]] = []
				nodeDetails[eachUserDetail[i][2]].append(eachUserDetail[i][0])
	print nodeDetails
	return nodeDetails


def getUserDetails():
	global userDetails
	userDetails = {}
	indata = open(path, 'r')
	data = indata.read()
	indata.close()
	enterSplitData = data.split('\n')
	for eachLine in enterSplitData:
		eachLine = eachLine.strip()
		eachWord = eachLine.split(',')
		dataFields = []
		for i in range(1,len(eachWord)):
			dataFields.append(eachWord[i].strip())

		if eachWord[0] != '':
			if eachWord[0] in userDetails:
				userDetails[eachWord[0]].append(dataFields)
			else:
				userDetails[eachWord[0]] = []
				userDetails[eachWord[0]].append(dataFields)
	print userDetails

def deleteUserDetails(user_name, vm_name):
	global userDetails
	getUserDetails()
	if user_name in userDetails:
		valueReturn = userDetails[user_name]
		for i in range(0,len(valueReturn)):
			if valueReturn[i][0] == vm_name:
				executeDeleteVm(vm_name)
				del userDetails[user_name][i]
				break
	else:
		print 'Wrong User Name'
	subprocess.call("./deleteetchost.sh "+vm_name, shell=True)
	writeUserDetails()

def modifyUserDetails(user_name, vm_name, parameter, data):
	global userDetails
	getUserDetails()
	key = ''
	if parameter == 'cpu':
		executeChangeCpuVm(vm_name, data)
		key = 3
	if parameter == 'memory':
		executeChangeMemoryVm(vm_name, data)
		key = 4
	if parameter == 'disk':
		executeScalingUp(user_name, vm_name, data)
		key = 5
	if parameter == 'io':
		key = 6
	if parameter == 'node':
		key = 2
	if user_name in userDetails:
		valueReturn = userDetails[user_name]
		for i in range(0,len(valueReturn)):
			if valueReturn[i][0] == vm_name:
				if key != '':
					valueReturn[i][key] = data
					userDetails[user_name][i][key] = data
					changeSucessfull = 1
				else:
					print 'Cannot modify due illegal parameter.. Only cpu, memory, disk, io'

		if changeSucessfull == 1:
			print 'Done'
		else:
			print 'No such VM'
	writeUserDetails()

def writeUserDetails():
	global userDetails
	outdata = open(path, 'w')
	for eachUser in userDetails:
		eachUserDetail = userDetails[eachUser]
		for i in range(0,len(eachUserDetail)):
			printData = eachUser
			for j in range(0,len(eachUserDetail[i])):
				printData = printData + ',' + eachUserDetail[i][j]
			outdata.write(printData)
			outdata.write('\n')
	outdata.close()

def addUserDetails(user_name, vm_name, IP_address, node_name, CPU, memory, disk, io, snapshot):
	printData = str(user_name) +','+ str(vm_name) +','+ str(IP_address) +','+ str(node_name) +','+ str(CPU) +','+ str(memory) +','+ str(disk) +','+ str(io) +','+ str(snapshot)
	with open(path, 'a') as outdata:
		outdata.write(printData)
		outdata.write('\n')
	outdata.close()


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


if __name__ == "__main__":
    main()
