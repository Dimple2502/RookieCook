#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install selenium


# In[1]:


import os
from selenium import webdriver
from selenium.webdriver.common.by import By


# In[2]:


import time


# In[3]:


import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup


# In[4]:


#os.environ['PATH'] += r"C:\Selenium Driver\chromedriver_win32"
driver = webdriver.Chrome()
driver.get('https://www.dmart.in/product/')
time.sleep(3)
content = driver.page_source
soup = BeautifulSoup(content)

search = input("Enter ur search: ")

# Find the search bar and input the search term
search_input = driver.find_element(By.XPATH, '//*[@id="scrInput"]')
search_bar = driver.find_element(By.ID,"scrInput")
search_bar.send_keys(search)  # replace with your desired search term
search_button = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/header/div/div[1]/div[2]/div/div[1]/div/button')
#search_bar.submit()
time.sleep(2)
search_button.click()


# In[5]:


time.sleep(3)
page2 = driver.page_source
#print(soup_pg2)
soup_pg2 = BeautifulSoup(page2, 'html.parser')


# Find all the links with class 'Product-name'
div = soup_pg2.find('div', {'class': 'src-client-app-search-landing-styles-__search-landing-module___searchMainContainer'})
#print(div)
anchor_tags = div.find_all('a')

# Extract the href attribute from each link and print it
links = set()
for anchor in anchor_tags:
    links.add(anchor['href'])
    
links


# In[6]:


links_list = list(links)
link = ''

for i in range (len(links_list)):
    print(i)
    print(links_list[i])
    if link != '':
        break
    
    if ((links_list[i].find('satyam') != -1) and (links_list[i].find(search) != -1)):
        link = links_list[i]
    elif ((links_list[i].find('tata') != -1) and (links_list[i].find(search) != -1)):
        link = links_list[i]
        
print(link)


# In[7]:


url = "https://www.dmart.in" + link
driver.get(url)
time.sleep(10)
page3 = driver.page_source
soup_pg3 = BeautifulSoup(page3)

#link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Gmail")))
#ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()


# In[8]:


info_div = soup_pg3.find('div', {'id': 'scrollable-auto-tabpanel-0'})
#print(div)

#data = info_div.find_all('p').text
for wrapper in info_div.find_all('p'):
    data = wrapper.text
    
data


# In[9]:


bannedWord = ['Satyam','Key', 'Features-','Packed', 'with', 'utmost', 'care' , 'Benefits', 'Overview', 'Tata']
result = ' '.join(i for i in data.split() if i not in bannedWord)
print(result)
print()

custom_stopwords = ["Buy Rawa online now!", "Hygienically packed- ", "Overview", "Tata Sampann ", "Sampann's"]
count = len(result.split())
j = 0
for i in custom_stopwords:
    result = result.replace(i, '') 
    
result


# In[ ]:





# In[ ]:




