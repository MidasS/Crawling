import pymysql
import Bimono

Bi = Bimono.Crawler('http://www.bymono.com/index.html')
href_urls = Bi.get_href('http://www.bymono.com/index.html')
Tshirt_img_List,Tshirt_href_List,Tshirt_name_List,Tshirt_price_List = Bi.get_part(href_urls[0])
Shirt_img_List,Shirt_href_List,Shirt_name_List,Shirt_price_List = Bi.get_part(href_urls[1])
Pants_img_List,Pants_href_List,Pants_name_List,Pants_price_List = Bi.get_part(href_urls[2])
Outer_img_List,Outer_href_List,Outer_name_List,Outer_price_List = Bi.get_part(href_urls[3])




for i in range(len(Tshirt_name_List)):
    Tshirt_name_List[i] = Tshirt_name_List[i][0]
    Tshirt_price_List[i] = Tshirt_price_List[i][0][:-1]

for i in range(len(Shirt_name_List)):
    Shirt_name_List[i] = Shirt_name_List[i][0]
    Shirt_price_List[i] = Shirt_price_List[i][0][:-1]

for i in range(len(Pants_name_List)):
    Pants_name_List[i] = Pants_name_List[i][0]
    Pants_price_List[i] = Pants_price_List[i][0][:-1]

for i in range(len(Outer_name_List)):
    Outer_name_List[i] = Outer_name_List[i][0]
    Outer_price_List[i] = Outer_price_List[i][0][:-1]


print(href_urls)
print(Tshirt_img_List)
print(Tshirt_href_List)
print(Tshirt_price_List)

# db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='gusdl57',charset ='utf8',db='company')
# c = db.cursor()

# for i in range(len(img_List)):
#     c.execute('INSERT INTO bymono VALUE("%s","%s","%s","%s","%s")'%(i,name_List[i],price_List[i],href_List[i],img_List[i]))
#
#
# c.execute('select * from bymono')
# rows = c.fetchall()
#
# for r in rows:
#     print(r)
#     c.close()
