from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pymongo import MongoClient , ASCENDING, DESCENDING 



                 # database connection
CONNECTION_STRING = "mongodb+srv://praveenmalav09:Praveen123@cluster0.pwmxmn5.mongodb.net"
# Create a connection using MongoClient. 
client = MongoClient(CONNECTION_STRING)
mydatabase = client['on_search_test'] 
# table ha
mycollection=mydatabase['product_in_test'] 



#    https://www.amazon.in/dp/B0BY8L3RZ6                https://www.amazon.in/dp/B0BZCSSNV7

amazon_sku_featch = mycollection.find( {} )
amazon_sku_featch_1 =[]
for i in amazon_sku_featch:

    amazon_sku_featch_2= i['amazon_sku']
    amazon_sku_featch_1.append(amazon_sku_featch_2)



link_1 =amazon_sku_featch_1[0]
link_2 ="https://www.amazon.in/dp/"

final_link= link_2 + link_1
print(final_link)

#                                                            # make connection on chrome
 

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver = webdriver.Firefox()
# driver.get(final_link)
# time.sleep(4)  # wait untill load

# soup= BeautifulSoup(driver.page_source ,'html.parser')                                                  

# with open("copy_next_step_1.html", 'wt', encoding='utf-8') as file:
#     for line in soup.prettify():
#         file.write(line)






with open('copy_next_step_1.html') as f:
    content = f.read()
    soup = BeautifulSoup(content, 'html.parser')



# current time for update
t1= round(time.time())
print(t1)

step_1= soup.find("div", {"id": "imgTagWrapperId"})
# print(step_1)
step_2 =step_1.find('img', class_='a-dynamic-image a-stretch-horizontal')
#print(step_2)


result_img=(step_2.attrs['src'])
result_name=(step_2.attrs['alt'])

print(result_img)
print(result_name)





step_3 =soup.find('span', class_='a-price aok-align-center reinventPricePriceToPayMargin priceToPay')
#print(step_3)

step_4 =step_3.find('span', class_='a-price-whole')
step_4_1=(step_4.get_text()).strip()
price_status=  float(step_4_1.replace(',', ''))
print(price_status)


step_5 =soup.find('span', class_='a-size-medium a-color-success')
stock_status =(step_5.get_text()).strip()
print(stock_status)

if stock_status:
    stock_status_1 = 1
else:
    stock_status_1 =0




step_7= soup.find_all('li', class_= "a-spacing-small item imageThumbnail a-declarative")

# print(step_7)
# print(len(step_7))

all_image=[]
for i in range(0,len(step_7)):
    step_7_1 =step_7[i]
    step_7_2 =step_7_1.find('img')
    step_7_3 = step_7_2.attrs['src']
    all_image.append(step_7_3)


#print(all_image)
    #result_img
    # handel the image if not find
if all_image:
    pass
else:
    all_image =result_img




is_detail_update =0

if result_name!= "" and result_img!= "" and price_status!= ""   and stock_status!=""  and all_image!= "":

    is_detail_update =1

    mycollection.update_one({ 'amazon_sku': amazon_sku_featch_1[0]} ,{ '$set' : {'Update_Time':t1  ,'product_image':all_image, 'price' : price_status , 'in_stock' : stock_status_1 , 'is_detail_update': is_detail_update}} )



