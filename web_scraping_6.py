from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pymongo import MongoClient , ASCENDING, DESCENDING 
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime



                 # database connection
CONNECTION_STRING = "mongodb+srv://praveenmalav09:Praveen123@cluster0.pwmxmn5.mongodb.net"
# Create a connection using MongoClient. 
client = MongoClient(CONNECTION_STRING)
mydatabase = client['web_scrapping'] 
# table ha
mycollection=mydatabase['keyword_log_ishu'] 




#                  insert data in database


# current_datetime = datetime.now()

# current_year = current_datetime.strftime("%Y")
# current_month = current_datetime.strftime("%m")
# current_day = current_datetime.strftime("%d")
# current_time = current_datetime.strftime("%H:%M:%S")
# current_date_time = current_datetime.strftime("%m/%d/%Y, %H:%M:%S")


# dic={}
# dic_list=[]
# name_keyword=['book', 'mobile', 'laptop', 'shirt', 'bottal']

# for i in range(1,6):
#     dic={ '_id' : i  , 'keyword': name_keyword[i-1] ,'current_date_time':current_date_time}
#     dic_list.append(dic)
# #print(dic_list)
# mycollection.insert_many(dic_list)




#collect_the_data_from_database = mycollection.find({}).limit(1)   #.limit(3).skip(2)   skip starting ka 2 skip  kar ka 3,4,5 lag ga q ki limit 3 ha
collect_the_data_from_database=mycollection.find(  { 'is_scrap': 0} )
print(collect_the_data_from_database)

print(list(collect_the_data_from_database))
# if collect_the_data_from_database:
#     pass
# else:
#     mycollection.update_one({ '_id': 1} ,{ '$set' : {'is_scrap': 1  }} )




# keyword_featch =[]

# j=1  # for updatation on id 
# for i in collect_the_data_from_database:

#     featch_2= i['keyword']
#     keyword_featch.append(featch_2)

#     try:

#         featch_field = i['is_scrap']

#         if featch_field == 1:

#             link_1 =featch_2
#             link_2 ="https://www.amazon.in/s?k="

#             final_link= link_2 + link_1
#             #print(final_link)

#             driver = webdriver.Firefox()
#             driver.get(final_link)
#             time.sleep(4)  # wait untill load


#             soup= BeautifulSoup(driver.page_source ,'html.parser')

#             html_name_1= "demo_webscrapping_on_field_"
#             html_name_2=".html"
#             final_name= html_name_1 + featch_2 + html_name_2
#             #print(final_name)

#             with open(final_name, 'wt', encoding='utf-8') as file:
#                 for line in soup.prettify():
#                     file.write(line)


#     except:
        
#         mycollection.update_one({ '_id': 1} ,{ '$set' : {'is_scrap': 1  }} )
#         #j=j+1









