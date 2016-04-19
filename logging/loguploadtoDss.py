#!/usr/bin/env python
import boto
import boto.s3.connection
from boto.s3.key import Key
import os
import pdb
from datetime import date, timedelta

import socket


access_key = 'dddddddddddddddddddddddddddddddd'
secret_key = 'dddddddddddddddddddddddddddddddd'
bucket_name = 'rahultest'
key_name = 'loglocation/logfiles'
file_path = '/home/ubuntu/logfile.gz'
host = 'dss.ind-west-1.staging.jiocloudservices.com'


def getMachineName():
    	machine_name=socket.gethostname()
        return machine_name

def getKeyName():
	global key_name
	days_to_subtract=1
	d = date.today() - timedelta(days=days_to_subtract)
	machine_name=getMachineName()
	month=`d.month`
	if d.month<10:
		month='0'+`d.month`	
	day=`d.day`
	if d.day<10:
		day='0'+`d.day`	
	key_name=key_name+'/'+`d.year`+'/'+month+'/'+day+'/'+machine_name+'.gz'
	print(key_name)
	return key_name
	





conn = boto.connect_s3(host=host,aws_access_key_id=access_key, aws_secret_access_key=secret_key,
                       is_secure=True,
                       calling_format = boto.s3.connection.OrdinaryCallingFormat(),)


b = conn.get_bucket(bucket_name,True)
if b != None:
    print b
else:
    conn.create_bucket(bucket_name)



def uploadLog():
	key_name=getKeyName()
	key = b.new_key(key_name)
	if key != None:
    		key.set_contents_from_filename(file_path)
	else:
    		print key


def printKeys():
     for key in b.list():
        print "{name}\t{size}\t{modified}".format(
                name = key.name,
                size = key.size,
                modified = key.last_modified,
                )
     return

uploadLog()
printKeys()
