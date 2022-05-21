#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy import stats
from scipy.stats import norm


# In[2]:


# For No investigation P(45<X<55)
# For Investigation 1-P(45<X<55)


# In[3]:


# find z-scores at x=45; z=(s_mean-P_mean)/(p_SD/sqrt(n))
z=(45-50)/(40/100**0.5)
z


# In[5]:


# find z-scores at x=55; z=(s_mean-P_mean)/(p_SD/sqrt(n))
z=(55-50)/(40/100**0.5)
z


# In[6]:


# For No investigation P(45<X<55) using z_scores = P(X<50)-P(X<45)
stats.norm.cdf(1.25)-stats.norm.cdf(-1.25)


# In[7]:


stats.norm.interval(0.7887,loc=50,scale=40/(100**0.5))


# In[8]:


# For Investigation 1-P(45<X<55)
1-0.7887


# In[ ]:


# hence Ans is D. 21.1%

