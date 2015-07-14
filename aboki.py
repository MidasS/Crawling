__author__ = '송동환'
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from tkinter import*
import urllib


class Crawler:
    def start(self, urlString):
        with urllib.request.urlopen(urlString) as url:
            s = url.read()

        soup = BeautifulSoup(s)

        comicList = soup.find('div',{'class':'position'}).find_all('a')
        print(comicList)
        print(len(comicList))


        href_urls = [a["href"] for a in comicList]
        href_urls = href_urls[4:10]
        print(type(href_urls))
        href_urls = ["http://www.bymono.com/" + R for R in href_urls]
        print(href_urls[0])

        self.part(href_urls[0])

        # for k in range(len(href_urls)):
        #     self.part(href_urls[k])


    def part(self, url_Href):
        with urllib.request.urlopen(url_Href) as url:
            s = url.read()
        soup = BeautifulSoup(s)
        part_List = soup.find_all("ul",{"class":"prdList column4"})
            # .find_next().find_all('img',{'class':'thumb'})
        print(part_List[1])
        # img_urls = [img["src"] for img in part_List]
        # print(img_urls)
    #     self.download(img_urls)
    #
    # def download(self, newImg,href_urls):
    #     for j in range(len(href_urls)):
    #         for k in range(len(newImg)):
    #             fname, header = urlretrieve(newImg[k],"comic/"+"원피스/" + "pic"+str(j+647)+"_"+str(k) + ".jpg")
    #

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
        self.Label1 = Label(self.input_frame, text="쇼핑몰이름")
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
        if(comic_Name == "바이모노"):
            urlString = 'http://www.bymono.com/index.html'
        else:
                print("Error")
        print(urlString)
        c = Crawler()
        c.start(urlString)


top = Tk()
F = MyApp(top)
top.mainloop()

