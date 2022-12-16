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


disBase = disdf[disdf["Vac"]==0.25]
disBase = disBase[disBase["Dp"]==0.15]
disBase300 = disBase[disBase["Relo"]==300000]
disBase750 = disBase[disBase["Relo"]==750000]

fig = plt.figure()
ax = plt.subplot(111)
plt.hlines(610000,0,1600,linestyles ="solid",color="green")
plt.scatter(disBase750["Dis"],disBase750["Sub"],color='green',marker="o")
plt.hlines(200000, 0, 1600,linestyles = "dashdot",color="green")
plt.scatter(disBase300["Dis"],disBase300["Sub"],color='green',marker="^" )

ax.legend(["$750,000 relocation cost \n without network effect","$750,000 relocation cost","$300,000 relocation cost \n without network effect","$300,000 relocation cost"],
          bbox_to_anchor=(1, 0.5))
ax.yaxis.set_ticks(np.arange(0,850000,50000))
ax.xaxis.set_ticks(np.arange(0,1600,100))
plt.xticks(rotation=45)
ax.yaxis.set_major_formatter(tick)
ax.set_xlabel("Neighborhood radius (m)")
ax.set_ylabel("Optimal subsidy")

fig = plt.figure()
ax = plt.subplot(111)
plt.hlines(785,0,1600,linestyles ="solid",color="orange")
plt.scatter(disBase750["Dis"],disBase750["Obj"]/1000000,color='orange',marker="o")
plt.hlines(431, 0, 1600,linestyles = "dashdot",color="orange")
plt.scatter(disBase300["Dis"],disBase300["Obj"]/1000000,color='orange',marker="^" )
#plt.hlines(785,0,1600,linestyles ="solid",color="orange")
#plt.hlines(431, 0, 1600,linestyles = "dashdot",color="orange")
ax.legend(["$750,000 relocation cost \n without network effect","$750,000 relocation cost","$300,000 relocation cost \n without network effect","$300,000 relocation cost"],
          bbox_to_anchor=(1, 0.5))
ax.yaxis.set_ticks(np.arange(0,950,50))
ax.xaxis.set_ticks(np.arange(0,1600,100))
plt.xticks(rotation=45)
ax.set_xlabel("Neighborhood radius (m)")
ax.set_ylabel("Objective value in millions ($)")


fig = plt.figure()
ax = plt.subplot(111)
plt.scatter(disBase750["Dis"],disBase750["Total"],color = 'orchid')
plt.hlines(843,0,1800,linestyles="solid",color ="orchid")
plt.scatter(disBase750["Dis"],disBase750["Free"],color='red')
plt.hlines(374,0,1800,linestyles="dashdot",color ="red")
plt.scatter(disBase750["Dis"],disBase750["Nei"],color = 'peru')

ax.legend(["Total relocations","Total relocations without network effect","Free riders","Free riders without network effect","Network relocations"], bbox_to_anchor=(1.75, 0.5))

ax.yaxis.set_ticks(np.arange(0,1300,100))
ax.xaxis.set_ticks(np.arange(0,1800,100))
plt.xticks(rotation=45)
ax.set_xlabel("Neighborhood distance radius (m) \n \n $750,000 relocation cost")
ax.set_ylabel("Number relocating")


fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(disBase300["Dis"],disBase300["Total"],color = 'orchid')
plt.hlines(848,0,1800,linestyles="solid",color ="orchid")
ax.scatter(disBase300["Dis"],disBase300["Free"],color='red')
plt.hlines(495,0,1800,linestyles="dashdot",color ="red")
ax.scatter(disBase300["Dis"],disBase300["Nei"],color = 'peru')
ax.yaxis.set_ticks(np.arange(0,1300,100))
ax.xaxis.set_ticks(np.arange(0,1800,100))
plt.xticks(rotation=45)
ax.set_xlabel("Neighborhood distance threshold (m) \n \n $300,000 relocation cost")
ax.set_ylabel("Number relocating")

dpSensi = disdf[disdf["Dis"]==800]
dpSensi = dpSensi[dpSensi["Vac"]==0.25]
dpSensi300 = dpSensi[dpSensi["Relo"]==300000]
dpSensi750 = dpSensi[dpSensi["Relo"]==750000]


fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(dpSensi300["Dp"],dpSensi300["Total"],color = 'orchid')
ax.scatter(dpSensi300["Dp"],dpSensi300["Free"],color='red')
ax.scatter(dpSensi300["Dp"],dpSensi300["Nei"],color = 'peru')

ax.yaxis.set_ticks(np.arange(0,1300,100))
ax.xaxis.set_ticks(np.arange(0,0.4,0.05))
plt.xticks(rotation=45)
ax.set_xlabel("Relocation decison probability \n \n $300,000 relocation cost")
ax.set_ylabel("Number relocating")

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(dpSensi750["Dp"],dpSensi750["Total"],color = 'orchid')
ax.scatter(dpSensi750["Dp"],dpSensi750["Free"],color='red')
ax.scatter(dpSensi750["Dp"],dpSensi750["Nei"],color = 'peru')
ax.legend(["Total relocations","Free riders","Network relocations"], bbox_to_anchor=(1, 0.9))

ax.yaxis.set_ticks(np.arange(0,1300,100))
ax.xaxis.set_ticks(np.arange(0,0.4,0.05))
plt.xticks(rotation=45)
ax.set_xlabel("Relocation decison probability \n \n $750,000 relocation cost")
ax.set_ylabel("Number relocating")


vacSensi = disdf[disdf["Dis"]==800]
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
ax.set_xlabel("Vaccancy threshold (%) \n \n $300,000 relocation cost")
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
ax.set_xlabel("Vaccancy threshold (%) \n \n $750,000 relocation cost")
ax.set_ylabel("Percentage of total relocation (%)")
