
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt


# In[2]:


file = r'C:\Users\Sara\Dropbox (Politecnico Di Torino Studenti)\Aplanet_\all_Madrid.xlsx'

xl= pd.ExcelFile(file)      # Load spreadsheet
df = xl.parse('Sheet1')    # Load a sheet into a DataFrame by name: df1
df.index  = np.arange(len(df))
df=df.iloc[:, [1,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208]]


# In[3]:


pd.set_option('display.max_columns', None)
df


# In[4]:


df1=df
df2=df
df3=df
df4=df

for i in range(181):
    if df1['mod'][i]!=1:
        df1=df1.drop(i)
    if df2['mod'][i]!=2:
        df2=df2.drop(i)
    if df3['mod'][i]!=3:
        df3=df3.drop(i)
    if df4['mod'][i]!=4:
        df4=df4.drop(i)
df1.index  = np.arange(len(df1))
df2.index  = np.arange(len(df2))
df3.index  = np.arange(len(df3))
df4.index  = np.arange(len(df4))

a=[df1,df2,df3,df4]
b=[df1,df2,df3,df4]
for k in range(4):
    for i in range(len(a[k])):
        if a[k]['player.SN_car_A'][i]==0:
            a[k]=a[k].drop(i)
    a[k].index  = np.arange(len(a[k]))
    for i in range(len(b[k])):
        if b[k]['player.SN_car_A'][i]==1:
            b[k]=b[k].drop(i)
    b[k].index  = np.arange(len(b[k]))


# In[11]:


EEa=[[],[],[],[]]
NEa=[[],[],[],[]]
EEb=[[],[],[],[]]
NEb=[[],[],[],[]]
for k in range(4):
    for i in range(len(a[k])):
        EEa[k] = np.append(EEa[k],(a[k]['player.HH'][i]-a[k]['player.LH'][i] + a[k]['player.HL'][i]-a[k]['player.LL'][i])/2)
        NEa[k] = np.append(NEa[k],(a[k]['player.HH'][i]-a[k]['player.HL'][i] + a[k]['player.LH'][i]-a[k]['player.LL'][i])/2)

    for i in range(len(b[k])):
        EEb[k] = np.append(EEb[k],(-b[k]['player.HH'][i]+b[k]['player.LH'][i] - b[k]['player.HL'][i]+b[k]['player.LL'][i])/2)
        NEb[k] = np.append(NEb[k],(-b[k]['player.HH'][i]+b[k]['player.HL'][i] - b[k]['player.LH'][i]+b[k]['player.LL'][i])/2) 


# In[20]:


plt.figure(figsize=(5,5))

for k in range(4):
    plt.plot(EEa[k],NEa[k],'ko',label='Private car')
    plt.plot(EEb[k],NEb[k],'ro',label='100 - Public transport')
    plt.xlabel("Empirical Expectation influence")
    plt.ylabel("Normative Expectation influence")
    plt.axhline(0, color='k')
    plt.axvline(0, color='k')
    plt.title('Treatment %d Madrid' %(k+1))
    plt.legend()
    plt.savefig('SN_madrid%d.png' %(k+1))
    plt.show()


# In[ ]:


new=df1.groupby(['By which mode do you travel with during this trip? If you travel with multiple modes choose the mode that takes you the longest time.','If you were to make this trip using a different mode of travel than your usual mode, which would be the best alternative?'])


# In[ ]:


chord=new.size().reset_index(name="Time")
#chord.to_excel("chord_madrid.xlsx") 


# In[77]:


groups = [self.getGroup(selected, header + i) for i in range(3)]

