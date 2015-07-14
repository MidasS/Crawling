from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import urllib


url2 = []

urlString = 'http://www.bymono.com/index.html'
with urllib.request.urlopen(urlString) as url:
    s = url.read()

soup = BeautifulSoup(s)

comicList = soup.find('div',{'class':'position'}).find_all('a')
print(comicList)
print(len(comicList))

herf_urls = [a["href"] for a in comicList]
herf_urls = herf_urls[4:10]
print(type(herf_urls))
print(herf_urls)

#
def get_herf():
    herf_urls = [div.a["href"] for div in comicList]
    herf_urls.remove(herf_urls[119])
    print(len(herf_urls))
    return herf_urls

def get_img():
    img_urls = [div.img["src"] for div in comicList]
    img_urls.remove(img_urls[119])
    print(len(img_urls))
    return img_urls

def get_title():
    title_urls = [div.img["title"] for div in comicList]
    title_urls.remove(title_urls[119])
    print(title_urls)
    return title_urls

def getHref(url1):
    for i in url1:
        url2.append("{}{}".format('http://comic.naver.com',i))
    return url2


def download(newImg,newTitle):
    for k in range(len(newImg)):
        fname, header = urlretrieve(newImg[k],newTitle[k]+".jpg")

img1 = get_img()
title1 = get_title()
herf1 = getHref(get_herf())
download(img1,title1)

# /////////////////////////////////////////////////

workbook = xlsxwriter.Workbook('webToonList.xlsx')
worksheet = workbook.add_worksheet()

webToon = ([img1,title1,herf1])
row = 0
col = 0

for title1 in title1:
    worksheet.write(row, col, title1)
    row += 1

row = 0

for herf1 in herf1:
    worksheet.write(row, col+1, herf1)
    row += 1
row =0

for img1 in img1:
    worksheet.write(row, col+2, img1)
    row += 1


workbook.close()