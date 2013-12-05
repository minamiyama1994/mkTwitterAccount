# coding:utf-8
import urllib2
import sys
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

		self.screen_name = screen_name
		self.password = password
		self.mailAddress = mailAddress
		self.user_id = user_id

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
		r = self.sess.post(url,cookies=self.cookie, params=params)
		print r.cookies

	def conform(self, conformURL):
		############################
		# Conform MailAddress
		############################
		r = self.sess.get(conformURL, cookies=self.cookie)
		#print r.text
		print "Fin"
		return
	
	def auth(self,authURL,returnURLPath):
		###########################
		# Auth your application
		##########################

		sess = requests.session()
		r = sess.get(authURL)
		#print r.cookies
		cookie_Session = r.cookies["_twitter_sess"]
		cookie_GuestID = r.cookies["guest_id"]
		#print "cookie_Session:%s\n" % cookie_Session
		#print "cookie_GuestID:%s\n" % cookie_GuestID
		
		#print r.headers
		
		cookie = {'cookie_Session' : cookie_Session, 'cookie_GuestID' : cookie_GuestID}

		html =  r.text

		# Authentivity_tokenを取り出す
		r = re.compile('<input name="authenticity_token" type="hidden" value=".{40}" />')
		match = r.search(html)
		authenticity_token = ''
		if match:
			authenticity_token = match.group().strip('<input name="authenticity_token" type="hidden" value="')
			authenticity_token = authenticity_token.strip('" />')
			#print authenticity_token
		else:
			print "Not found Authenticity_Token"

		# Oauth_Tokenを取り出す
		r = re.compile('<input id="oauth_token" name="oauth_token" type="hidden" value=".{40,45}" />')
		#<input id="oauth_token" name="oauth_token" type="hidden" value=".{41}" />
		match = r.search(html)
		oauth_token = ''
		if match:
		    oauth_token = match.group().strip('<input id="oauth_token" name="oauth_token" type="hidden" value="')
		    oauth_token = oauth_token.strip('" />')
		    #print oauth_token
		else:
		    print "Not found Oauth_Token"

		params = {'authenticity_token': authenticity_token, 'oauth_token': oauth_token, 'session[username_or_email]': self.user_id, 'session[password]': self.password, 'remember_me': 1}

		url = 'https://api.twitter.com/oauth/authenticate?%s' % cookie_Session

		r = sess.post(url,cookies=cookie, params=params)

		#print r.text
		html = r.text
		r = re.compile('<a href="%s\?oauth_token=.{40,45}&oauth_verifier=.{40,45}" class="maintain-context">' % returnURLPath)

		match = r.search(html)
		returnURL = ''
		if match:
			returnURL = match.group()
			returnURL = returnURL.replace('<a href="', '')
			returnURL = returnURL.strip('" class="maintain-context">')
			#print 'returnURL:%s' % returnURL
		else:
			print 'Not Found ReturnURL'

		r = sess.get(returnURL, cookies = cookie)
		#print r.text
		return
