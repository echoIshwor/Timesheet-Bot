#!/usr/bin/env python

import credentials
import bash
import sys
import cookielib 
import urllib2
import mechanize
import time
from time import gmtime, strftime

reload(sys)
sys.setdefaultencoding('utf8')

br = mechanize.Browser()

# Enable cookie support for urllib2 
cookiejar = cookielib.LWPCookieJar() 
br.set_cookiejar( cookiejar ) 

# Broser options 
br.set_handle_equiv( True ) 
br.set_handle_gzip( True ) 
br.set_handle_redirect( True ) 
br.set_handle_referer( True ) 
br.set_handle_robots( False ) 


br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1 ) 

br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ] 

print "Connecting to a server ..."
# authenticate 
br.open(credentials.LOGIN_URL)

def select_form(form):
  return form.attrs.get('action', None) == '/login'

br.select_form(predicate=select_form)

br[ "username" ] = credentials.USER_NAME
br[ "password" ] = credentials.PASSWORD
res = br.submit()

print "User Login success!!"

print "Sending timesheet data to a server ..."
url = br.open(credentials.TIME_SHEET_URL)

def select_form(form):
  return form.attrs.get('action', None) == '/time_entries'

br.select_form(predicate=select_form)

br[ "time_entry[issue_id]" ] = ''
br[ "time_entry[spent_on]" ] = strftime("%Y-%m-%d", gmtime())
br[ "time_entry[hours]" ] =  '7'
br[ "time_entry[comments]" ] = bash.getParsedSvnCommits()
br[ "time_entry[activity_id]" ] = ['9',]
br[ "time_entry[custom_field_values][8]" ] = ['1',]
br.submit(name='commit')


print strftime("%Y-%m-%d", gmtime())

print "Timesheet data submission success, yaay!!"
