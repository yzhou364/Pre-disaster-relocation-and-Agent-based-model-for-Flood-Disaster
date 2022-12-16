import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

df = pd.read_csv("ny_fill.csv")
df = pd.read_csv("tx_fill.csv")
fig = plt.figure()
ax = plt.subplot(111)


ax.scatter(df["altitude (m)"],df["totalmarketvalue"],color = "blue")
ax.set_xlabel("Elevation (m)")
ax.set_ylabel("House market value")
fmt = '${x:,.0f}'
ax.xaxis.set_ticks(np.arange(0,10,1))
ax.yaxis.set_ticks(np.arange(0,3500000,500000))
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick) 
