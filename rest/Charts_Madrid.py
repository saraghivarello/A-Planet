
# coding: utf-8


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

file2 = r'C:\Users\Sara\Dropbox (Politecnico Di Torino Studenti)\Aplanet_\all_Madrid.xlsx'
xl2= pd.ExcelFile(file2)      # Load spreadsheet
df2 = xl2.parse('Sheet1')    # Load a sheet into a DataFrame by name: df1
df2.index  = np.arange(len(df2))
df_mad=df2.drop(['Unnamed: 0'], axis=1)
file3 = r'C:\Users\Sara\Dropbox (Politecnico Di Torino Studenti)\Aplanet_\all_parts.xlsx'
xl3= pd.ExcelFile(file3)      # Load spreadsheet
df3 = xl3.parse('Sheet1')    # Load a sheet into a DataFrame by name: df1
df3.index  = np.arange(len(df3))
df_all=df3.drop(['Unnamed: 0'], axis=1)

v=[]
for i in df_mad['mod']:
    if math.isnan(i) is True:
        v.append('-')
    elif i==1:
        v.append('No information')
    elif i==2:
        v.append('Congestion and pollution')
    elif i==3:
        v.append('Public services')
    elif i==4:
        v.append('Redistribution')
df_mad.insert(loc=1, column='Treatment', value=v)
#df.drop(['mod'], inplace=True, axis=1)
df_mad=df_mad.rename(columns={"player.HH": "High EE High NE","player.HL": "High EE Low NE", "player.LH": "Low EE High NE","player.LL": "Low EE Low NE"})

v=[]
for i in df_all['mod']:
    if math.isnan(i) is True:
        v.append('-')
    elif i==1:
        v.append('No information')
    elif i==2:
        v.append('Congestion and pollution')
    elif i==3:
        v.append('Public services')
    elif i==4:
        v.append('Redistribution')
df_all.insert(loc=1, column='Treatment', value=v)
#df.drop(['mod'], inplace=True, axis=1)
df_all=df_all.rename(columns={"player.HH": "High EE High NE","player.HL": "High EE Low NE", "player.LH": "Low EE High NE","player.LL": "Low EE Low NE"})


column= df_mad['Which year were you born?']
mean_m_age=np.mean(column)
std_m_age=np.std(column)
age=2022-mean_m_age

column= df_mad['player.gender']
for i in df_mad.index:
    if column[i] == 2 or column[i] == 3:
        print('a')
        column[i]=0.5
mean_m_g=np.mean(column)
std_m_g=np.std(column)
sum(column)/len(column)
df_mad.index
1-mean_m_g

column= df_mad['player.family']
mean_m_f=np.mean(column)
std_m_f=np.std(column)
len(column)


column= df_mad['player.children']
mean_m_c=np.mean(column)
std_m_c=np.std(column)
max(column)

summm=0.065*1+0.199*2+0.255*3+0.107*4+0.362*5
np.sqrt(0.065*(1-summm/15)**2+0.199*(2-summm/15)**2)
# df_mad=df_mad.rename(columns={"How much do you personally trust the following institutions from 1 to 7, where 1 means ‘No trust at all’ and 7 means ‘Trust compltely’? Parlament: ": "Parlament","County council:":"County\ncouncil","Municipal council": "Municipal\ncouncil","Government:": "Government", "National politicians:":"National\npoliticians", "Political parties: ":"Political\nparties"})
# d=pd.DataFrame( index=[0,1])
# for i in [222,224,226,228,230]:
#     column= df_mad.columns[i]
#     a=df_mad.groupby([column]).count()['mod']
#     per=0
#     s=0
#     dev=0
#     for j in range(1,8):
#         per=per+j*a[j]
#         s=s+a[j]
#     d.at[0,column] = per/s
#     for j in range(1,8):  
#         dev=dev+(a[j]*(j-d.at[0,column])**2)
#     d.at[1,column] = np.sqrt(dev/s)
# column= df_mad.columns[232]
# a=df_mad.groupby([column]).count()['mod']
# per=0
# s=0
# dev=0
# for j in range(1,7):
#     per=per+j*a[j]
#     s=s+a[j]
# d.at[0,column] = per/s
# for j in range(1,7):  
#     dev=dev+(a[j]*(j-d.at[0,column])**2)
# d.at[1,column] = np.sqrt(dev/s)
    
v_mean=[]
v_std=[]
d=pd.DataFrame( index=[0,1])
for i in [222,224,226,228,230,232]:
    column= df_mad.columns[i]
    integers = [x for x in df_mad[column] if isinstance(x, int)]
    v_mean.append(np.mean(integers))
    v_std.append(np.std(integers))

plt.figure(figsize=(10,7))
plt.bar(np.linspace(0,6,6), v_mean, yerr=v_std, width=0.7, edgecolor='k',color='moccasin')
plt.xticks(np.linspace(0,6,6),['Parlament','County\ncouncil','Municipal\ncouncil','Government','National\npoliticians','Political\nparties'], fontsize=12)
plt.ylim([0,7])
#plt.savefig(r'C:\Users\Sara\Dropbox (Politecnico Di Torino Studenti)\Aplanet_\rate_gov_m.png')

df_mad=df_mad.rename(columns={"How much do you agree with the following statements from 1 to 7, where 1 means ‘I completely disagree’ and 7 means ‘I completely agree’? Air pollution derived by cars is one of the major causes of premature death in Europe:": r"$\bf{Air }$ "+r"$\bf{pollution}$ "+"derived by cars\nis one of the major causes\nof premature death in Europe","The introduction of policies such as road pricing will alleviate congestion problems:":"The introduction of policies\nsuch as "+r"$\bf{road }$ "+r"$\bf{pricing}$ "+"will\nalleviate congestion problems","Revenues collected through taxes are used to create a well-functioning welfare state and society:": r"$\bf{Revenues}$ "+"collected through taxes\nare used to create a well-functioning\nwelfare state and society","Tax revenues should be used to help those who are more in need:": r"$\bf{Tax}$ "+"revenues should\nbe used to help those\nwho are more in need"})
def bar(d):
    d.index  = np.arange(len(d))
    x=pd.DataFrame( index=[0,1])
    for i in [236,238,240,242]:
        column= d.columns[i]
        x.at[0,column] = d[column].mean()
        x.at[1,column] = d[column].std()/np.sqrt(len(d[column]))    
    return x
df_mad=df_mad.rename(columns={"How much do you agree with the following statements from 1 to 7, where 1 means ‘I completely disagree’ and 7 means ‘I completely agree’? Air pollution derived by cars is one of the major causes of premature death in Europe:": r"$\bf{Air }$ "+r"$\bf{pollution}$ "+"derived by cars\nis one of the major causes\nof premature death in Europe","The introduction of policies such as road pricing will alleviate congestion problems:":"The introduction of policies\nsuch as "+r"$\bf{road }$ "+r"$\bf{pricing}$ "+"will\nalleviate congestion problems","Revenues collected through taxes are used to create a well-functioning welfare state and society:": r"$\bf{Revenues}$ "+"collected through taxes\nare used to create a well-functioning\nwelfare state and society","Tax revenues should be used to help those who are more in need:": r"$\bf{Tax}$ "+"revenues should\nbe used to help those\nwho are more in need"})

fig=plt.figure(figsize=(17,8))
ind = np.arange(4)
width = 0.2

plt.bar(ind, bar(df_mad).loc[0][:], yerr=bar(df_mad).loc[1][:], width=width, edgecolor='k', label='Madrid')
plt.bar(ind+width, bar(df_all).loc[0][:], yerr=bar(df_all).loc[1][:], width=width, edgecolor='k', label='All population')

plt.xticks([r + width*1/2 for r in range(4)], df_mad.columns[[237,239,241,243]], fontsize=15)
plt.yticks(fontsize=15)
plt.ylim([0,7])
leg=plt.legend(loc='best',fontsize=15)
plt.tight_layout(pad=2,w_pad=8, h_pad=3)
plt.grid()
plt.savefig(r'C:\Users\Sara\Dropbox (Politecnico Di Torino Studenti)\Aplanet_\bars\agree_mad_all.png')
plt.show()


plt.figure(figsize=(12,9))
plt.bar(np.linspace(0,12,4), d.loc[0][:], yerr=d.loc[1][:], width=1.2, edgecolor='k',color='moccasin')
plt.xticks(np.linspace(0,12,4),d.columns, fontsize=10)
plt.ylim([0,7])
#plt.savefig(r'C:\Users\Sara\Dropbox (Politecnico Di Torino Studenti)\Aplanet_\air_poll_m.png')

df_mad.columns[225]

def bar1(d):
    d.index  = np.arange(len(d))
    x=pd.DataFrame( index=[0,1])
    for i in [222,224,226,228,230,232]:
        column= d.columns[i]
        x.at[0,column] = d[column].mean()
        x.at[1,column] = d[column].std()/np.sqrt(len(d[column]))    
    return x
bar1(df_mad)

df_mad=df_mad.rename(columns={"How much do you personally trust the following institutions from 1 to 7, where 1 means ‘No trust at all’ and 7 means ‘Trust compltely’? Parlament: ": "Parlament","County council:":"County\n council","Government:": "Government", "National politicians:":"National\n politicians", "Political parties: ":"Political\n parties"})

fig=plt.figure(figsize=(15,8))
ind = np.arange(6)
width = 0.2

plt.bar(ind, bar1(df_mad).loc[0][:], yerr=bar1(df_mad).loc[1][:], width=width, edgecolor='k', label='Madrid')
plt.bar(ind+width, bar1(df_all).loc[0][:], yerr=bar1(df_all).loc[1][:], width=width, edgecolor='k', label='All population')

plt.xticks([r + width*1/2 for r in range(6)], df_mad.columns[[223,225,227,229,231,233]], fontsize=15)
plt.yticks(fontsize=15)
plt.ylim([0,7])
leg=plt.legend(loc='best',fontsize=15)
plt.tight_layout(pad=2,w_pad=8, h_pad=3)
plt.grid()
plt.savefig(r'C:\Users\Sara\Dropbox (Politecnico Di Torino Studenti)\Aplanet_\bars\trust_mad_all.png')
plt.show()
