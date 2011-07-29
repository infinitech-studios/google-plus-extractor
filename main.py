import sys
import urllib2
import re
import json
from BeautifulSoup import BeautifulSoup

if (len(sys.argv) > 1):
	plusId = str(sys.argv[1])
	page = urllib2.urlopen("https://plus.google.com/%s/posts" % (plusId,))
	soup = BeautifulSoup(page)

	mydivs = soup.findAll("div",'a-b-c-ka-Mc a-c-ka-Mc')
	headers = mydivs[0].contents[3].contents[1:3]
	outer = re.compile("\((.+)\)")
	
	followingHeading = headers[0].find('h4').contents[0]
	following = outer.search(str(followingHeading)).group().strip('()')
	
	followersHeading = headers[1].find('h4').contents[0]
	followers = outer.search(str(followersHeading)).group().strip('()')
	
	print json.dumps({'following':following,'followers':followers})
	
else:
	print "You cannot invoke this script directly without arguments. Pass the Google Plus ID as an argument"