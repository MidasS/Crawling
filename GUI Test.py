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

        href_urls1 = [p.a["href"] for p in comicList]
        href_urls = href_urls1[65:]
        print(href_urls)

        for k in range(len(href_urls)):
            self.part(href_urls[k],href_urls)

    def part(self, url_Href,href_urls):
        with urllib.request.urlopen(url_Href) as url:
            s = url.read().decode('utf-8')
        soup = BeautifulSoup(s)
        comicList2 = soup.find_all("div","separator")
        # print(comicList2)
        img_urls = [div.img["src"] for div in comicList2]
        print(img_urls)
        self.download(img_urls,href_urls)
    #
    def download(self, newImg,href_urls):
        for j in range(len(href_urls)):
            for k in range(len(newImg)):
                fname, header = urlretrieve(newImg[k],"comic/"+"원피스/" + "pic"+str(j+647)+"_"+str(k) + ".jpg")


class MyApp:
    def __init__(self,parent):

        self.myParent = parent
        self.myParent.geometry("300x200")

        self.myContainer1 = Frame(parent , relief="sunken" , border=1)
        self.myContainer1.pack(expand=YES, fill=BOTH)
        # BF = Frame(top)
        # BF.pack()
        self.input_frame = Frame(self.myContainer1, relief="sunken" , border=1)
        self.input_frame.configure(background="red")
        self.input_frame.pack()

        # myMessage="This Program is crawling the comic"
        # Label(self.control_frame, text=myMessage, justify=LEFT).pack(side=TOP,anchor=W)
        self.Label1 = Label(self.input_frame, text="만화책명")
        self.Label1.pack(side = LEFT)
        self.E1 = Entry(self.input_frame, bd =5)
        self.E1.pack(side=RIGHT)

        self.buttons_frame = Frame(self.myContainer1)
        self.buttons_frame.pack()

        self.buttonA = Button(self.buttons_frame, text="다운받기", command=self.get)
        self.buttonA.pack(side=LEFT , padx= 15, pady = 15)
        self.buttonA.bind(self,"", self.evHotKey)

        self.buttonB = Button(self.buttons_frame, text="끝내기", command=self.quit)
        self.buttonB.pack(side=RIGHT , padx= 15, pady = 15)

    def evHotKey(self,event):
        self.get()


    def quit(self):
        self.myParent.destroy()

    def get(self):
        comic_Name = self.E1.get()
        if(comic_Name == "원피스"):
                urlString = 'http://kiraharu4.tumblr.com/onepiece'
        else:
                print("Error")
        print(urlString)
        c = Crawler()
        c.start(urlString)


top = Tk()
F = MyApp(top)
top.mainloop()

