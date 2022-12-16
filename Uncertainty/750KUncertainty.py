import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
import matplotlib
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
df = pd.read_csv("750K.csv")
matplotlib.rcParams['legend.fontsize'] = 11
fig = plt.figure()
ax = plt.subplot(111)
ax.bar(df["Experiment"][:3],df["Optimal subisdy"][:3],color = 'green')
ax.axhline(df["Optimal subisdy"][5],linewidth=2,ls="-.", color='firebrick',label="(1/10, 8/10, 1/10)")
ax.axhline(df["Optimal subisdy"][4],linewidth=2,ls="-.", color='red', label="(1/5, 3/5, 1/5)")
ax.axhline(df["Optimal subisdy"][3],linewidth=2,ls="-.", color='lightcoral',label="(1/3,1/3,1/3)")
ax.yaxis.set_ticks(np.arange(0,950000,100000))
ax.legend()
ax.set_xticklabels(df["Experiment"], rotation=70)
ax.yaxis.set_major_formatter(tick) 
ax.set_ylabel("Optimal subsidy")
ax.set_xlabel("Scenarios \n \n $750,000 relocation cost")

fig = plt.figure()
ax = plt.subplot(111)
ax.bar(df["Experiment"][:3],df["Objective"][:3]/1000000,color = 'orange')
ax.axhline(df["Objective"][5]/1000000,linewidth=2,ls="-.", color='firebrick',label="(1/10, 8/10, 1/10)")
ax.axhline(df["Objective"][4]/1000000,linewidth=2,ls="-.", color='red', label="(1/5, 3/5, 1/5)")
ax.axhline(df["Objective"][3]/1000000,linewidth=2,ls="-.", color='lightcoral',label="(1/3,1/3,1/3)")
ax.yaxis.set_ticks(np.arange(0,1000,100))
ax.legend(bbox_to_anchor=(1.0, 0.3))
ax.set_xticklabels(df["Experiment"], rotation=70) 
ax.set_ylabel("Objective value in millions")
ax.set_xlabel("Scenarios \n \n $750,000 relocation cost")


fig = plt.figure()
ax = plt.subplot(111)
ax.bar(df["Experiment"][:3],df["Free riders"][:3],color = 'red')

ax.axhline(df["Free riders"][3],linewidth=2,ls="-.", color='lightcoral',label="(1/3,1/3,1/3)")
ax.axhline(df["Free riders"][4],linewidth=2,ls="-.", color='red', label="(1/5, 3/5, 1/5)")
ax.axhline(df["Free riders"][5],linewidth=2,ls="-.", color='firebrick',label="(1/10, 8/10, 1/10)")
ax.yaxis.set_ticks(np.arange(0,1000,100))
ax.legend()
ax.set_xticklabels(df["Experiment"], rotation=70)
ax.set_ylabel("Number of free riders")
ax.set_xlabel("Scenarios \n \n $750,000 relocation cost")