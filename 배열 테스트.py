from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from tkinter import*
import urllib

class Crawler:
    def start(self, urlString):
        #urlString = 'http://kiraharu4.tumblr.com/belb'
        with urllib.request.urlopen(urlString) as url:
            s = url.read().decode('utf-8')

        soup = BeautifulSoup(s)

        comicList = soup.find_all("p")

        href_urls = [p.a["href"] for p in comicList]
        del href_urls[4:]
        print(href_urls)

        for k in range(len(href_urls)):
            self.part(href_urls[k])

    def part(self, url_Href):
        with urllib.request.urlopen(url_Href) as url:
            s = url.read().decode('utf-8')
        soup = BeautifulSoup(s)
        comicList = soup.find_all("p")
        img_urls = [p.img["src"] for p in comicList]
        print(img_urls)
        self.download(img_urls)

    def download(self, newImg):
        for j in range(4):
            for k in range(len(newImg)):
                fname, header = urlretrieve(newImg[k],"comic/"+"벨제바브" + str(j+1) +"/" + "pic"+ str(k) + ".jpg")




top = Tk()
F = Frame(top)
F.pack()
BF = Frame(top)
BF.pack()

def get():
    comic_Name = E1.get()
    if(comic_Name == "벨제바브"):
            urlString = 'http://kiraharu4.tumblr.com/belb'
    else:
            print("Error")
    print(urlString)
    c = Crawler()
    c.start(urlString)



L1 = Label(F, text="만화책명")
L1.pack( side = LEFT)
E1 = Entry(F, bd =5)

E1.pack(side = RIGHT)



B1 = Button(BF, text="다운받기", command= get)
B1.pack()

F.mainloop()

