import urllib2
import re


def scrape(html):
    area = re.findall('<td class="w2p_fw">(.*?)</td>', html)
    return area


if __name__ == '__main__':
    html = urllib2.urlopen('http://example.webscraping.com/view/United-Kingdom-239').read()
    print scrape(html)