import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd


df = pd.read_csv("houseprice.csv")

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"],df["Total movements"]/1143)
ax.scatter(df["Experiment parameter"],df["Free riders"]/1143)

ax.yaxis.set_ticks(np.arange(-100,1000,100))
ax.legend(["Total movements","Free riders"], bbox_to_anchor=(1.0, 0.2))
ax.set_ylim(0,1)
ax.set_xlabel("House price cutoff percentile")
ax.set_ylabel("Number relocating")
ax.set_xlim(0,90)
#ax.set_title("Number of moving residents sensitivity of 750K base case")

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"],df["Optimal subisdy"],color = "green")
ax.set_xlabel("House price cutoff (%)")
ax.set_ylabel("Optimal subsidy ($)")
fmt = '${x:,.0f}'
ax.yaxis.set_ticks(np.arange(0,800000,50000))
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick) 
ax.legend(["Optimal subsidy"], bbox_to_anchor=(1.0, 0.2))
ax.set_title("Optimal subsidy sensitivity of 750K base case")

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"],df["Objective"],color = "green")
ax.set_xlabel("House price cutoff (%)")
ax.set_ylabel("ObjectiveV Value ($)")
fmt = '${x:,.0f}'
ax.yaxis.set_ticks(np.arange(0,950000000,50000000))
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick) 
ax.legend(["Objective value"], bbox_to_anchor=(1.0, 0.2))
ax.set_title("Objective value sensitivity of 750K base case")
"""
fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"],df["Optimal subisdy"])
ax.set_xlabel("House price cutoff (%)")
ax.set_ylabel("Optimal subsidy ($)")
fmt = '${x:,.0f}'
ax.yaxis.set_ticks(np.arange(0,800000,50000))
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick) 
ax.set_title("Optimal subsidy sensitivity")

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"],df["Objective"])
ax.set_xlabel("House price cutoff (%)")
ax.set_ylabel("ObjectiveV Value ($)")
fmt = '${x:,.0f}'
ax.yaxis.set_ticks(np.arange(0,950000000,50000000))
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick) 
ax.set_title("Objective value sensitivity")

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"],df["Total movements"])
ax.yaxis.set_ticks(np.arange(0,1000,100))
ax.set_xlabel("House price cutoff (%)")
ax.set_ylabel("Number of total movement")
ax.set_title("Number of total movement sensitivity")


df = pd.read_csv("lowDis.csv")
fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"]*100,df["Free riders"])
ax.yaxis.set_ticks(np.arange(0,1000,100))
ax.set_xlabel("Lower class discount rate (%)")
ax.set_ylabel("Number of free riders")
ax.set_title("Number of free riders sensitivity")

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"]*100,df["Optimal subisdy"])
ax.set_xlabel("Lower class discount rate (%)")
ax.set_ylabel("Optimal subsidy ($)")
fmt = '${x:,.0f}'
ax.yaxis.set_ticks(np.arange(0,800000,50000))
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick) 
ax.set_title("Optimal subsidy sensitivity")


fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"]*100,df["Objective"])
ax.set_xlabel("Lower class discount rate (%)")
ax.set_ylabel("ObjectiveV Value ($)")
fmt = '${x:,.0f}'
ax.yaxis.set_ticks(np.arange(0,950000000,50000000))
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick) 
ax.set_title("Objective value sensitivity")

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"]*100,df["Total movements"])
ax.yaxis.set_ticks(np.arange(0,1000,100))
ax.set_xlabel("Lower class discount rate (%)")
ax.set_ylabel("Number of total movement")
ax.set_title("Number of total movement sensitivity")

df = pd.read_csv("midDis.csv")
fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"]*100,df["Free riders"])
ax.yaxis.set_ticks(np.arange(0,1000,100))
ax.set_xlabel("Upper class discount rate (%)")
ax.set_ylabel("Number of free riders")
ax.set_title("Number of free riders sensitivity")

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"]*100,df["Optimal subisdy"])
ax.set_xlabel("Upper class discount rate (%)")
ax.set_ylabel("Optimal subsidy ($)")
fmt = '${x:,.0f}'
ax.yaxis.set_ticks(np.arange(0,800000,50000))
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick) 
ax.set_title("Optimal subsidy sensitivity")


fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"]*100,df["Objective"])
ax.set_xlabel("Upper class discount rate (%)")
ax.set_ylabel("ObjectiveV Value ($)")
fmt = '${x:,.0f}'
ax.yaxis.set_ticks(np.arange(0,950000000,50000000))
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick) 
ax.set_title("Objective value sensitivity")

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"]*100,df["Total movements"])
ax.yaxis.set_ticks(np.arange(0,1000,100))
ax.set_xlabel("Upper class discount rate (%)")
ax.set_ylabel("Number of total movement")
ax.set_title("Number of total movement sensitivity")


df = pd.read_csv("govDis.csv")
fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"]*100,df["Free riders"])
ax.yaxis.set_ticks(np.arange(0,1000,100))
ax.set_xlabel("Government discount rate (%)")
ax.set_ylabel("Number of free riders")
ax.set_title("Number of free riders sensitivity")

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"]*100,df["Optimal subisdy"])
ax.set_xlabel("Government discount rate (%)")
ax.set_ylabel("Optimal subsidy ($)")
fmt = '${x:,.0f}'
ax.yaxis.set_ticks(np.arange(0,800000,50000))
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick) 
ax.set_title("Optimal subsidy sensitivity")


fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"]*100,df["Objective"])
ax.set_xlabel("Government discount rate (%)")
ax.set_ylabel("ObjectiveV Value ($)")
fmt = '${x:,.0f}'
ax.yaxis.set_ticks(np.arange(0,950000000,50000000))
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick) 
ax.set_title("Objective value sensitivity")

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"]*100,df["Total movements"])
ax.yaxis.set_ticks(np.arange(0,1000,100))
ax.set_xlabel("Government discount rate (%)")
ax.set_ylabel("Number of total movement")
ax.set_title("Number of total movement sensitivity")

df = pd.read_csv("relo.csv")
fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"],df["Free riders"])
ax.yaxis.set_ticks(np.arange(0,1000,100))
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.set_xlabel("Relocation cost ($)")
ax.set_ylabel("Number of free riders")
ax.xaxis.set_major_formatter(tick) 
ax.set_title("Number of free riders sensitivity")

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"],df["Optimal subisdy"])
ax.set_xlabel("Relocation cost ($)")
ax.set_ylabel("Optimal subsidy ($)")
fmt = '${x:,.0f}'
ax.yaxis.set_ticks(np.arange(0,800000,50000))
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick) 
ax.set_title("Optimal subsidy sensitivity")


fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"],df["Objective"])
ax.set_xlabel("Relocation cost ($)")
ax.set_ylabel("ObjectiveV Value ($)")
fmt = '${x:,.0f}'
ax.yaxis.set_ticks(np.arange(0,950000000,50000000))
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick) 
ax.xaxis.set_major_formatter(tick) 
ax.set_title("Objective value sensitivity")

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df["Experiment parameter"],df["Total movements"])
ax.yaxis.set_ticks(np.arange(0,1000,100))
ax.set_xlabel("Relocation cost ($)")
ax.set_ylabel("Number of total movement")
ax.xaxis.set_major_formatter(tick) 
ax.set_title("Number of total movement sensitivity")"""