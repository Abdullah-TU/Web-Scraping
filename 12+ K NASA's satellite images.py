#!/usr/bin/env python
# coding: utf-8

# ![image.png](attachment:image.png)

# In[1]:


import requests
import os

# Define URL and headers
url = 'https://earthobservatory.nasa.gov/images/getRecords?page='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# Set image directory
image_directory = "C:\\Users\\Mamun\\A_Python_Learning\\Python_folder\\Integrify\\Nasa_Images"

if not os.path.exists(image_directory):
    os.makedirs(image_directory)

image_count = 0
    
# Loop through pages
for page in range(1, 2960): 
    page_url = url + str(page)
    print()
    print(f"Page Number: {page}")    
    
    # Get JSON data for page
    try:
        response = requests.get(page_url, headers=headers)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}, skipping page {page}")
        continue
        
    # Download images from page
    for record in data['data']:
        image_url = record['image_path'] + record['thumbnail_file']
        title = record['title']
        
        # Replace special characters(i.e.: ? or some other) in the title with hyphens
        filename = "".join(c if c.isalnum() or c in ['.', '-'] else ' ' for c in title) 
        
        # Append the file extension to the filename
        file_extension = image_url.split('.')[-1]
        filename = f"{filename}.{file_extension}"
        
        filepath = os.path.join(image_directory, filename)
        if not os.path.exists(filepath):
            image_count += 1
            print(f"Image {image_count}: {filename} downloaded.")
            
            try:
                image_response = requests.get(image_url)
                image_response.raise_for_status()
                with open(filepath, 'wb') as f:
                    f.write(image_response.content)
            except requests.exceptions.RequestException as e:
                print(f"Error downloading {filename}: {e}")
        else:
            print(f"{filename} already downloaded.")    


# ### A total of 10,000 images were downloaded from NASA's satellite website.

# ![image-2.png](attachment:image-2.png)
