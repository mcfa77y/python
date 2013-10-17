#!/cygdrive/c/Python33/python
from urllib.request import urlopen,urlretrieve,FancyURLopener
from bs4 import BeautifulSoup
import re
# dup a user agent to bypass 403 HTTP errors
class MyOpener(FancyURLopener):
	version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

MAX=120
COUNTER=0
#URL='http://greenwake.keenspot.com/d/20120206.html'
#IMG_PATTERN=re.compile('http://cdn.greenwake.keenspot.com/comics/gw\d+\.jpg')
URL='http://www.dis-connection.com/?cid=2'
IMG_PATTERN=re.compile('http://dis-connection.com/comics/\d+\.jpg')



def main(url):	
	global MAX, COUNTER, IMG_PATTERN
	soup = BeautifulSoup(urlopen(url))
	pageText = soup.prettify()
	#nextPageURL = getNextPage(soup)
	nextPageURL = getNextSimpleCounter()

	nextPattern=re.compile(r'.*Next\.png.*')

	#print(a)
	imgURL = re.search(IMG_PATTERN,pageText).group(0)
	print(imgURL, nextPageURL)
	#grab filename
	imgFN=imgURL[imgURL.rfind('/')+1:]
	myopener = MyOpener()
	#dl the image
	myopener.retrieve(imgURL, imgFN)
	COUNTER+=1
	if COUNTER>MAX:
		return
	else:
		main(nextPageURL)

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