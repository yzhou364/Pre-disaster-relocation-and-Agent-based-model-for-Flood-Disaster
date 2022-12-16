import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
df1 = pd.read_csv("300K.csv")
df2 = pd.read_csv("750K.csv")

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df2["Type"],df2["OptimalSub"],color = 'green',marker='^')
ax.scatter(df1["Type"],df1["OptimalSub"],color = 'green',marker='o')
ax.set_ylabel("Optimal subsidy")
ax.set_xlabel("Number of flood types")
ax.legend(["$750,000 relocation cost","$300,000 relocation cost"], bbox_to_anchor=(1.0, 0.2))
ax.yaxis.set_ticks(np.arange(0,750000,50000))
ax.yaxis.set_major_formatter(tick)
