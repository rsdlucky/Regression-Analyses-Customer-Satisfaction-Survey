#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


# In[46]:


survey = pd.read_csv("C:\\Users\\DBSOM-L490-10\\OneDrive\\Desktop\\survey.csv")


# In[47]:


survey.head(10)


# In[48]:


survey.corr()


# In[24]:


import seaborn as sns


# In[25]:


sns.pairplot(survey)


# In[8]:


import statsmodels.formula.api as smf


# In[59]:


import statsmodels.api as sm


# In[49]:


survey.columns


# In[39]:


df = pd.DataFrame({"How satisfied were you with your experience with us?","How do you rate the environment and ambience of our store?","How do you rate the behavior and support of the staff at our store?","How would you rate the quality of our products?","How much are you satisfied with our customer service?"})


# In[40]:


print(df)


# In[56]:


x = survey[['How do you rate the environment and ambience of our store?','How do you rate the behavior and support of the staff at our store?','How would you rate the quality of our products?','How much are you satisfied with our customer service?']]


# In[57]:


y = survey['How satisfied were you with your experience with us?']


# In[60]:


X = sm.add_constant(x)


# In[65]:


ml1 = sm.OLS(y, X).fit()


# In[66]:


ml1.summary()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




