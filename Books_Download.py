#!/usr/bin/env python
# coding: utf-8

# In[16]:


from tqdm import trange
from time import sleep
import requests as re
import openpyxl as xl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# In[2]:


driver = webdriver.Chrome()


# In[3]:


bk = xl.load_workbook('data.xlsx')
sheet = bk.active


# In[4]:


def extractor(co):
    i = 3
    lis = list()
    for i in range(3, 411):
        lis.append(sheet.cell(row=i, column=co).value)
        i += 1
    return lis


# In[5]:


names = extractor(2)


# In[6]:


linkz = extractor(5)


# In[7]:


book_links = list()
z = 0
for z in trange(len(linkz)):
    driver.get(linkz[z])
    data = (driver.find_element_by_partial_link_text("Download").get_attribute('href'))
    book_links.append(data)
    z += 1
    sleep(0.01)


# In[19]:


for t in trange(len(linkz)):
    r = re.get(book_links[t])
    open(names[t] + '.pdf', 'wb').write(r.content)
    sleep(0.01)


# In[ ]:




