#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tqdm import trange
from time import sleep
import requests as re
import openpyxl as xl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# In[ ]:


driver = webdriver.Chrome()


# In[ ]:


bk = xl.load_workbook('data.xlsx')
sheet = bk.active


# In[ ]:


def extractor(co):
    i = 3
    lis = list()
    for i in range(3, 411):
        lis.append(sheet.cell(row=i, column=co).value)
        i += 1
    return lis


# In[ ]:


names = extractor(2)


# In[ ]:


linkz = extractor(5)


# In[ ]:


words =['Download' + ' ' + 'book' + ' ' + 'PDF']
y = 0
for y in trange(len(names)):
    if y >= len(names):
        break
    site = re.get(linkz[y]).text
    for word in words:
        if word in site:
            y += 1
        else:
            names.remove(names[y])
            linkz.remove(linkz[y])
            sleep(0.01)
print(len(linkz))
print(len(names))


# In[ ]:


book_links = list()
z = 0
for z in trange(len(linkz)):
    driver.get(linkz[z])
    data = (driver.find_element_by_partial_link_text("Download").get_attribute('href'))
    book_links.append(data)
    z += 1
    sleep(0.01)
print(len(book_links))


# In[ ]:


for t in trange(len(book_links)):
    r = re.get(book_links[t])
    open(names[t] + '.pdf', 'wb').write(r.content)
    sleep(0.01)

