import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

df = pd.read_csv("750Kdata.csv",index_col=False)

### F1
fig = plt.figure()
ax = plt.subplot(111)
rateLabel = ["Low income","Middle income"]
ax.scatter(100*(df.loc[df["freeRiderFlag"] == False]["disRate"]+0.005),df.loc[df["freeRiderFlag"] == False]["alt"],
           color = 'orchid',alpha = 0.5)
ax.scatter(100*(df.loc[df["freeRiderFlag"] == True]["disRate"]),df.loc[df["freeRiderFlag"] == True]["alt"],
           color = "r",alpha = 1)
ax.xaxis.set_ticks([0,12,18,30])

ax.yaxis.set_ticks(np.arange(0,10,1))
ax.legend(['Not free rider',"Free rider"],loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel("Residential discount rate (%)\n \n $750,000 relocation cost")
ax.set_ylabel("Elevation (m)")
#ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))
#ax.set_title("Free rider information based on elevation (m)")
### F2
fig = plt.figure()
ax = plt.subplot(111)
rateLabel = ["Low income","Middle income"]
ax.scatter(100*(df.loc[df["freeRiderFlag"] == False]["disRate"]+0.005),df.loc[df["freeRiderFlag"] == False]["mktValue"]/1000000,
           color = 'orchid',alpha = 0.5)
ax.scatter(100*(df.loc[df["freeRiderFlag"] == True]["disRate"]),df.loc[df["freeRiderFlag"] == True]["mktValue"]/1000000,
           color = "r",alpha = 1)
ax.xaxis.set_ticks([0,12,18,30])
ax.yaxis.set_ticks(np.arange(0,4,1))
#ax.yaxis.set_ticks(np.arange(0,20000,2500))
#ax.set_ylim([0, 20000])
ax.legend(['Not free rider',"Free rider"],loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel("Residential discount rate (%)\n \n $750,000 relocation cost")
ax.set_ylabel("House market value in millions")
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)

#ax.ticklabel_format(useOffset=False, style='plain')
#ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))
#ax.set_title("Free rider information based on house market value")
###F3
df_time1 = df.groupby(df["selfMoveYear"]).agg("count")
df_time2 = df.groupby(df["motMoveYear"]).agg("count")
fig = plt.figure()
ax = plt.subplot(111)
#ax.set_title("Motivated moving and self moving time histgram comparison",x=0.5, y=1.1)
ax.bar(df_time2.index[:-1]+0.5,df_time2["disRate"][:-1], color = "green",width=0.7)
ax.bar(df_time1.index[:-1],df_time1["disRate"][:-1], color = "blue",width=0.7)
ax.set_xlabel("Year\n \n $750,000 relocation cost")
ax.set_ylabel("Number relocating")
ax.xaxis.set_ticks(np.arange(0,100,5))
ax.set_xlim([0, 80])
ax.legend(['With optimal subsidy',"Without subsidy"],loc='center left', bbox_to_anchor=(1, 0.9))

def fillup(ylist,xorig,xlist):
    res = []
    for i in range(len(xlist)):
        if i >= len(xorig):
            res.append(ylist[-1])
        else:
            if i in xorig:
                res.append(ylist[i])
            else:
                res.append(ylist[i-1])
    return res
df_time1_cum = df_time1.cumsum()
df_time2_cum = df_time2.cumsum()
fig = plt.figure()
ax = plt.subplot(111)
#ax.set_title("Cumulative motivated moving and self moving time distribution comparison",x=0.5, y=1.1)
xlist = np.linspace(0, 80,81)
xorig = list(df_time2_cum.index[:-1])
ylist = list(100*df_time2_cum["disRate"][:-1]/df.shape[0])
res2 = fillup(ylist, xorig, xlist)
xorig = list(df_time1_cum.index[:-1])
ylist = list(100*df_time1_cum["disRate"][:-1]/df.shape[0])
res1 = fillup(ylist, xorig, xlist)
ax.bar(xlist, res2, color = "green")
ax.bar(xlist, res1, color = "blue")
#ax.axhline(y=374/1143,color='r')
ax.set_xlabel("Year\n \n $750,000 relocation cost")
ax.set_ylabel("Cumulative relocations (%)")
ax.xaxis.set_ticks(np.arange(0,100,5))
ax.set_xlim([0, 80])
ax.set_ylim([0,100])
ax.legend(['With optimal subsidy',"Without subsidy"],loc='center left', bbox_to_anchor=(1, 0.9))
### F4
ax.axhline(y=374/1143*100,color='lightgreen')
df_middle  = df[df["className"]=="M"]
df_low  = df[df["className"]=="L"]
df_middle_mot_cum = df_middle.groupby(df["motMoveYear"]).agg("count").cumsum()
df_low_mot_cum = df_low.groupby(df["motMoveYear"]).agg("count").cumsum()
df_middle_self_cum = df_middle.groupby(df["selfMoveYear"]).agg("count").cumsum()
df_low_self_cum = df_low.groupby(df["selfMoveYear"]).agg("count").cumsum()
fig = plt.figure()
ax = plt.subplot(111)
#ax.set_title("Cumulative motivated moving and self moving time number cumulative comparison by class",x=0.5, y=1.1)

xlist = np.linspace(0, 80,81)
xorig = list(df_middle_mot_cum.index[:-1])
ylist = list(df_middle_mot_cum["disRate"][:-1])
res2 = fillup(ylist, xorig, xlist)
xorig = list(df_middle_self_cum.index[:-1])
ylist = list(df_middle_self_cum["disRate"][:-1])
res1 = fillup(ylist, xorig, xlist)
xorig = list(df_low_mot_cum.index[:-1])
ylist = list(df_low_mot_cum["disRate"][:-1])
res3 = fillup(ylist, xorig, xlist)
xorig = list(df_low_self_cum.index[:-1])
ylist = list(df_low_self_cum["disRate"][:-1])
res4 = fillup(ylist, xorig, xlist)


ax.scatter(xlist,res2, color="green", marker = "o")
ax.scatter(xlist,res1,color="blue", marker = "o")
ax.scatter(xlist,res3,color="lime", marker = "x")
ax.scatter(xlist,res4,color="cornflowerblue", marker = "x")
ax.set_xlabel("Year\n \n $750,000 relocation cost")
ax.set_ylabel("Number relocating")
ax.xaxis.set_ticks(np.arange(0,100,5))
ax.set_xlim([0, 80])
ax.yaxis.set_ticks(np.arange(0,4000,500))
ax.legend(['Upper-income with optimal subsidy',"Upper-income without subsidy","Lower-income with optimal subsidy","Lower-income without subsidy"],loc='center left', bbox_to_anchor=(1, 0.9))


### F6
df["Diff"] = df["selfMoveYear"] - df["motMoveYear"]
df_1 =  df[df["Diff"]<=30]
fig = plt.figure()
ax = plt.subplot(111)
df_1M = df_1[df_1["className"]=="M"].groupby(["motMoveYear"]).agg("count")
df_1L = df_1[df_1["className"]=="L"].groupby(["motMoveYear"]).agg("count")
ax.scatter(df_1M.index,df_1M["alt"], marker = "o", color ="green" )
ax.scatter(df_1L.index,df_1L["alt"], marker = "x",color="lime")
ax.legend(['Upper-income',"Lower-income"],loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel("Years by which relocation is accelerated\n \n $750,000 relocation cost")
ax.set_ylabel("Number relocating")
ax.set_ylim([0, 80])
ax.set_xlim([0, 50])
#ax.set_title("Accelerated moving time distribution comparison by class",x=0.5, y=1.1)

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df_1[df_1["className"]=="M"]["selfMoveYear"],df_1[df_1["className"]=="M"]["Diff"],marker = "o", color ="green" )

ax.scatter(df_1[df_1["className"]=="L"]["selfMoveYear"],df_1[df_1["className"]=="L"]["Diff"],marker = "x",color="lime")
ax.legend(['Upper-income',"Lower-income"],loc='center left', bbox_to_anchor=(1, 0.9))
ax.set_xlabel("Relocation year with no subsidy\n \n $750,000 relocation cost")
ax.set_ylabel("Years by which relocation is accelerated")
ax.yaxis.set_ticks(np.arange(0,50, 5))
ax.set_xlim([0, 80])
#ax.set_title("Accelerated moving time versus original moving time",x=0.5, y=1.1)