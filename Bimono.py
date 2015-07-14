__author__ = '송동환'
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import urllib
import xlsxwriter



class Crawler:

    def __init__(self,urlString):
        # self.get_href(urlString)
        self.urlString = urlString

    def get_href(self, urlString):
        with urllib.request.urlopen(urlString) as url:
            s = url.read()

        soup = BeautifulSoup(s)

        comicList = soup.find('div',{'class':'position'}).find_all('a')
        # print(comicList)


        href_urls = [a["href"] for a in comicList]
        href_urls = href_urls[4:10]
        href_urls = ["http://www.bymono.com/" + R for R in href_urls]

        # self.part(href_urls[0])
        # print(self.part(href_urls[0]))

        # for k in range(len(href_urls)):
        #     self.part(href_urls[k])
        return href_urls

    def get_part(self, url_Href):
        with urllib.request.urlopen(url_Href) as url:
            s = url.read()
        soup = BeautifulSoup(s)

        if "other" in str(soup):
            part_List = soup.find_all("ul",{"class":"prdList column4"})
            item_List = part_List[1].find_all('li',{'class':'item xans-record-'})
            img_List = [div.img["src"] for div in item_List]
            href_List= [div.a["href"] for div in item_List]
            # print(img_List)
            # print(href_List)
            name_List = [div.p.a.font.next_sibling.contents for div in item_List]
            price_List = [div.ul.li.span.next_element.next_element.next_element.next_element.contents for div in item_List]
            # print(price_List)
            # print(name_List)



            for i in range(0,len(name_List)):
                if len(name_List[i]) == 2:
                    del name_List[i][1]
                else : continue


            with urllib.request.urlopen(url_Href+"&page=2") as url:
                s2 = url.read()
                soup2 = BeautifulSoup(s2)
                part_List2 = soup2.find_all("ul",{"class":"prdList column4"})
                item_List2 = part_List2[1].find_all('li',{'class':'item xans-record-'})
                img_List2 = [div.img["src"] for div in item_List2]
                href_List2 = [div.a["href"] for div in item_List2]
                # print(img_List2)
                # print(href_List2)
                name_List2 = [div.p.a.font.next_sibling.contents for div in item_List2]
                price_List2 = [div.ul.li.span.next_element.next_element.next_element.next_element.contents for div in item_List2]
                # print(name_List2)
                # print(price_List2)
            img_List+=img_List2
            href_List+=href_List2
            name_List+=name_List2
            price_List+=price_List2
            print("두번째 페이지가 있음")
            # print(img_List)
            # print(href_List)
            # print(name_List)
            # print(price_List)
        else:
            part_List = soup.find_all("ul",{"class":"prdList column4"})
            item_List = part_List[1].find_all('li',{'class':'item xans-record-'})
            img_List = [div.img["src"] for div in item_List]
            href_List= [div.a["href"] for div in item_List]
            # print(img_List)
            # print(href_List)
            name_List = [div.p.a.font.next_sibling.contents for div in item_List]
            price_List = [div.ul.li.span.next_element.next_element.next_element.next_element.contents for div in item_List]
            # print(price_List)
            # print(name_List)

            for i in range(0,len(name_List)):
                if len(name_List[i]) == 2:
                    del name_List[i][1]
                else : continue

            print("두번째 페이지가 없음")

        return img_List,href_List,name_List,price_List




        #     self.download(img_urls)
        #
        # def download(self,newImg,href_urls):
        #     for j in range(len(href_urls)):
        #         for k in range(len(newImg)):
        #             fname, header = urlretrieve(newImg[k],"comic/"+"원피스/" + "pic"+str(j+647)+"_"+str(k) + ".jpg")



# c = Crawler('http://www.bymono.com/index.html')

# c. start('http://www.bymono.com/index.html')

