#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
import pandas as pd
from pandas.io.json import json_normalize
from sqlalchemy import create_engine


# In[5]:


import requests

# make a request to the server 
response = requests.get(URI)

# parse the response (only works for JSON format)
data = response.json() 


# In[6]:


print(data)


# In[ ]:





# In[117]:


def get_URI(query:str, page_num:int, sort_order:str, API_KEY:str) -> str:
    
    # create a URI string
    URI = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q='+"covid"
    
    # if a page number is mentioned, add it to the URI
    if page_num:
        add_to_URI = '&page='+str(page_num)
        URI+= add_to_URI
    
    # if the sorting order is mentioned, add it to the URI
    if sort_order:
        add_to_URI = '&sort='+sort_order
        URI += add_to_URI
    
    # add the given API key to the URI
    add_to_URI = '&api-key='+API_KEY
    URI += add_to_URI
    
    # return the new URI 
    return URI


# In[118]:



# get the URI needed for the articles related to Winter Olympics in page 1 from newest to oldest
URI = get_URI(query='covid', page_num=1, sort_order='newest', API_KEY="cLado0kSBDKhVRbKrTKsOf5KcQHeuAhA")


# In[119]:


import requests

# make a request to the server 
response = requests.get(URI)

# parse the response (only works for JSON format)
data = response.json() 


# In[120]:


print(data)


# In[121]:


from pandas.io.json import json_normalize

# convert JSON response to a data frame
df = json_normalize(data['response'], record_path=['docs'])


# In[122]:


df[['headline.main', 'pub_date']].head(5)


# In[ ]:





# In[123]:


pip install gTTS


# In[41]:


from gtts import gTTS

text = "Hello! My name is Vishwa."
tts = gTTS(text)
tts.save("hi.mp3")


# In[ ]:





# In[42]:


text = input("Enter your text: ")
tts = gTTS(text)
tts.save("user_input.mp3")


# In[43]:


import os 
os.system("hi.mp3")


# In[45]:


pip install playsound


# In[46]:


from playsound import playsound
os.system("user_input.mp3")


# In[124]:


if len(df['_id'].unique()) < len(df):
    print('There are duplicates in the data')
    df = df.drop_duplicates('_id', keep='first')

# search for and replace articles with missing headlines
if df['headline.main'].isnull().any():
    print('There are missing values in this dataset')
    df = df[df['headlinee.main'].isnull()==False]

# filter out any op-eds
df = df[df['type_of_material']!='op-ed']

# keep only headline, publication_date, author name, and url
df = df[['headline.main', 'pub_date', 'byline.original', 'web_url']]

# rename columns
df.columns = ['headline', 'date', 'author', 'url']


# In[125]:


df


# In[126]:


df.columns


# In[127]:


df2 = df[['headline','author']]


# In[128]:


df2


# In[ ]:





# In[89]:


import pandas as pd
import sqlalchemy


# In[86]:


#engine = sqlalchemy.create_engine('mysql+pymysql://root:admin@localhost:3306/applications')


# In[ ]:





# In[131]:


from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:1234@localhost:5432/covid_data')
df2.to_sql('covid_data5', engine)


# In[133]:


df2


# In[ ]:




