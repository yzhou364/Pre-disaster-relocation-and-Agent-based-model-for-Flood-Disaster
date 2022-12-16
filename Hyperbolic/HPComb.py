
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
import matplotlib

fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
df1 = pd.read_csv("300KHT.csv")
df2 = pd.read_csv("750KHT.csv")
matplotlib.rcParams['legend.fontsize'] = 15
fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df1["Param"],df2["Optimal Subsidy"],color = 'green',marker="o")
ax.scatter(df1["Param"],df1["Optimal Subsidy"],color = 'green',marker="^")
string = "Hyperbolic parameter  "+chr(913).lower() 
ax.set_xlabel(string)
ax.xaxis.set_ticks(np.arange(0,8.5,0.5))

ax.legend(["$750,000 relocation cost","$300,000 relocation cost"])
ax.set_ylabel("Optimal subsidy")
ax.yaxis.set_major_formatter(tick) 
ax.yaxis.set_ticks(np.arange(0,1000000,100000))
 


fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df2["Param"],df2["Objective"]/1000000,color = 'orange',marker="o")
ax.scatter(df1["Param"],df1["Objective"]/1000000,color = 'orange',marker="^")

string = "Hyperbolic parameter  "+chr(913).lower()
ax.set_xlabel(string)
ax.legend(["$750,000 relocation cost","$300,000 relocation cost"])
ax.set_ylabel("Objective value in millions ($)")
ax.xaxis.set_ticks(np.arange(0,8.5,0.5))

ax.yaxis.set_ticks(np.arange(0,1500,100))

