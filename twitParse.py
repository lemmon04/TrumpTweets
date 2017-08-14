import re
from re import sub
import time
import cookielib
from cookielib import CookieJar
import urllib2
from urllib2 import urlopen
import fileinput
import difflib

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/54.0.1')]

keyWord = 'trump'


def main():
    oldTwit = []
    newTwit = []
    try:
        sourceCode = opener.open('https://twitter.com/realDonaldTrump').read()
        #print sourceCode
        
        splitSource = re.findall(r'<p class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text" lang="en" data-aria-label-part="0">(.*?)</p>',sourceCode)
        for item in splitSource:
            item = item.replace("&amp;", "&")
            item = item.replace("&#39;", "'")
            item = item.replace("â€™", "'")
            aTweet = re.sub(r'<.*?>','',item) + "\n"
            print aTweet



    except Exception, e:
        print str(e)
        print 'errored in the main try'
        time.sleep(555)
main()
