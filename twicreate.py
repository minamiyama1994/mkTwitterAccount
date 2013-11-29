# coding:utf-8
import urllib2
import config # Need this file!
import requests # Need to install!
import re

screen_name = config.screen_name
password = config.password
mailAddress = config.mailAddress
user_id = config.user_id

##################################
#   Get Cookie and Session
##################################

url = 'https://twitter.com/signup'

s = requests.session()
r = s.get(url)
cookie_Session = r.cookies["_twitter_sess"]
cookie_GuestID = r.cookies["guest_id"]

print "cookie_Session:%s\n" % cookie_Session
print "cookie_GuestID:%s\n" % cookie_GuestID
html = r.text
print "\n\n\n\n\n"

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

cookie = {'cookie_Session' : cookie_Session, 'cookie_GuestID' : cookie_GuestID}

r = s.post(url,cookies=cookie, params=params)
html = r.text

#print html

