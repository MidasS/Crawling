from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import urllib

urlString = 'http://kiraharu4.tumblr.com/belb'
with urllib.request.urlopen(urlString) as url:
    s = url.read().decode('utf-8')

soup = BeautifulSoup(s)

comicList = soup.find_all("p")

href_urls = [p.a["href"] for p in comicList]
del href_urls[4:]
print (href_urls)

def part(url_Href):
    with urllib.request.urlopen(url_Href) as url:
        s = url.read().decode('utf-8')
    soup = BeautifulSoup(s)
    comicList = soup.find_all("p")
    img_urls = [p.img["src"] for p in comicList]
    print(img_urls)
    download(img_urls)

def download(newImg):
    for j in range(4):
        for k in range(len(newImg)):
            fname, header = urlretrieve(newImg[k],"comic/"+"벨제바브" + str(j+1) +"/" + "pic"+ str(k) + ".jpg")


for k in range(len(href_urls)):
    part(href_urls[k])
