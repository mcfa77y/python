import re, urllib
import mechanize
import cookielib
#URL='http://greenwake.keenspot.com/d/20120206.html'
#IMG_PATTERN=re.compile('http://cdn.greenwake.keenspot.com/comics/gw\d+\.jpg')
#URL='http://portal.ntdom1.personneldecisions.com/'
#URL='http://www.scientificamerican.com/article.cfm?id=toxic-waste-sites-take-toll-millions-poor-nations'
URL='https://cccwpd.edd.ca.gov/Security/Login.aspx'



def main(url):
	cj = cookielib.CookieJar()
	br = mechanize.Browser()
	br.set_cookiejar(cj)
	br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11')]
	br.open(url)
	f = open('workfile.html', 'w')
	f.write(br.response().read())
	f.close()
	print("br.read: "+ br.response().read())
	br.select_form(nr=0)
	br.form['ctl00_cphMain_ctlLogin_UserName'] = 'lau.joe.a@gmail.com'
	br.form['ctl00_cphMain_ctlLogin_Password'] = '0n3w0rdFJ!'
	br.submit()
	print("br.read: "+ br.response().read())
	f = open('workfile22.html', 'w')
	f.write(br.response().read())
	f.close()

main(URL)
