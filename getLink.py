from bs4 import BeautifulSoup
import urllib.request, urllib.error
import re

def getLinks(url):
    html_page = urllib.request.urlopen(url)
    soup = BeautifulSoup(html_page, features = "lxml")
    links = []

    for link in soup.findAll('a', attrs={'href': re.compile("txt$")}):
        links.append(link.get('href'))

    return links

#print( getLinks("https://www.sec.gov/cgi-bin/srch-edgar?text=GM%20%20abs-ee&start=1&count=80&first=2016&last=2020") )

def link_by_text(url,text):
    """
    :param url: input the url you want to parse
    :param text: input the text you want to use as an indicator or cursor
    :return: the link ended by .txt right after the text
    """
    sauce = urllib.request.urlopen (url).read ()
    soup = BeautifulSoup (sauce, 'lxml')
    pool = soup.findAll ('a', string=text)
    links = []
    for i in pool:
        link = i.find_next ('a', attrs={'href': re.compile ("txt$")})
        links.append (link.get ('href'))

    return links
#print( link_by_text("https://www.sec.gov/cgi-bin/srch-edgar?text=GM%20%20abs-ee&start=1&count=80&first=2016&last=2020", 'GM Financial Automobile Leasing Trust 2017-1'))

def date_by_text(url,text):
    """
    :param url: input the url you want to parse
    :param text: input the text you want to use as an indicator or cursor
    :return: the date ended by .txt right after the text
    """
    sauce = urllib.request.urlopen (url).read ()
    soup = BeautifulSoup (sauce, 'lxml')
    pool = soup.findAll ('a', string=text)
    dates = []
    for i in pool:
        date = i.find_next ('td', string = re.compile(r'(\d+/\d+/\d+)'))
        dates.append (date.string)

    return dates

# print( date_by_text("https://www.sec.gov/cgi-bin/srch-edgar?text=GM%20%20abs-ee&start=1&count=80&first=2016&last=2020", 'GM Financial Automobile Leasing Trust 2017-1'))