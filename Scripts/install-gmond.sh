wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
rpm -Uvh epel-release-latest-7.noarch.rpm 
yum -y install apr-devel apr-util check-devel cairo-devel pango-devel libxml2-devel rpmbuild glib2-devel dbus-devel freetype-devel fontconfig-devel gcc-c++ expat-devel python-devel libXrender-devel
yum install ganglia ganglia-gmond
mv gmond.conf.template /etc/ganglia/gmond.conf
service gmond start
