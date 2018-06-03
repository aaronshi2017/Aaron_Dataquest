
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib 
get_ipython().magic('matplotlib inline')


# In[3]:


recent_grads=pd.read_csv("recent-grads.csv")
print(recent_grads.iloc[0])
print(recent_grads.head())
print(recent_grads.tail())
print(recent_grads.describe())


# In[10]:


raw_data_count=len(recent_grads.index)
#print(recent_grads)
recent_grads=recent_grads.dropna()
cleaned_data_count=len(recent_grads.index)
print(raw_data_count)
print(cleaned_data_count)


# In[14]:


recent_grads.plot(x="Sample_size",y="Median",kind='scatter', title='Median vs. Sample_size', figsize=(5,10))
recent_grads.plot(x="Sample_size",y="Unemployment_rate",kind='scatter', title='Unemployment_rate vs. Sample_size', figsize=(5,10))
recent_grads.plot(x="Full_time",y="Median",kind='scatter', title='Median vs. Full_time', figsize=(5,10))
recent_grads.plot(x="ShareWomen",y="Unemployment_rate",kind='scatter', title='Unemployment_rate vs. ShareWomen', figsize=(5,10))
recent_grads.plot(x="Men",y="Median",kind='scatter', title='Median vs.Men ', figsize=(5,10))
recent_grads.plot(x="Women",y="Median",kind='scatter', title='Median vs.Women ', figsize=(5,10))


# In[23]:


recent_grads["Sample_size"].hist(bins=25)  
recent_grads["Median"].hist(bins=25)  
recent_grads["Employed"].hist(bins=25)  
recent_grads["Full_time"].hist(bins=25)  
recent_grads["ShareWomen"].hist(bins=25)  
recent_grads["Unemployment_rate"].hist(bins=25)  
recent_grads["Men"].hist(bins=25)  
recent_grads["Women"].hist(bins=25)  


# In[25]:


from pandas.tools.plotting import scatter_matrix
scatter_matrix(recent_grads[["Sample_size","Median"]],figsize=(10,10))
scatter_matrix(recent_grads[["Sample_size","Median","Unemployment_rate"]])


# In[30]:


recent_grads=recent_grads.sorted_
recent_grads[:10]["ShareWomen"].plot(kind="bar")


# In[29]:


recent_grads[-10:]["ShareWomen"].plot(kind="bar")

