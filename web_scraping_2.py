import threading 
import urllib3
from bs4 import BeautifulSoup
import time

#Creating a PoolManager instance for sending requests.

# http = urllib3.PoolManager()


# def MYthread_Response_url():

#     print(threading.current_thread().getName() +" " )
#     # Sending a GET request and getting back response as HTTPResponse object.

#     resp = http.request("GET", "https://www.amazon.in/s?k=mobile")
#     print(resp.status)

#     soup= BeautifulSoup(resp.data ,'html.parser')
#     time.sleep(4)

#     with open("copy_1.html", 'wt', encoding='utf-8') as file:
#         for line in soup.prettify():
#             file.write(line)


   
# for i in range(0,1):
#     t1=threading.Thread(target=MYthread_Response_url, args=[])
#     t1.start()


# t1.join()



       #  open the file

with open('copy_1.html') as f:
    content = f.read()
    soup = BeautifulSoup(content, 'html.parser')

# print((soup.title).get_text())





step_1= soup.find('div', class_='s-main-slot s-result-list s-search-results sg-row')


step_2 =step_1.find_all('img', class_='s-image')
#print(step_2)
# print(len(step_2))

# print(step_2[2])


result_img =[]
result_name=[]
for i in range(2,len(step_2) ):

    img_all_list= step_2[i]

    if img_all_list :

        result_img.append(img_all_list.attrs['src'])
        result_name.append(img_all_list.attrs['alt'])


print()
print(result_name)
print(len(result_name))

print()
print(result_img)
print(len(result_img))


step_3 =step_1.find_all('span', class_='a-price-whole')
#print(step_3)
#print(len(step_3))

result_price=[]

for i in range(0,len(step_3)):
    res= (step_3[i])
    res=(res.get_text()).strip()
    result_price.append(res)

print()
print(result_price)
print(len(result_price))



result_dic={ }
results_list =[]

for i in range(0,15):

    result_dic= { 'name':result_name[i], 'img' :result_img[i] , 'price': result_price[i] }
    results_list.append(result_dic)


print()
print(results_list)
print(results_list[0])