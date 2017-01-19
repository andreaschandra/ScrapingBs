# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup

def scrape(html):
    soup = BeautifulSoup(html, "html.parser") 
    div = soup.find(attrs={'class':'zn-body__paragraph'}) # locate the area row
    # 'class' is a special python attribute so instead 'class_' is used
    """td = tr.find(attrs={'class':'w2p_fw'})  # locate the area tag"""
    area = div.text  # extract the area contents from this tag
    return area

if __name__ == '__main__':
    html = urllib2.urlopen('http://edition.cnn.com/2017/01/18/opinions/trump-presidency-international-views-roundup/index.html').read()
    print scrape(html)