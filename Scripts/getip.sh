nmap -v -sn -n 192.168.1.1-50 -oG - | grep -w 'Status: Down' |awk 'FNR <= '$1' {print $2}'
