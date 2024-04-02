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


keyword_list =['mobile' , 'book' , 'bottal']
name_file_1= "web_scrapping_multi_page_multi_product_"
link_1 ="https://www.amazon.in/s?k="



#    program for mobile

def Product_page(name ,key_name):
    
     #  open the file
    with open(name ) as f:
        content = f.read()
        soup = BeautifulSoup(content, 'html.parser')


    mobile_product_page_1= soup.find('div', class_='s-main-slot s-result-list s-search-results sg-row')
    mobile_product_page_1_1 =mobile_product_page_1.find_all('img', class_='s-image')
    # print(mobile_product_page_1_1[0])
    # print(len(mobile_product_page_1_1))

    result_img =[]
    result_name=[]
    for i in range(0,len(mobile_product_page_1_1) ):

        img_all_list= mobile_product_page_1_1[i]

        if img_all_list :

            result_img.append(img_all_list.attrs['src'])
            result_name.append(img_all_list.attrs['alt'])


    # print(result_img)
    # print()
    # print(result_name)
    # print()

    result_price=[]
    product_price  =mobile_product_page_1.find_all('span', class_='a-price-whole')
    for i in product_price:

        product_price_1 = i.get_text()
        product_price_1 = product_price_1.strip()
        product_price_1= (product_price_1.replace(',', ''))
        product_price_1= (product_price_1.replace(' ', ''))
        product_price_1= (product_price_1.replace('\n', ''))
        product_price_1= float(product_price_1)
        
        result_price.append(product_price_1)



# for product link
    step_5= soup.find_all('a', class_='s-no-outline')
    

    # print(len(step_5))
    # print((step_5[2]))

    produck_link_final = []
    # print(len(step_5))
    # print(step_5[1])
   
    for k in range(0,len(step_5)):
        produck_link= step_5[k]
        produck_link_1 = produck_link.attrs['href']

        #print(produck_link_1)
        #print()

        if produck_link_1:

            produck_link_2 = produck_link_1.split("/dp/")
            produck_link_2_1 = produck_link_1.split("%2Fdp%2")


            if len(produck_link_2_1)> 1:

                produck_link_2_1_2 =(produck_link_2_1[1])
                produck_link_2_1_3 =produck_link_2_1_2[:11]
               
                #print(produck_link_2_1_3)
                produck_link_final.append(produck_link_2_1_3)
                #print()


            if len(produck_link_2)> 1:
               
                produck_link_2_1 =produck_link_2[1]
                produck_link_2_2 =produck_link_2_1[:11]         
                #print(produck_link_2_2)
                produck_link_final.append(produck_link_2_2)
                #print()


    
    
    print(produck_link_final)
    print()
    #print(produck_link_final[1])
    #print(result_price)
    # print(len(result_price))
    # print(len(result_img))
    #print(len(result_name))
    

    result_dic={ }
    results_list =[]

    for i in range(0,len(result_price)):

        try:

            if result_name[i] != "" and result_img[i]!= "" and result_price[i]!= "" and produck_link_final[i]!="":

                result_dic= { 
                    'product_title':result_name[i], 'product_image' :result_img[i] , 'price': result_price[i] ,'keyword':key_name ,'amazone_sku':produck_link_final[i]
                        ,'is_update':0
                        }
                results_list.append(result_dic)
        except:
            pass


    
    try:

        collect_the_data_from_database = mycollection.count_documents({})
        if collect_the_data_from_database > 200:
            
            pass

        else:

            (mycollection.insert_many(results_list))
            #pass

    except:
        print('Errorn in Count from data base')
        


        

def Product_Page_(n ,name_product ):


    file_name_product = n + ".html"

    
    Product_page(file_name_product ,name_product)



name_product_1= keyword_list[0]
name_product_2 = keyword_list[1]
name_product_3= keyword_list[2]


for i in range(0,len(keyword_list) ):


    name_product_page_1 = name_product_1 + "_page_" + str(i+1)
    name_product_page_2 = name_product_2 + "_page_" + str(i+1)
    name_product_page_3 = name_product_3 + "_page_" + str(i+1)

    print()


    mobile1=threading.Thread(target=Product_Page_, args=[ name_product_page_1,name_product_1 ] )
    book1=threading.Thread(target=Product_Page_,   args=[name_product_page_2 ,name_product_2  ])
    bottal1=threading.Thread(target=Product_Page_, args=[name_product_page_3 ,name_product_3  ])

    mobile1.start()
    book1.start()
    bottal1.start()

    mobile1.join()
    book1.join()
    bottal1.join()


