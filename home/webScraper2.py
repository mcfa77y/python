#!/cygdrive/c/Python33/python
from urllib.request import urlopen,urlretrieve,FancyURLopener, ProxyHandler,ProxyBasicAuthHandler,build_opener
from bs4 import BeautifulSoup
import re, urllib

# dup a user agent to bypass 403 HTTP errors
class MyOpener(FancyURLopener):
	version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

MAX=120
COUNTER=0
#URL='http://greenwake.keenspot.com/d/20120206.html'
#IMG_PATTERN=re.compile('http://cdn.greenwake.keenspot.com/comics/gw\d+\.jpg')
#URL='http://portal.ntdom1.personneldecisions.com/'
URL='http://www.scientificamerican.com/article.cfm?id=toxic-waste-sites-take-toll-millions-poor-nations'
IMG_PATTERN=re.compile('http://dis-connection.com/comics/\d+\.jpg')



def main(url):	
	global MAX, COUNTER, IMG_PATTERN

	
	
	
	proxy_handler = ProxyHandler({url})
	proxy_auth_handler = ProxyBasicAuthHandler()
	proxy_auth_handler.add_password("http", url, "jlau", "D0theylikepuppies")

	opener = build_opener(proxy_handler, proxy_auth_handler)
	# This time, rather than install the OpenerDirector, we use it directly:
	opener.open('http://portal.ntdom1.personneldecisions.com/irj/portal/')
	
	
def getNextPage(soup):
	links = soup.find_all('a')
	return getNextSimpleCounter(links)
	
	#return getNextGW(links)
def getNextSimpleCounter():
	global COUNTER
	url = 'http://www.dis-connection.com/?cid='
	return url+str(COUNTER+1)
	
def getNextGW(links):
	# search all links
	for link in links:
		# match the next link for the next address
		try:
			# filter by rel == next and set nextPageURL
			if link.attrs['rel'][0]=='next':
				#nextPageURL=link.attrs['href']
				#print('found next link', link.attrs['href'])
				return link.attrs['href']
		# skip links w/o rel attributes		
		except KeyError:
			pass		
main(URL)