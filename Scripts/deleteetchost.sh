sed -ie "/$1/d" /etc/hosts
rm -rf /var/lib/ganglia/rrds/cloud1/$1
sed -ie "/$1/d" ~/.ssh/known_hosts
