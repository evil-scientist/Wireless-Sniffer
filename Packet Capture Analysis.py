#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
from matplotlib.patches import Rectangle
data = pd.read_csv("data/netflix_results.csv") 


# In[2]:


# Preview the first 5 lines of the loaded data 
data.head()


# In[3]:


#Number of Packets in captured Session
data['frame.number'].count()


# In[4]:


print('The largest frame that was captured: ', data['frame.len'].max(), ' bytes')
print('The smallest frame that was captured: ', data['frame.len'].min(), ' bytes')
print('The lowest radio signal strength: ', data['wlan_radio.signal_dbm'].max(),' dBm')
print('The highest radio signal strength: ', data['wlan_radio.signal_dbm'].min(),' dBm')


# In[5]:


# How many Packets are there for each Frame Type?
data['wlan.fc.type'].value_counts()


# In[6]:


#Plot the distribution:
ftypes = ['Management Frame','Control Frame','Data Frame']
pos = np.arange(len(ftypes))
data.groupby('wlan.fc.type')['frame.number'].nunique().plot(kind='bar')
plt.title("Distribution of frames on type")
plt.xlabel("Frame type")
plt.ylabel("Number of Packets")
plt.xticks(pos,ftypes,rotation=0)
plt.show()


# In[7]:


# How many Packets are there for each SubFrame Type?
data.groupby('wlan.fc.type')['wlan.fc.subtype'].value_counts()


# In[8]:


data.groupby(['wlan.fc.type','wlan.fc.subtype'])['frame.number'].nunique()


# In[20]:


#Plot the distribution:
ftypes = ['Association Request','Probe Request','Probe Response','Beacon',
            'Annoucement Traffic Indication Map','Authentication','DeAuthentication','Action Frames','Control Frame End']
pos = np.arange(len(ftypes))
data.groupby(['wlan.fc.type','wlan.fc.subtype'])['frame.number'].nunique().plot(kind='bar')
#data.groupby('wlan.fc.subtype')['frame.number'].nunique().plot(kind='bar')
plt.title("Distribution of frames on subtype")
plt.xlabel("Frame Subtype")
plt.ylabel("Number of Packets")
#plt.xticks(pos,ftypes,rotation=0)
plt.show()


# In[10]:


#Which direction does the data flow (number of Packets)?
data['wlan.fc.ds'].value_counts()


# In[11]:


#Plot the distribution:
ftypes = ['STA to STA','STA to AP','AP to STA','AP to AP']
pos = np.arange(len(ftypes))
data.groupby('wlan.fc.ds')['frame.number'].nunique().plot(kind='bar')
plt.title("Distribution of Traffic Direction")
plt.xlabel("Traffic Direction")
plt.ylabel("Number of Packets")
plt.xticks(pos,ftypes,rotation=0)
plt.show()


# In[12]:


#What QoS does the data flows have?
data['wlan.qos.priority'].value_counts()


# In[13]:


#Plot the distribution:
ftypes = ['Best Effort','Spare(Background)','Video (Controlled Load)','Video','Voice']
pos = np.arange(len(ftypes))
data.groupby('wlan.qos.priority')['frame.number'].nunique().plot(kind='bar')
plt.title("Distribution of QoS Traffic")
plt.xlabel("QoS Class")
plt.ylabel("Number of Packets")
plt.xticks(pos,ftypes,rotation=0)
plt.show()


# In[14]:


#Max data transferred in a packet(bytes)
data['data.len'].max()


# In[15]:


#Min data transferred in a packet(bytes)
data['data.len'].min()


# In[16]:


#Plot the distribution of data length (bytes):
bin1 = [i for i in range(0,1000,10)]
data[['data.len']].plot(kind='hist',bins=bin1,rwidth=0.8)
plt.show()


# In[17]:


#Plot the distribution of data length (bytes):
bin1 = [i for i in range(0,1600,10)]
data[['data.len']].plot(kind='hist',bins=bin1,rwidth=0.8)
plt.show()


# In[18]:


data['data.len'].value_counts()


# In[ ]:




