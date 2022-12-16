# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 10:34:53 2022

@author: yzhou364
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd



df = pd.read_csv(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\NY_Res\OldResults\4.24\houSummary.csv")

fig = plt.figure()
ax = plt.subplot(111)
#plt.scatter(df["CutOff"]/1000000,df["Total"]/1143*100,c=df["Obj"]/1000000000,marker="s",cmap="binary" )
#plt.scatter(df["CutOff"]/1000000,df["Free"]/1143*100,c=df["Obj"]/1000000000,marker="^",cmap="binary")

plt.scatter(df["CutOff"]/1000000,df["Total"]/1143*100,c=df["Obj"]/1000000000,marker="s",cmap="autumn_r" )
plt.scatter(df["CutOff"]/1000000,df["Free"]/1143*100,c=df["Obj"]/1000000000,marker="^",cmap="autumn_r")
ax.legend(["Total","Free riders"],loc='center left', bbox_to_anchor=(0.6, 0.9))
ax.axvline(x=.7,c="purple")

#ax.text(0.8, 40, 'Optimal cutoff line', style ='italic',fontsize = 10, color ="black")

ax.set_xlabel("House price cutoff ($ million)")
ax.set_ylabel("Percent relocating (%)")
ax.set_ylim([0,100])

plt.colorbar(label="Objective value ($ billion)", orientation="vertical",cax = fig.add_axes([0.95, 0.5, 0.03, 0.38]))
plt.show()

fig = plt.figure()
ax = plt.subplot(111)
plt.scatter(df["CutOff"]/1000000,df["Total"]/1143*100,c=df["Subsidy"]/1000000,marker="s",cmap="viridis")
plt.scatter(df["CutOff"]/1000000,df["Free"]/1143*100,c=df["Subsidy"]/1000000,marker="^",cmap="viridis")
ax.legend(["Total","Free riders"],loc='center left', bbox_to_anchor=(0.6, 0.9))
ax.axvline(x=.6,c="purple")
ax.set_xlabel("House price cutoff ($ million)")
ax.set_ylabel("Percent relocating (%)")
ax.set_ylim([0,100])

plt.colorbar(label="Optimal subsidy ($ million)", orientation="vertical",cax = fig.add_axes([0.95, 0.5, 0.03, 0.38]))
plt.show()

df = pd.read_csv(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\NY_Res\OldResults\4.25\eleSummary.csv")

fig = plt.figure()
ax = plt.subplot(111)
#plt.scatter(df["CutOff"],df["Total"]/1143*100,c=df["Obj"]/1000000000,marker="s",cmap="binary" )
#plt.scatter(df["CutOff"],df["Free"]/1143*100,c=df["Obj"]/1000000000,marker="^",cmap="binary")

plt.scatter(df["CutOff"],df["Total"]/1143*100,c=df["Obj"]/1000000000,marker="s",cmap="autumn_r" )
plt.scatter(df["CutOff"],df["Free"]/1143*100,c=df["Obj"]/1000000000,marker="^",cmap="autumn_r")
ax.legend(["Total","Free riders"],loc='center left', bbox_to_anchor=(0.6, 0.9))

ax.axvline(x=1.9,c="purple")
ax.set_xlabel("Elevation cutoff (m)")
ax.set_ylabel("Percent relocating (%)")
ax.set_ylim([0,100])
ax.set_xlim([0,5])

#ax.legend(["Total","Free rider"],loc='center left', bbox_to_anchor=(0.6, 0.9))
plt.colorbar(label="Objective value ($ billion)", orientation="vertical",cax = fig.add_axes([0.95, 0.5, 0.03, 0.38]))
plt.show()

fig = plt.figure()
ax = plt.subplot(111)
plt.scatter(df["CutOff"],df["Total"]/1143*100,c=df["Subsidy"]/1000000,marker="s",cmap="viridis"    )
plt.scatter(df["CutOff"],df["Free"]/1143*100,c=df["Subsidy"]/1000000,marker="^",cmap="viridis")
ax.legend(["Total","Free riders"],loc='center left', bbox_to_anchor=(0.6, 0.9))
ax.axvline(x=1.9,c="purple")
ax.set_xlabel("Elevation price cutoff (m)")
ax.set_ylabel("Percent relocating (%)")
ax.set_ylim([0,100])
ax.set_xlim([0,5])
#ax.legend(["Total","Free rider"],loc='center left', bbox_to_anchor=(0.6, 0.9))
plt.colorbar(label="Optimal subsidy ($ million)", orientation="vertical",cax = fig.add_axes([0.95, 0.5, 0.03, 0.38]))
plt.show()