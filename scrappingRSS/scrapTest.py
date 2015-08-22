__author__ = 'eliandaiva'

import urllib2
from urllib2 import urlopen
import cookielib
from cookielib import CookieJar
import re
import time
from bs4 import BeautifulSoup
import requests


cj = CookieJar()

cookieProcess = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookieProcess)
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

def main():

    try:
        page = 'http://feeds.reuters.com/reuters/technologyNews'
        sourcecode = opener.open(page).read()
        print sourcecode
        print '#####################################################'

        try:
            titles = re.findall(r'<title>(.*?)</title>',sourcecode)
            links = re.findall(r'<link>(.*?)</link>',sourcecode)
            for title in titles:
                print title
            #print '----------------------------------------------------'
            for link in links:
                #print link
                if '.rdf' in link:
                    pass
                else:
                    print 'let\'s visit:', link
                    print ' _____________________________________'
                    linkSource = opener.open(link).read()
                    #content = re.findall(r'<p>(.*?)</p>',linkSource)
                    #content = re.findall(r'<p>((.|\n)*)<p>___</p>',linkSource)
                    content = re.findall(r'<p>(.*?)</p>',linkSource)
                    linesOfInterest = re.findall(r'<p>(.*?)</p>',str(content))
                    print title
                    print 'Content:'
                    for theContent in content:
                        #print title
                        print theContent
                    print '***************************************'
                    time.sleep(3)



        except Exception, e:
            print str(e)

    except Exception, e:
        print str(e)

main()
