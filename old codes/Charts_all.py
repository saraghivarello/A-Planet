# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


file = r'C:\Users\Sara\Dropbox (Politecnico Di Torino Studenti)\Aplanet_\all_parts.xlsx'
xl1= pd.ExcelFile(file)      # Load spreadsheet
df1 = xl1.parse('Sheet1')    # Load a sheet into a DataFrame by name: df1
df1.index  = np.arange(len(df1))
df_all=df1.drop(['Unnamed: 0'], axis=1)

non=0
column= df_all['player.gender']
for i in df_all.index:
    if column[i] == 2 or column[i] == 3:
        non+=1
        #column[i]=0.5
mean_m_g=np.mean(column)
std_m_g=np.std(column)
1-mean_m_g


column= df_all['Which year were you born?']
mean_m_age=np.mean(column)
std_m_age=np.std(column)
len(column)

column= df_all['player.family']
mean_m_f=np.mean(column)
std_m_f=np.std(column)
len(column)


column= df_all['player.children']
mean_m_c=np.mean(column)
std_m_c=np.std(column)
min(column)



column= df_all['Which year were you born?']
x=df_all.groupby([column]).count()['mod']
df_age = pd.DataFrame([x]).T
df_age.reset_index(inplace=True)
summ=0
for i in range(len(df_age['mod'])):
    summ=summ+df_age['Which year were you born?'][i]*df_age['mod'][i]
mean=summ/df_age['mod'].sum()

column= df_all['How do you identify as?']
x=df_all.groupby([column]).count()['mod']
df_gender = pd.DataFrame([x]).T
df_gender.reset_index(inplace=True)

# df_all=df_all.rename(columns={"How much do you personally trust the following institutions from 1 to 7, where 1 means ‘No trust at all’ and 7 means ‘Trust compltely’? Parlament: ": "Parlament","County council:":"County\ncouncil","Municipal council": "Municipal\ncouncil","Government:": "Government", "National politicians:":"National\npoliticians", "Political parties: ":"Political\nparties"})
# d=pd.DataFrame( index=[0,1])
# for i in [222,224,226,228,230,232]:
#     column= df_all.columns[i]
#     a=df_all.groupby([column]).count()['mod']
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

# plt.figure(figsize=(12,9))
# plt.bar(np.linspace(0,6,6), d.loc[0][:], yerr=d.loc[1][:], width=0.7, edgecolor='k',color='azure')
# plt.xticks(np.linspace(0,6,6),d.columns, fontsize=12)
# plt.ylim([0,7])
# plt.savefig(r'C:\Users\Sara\Dropbox (Politecnico Di Torino Studenti)\Aplanet_\rate_gov.png')
    
v_mean=[]
v_std=[]
d=pd.DataFrame( index=[0,1])
for i in [222,224,226,228,230,232]:
    column= df_all.columns[i]
    integers = [x for x in df_all[column] if isinstance(x, int)]
    v_mean.append(np.mean(integers))
    v_std.append(np.std(integers))

plt.figure(figsize=(10,7))
plt.bar(np.linspace(0,6,6), v_mean, yerr=v_std, width=0.7, edgecolor='k',color='azure')
plt.xticks(np.linspace(0,6,6),['Parlament','County\ncouncil','Municipal\ncouncil','Government','National\npoliticians','Political\nparties'], fontsize=12)
plt.ylim([0,7])
plt.savefig(r'C:\Users\Sara\Dropbox (Politecnico Di Torino Studenti)\Aplanet_\rate_gov.png')



df_all=df_all.rename(columns={"How much do you agree with the following statements from 1 to 7, where 1 means ‘I completely disagree’ and 7 means ‘I completely agree’? Air pollution derived by cars is one of the major causes of premature death in Europe:": r"$\bf{Air }$ "+r"$\bf{pollution}$ "+"derived by cars\nis one of the major causes\nof premature death in Europe","The introduction of policies such as road pricing will alleviate congestion problems:":"The introduction of policies\nsuch as "+r"$\bf{road }$ "+r"$\bf{pricing}$ "+"will\nalleviate congestion problems","Revenues collected through taxes are used to create a well-functioning welfare state and society:": r"$\bf{Revenues}$ "+"collected through taxes\nare used to create a well-functioning\nwelfare state and society","Tax revenues should be used to help those who are more in need:": r"$\bf{Tax}$ "+"revenues should\nbe used to help those\nwho are more in need"})
d=pd.DataFrame( index=[0,1])
for i in [236,238,240,242]:
    column= df_all.columns[i]
    a=df_all.groupby([column]).count()['mod']
    per=0
    s=0
    dev=0
    for j in range(1,8):
        per=per+j*a[j]
        s=s+a[j]
    d.at[0,column] = per/s
    for j in range(1,8):  
        dev=dev+(a[j]*(j-d.at[0,column])**2)
    d.at[1,column] = np.sqrt(dev/s)

plt.figure(figsize=(12,9))
plt.bar(np.linspace(0,12,4), d.loc[0][:], yerr=d.loc[1][:], width=1.2, edgecolor='k',color='azure')
plt.xticks(np.linspace(0,12,4),d.columns, fontsize=10)
plt.ylim([0,7])
plt.savefig(r'C:\Users\Sara\Dropbox (Politecnico Di Torino Studenti)\Aplanet_\air_poll.png')
