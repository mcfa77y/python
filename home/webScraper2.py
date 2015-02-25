import re, urllib
import mechanize
import cookielib
#URL='http://greenwake.keenspot.com/d/20120206.html'
#IMG_PATTERN=re.compile('http://cdn.greenwake.keenspot.com/comics/gw\d+\.jpg')
#URL='http://portal.ntdom1.personneldecisions.com/'
#URL='http://www.scientificamerican.com/article.cfm?id=toxic-waste-sites-take-toll-millions-poor-nations'
URL='https://cccwpd.edd.ca.gov/Security/Login.aspx'

# http://wwwsearch.sourceforge.net/mechanize/#examples
USERNAME_ID = 'ctl00$cphMain$ctlLogin$UserName'
PASSWORD_ID = 'ctl00$cphMain$ctlLogin$Password'

USERNAME = 'lau.joe.a@gmail.com'
PASSWORD = '0n3w0rdFJ!'


def main(url):
	br = initBrowser(url)
	login(br, USERNAME_ID, PASSWORD_ID, USERNAME, PASSWORD)

	f = open('workfile2.html', 'w')
	f.write(br.response().read())
	f.close()
	
	gotoLink = ""
	for link in br.links(text="English"):
		print("link: "+ str(link) + "\n")
		gotoLink = link
	br.follow_link(gotoLink)	
	f = open('workfile3.pdf', 'w')
	f.write(br.response().read())
	f.close()

def initBrowser(url):
	cj = cookielib.CookieJar()
	br = mechanize.Browser()
	br.set_cookiejar(cj)
	br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11')]
	br.open(url)
	return br

def login(br, userIdPattern, passwordIdPattern, username, password):
	br.select_form(nr=0)
	br.form[userIdPattern] = username
	br.form[passwordIdPattern] = password
	br.submit()


main(URL)
