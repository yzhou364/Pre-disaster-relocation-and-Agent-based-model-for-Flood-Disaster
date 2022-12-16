import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
df = pd.read_csv("750KHT.csv")

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Param"],df["Optimal Subsidy"],color = 'green')
string = "Hyperbolic paramater  "+chr(913).lower() + "\n\n $750,000 relocation cost"
ax.set_xlabel(string)
ax.set_ylabel("Optimal subsidy")
ax.yaxis.set_major_formatter(tick) 
ax.yaxis.set_ticks(np.arange(0,1000000,50000))
 
ax.xaxis.set_ticks(np.arange(0,8.5,0.5))

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Param"],df["Objective"]/1000000,color = 'orange')
string = "Hyperbolic paramater  "+chr(913).lower() + "\n\n $750,000 relocation cost"
ax.set_xlabel(string)
ax.set_ylabel("Objective value in millions")

ax.yaxis.set_ticks(np.arange(0,1000,100))

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Param"],df["TotalMovement"],color = 'blue')
ax.scatter(df["Param"],df["Free rider"],color = 'red')
ax.scatter(df["Param"],df["TotalMovement"],color = 'blue')
string = "Hyperbolic paramater  "+chr(913).lower() + "\n\n $750,000 relocation cost"
ax.set_xlabel(string)
ax.set_ylabel("Number relocating")

ax.xaxis.set_ticks(np.arange(0,8.5,0.5))
ax.yaxis.set_ticks(np.arange(0,1000,100))
ax.legend(["Total relocations","Free riders"], bbox_to_anchor=(0.95, 0.5))