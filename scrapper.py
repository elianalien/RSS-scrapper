__author__ = 'eliandaiva'

import urllib2
from urllib2 import urlopen
import re
import cookielib
from cookielib import CookieJar
import time

cj = CookieJar
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent','Mozilla/5.0')]

def main():
    try:
        page = 'http://www.cbc.ca/cmlink/rss-topstories'
        sourceCode = opener.open(page).read()
        print sourceCode

    except Exception, e:
        print str(e)

main()
