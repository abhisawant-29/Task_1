#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv("Salesdata.csv")
print(df.info())
print(df.head())


# In[4]:


df.rename(columns={'c':'Order_Date'}, inplace=True)


# In[5]:


df['Price'] = pd.to_numeric(df['Price'],errors='coerce')


# In[6]:


df['Order_Date']=pd.to_datetime(df['Order_Date'],errors='coerce')


# In[9]:


df[' Account_Created']=pd.to_datetime(df['Last_Login'],errors='coerce')


# In[10]:


df['Price'].fillna(df['Price'].median(),inplace=True)


# In[11]:


df['State'].fillna('Unknown', inplace=True)


# In[13]:


df.drop_duplicates(inplace=True)


# In[15]:


df.drop(columns=['Order_Date'],inplace=True)


# In[16]:


print(df.head())


# In[18]:


df.head(10).style.set_table_styles([{'selector': 'th', 'props': [('font-size', '12pt'), ('background-color', '#f0f0f0')]}]).set_properties(**{'text-align': 'left'}).hide(axis="index")


# In[ ]:




