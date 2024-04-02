from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from pymongo import MongoClient , ASCENDING, DESCENDING 
import threading 



                 # database connection
CONNECTION_STRING = "mongodb+srv://praveenmalav09:Praveen123@cluster0.pwmxmn5.mongodb.net"
# Create a connection using MongoClient. 
client = MongoClient(CONNECTION_STRING)
mydatabase = client['web_scrapping'] 
# table ha
mycollection=mydatabase['Multi_Page_Scraping_And_Product']






amazon_sku_featch = mycollection.find( {} )
amazon_sku_featch_1 =[]
for i in amazon_sku_featch:

    amazon_sku_featch_2= i['amazone_sku']
    #print(amazon_sku_featch_2)
    amazon_sku_featch_1.append(amazon_sku_featch_2)


print(len(amazon_sku_featch_1))

link_1 ="https://www.amazon.in/dp/"
link_2 =amazon_sku_featch_1[4]

final_link= link_1 + link_2
print(final_link)




link_2 =amazon_sku_featch_1[5]

final_link= link_1 + link_2
print(final_link)

link_2 =amazon_sku_featch_1[6]

final_link= link_1 + link_2
print(final_link)