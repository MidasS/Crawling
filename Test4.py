from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import urllib
import xlsxwriter

url2 = []

urlString = 'http://comic.naver.com/webtoon/weekday.nhn'
with urllib.request.urlopen(urlString) as url:
    s = url.read().decode('utf-8')

soup = BeautifulSoup(s)

comicList = soup.find_all("div","thumb")
print(comicList)
print(len(comicList))
data = {}

def get_data():
    temp = ['href', 'src', 'title']
    for l in temp:
        if l == 'href':
            urls = [div.a[l] for div in comicList]
        else:
            urls = [div.img[l] for div in comicList]

        urls.remove(urls[119])
        data[l] = urls
        print(urls)

def get_href(url1):
    for m in url1:
        url2.append("{}{}".format('http://comic.naver.com', m))
    return url2

def download(newImg, newTitle):
    for k in range(len(newImg)):
        fname, header = urlretrieve(newImg[k], newTitle[k] + ".jpg")


get_data()
download(data['src'], data['title'])

# /////////////////////////////////////////////////

workbook = xlsxwriter.Workbook('webToonList.xlsx')
worksheet = workbook.add_worksheet()

webToon = ([data['src'], data['title'], data['href']])
col = -1
for i in data:
    row = 0
    col += 1
    for j in i:
        worksheet.write(row, col, j)
        row += 1


workbook.close()