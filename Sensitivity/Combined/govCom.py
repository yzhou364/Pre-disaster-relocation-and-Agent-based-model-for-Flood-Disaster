import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd


df750 = pd.read_csv("750govDis.csv")
df300 = pd.read_csv("300govDis.csv")



#ax.set_title("Number of moving residents sensitivity of 750K base case")

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df750["Experiment parameter"]*100,df750["Optimal subisdy"],color = "green",marker="o")
ax.scatter(df300["Experiment parameter"]*100,df300["Optimal subisdy"],color = "green",marker="^")
ax.set_xlabel("House price cutoff (%)")
ax.set_ylabel("Optimal subsidy")
fmt = '${x:,.0f}'
ax.yaxis.set_ticks(np.arange(0,800000,50000))
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick) 
ax.legend(["$750,000 relocation cost","$300,000 relocation cost"])
ax.set_xlabel("Government discount rate (%)")
ax.xaxis.set_ticks(np.arange(0,9.0,1))


fig = plt.figure()
ax = plt.subplot(111)

ax.scatter(df750["Experiment parameter"]*100,df750["Objective"]/1000000,color = "orange",marker="o")
ax.scatter(df300["Experiment parameter"]*100,df300["Objective"]/1000000,color = "orange",marker="^")

ax.set_xlabel("House price cutoff (%)")
ax.set_ylabel("Objective value in millions ($)")
fmt = '${x:,.0f}'
ax.yaxis.set_ticks(np.arange(0,950,50))
tick = mtick.StrMethodFormatter(fmt)
ax.legend(["$750,000 relocation cost","$300,000 relocation cost"])
ax.set_xlabel("Government discount rate (%)")
ax.xaxis.set_ticks(np.arange(0,9.0,1))