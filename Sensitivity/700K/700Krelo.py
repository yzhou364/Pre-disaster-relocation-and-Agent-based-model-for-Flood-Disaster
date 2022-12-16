import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
df = pd.read_csv("relo.csv")

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"]/100000,df["Total movements"],color = 'orchid')
ax.scatter(df["Experiment parameter"]/100000,df["Free riders"], color = "r")
ax.yaxis.set_ticks(np.arange(0,1000,100))
ax.legend(["Total movements","Free riders"], bbox_to_anchor=(1.0, 0.2))
ax.set_xlabel("Relocaiton cost in million ($)")
ax.xaxis.set_ticks(np.arange(3,9,1))

ax.xaxis.set_major_formatter(tick) 
ax.set_ylabel("Number relocating")
#ax.set_title("Number of moving residents sensitivity of 750K base case")

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"]/100000,df["Optimal subisdy"],color = "green")
ax.set_xlabel("Relocaiton cost in million ($)")
ax.set_ylabel("Optimal subsidy ($)")

ax.yaxis.set_ticks(np.arange(0,800000,50000))
ax.xaxis.set_ticks(np.arange(3,9,1))
ax.xaxis.set_major_formatter(tick) 
ax.yaxis.set_major_formatter(tick) 
ax.legend(["Optimal subsidy"], bbox_to_anchor=(1.0, 0.2))

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"]/100000,df["Objective"],color = "orange")
ax.set_xlabel("Relocaiton cost in million ($)")
ax.set_ylabel("ObjectiveV Value ($)")
fmt = '${x:,.0f}'
ax.yaxis.set_ticks(np.arange(0,950000000,50000000))
ax.xaxis.set_ticks(np.arange(3,9,1))
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick) 
ax.xaxis.set_major_formatter(tick) 
ax.legend(["Objective value"], bbox_to_anchor=(1.0, 0.2))



fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"]/100000,df["Objective"],color = "orange")
ax.set_xlabel("Relocaiton cost in million ($)")
ax.set_ylabel("ObjectiveV Value ($)")
fmt = '${x:,.0f}'
ax.yaxis.set_ticks(np.arange(0,950000000,50000000))
ax.xaxis.set_ticks(np.arange(3,9,1))
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick) 
ax.xaxis.set_major_formatter(tick) 
ax.legend(["Objective value"], bbox_to_anchor=(1.0, 0.2))

from brokenaxes import brokenaxes

fig = plt.figure(figsize=(8,5))
ax = brokenaxes(xlims=((0,2.5), (3, 9)), hspace=.05)
x = np.linspace(0, 1, 100)
ax.scatter(df["Experiment parameter"]/100000,df["Objective"],color = "orange")
ax.set_xlabel("Relocaiton cost in million ($)")
ax.set_ylabel("ObjectiveV Value ($)")
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick) 
ax.xaxis.set_major_formatter(tick) 
ax.legend(["Objective value"], bbox_to_anchor=(1.0, 0.2))
