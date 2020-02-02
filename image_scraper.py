import urllib.request
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re
import os.path

save_path = 'C:/projects/testpics/test/'

mainUrl="https://wallpaperaccess.com"

html_page = urllib.request.urlopen(mainUrl)
soup = BeautifulSoup(html_page)
urlsLst = []
for link in soup.findAll('a'):
    urlsLst.append(link.get('href'))

reFormats = ('.png' or '.jpg' or '.jpeg')
for u in urlsLst:
    htmlLink = str(mainUrl)+str(u)
    html = urlopen(htmlLink)
    bs = BeautifulSoup(html, 'html.parser')
   
    # images = bs.find_all('img', {'src':re.compile('.jpg')})
    images = bs.find_all('img', {'src':re.compile(reFormats)})
    for image in images: 
        i = image['src'].split("/")[-1]
        completeName = os.path.join(save_path, str(i))
        f = open(completeName,'wb')
        url = mainUrl+image['src']
        f.write(requests.get(url).content)
        f.close()
