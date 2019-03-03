#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
from matplotlib.patches import Rectangle
data = pd.read_csv("Data/Cafeteria_2_results.csv") 
# Preview the first 5 lines of the loaded data 
data.head()


# In[2]:


print('The number of frames that were captured: ', data['frame.number'].count(), ' frames')
print('The largest frame that was captured: ', data['frame.len'].max(), ' bytes')
print('The smallest frame that was captured: ', data['frame.len'].min(), ' bytes')
print('The lowest radio signal strength: ', data['wlan_radio.signal_dbm'].max(),' dBm')
print('The highest radio signal strength: ', data['wlan_radio.signal_dbm'].min(),' dBm')


# In[3]:


direction = []
for x in data.groupby('wlan.fc.ds')['frame.number'].nunique():
    direction.append(x/data['frame.number'].count()*100)
if len(direction) != 4:
    direction.append(0)
#print(direction)


# In[6]:


#Plot the distribution:
ftypes = ['STA to STA','STA to AP','AP to STA','AP to AP']
pos = np.arange(len(ftypes))
#data.groupby('wlan.fc.ds')['frame.number'].nunique().plot(kind='bar')
rect1 = plt.bar(x=pos, height=direction, width=0.8, align='center', color=['#1F77B4','#FF7F0E','#2CA02C','#D62728'])
plt.title("Distribution of Traffic Direction")
plt.xlabel("Traffic Direction")
plt.ylabel("Packets %")
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2., 1.0*height,
                '%0.2f%%' % (height),
                ha='center', va='bottom')
autolabel(rect1)
plt.xticks(pos,ftypes,rotation=0)
plt.show()


# In[ ]:


# How many Packets are there for each Frame Type?
data['wlan.fc.type'].value_counts()


# In[ ]:


types = list(data['wlan.fc.type'].value_counts())
types = (types/data['frame.number'].count())*100
print(types)


# In[ ]:



#Plot the distribution:
ftypes = ['Management Frame','Control Frame','Data Frame','Corrupted Frame']
pos = np.arange(len(ftypes))
#data.groupby('wlan.fc.type')['frame.number'].nunique().plot(kind='bar')
rect2 = plt.bar(x=pos, height=types, width=0.5, align='center', color=['#1F77B4','#FF7F0E','#2CA02C','#D62728'])
plt.title("Distribution of frames based on type")
plt.xlabel("Frame type")
plt.ylabel("Packets %")
autolabel(rect2)
plt.xticks(pos,ftypes,rotation=0)
plt.show()


# In[ ]:


# How many Packets are there for each SubFrame Type?
for x in data.groupby('wlan.fc.type')['wlan.fc.subtype'].value_counts():
    print (x)


# In[ ]:


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
plt.xticks(rotation=0)

plt.show()


# In[ ]:


#Which direction does the data flow (number of Packets)?
data['wlan.fc.ds'].value_counts()


# In[ ]:


#What QoS does the data flows have?
qos=list(data['wlan.qos.priority'].value_counts())
print(qos)
total_qos =sum(qos)
for x in range(len(qos)):
    qos[x] = (qos[x]/total_qos)*100
print(qos)


# In[ ]:



#Plot the distribution:
ftypes = ['Best Effort','Spare \n (Background)','Video \n (Controlled Load)','Video','Voice']
pos = np.arange(len(ftypes))
rects3 = plt.bar(x=pos, height=qos, width=0.5, align='center', color=['#17BECF','#1F77B4','#FF7F0E','#2CA02C','#D62728'])
plt.title("Distribution of QoS Traffic")
plt.xlabel("QoS Class")
plt.ylabel("Number of Packets")
plt.xticks(pos,ftypes,rotation=0, fontsize=8)

autolabel(rects3)
plt.show()


# In[ ]:


#Max data transferred in a packet(bytes)
data['data.len'].max()


# In[ ]:


#Min data transferred in a packet(bytes)
data['data.len'].min()


# In[ ]:


#Plot the distribution of data length (bytes):
bin1 = [i for i in range(0,1000,10)]
data[['data.len']].plot(kind='hist',bins=bin1,rwidth=0.8)
plt.show()


# In[ ]:


#Plot the distribution of data length (bytes):
bin1 = [i for i in range(0,1600,10)]
data[['data.len']].plot(kind='hist',bins=bin1,rwidth=0.8)
plt.show()


# In[ ]:


data['data.len'].value_counts()


# In[ ]:


#Packet Size over Time
plt.plot(data['frame.time_relative'], data['data.len'])

#bin1 = [i for i in range(0,1600,100)]
#data[['data.len']].plot(kind='hist',bins=bin1,rwidth=0.8)
plt.show()


# In[ ]:


#Packet Size over Time
plt.scatter(data['wlan_radio.signal_dbm'], data['wlan_radio.data_rate'],marker='X',s=1**2)

#bin1 = [i for i in range(0,1600,100)]
#data[['data.len']].plot(kind='hist',bins=bin1,rwidth=0.8)
plt.show()


# In[ ]:


data[['wlan_radio.signal_dbm']].plot(kind='bar')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




