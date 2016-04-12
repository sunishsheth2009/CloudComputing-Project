import os, sys
import subprocess
from subprocess import call


def main():
	if len(sys.argv) > 1 and len(sys.argv) < 8:
		
		if sys.argv[1] == '--status':
			if len(sys.argv) != 3:
				printUsage()
			else:
				if sys.argv[2] == '--all':
					nodelist = subprocess.check_output('gstat --all | awk \'FNR >=12 && FNR%2==0 {print$1}\'', shell=True)
					nodes = nodelist.split('\n')
					for node in nodes:
						if node != '':
							printAllMetrics(node)
							print '\n'
				else:
					node = sys.argv[2]
					nodelist = subprocess.check_output('gstat --all | awk \'FNR >=12 && FNR%2==0 {print$1}\'', shell=True)
                                        nodes = nodelist.split('\n')
					if node in nodes:
						printAllMetrics(node)
					else:
						print 'Node is down or does not exist'

                if sys.argv[1] == '--metric' and sys.argv[2] == '--all':
                        if len(sys.argv) != 4:
                                printUsage()
                        else:
                                node = sys.argv[3]
                                nodelist = subprocess.check_output('gstat --all | awk \'FNR >=12 && FNR%2==0 {print$1}\'', shell=True)
                                nodes = nodelist.split('\n')
                                if node in nodes:
					mem_free = float(printMetric(node,'mem_free').rstrip())
					mem_total = float(printMetric(node,'mem_total').rstrip())
					mem_cached = float(printMetric(node,'mem_cached').rstrip())
					print "{0:.2f}".format((mem_total-mem_free-mem_cached)*100/mem_total)
                                        print printMetric(node,'cpu_wio').rstrip()
                                        print printMetric(node,'cpu_user').rstrip()
                                        disk_free =  float(printMetric(node,'disk_free').rstrip())
                                        disk_total = float(printMetric(node,'disk_total').rstrip())
					print "{0:.2f}".format((disk_total-disk_free)*100/disk_total)
                                else:
                                        print 'Node is down or does not exist'
                elif sys.argv[1] == '--metric' and sys.argv[2] == '--all-total':
                        if len(sys.argv) != 4:
                                printUsage()
                        else:
                                node = sys.argv[3]
                                nodelist = subprocess.check_output('gstat --all | awk \'FNR >=12 && FNR%2==0 {print$1}\'', shell=True)
                                nodes = nodelist.split('\n')
                                if node in nodes:
                                        print float(printMetric(node,'mem_total').rstrip())*0.976562
                                        print printMetric(node,'cpu_num').rstrip()
                                        print float(printMetric(node,'disk_total').rstrip())*0.931323
                                else:
                                        print 'Node is down or does not exist'
		elif sys.argv[1] == '--metric':
			if len(sys.argv) != 4:
				printUsage()
			else:
				node = sys.argv[3]
				nodelist = subprocess.check_output('gstat --all | awk \'FNR >=12 && FNR%2==0 {print$1}\'', shell=True)
                                nodes = nodelist.split('\n')
                                if node in nodes:
                                	metricname = sys.argv[2]
                                	print metricname+' : '+printMetric(node,metricname).rstrip()
				else:
					print 'Node is down or does not exist'


		if sys.argv[1] == '--live-nodes':
                        if len(sys.argv) != 2:
                                printUsage()
                        else:
                                nodelist = subprocess.check_output('gstat --all | awk \'FNR >=12 && FNR%2==0 {print$1}\'', shell=True)
                                nodes = nodelist.split('\n')
				#print '---------Live Hosts-----------'
				for node in nodes:
					print node.rstrip()

		if sys.argv[1] == '--dead-nodes':
                        if len(sys.argv) != 2:
                                printUsage()
                        else:
                                nodelist = subprocess.check_output('gstat --dead | awk \'FNR >=10 {print$1}\'', shell=True)
                                nodes = nodelist.split('\n')
                                #print '---------Dead Hosts-----------'
                                for node in nodes: 
                                        print node.rstrip()

					
		if sys.argv[1] == '--cluster-info':
                        if len(sys.argv) != 2:
                                printUsage()
                        else:
				subprocess.call('gstat --all | awk \'FNR <= 5 && FNR!=4\'', shell=True)
                                
				nodelist = subprocess.check_output('gstat --all | awk \'FNR >=12 && FNR%2==0 {print$1}\'', shell=True)
                                nodes = nodelist.split('\n')
                                print '---------Live Hosts-----------'
                                for node in nodes:
                                        print node

				nodelist = subprocess.check_output('gstat --dead | awk \'FNR >=10 {print$1}\'', shell=True)
                                nodes = nodelist.split('\n')
                                print '---------Dead Hosts-----------'
                                for node in nodes:
                                        print node

		if sys.argv[1] == '--graph':
                        if len(sys.argv) != 6:
                                printUsage()
                        else:
				node = sys.argv[5]
                                metricname = sys.argv[4]
				nodelist = subprocess.check_output('gstat --all | awk \'FNR >=12 && FNR%2==0 {print$1}\'', shell=True)
                                nodes = nodelist.split('\n')
				if node in nodes:
					time = sys.argv[2]
					t = sys.argv[3]

					if time == '--hour':
						total_sec = float(t)*3600
					elif time == '--second':
						total_sec = float(t)
					elif time == '--minute':
						total_sec = float(t)*60
					elif time == '--day':
						total_sec = float(t)*24*60*60
					else:
						printUsage()
						return
					subprocess.call('sudo rrdtool graph /var/lib/ganglia/graphs/cloud1/'+node+'/'+metricname+'.png --end now --start end-'+str(total_sec)+'s --width 400 DEF:myline=/var/lib/ganglia/rrds/cloud1/'+node+'/'+metricname+'.rrd:sum:AVERAGE AREA:myline#0000FF:\"'+metricname+'\n\"',shell=True)
                                

	else:
		printUsage()

def printAllMetrics(node):
	print '-----------'+node+'------------'
	m1 = 'CPUs [Running Procs/Total] : '+printMetric(node, 'cpu_num').rstrip()+' ['+printMetric(node, 'proc_run').rstrip()+'/'+printMetric(node, 'proc_total').rstrip()+']'
        m2 = 'CPU Usage [ User,  Nice, System, Idle, Wio] : ['+printMetric(node, 'cpu_user').rstrip()+' , '+printMetric(node, 'cpu_nice').rstrip()+' , '+printMetric(node, 'cpu_system').rstrip()+' , '+printMetric(node, 'cpu_idle').rstrip()+' , '+printMetric(node, 'cpu_user').rstrip()+']';
	m3 = 'Memory [Available/Total] : ['+printMetric(node, 'mem_free').rstrip()+'/'+printMetric(node, 'mem_total')+']'
	m4 = 'Disk [Available/Total] : ['+printMetric(node, 'disk_free').rstrip()+'/'+printMetric(node, 'disk_total').rstrip()+']'
	m5 = 'Load [1m , 5m, 15min] : ['+printMetric(node, 'load_one').rstrip()+' , '+printMetric(node, 'load_five').rstrip()+' , '+printMetric(node, 'load_fifteen').rstrip()+']'
	print m1+'\n'+m2+'\n'+m3+'\n'+m4+'\n'+m5

def  printMetric(node,metricname):
	output = subprocess.check_output('rrdtool lastupdate /var/lib/ganglia/rrds/cloud1/'+node+'/'+metricname+'.rrd | awk \'FNR==3 {print $2}\'', shell=True)	
        return output


def printUsage():
	print color.BOLD + 'NAME' + color.END
	print '\t monitor -- type of information'
	print color.BOLD + 'SYNOPSIS' + color.END
	print '\t monitor --status --all'
	print '\t monitor --status nodename'
	print '\t monitor --metric metricname nodename'
	print '\t monitor --metric --all nodename'
	print '\t monitor --metric --all-total nodename'
	print '\t monitor --live-nodes'
	print '\t monitor --dead-nodes'
	print '\t monitor --cluster-info'
	print '\t monitor --graph time[--second seconds | --hour hours | --day days | --week weeks] metricname nodename'
	
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
