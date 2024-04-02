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
