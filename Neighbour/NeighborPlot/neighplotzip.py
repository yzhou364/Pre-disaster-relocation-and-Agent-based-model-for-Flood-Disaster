import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import matplotlib.ticker as mtick

fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
#ax.yaxis.set_major_formatter(tick) 

disdf = pd.read_csv("neiSummary.csv")
simidf = pd.read_csv("neiZipSimiSummary.csv")
zipdf = pd.read_csv("neiZipSummary.csv")




vacSensi = zipdf
vacSensi = vacSensi[vacSensi["Dp"]==0.15]
vacSensi300 = vacSensi[vacSensi["Relo"]==300000]
vacSensi750 = vacSensi[vacSensi["Relo"]==750000]


fig = plt.figure()
ax = plt.subplot(111)
#ax.scatter(vacSensi300["Vac"]*100,vacSensi300["Total"],color = 'orchid')
ax.scatter(vacSensi300["Vac"]*100,vacSensi300["Free"]*100/vacSensi300["Total"],color='red')
ax.scatter(vacSensi300["Vac"]*100,vacSensi300["Nei"]*100/vacSensi300["Total"],color = 'peru')

ax.yaxis.set_ticks(np.arange(0,100,10))
ax.xaxis.set_ticks(np.arange(0,50,5))
plt.xticks(rotation=45)
ax.set_xlabel("Vaccancy percent threshold (%) \n \n $300,000 relocation cost")
ax.set_ylabel("Percentage of total relocation (%)")

fig = plt.figure()
ax = plt.subplot(111)
#ax.scatter(vacSensi750["Vac"]*100,vacSensi750["Total"],color = 'orchid')
ax.scatter(vacSensi750["Vac"]*100,vacSensi750["Free"]*100/vacSensi750["Total"],color='red')
ax.scatter(vacSensi750["Vac"]*100,vacSensi750["Nei"]*100/vacSensi750["Total"],color = 'peru')
ax.legend(["Free riders","Network relocations"], bbox_to_anchor=(1, 0.9))

ax.yaxis.set_ticks(np.arange(0,100,10))
ax.xaxis.set_ticks(np.arange(0,50,5))
plt.xticks(rotation=45)
ax.set_xlabel("Vaccancy percent threshold (%) \n \n $750,000 relocation cost")
ax.set_ylabel("Percentage of total relocation (%)")
