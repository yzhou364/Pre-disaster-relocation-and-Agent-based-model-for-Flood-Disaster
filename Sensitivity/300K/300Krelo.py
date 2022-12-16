import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
df = pd.read_csv("relo.csv")

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"]/1000,df["Total movements"],color = 'blue')
ax.scatter(df["Experiment parameter"]/1000,df["Free riders"], color = "r")
ax.yaxis.set_ticks(np.arange(0,1300,100))
ax.legend(["Total relocations","Free riders"], bbox_to_anchor=(1.0, 0.2))
ax.set_xlabel("Relocation cost in thousands ($)")
ax.xaxis.set_ticks(np.arange(0,900,100))
ax.set_ylabel("Number relocating")
#ax.set_title("Number of moving residents sensitivity of 750K base case")

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"]/1000,df["Optimal subisdy"],color = "green")
ax.set_xlabel("Relocation cost in thousands ($)")
ax.set_ylabel("Optimal subsidy")

ax.yaxis.set_ticks(np.arange(0,800000,50000))
ax.xaxis.set_ticks(np.arange(0,900,100)) 
ax.yaxis.set_major_formatter(tick) 


fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"]/1000,df["Objective"]/1000000,color = "orange")
ax.set_xlabel("Relocation cost in thousands ($)")
ax.set_ylabel("Objective Value in millions ($)")
fmt = '${x:,.0f}'
ax.yaxis.set_ticks(np.arange(0,950,50))
ax.xaxis.set_ticks(np.arange(0,900,100))
tick = mtick.StrMethodFormatter(fmt)

