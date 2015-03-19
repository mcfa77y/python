#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import urllib
import mechanize
import cookielib
from bs4 import BeautifulSoup
import itertools
# URL='http://greenwake.keenspot.com/d/20120206.html'
# IMG_PATTERN=re.compile('http://cdn.greenwake.keenspot.com/comics/gw\d+\.jpg')
# URL='http://portal.ntdom1.personneldecisions.com/'
# URL='http://www.scientificamerican.com/article.cfm?id=toxic-waste-sites-take-toll-millions-poor-nations'

URL = 'https://codility.com/test/?ticket=U6654T-'

#URL = 'file:///Users/joelau/Dropbox/python/home/q2.html'

# URL = 'http://www.vgcats.com/super/?strip_id='

# http://wwwsearch.sourceforge.net/mechanize/#examples


def writeResponseToFile(filename, br):
    with open(filename, 'w') as f:
        f.write(br.response().read())
def getPerms():
    perms = list(itertools.product(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], repeat=3))
    result = []
    for p in perms:
        result.append(''.join(p))
    return result

def main(url):
    print (getPerms()[0])

    # # init html page w headers and such

    br = initBrowser(url)

    # imagePattern = re.compile('images/\d+\.gif')

    # for i in range(0, 86):
    #     br.open(getNextUrl(i))

    #     # convert page to beautiful soup object

    #     bsPage = BeautifulSoup(br.response().read())

    #     # find all img tags on page and select the comic page

    #     images = bsPage.find_all('img')
    #     for image in images:

    #         # find comic page

    #         src = str(image['src'])
    #         result = imagePattern.match(src)

    #         # when found write image to file

    #         if result:
    #             print 'image: ' + src
    #             br.open(src)
    #             f = open(createFileName('super_effective_', i, '.gif',
    #                      4), 'w')
    #             f.write(br.response().read())
    #             f.close()
    #             break


def initBrowser(url):
    cj = cookielib.CookieJar()
    br = mechanize.Browser()
    br.set_cookiejar(cj)
    br.addheaders = [('User-agent',
                     'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
                     )]
    br.open(url)
    return br


def createFileName(
    base,
    index,
    suffix,
    bufferSize,
    ):
    newIndex = str(index + 1)
    while len(newIndex) < bufferSize:
        newIndex = '0' + newIndex
    return base + newIndex + suffix


def getNextUrl(i):
    return URL + str(i)


def login(
    br,
    userIdPattern,
    passwordIdPattern,
    username,
    password,
    ):

    br.select_form(nr=0)
    br.form[userIdPattern] = username
    br.form[passwordIdPattern] = password
    br.submit()


main(URL)
