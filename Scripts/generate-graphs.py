import os, sys
import subprocess
import time
import random
from subprocess import call
from time import sleep

def main():
	while 1:
		nodelist = subprocess.check_output('gstat --all | awk \'FNR >=12 && FNR%2==0 {print$1}\'', shell=True)
        	nodes = nodelist.split('\n')
		#print '---------Live Hosts-----------'
		for node in nodes:
  			out = subprocess.check_output('ls /var/lib/ganglia/graphs/cloud1', shell=True)
			if node not in out:
				subprocess.call('mkdir /var/lib/ganglia/graphs/cloud1/'+node, shell=True)

			subprocess.call('python monitor.py --graph --hour 1 cpu_wio '+node+' > /dev/null 2>&1', shell=True)
			subprocess.call('python monitor.py --graph --hour 1 cpu_user '+node+' > /dev/null 2>&1', shell=True)
			subprocess.call('python monitor.py --graph --hour 1 cpu_system '+node+' > /dev/null 2>&1', shell=True)
			subprocess.call('python monitor.py --graph --hour 1 cpu_idle '+node+' > /dev/null 2>&1', shell=True)
			subprocess.call('python monitor.py --graph --hour 1 mem_free '+node+' > /dev/null 2>&1', shell=True)
			subprocess.call('python monitor.py --graph --hour 1 mem_total '+node+' > /dev/null 2>&1', shell=True)
			subprocess.call('python monitor.py --graph --hour 1 mem_cached '+node+' > /dev/null 2>&1', shell=True)
			subprocess.call('python monitor.py --graph --hour 1 disk_free '+node+' > /dev/null 2>&1', shell=True)
			subprocess.call('python monitor.py --graph --hour 1 disk_total '+node+' > /dev/null 2>&1', shell=True)
		generate_aggregated('cpu_user')
		generate_aggregated('mem_free')
		generate_aggregated('disk_free')
		sleep(5)

def generate_aggregated(metric):
	nodelist = subprocess.check_output('gstat --all | awk \'FNR >=12 && FNR%2==0 {print$1}\'', shell=True)
        nodes = nodelist.split('\n')
        #print '---------Live Hosts-----------'
        query='rrdtool graph /var/lib/ganglia/graphs/cloud1/aggregated/'+metric+'.png --end now --start end-600s --width 800 --height 350'
        for node in nodes:
		if node:
			query=query+' DEF:'+node+'=/var/lib/ganglia/rrds/cloud1/'+node+'/'+metric+'.rrd:sum:AVERAGE LINE:'+node+generate_color()+':\"'+node+'\\n\" '
	subprocess.call(query+'> /dev/null 2>&1',shell=True)

def generate_color():
    	color = '#{:02x}{:02x}{:02x}'.format(*map(lambda x: random.randint(0, 255), range(20)))
  	return color


if __name__ == "__main__":
    main()
