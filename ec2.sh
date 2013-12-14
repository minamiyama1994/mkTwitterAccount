#!/bin/bash

# config
instanceID="i-XXXXXXXX"
keyPlace="./ec2.pem"
region="us-west-2"

# Read text
nowCount=`cat out.txt`

# try 600 time
for i in `seq ${nowCount} 600`
do
	echo ${i}
	ec2-start-instances ${instanceID} -region ${region}
	sleep 220
	ipAddress=`ec2-describe-instances ${instanceID} -region us-west-2 | grep "INSTANCE" | cut -f17`
	ssh -i ${keyPlace} -oStrictHostKeyChecking=no ec2-user@${ipAddress} python ./mkTwitterAccount/main.py
	ec2-stop-instances ${instanceID} -region ${region}
	echo ${i} > out.txt
	sleep 50
done

