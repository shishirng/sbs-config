FileName="/home/ubuntu/logfile.gz"

dateValue=`date --date="today" +%Y-%m-%d`
echo $dateValue

#dateValue="2016-04-04"

sudo tar cvzf $FileName /var/log/*/*$dateValue* /var/log/*$dateValue*   /etc/cinder/cinder.conf /etc/cinder/api-paste.ini /etc/ec2api/ec2api.conf /etc/ceph/ceph.conf /etc/haproxy/haproxy.cfg /etc/keepalived/keepalived.conf /etc/mysql/my.cnf /etc/oslo/matchmaker_ring.json /etc/telegraf/telegraf.conf /etc/supervisor/supervisord.conf /etc/hosts /etc/logrotate.d/*
