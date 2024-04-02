
#####################################         my final web scraping     #########################################################################################

import threading 
import urllib3
from bs4 import BeautifulSoup
import time

# Creating a PoolManager instance for sending requests.

# http = urllib3.PoolManager()


# def MYthread_Response_url():

#     print(threading.current_thread().getName() +" " )
#     # Sending a GET request and getting back response as HTTPResponse object.

#     resp = http.request("GET", "https://www.amazon.in/Pigeon-Electric-Stainless-Shut-off-Feature/dp/B07WMS7TWB/?_encoding=UTF8&pd_rd_w=4m7EB&content-id=amzn1.sym.aff93425-4e25-4d86-babd-0fa9faf7ca5d%3Aamzn1.symc.36bd837a-d66d-47d1-8457-ffe9a9f3ddab&pf_rd_p=aff93425-4e25-4d86-babd-0fa9faf7ca5d&pf_rd_r=0Y7NH0V4GQ9VJBSRP0SX&pd_rd_wg=Yuh1l&pd_rd_r=c92cb190-c737-4604-87cd-4142e7aa4766&ref_=pd_gw_ci_mcx_mr_hp_atf_m")
#     print(resp.status)
#     #time.sleep(4)
   


# # multi threading

# #t1.start()
# #10 time thread runs
# for i in range(0,10):
#     t1=threading.Thread(target=MYthread_Response_url, args=[])
#     t1.start()


# t1.join()


# with open('page_source.html', 'w') as fid:
#     fid.write(resp.data)


# soup= BeautifulSoup(resp.data ,'html.parser')



# with open("copy.html", 'wt', encoding='utf-8') as file:
#     for line in soup.prettify():
#         file.write(line)


       #  open the file

with open('copy.html') as f:
    content = f.read()
    soup1 = BeautifulSoup(content, 'html.parser')

# print((soup1.title).get_text())



# find the image
img=soup1.find('img', id='landingImage')
print("first image")
print(img.attrs['src'])

# find the price

price= soup1.find('span', class_='a-price-whole')

# in stock
in_stock=soup1.find('span', class_='a-size-medium a-color-success')




image_all_list= soup1.find('ul', class_="a-unordered-list a-nostyle a-button-list a-vertical a-spacing-top-micro gridAltImageViewLayoutIn1x7")  
#print(image_all_list)


image_all_list_1 = image_all_list.find_all('li', class_="a-spacing-small")  
#print(image_all_list_1)
#print(" ############################################## ")



result=[]
for i in range(0,len(image_all_list_1) -2):

    img_all_list= image_all_list_1[i]
    img_all_list_1 = img_all_list.find('img')

    if img_all_list_1 :

        result.append(img_all_list_1.attrs['src'])
       


#print(result)




profile_title = ((soup1.title).get_text()).strip()
prices =   (price.get_text()).strip()
prices= float(prices[:3])

In_Stock=   (  in_stock.get_text().strip())

print((profile_title))
print(prices)
print(In_Stock)

# making dictonar to all the values
data={ 'profile_title':  profile_title , 'Price': prices , 'prod_img': result , 'Stock':In_Stock}

print(data)




####################################################       web scraping and file to be store in local drive      ################################################



import threading 
import urllib3
from bs4 import BeautifulSoup
import time

# Creating a PoolManager instance for sending requests.
http = urllib3.PoolManager()


def MYthread_Response_url():

    print(threading.current_thread().getName() +" " )
    # Sending a GET request and getting back response as HTTPResponse object.

    resp = http.request("GET", "https://www.amazon.in/Pigeon-Electric-Stainless-Shut-off-Feature/dp/B07WMS7TWB/?_encoding=UTF8&pd_rd_w=4m7EB&content-id=amzn1.sym.aff93425-4e25-4d86-babd-0fa9faf7ca5d%3Aamzn1.symc.36bd837a-d66d-47d1-8457-ffe9a9f3ddab&pf_rd_p=aff93425-4e25-4d86-babd-0fa9faf7ca5d&pf_rd_r=0Y7NH0V4GQ9VJBSRP0SX&pd_rd_wg=Yuh1l&pd_rd_r=c92cb190-c737-4604-87cd-4142e7aa4766&ref_=pd_gw_ci_mcx_mr_hp_atf_m")
    print(resp.status)
    #time.sleep(4)
   


# multi threading

#t1.start()
#10 time thread runs
for i in range(0,10):
    t1=threading.Thread(target=MYthread_Response_url, args=[])
    t1.start()


t1.join()



###########################################################           stablished the connection on web scraping                    #####################################
import urllib3

# Creating a PoolManager instance for sending requests.
http = urllib3.PoolManager()

# Sending a GET request and getting back response as HTTPResponse object.
for i in range(0,10):
    resp = http.request("GET", "https://www.amazon.in/Pigeon-Electric-Stainless-Shut-off-Feature/dp/B07WMS7TWB/?_encoding=UTF8&pd_rd_w=4m7EB&content-id=amzn1.sym.aff93425-4e25-4d86-babd-0fa9faf7ca5d%3Aamzn1.symc.36bd837a-d66d-47d1-8457-ffe9a9f3ddab&pf_rd_p=aff93425-4e25-4d86-babd-0fa9faf7ca5d&pf_rd_r=0Y7NH0V4GQ9VJBSRP0SX&pd_rd_wg=Yuh1l&pd_rd_r=c92cb190-c737-4604-87cd-4142e7aa4766&ref_=pd_gw_ci_mcx_mr_hp_atf_m")
    print(resp.status)
#time.sleep(4)  # wait untill load






#########################################################      web scraping through selenium                       ##############################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time


from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.amazon.in/boAt-Airdopes-Atom-81-Wireless/dp/B0BKG5PQ6T")

time.sleep(4)  # wait untill load
print(3)
# title = driver.title
# print(title)


soup= BeautifulSoup(driver.page_source ,'html.parser')


with open("copy.html", 'wt', encoding='utf-8') as file:
    for line in soup.prettify():
        file.write(line)








# file to read
# f = open("copy.html", "r")



# with open('copy.html') as f:
#     content = f.read()
#     soup1 = BeautifulSoup(content, 'html.parser')

# print(soup1.title)
# print(soup1.find('meta'))





###############################################################     web scraping through request methods                 #############################







import requests
from bs4 import BeautifulSoup
#url =requests.get('https://www.flipkart.com/ketch-men-checkered-casual-white-shirt/p/itm0a0f5af491e70?pid=SHTG8GMYJQRSJZZK&lid=LSTSHTG8GMYJQRSJZZK7X7UDM&marketplace=FLIPKART&store=clo%2Fash%2Faxc%2Fmmk%2Fkp7&srno=b_1_5&otracker=browse&fm=organic&iid=d3d9a336-78f5-40a4-a2ce-3c9896cac938.SHTG8GMYJQRSJZZK.SEARCH&ppt=browse&ppn=browse&ssid=0iv6iycvgw0000001708342260180')

# url=requests.get('https://www.amazon.in/dp/B0C8ZZFL6Y/ref=sspa_dk_detail_2?psc=1&pd_rd_i=B0C8ZZFL6Y&pd_rd_w=69zka&content-id=amzn1.sym.dcd65529-2e56-4c74-bf19-15db07b4a1fc&pf_rd_p=dcd65529-2e56-4c74-bf19-15db07b4a1fc&pf_rd_r=TZM7W3JHTDJ3GCT5QXKC&pd_rd_wg=0r6f6&pd_rd_r=2144ddaf-ad09-4c02-9665-4624ef5e495b&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM')


# #cheak the status code
# print(url)
# print(url.status_code)
# print(url.url)

# soup= BeautifulSoup(url.content ,'html.parser')


# print(soup.title)
# print(soup.title.name)

# # get the parent tag
# print(soup.title.parent.name)




# content of the website
#print(r.content)



# content in html
#print(soup.prettify())

# to get the title

# file to open 
# with open("copy.html", "w") as file:
#     file.write(str(soup))

# file to read
# f = open("copy.html", "r")
# print(f.read())


#####################################################################   third party used to by pass       ################################################################################

import requests
from selenium import webdriver
from lxml import html
from bs4 import BeautifulSoup

headerAgent = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

url = requests.get('https://www.amazon.in/dp/B0C8ZZFL6Y/ref=sspa_dk_detail_2?psc=1&pd_rd_i=B0C8ZZFL6Y&pd_rd_w=69zka&content-id=amzn1.sym.dcd65529-2e56-4c74-bf19-15db07b4a1fc&pf_rd_p=dcd65529-2e56-4c74-bf19-15db07b4a1fc&pf_rd_r=TZM7W3JHTDJ3GCT5QXKC&pd_rd_wg=0r6f6&pd_rd_r=2144ddaf-ad09-4c02-9665-4624ef5e495b&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM &readType=1',headers=headerAgent)
url.raise_for_status()

soup= BeautifulSoup(url.content ,'html.parser')

with open("copy.html", "w") as file:
    file.write(str(soup))



################################################################    beautiful soup tuotial                     ######################################################################################################
# find all the link
# for link in soup.find_all('a'):
#     print(link.get('href'))


# print()



# images = soup.select('div img') 
# print(images)



# Finding by id 
# s = soup.find_all('div',class_="_3kidJX") #_1BweB8 _2S1qQy  #_312yBx SFzpgZ         _2r_T1I _396QI4
# print(s)




# s = soup.find('div',class_="_3kidJX") #_1BweB8 _2S1qQy  #_312yBx SFzpgZ         _2r_T1I _396QI4
# s1=s.find_all('div' ,class_="_3A1TYz")
# print(s)
# print(s1)




# images_list=[]
# images = soup.select('img') 
# for image in images: 
#     src = image.get('src') 
#     alt = image.get('alt') 
#     images_list.append({"src": src, "alt": alt}) 


# for image in images_list: 
#     print(image)