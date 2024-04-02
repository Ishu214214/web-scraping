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


                                                                          # make connection on chrome
 

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))        
# driver.get("https://www.amazon.in/boAt-Airdopes-Atom-81-Wireless/dp/B0BKG5PQ6T")               #   https://www.amazon.in/dp/B0CSDQ434W
# time.sleep(4)  # wait untill load


# soup= BeautifulSoup(driver.page_source ,'html.parser')


                                                               

# with open("copy.html", 'wt', encoding='utf-8') as file:
#     for line in soup.prettify():
#         file.write(line)





with open('copy_1.html') as f:
    content = f.read()
    soup = BeautifulSoup(content, 'html.parser')





step_1= soup.find('div', class_='s-main-slot s-result-list s-search-results sg-row')
step_2 =step_1.find_all('img', class_='s-image')



result_img =[]
result_name=[]
for i in range(2,len(step_2) ):

    img_all_list= step_2[i]

    if img_all_list :

        result_img.append(img_all_list.attrs['src'])
        result_name.append(img_all_list.attrs['alt'])



# print()
# print(result_name)
# print(len(result_name))

# print()
# print(result_img)
# print(len(result_img))


step_3 =step_1.find_all('span', class_='a-price-whole')
#print(step_3)
#print(len(step_3))


result_price=[]

for i in range(0,len(step_3)):
    res= (step_3[i])
    res=(res.get_text()).strip()
    res1=  float(res.replace(',', ''))
    result_price.append(res1)



# print()
# print(result_price)
# print(len(result_price))




# for product link
step_5= soup.find_all('a', class_='s-no-outline')

# print(len(step_5))
# print((step_5[2]))

produck_link_final = []


for k in range(2,len(step_5)):
    produck_link= step_5[k]
    #print(produck_link)
    produck_link_1 = produck_link.attrs['href']

    if produck_link_1:

        produck_link_2 = produck_link_1.split("/")
        produck_link_2 = produck_link_2[::-1]
        print(produck_link_2[0])
        #print()
        produck_link_final.append(produck_link_2[0])
        #print(produck_link_1)



# print(produck_link_final)
#print(len(produck_link_final))


# current time
now = time.time()
current_time = round(time.time())
print(current_time)

update_time = round(time.time())
print(update_time)



result_dic={ }
results_list =[]

for i in range(0,16):

    if result_name[i] != "" and result_img[i]!= "" and result_price[i]!= ""   and produck_link_final[i]!="" :

        result_dic= { 'product_title':result_name[i], 'product_image' :result_img[i] , 'price': result_price[i] ,'amazon_sku': produck_link_final[i] 
                       , 'Current_time': current_time , 'Update_Time': update_time
                     }
        results_list.append(result_dic)
    #print(i)



# print()
# print(results_list)
# print(results_list[0])
# print(len(results_list))



mycollection.create_index('amazon_sku', unique = True)
mycollection.create_index( [("price", ASCENDING )] )
#mycollection.insert_many(results_list)


#  searching
# findind_price=mycollection.find(  {  'price': { '$gte': 5000 }} )
# print(list(findind_price))