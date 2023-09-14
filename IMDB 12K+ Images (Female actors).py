#!/usr/bin/env python
# coding: utf-8

# ![image.png](attachment:image.png)

# In[1]:


import urllib.request
import time
import os
from bs4 import BeautifulSoup

url_template = "https://www.imdb.com/search/name/?gender=female&count=100&start={}&ref_=rlm"

# Folder to store downloaded images
folder = "C:\\Users\\Mamun\\A_Python_Learning\\Python_folder\\Integrify\\female_imdb"

# Create folder if it doesn't exist
if not os.path.exists(folder):
    os.makedirs(folder)

# Initialize count
count = 1

# Loop through the search result pages and download images
for start in range(1, 10001, 100):
    url = url_template.format(start)
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all("div", {"class": "lister-item mode-detail"})
    
    for result in results:
        # Extract name and image URL from search result
        name = result.find("img").get('alt')
        img_url = result.find("img").get('src')
        
        # Replace special characters in the name with hyphens
        img_name = name.replace(" ", "_") + ".jpg"        
        
        # Download the image and save to folder
        img_path = os.path.join(folder, img_name)
        urllib.request.urlretrieve(img_url, img_path)   
        
        print(f'Image {count}: {img_name} downloaded!')
        count += 1
        
    time.sleep(1)


# ### A total of 10,000 images of female actresses were downloaded from popular IMDB.

# ![image.png](attachment:image.png)
