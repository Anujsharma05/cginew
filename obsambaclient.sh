yum install cifs-utils samba-client -y
mkdir /media/stark
mount -o username=test //192.168.122.163/stark /media/stark
