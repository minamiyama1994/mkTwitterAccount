# coding:utf-8
import urllib2
import requests # Need to install!
import re

##################################
#   Get Cookie and Session
##################################

class mktwi:
	
	# アカウント作成処理
	def __init__(self, screen_name, password, mailAddress, user_id):
		#############################
		# Get Session and Cookie
		#############################
		url = 'https://twitter.com/signup'
		self.sess = requests.session()
		r = self.sess.get(url)
		cookie_Session = r.cookies["_twitter_sess"]
		cookie_GuestID = r.cookies["guest_id"]
		print "cookie_Session:%s\n" % cookie_Session
		print "cookie_GuestID:%s\n" % cookie_GuestID
		html = r.text
		r = re.compile('<input type="hidden" value=".{40}" name="authenticity_token"/>')
		match = r.search(html)
		authKey = ""
		if match:
			authKey = match.group().strip('<input type="hidden" value="')
			authKey = authKey.strip('" name="authenticity_token"/>')
			print authKey
		else:
			print "NotFound Authenticity_Token"
		
		#############################
		# Create Account
		#############################
		url = 'https://twitter.com/account/create'
		params ={'authenticity_token' : authKey, 'user[name]' : screen_name, 'user[email]' : mailAddress, 'user[user_password]' : password, 'user[screen_name]' : user_id, 'user[remember_me_on_signup]' : '0', 'user[use_cookie_personalization]' : '0', 'asked_cookie_personalization_setting' : '1', 'context' : '', 'ad_id' : '', 'ad_ref' : '', 'submit_button' : 'アカウントを作成する', 'user[discoverable_by_email]' : '1', 'user[send_email_newsletter]' : '1'}
		self.cookie = {'cookie_Session' : cookie_Session, 'cookie_GuestID' : cookie_GuestID}
		r = self.sess.post(url,cookies=cookie, params=params)
		print r.cookies
	
	def conform(self, conformURL):
		############################
		# Conform MailAddress
		############################
		r = self.sess.post(conformURL, cookies=self.cookie)
		print r.text
		return	
