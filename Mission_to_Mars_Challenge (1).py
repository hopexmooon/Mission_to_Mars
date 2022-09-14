#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[38]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[40]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

#slide_elem = news_soup.select_one('div.list_text')
slide_elem = news_soup.find('div', class_ = 'list_text')

print(slide_elem)


# In[33]:


slide_elem.find('div', class_='content_title')


# In[34]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[35]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[41]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[42]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[43]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[44]:


img_soup.find('img', class_='fancybox-image')


# In[45]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[46]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[49]:


#pd.read_html('https://galaxyfacts-mars.com')


# ### Mars Facts

# In[51]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[52]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[53]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[3]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[55]:


for hem in range(4):
    print(hem)


# In[57]:


len(browser.links.find_by_partial_text('Hemisphere'))


# In[63]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for hem in range(4):
    browser.links.find_by_partial_text('Hemisphere')[hem].click()

        
    # Parse the HTML
    html = browser.html
    hem_soup = soup(html,'html.parser')
        
    # Scraping
    img_url = hem_soup.find("a", text="Sample").get("href")
    title =  hem_soup.find("h2", class_="title").get_text()

    #title = hem_soup.find('a', class_='itemLink').text
    #img_url = hem_soup.find('a').get('item')
        
    # Store findings into a dictionary and append to list
    hemispheres = {}
    hemi_dict = {'img_url': img_url,'title': title}
    hemisphere_image_urls.append(hemi_dict)
    browser.back()
   

    
    


# In[64]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[65]:


# 5. Quit the browser
browser.quit()


# In[ ]:




