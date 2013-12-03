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

		mailRegu = re.compile('<input size="30" type="text" value=".{26}"/>')
		self.mailAddress = ''
		match = mailRegu.search(html)
		if match:
			address = match.group().strip('<input size="30" type="text" value="')
			address = address.strip('"/>')
			self.mailAddress = address
			print "Get MailAddress:%s" % self.mailAddress
		else:
			print "Not Found Authenticity_Token"

	def GetConformMail(self):
		req = self.sess.post('http://15qm.com/?act=recv')
		html = req.text

		# 受信確認を行い、Twitterの確認メールへのリンクだけを取り出す
		checkRegu = re.compile('http://15qm.com/\?act=mde&amp;mid=%3C.{20}%40.{10,17}.twitter.com%3E&amp;no=1&n=\d{4}')
		mailUrl = ""
		match = checkRegu.search(html)
		if match:
			mailUrl = match.group()
			mailUrl = mailUrl.replace('&amp;', '&')
			mailUrl = mailUrl.replace('%3C', '<')
			mailUrl = mailUrl.replace('%40', '@')
			mailUrl = mailUrl.replace('%3E', '>')

			print "MailUrl:%s" % mailUrl
		else:
			print "Did not receive conform mail"
			print html
			return ""
		
		# 読み取ったURLから 
		req = self.sess.post(mailUrl)
		html = req.text
		# 取り出した確認メールから確認用URLだけを取り出す
		conformRegu = re.compile('https://twitter.com/account/confirm_email/[\w]+/[\w-]{15,20}')
		conformUrl = ""
		match = conformRegu.search(html)
                if match:
			conformUrl = match.group()
                        print "ConformUrl:%s" % conformUrl
			return conformUrl
                else:
                        print "Not Found ConformUrl"
			print html
			return ""

