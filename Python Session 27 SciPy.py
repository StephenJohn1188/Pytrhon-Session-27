#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


data=pd.read_csv('brain_size.csv',sep=';',na_values='.')
data


# In[4]:


from scipy import stats


# In[5]:


stats.ttest_1samp(data['PIQ'],106)


# In[7]:


data.corr()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




