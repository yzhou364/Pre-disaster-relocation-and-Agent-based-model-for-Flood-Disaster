import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd


df = pd.read_csv("govDis.csv")

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"]*100,df["Total movements"],color = 'orchid')
ax.scatter(df["Experiment parameter"]*100,df["Free riders"], color = "r")
ax.yaxis.set_ticks(np.arange(0,1000,100))
ax.legend(["Total movements","Free riders"], bbox_to_anchor=(0.7, 0.2))
ax.set_xlabel("Government discount rate (%)  \n \n $750,000 additional moving cost")
ax.set_ylabel("Number relocating")
ax.xaxis.set_ticks(np.arange(0,9.0,1))


#ax.set_title("Number of moving residents sensitivity of 750K base case")

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"]*100,df["Optimal subisdy"]/1000,color = "green")
ax.set_xlabel("House price cutoff (%)")
ax.set_ylabel("Optimal subsidy in thousand dollar")
fmt = '${x:,.0f}'
ax.yaxis.set_ticks(np.arange(0,800,50))
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick) 
ax.legend(["Optimal subsidy"], bbox_to_anchor=(1.0, 0.2))
ax.set_xlabel("Government discount rate (%)  \n \n $750,000 additional moving cost")
ax.xaxis.set_ticks(np.arange(0,9.0,1))


fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"]*100,df["Objective"]/1000000,color = "orange")
ax.set_xlabel("House price cutoff (%)")
ax.set_ylabel("ObjectiveV Value in million")
fmt = '${x:,.0f}'
ax.yaxis.set_ticks(np.arange(0,950,50))
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick) 
ax.legend(["Objective value"], bbox_to_anchor=(1.0, 0.2))
ax.set_xlabel("Government discount rate (%)  \n \n $750,000 additional moving cost")
ax.xaxis.set_ticks(np.arange(0,9.0,1))