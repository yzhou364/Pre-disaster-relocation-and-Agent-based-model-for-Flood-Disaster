import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd


df_750 = pd.read_csv("750midDis.csv")
df_300 = pd.read_csv("300midDis.csv")

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df_750["Experiment parameter"]*100,df_750["Total movements"],color = 'orchid',marker="x")
ax.scatter(df_750["Experiment parameter"]*100,df_750["Free riders"], color = "r",marker="x")
ax.scatter(df_300["Experiment parameter"]*100,df_300["Total movements"],color = 'orchid',marker="+")
ax.scatter(df_300["Experiment parameter"]*100,df_300["Free riders"], color = "r",marker="+")
ax.yaxis.set_ticks(np.arange(0,1000,100))
ax.legend(["Total movements","Free riders"], bbox_to_anchor=(1.0, 0.2))
ax.legend(["$750000 relocation cost","$300000 relocation cost"], bbox_to_anchor=(1.0, 0.2))

ax.set_xlabel("Upper-income homeowner discount rate (%)")

ax.set_ylabel("Number relocating")
#ax.set_title("Number of moving residents sensitivity of 750K base case")
"""
fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"]*100,df["Optimal subisdy"],color = "green")
ax.set_xlabel("Lower-income homeowner discount rate (%)\n \n $750,000 additional moving cost")
ax.set_ylabel("Optimal subsidy ($)")
fmt = '${x:,.0f}'
ax.yaxis.set_ticks(np.arange(0,800000,50000))
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick) 
ax.legend(["Optimal subsidy"], bbox_to_anchor=(1.0, 0.2))

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"]*100,df["Objective"],color = "orange")
ax.set_xlabel("Lower-income homeowner discount rate (%)\n \n $750,000 additional moving cost")
ax.set_ylabel("ObjectiveV Value ($)")
fmt = '${x:,.0f}'
ax.yaxis.set_ticks(np.arange(0,950000000,50000000))
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick) 
ax.legend(["Objective value"], bbox_to_anchor=(1.0, 0.2))
"""