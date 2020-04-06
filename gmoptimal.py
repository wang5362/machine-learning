from bs4 import BeautifulSoup
import urllib.request, urllib.error
import ssl
import pandas as pd
from getLink import link_by_text as lbt


ctx = ssl.create_default_context () # https://docs.python.org/3/library/ssl.html#ssl-security
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

text = 'GM Financial Automobile Leasing Trust 2017-2'
url = "https://www.sec.gov/cgi-bin/srch-edgar?text=GM%20%20abs-ee&start=1&count=80&first=2016&last=2020"
links = lbt(url = url, text = text)

server = "https://www.sec.gov"

for link in links:
    sauce = urllib.request.urlopen (server + link).read ()
    soup = BeautifulSoup (sauce, 'lxml')
    assetData = soup.find_all ('assets')

    contents = []
    names = []
    for assets in assetData:
        children = assets.findChildren ()
        for child in children:
            contents.append(child.contents)
            names.append(child.name)

    df = pd.DataFrame(contents, index=names)
    df.to_csv(link[link.rfind('/')+1:link.find('.')]+".csv")