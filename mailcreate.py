# coding:utf-8
import requests # Need to install!
import re

#####################################
# Make mail address
# クイックメール(15分間フリーメール)
#####################################
class twimail:

	def __init__(self):
		self.sess = requests.session()
		req = self.sess.get('http://15qm.com/?act=sevin')
		html = req.text

		r = re.compile('<input size="30" type="text" value=".{26}"/>')
		self.mailAddress = ''
		match = r.search(html)
		if match:
			address = match.group().strip('<input size="30" type="text" value="')
			address = address.strip('"/>')
			self.mailAddress = address
			print "Get MailAddress:%s" % self.mailAddress
		else:
			print "Not Found Authenticity_Token"

	def GetConformMail():
		req = self.sess.post('http://15qm.com/?act=recv&n=1056')
		html = req.text

		r = re.compile('<a href="https://twitter.com/account/confirm_email/.{33}" target="_blank">')
		match = r.search(html)
                if match:
                        conformUrl = match.group().strip('<a href="https://twitter.com/account/confirm_email/')
                        conformUrl = conformUrl.strip('" target="_blank">')	
                        print "ConformUrl:%s" % conformUrl
			return conformUrl
                else:
                        print "Not Found ConformUrl"

