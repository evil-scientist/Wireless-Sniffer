#!/usr/bin/env python
# coding: utf-8

# In[34]:


import matplotlib.pyplot as plt
import pandas as pd 
data = pd.read_csv("data/netflix_results.csv") 


# In[35]:


# Preview the first 5 lines of the loaded data 
data.head()


# In[36]:


#Number of Packets in captured Session
data['frame.number'].count()


# In[37]:


print('The largest frame that was captured: ', data['frame.len'].max(), ' bytes')
print('The smallest frame that was captured: ', data['frame.len'].min(), ' bytes')
print('The lowest radio signal strength: ', data['wlan_radio.signal_dbm'].max(),' dBm')
print('The highest radio signal strength: ', data['wlan_radio.signal_dbm'].min(),' dBm')


# In[38]:


# How many Packets are there for each Frame Type?
data['wlan.fc.type'].value_counts()


# In[41]:


#Plot the distribution:
data.groupby('wlan.fc.type')['frame.number'].nunique().plot(kind='bar')
plt.title("Distribution of frames on type")
plt.xlabel("Frame type")
plt.ylabel("Number of Packets")
plt.show()


# In[6]:


# How many Packets are there for each SubFrame Type?
data['wlan.fc.subtype'].value_counts()


# In[40]:


#Plot the distribution:
data.groupby('wlan.fc.subtype')['frame.number'].nunique().plot(kind='bar')
plt.title("Distribution of frames on subtype")
plt.xlabel("Frame Subtype")
plt.ylabel("Number of Packets")
plt.show()


# In[7]:


#Which direction does the data flow (number of Packets)?
data['wlan.fc.ds'].value_counts()


# In[18]:


#Plot the distribution:
data.groupby('wlan.fc.ds')['frame.number'].nunique().plot(kind='bar')
plt.show()


# In[8]:


#What QoS does the data flows have?
data['wlan.qos.priority'].value_counts()


# In[19]:


#Plot the distribution:
data.groupby('wlan.qos.priority')['frame.number'].nunique().plot(kind='bar')
plt.show()


# In[23]:


#Max data transferred in a packet(bytes)
data['data.len'].max()


# In[24]:


#Min data transferred in a packet(bytes)
data['data.len'].min()


# In[33]:


#Plot the distribution of data length (bytes):
bin1 = [i for i in range(0,1400,10)]
data[['data.len']].plot(kind='hist',bins=bin1,rwidth=0.8)
plt.show()


# In[ ]:




