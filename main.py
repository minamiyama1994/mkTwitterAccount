# coding:utf-8
import mailcreate
import twicreate
import random
import time

##############################
# Define config
##############################
authURL = "http://example.com/"
authReturnURL = "http://example.com/return.cgi"

#############################
# Example to use method
#############################

conformMail = mailcreate.twimail()
mailAddress = conformMail.mailAddress

# user_id and user_name is same
user_id = "".join([chr(random.randint(97,122)) for i in range(15)])
password = "".join([chr(random.randint(97,122)) for i in range(25)])
print "user_id:%s" % user_id
print "password:%s" % password
mkTwitter = twicreate.mktwi(user_id, password, mailAddress, user_id)

print "Wait to receive mail"
for i in range (1,30):
	print i
	time.sleep(1)
conformURL = conformMail.GetConformMail()
print "ConformURL:%s" % conformURL
mkTwitter.conform(conformURL)
mkTwitter.auth(authURL, authReturnURL)
print "Finish"
