import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

df = pd.read_csv(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\NY_Res\4.6\for_run_combination_250000.0_0.025_0.12_0.22_50000_750000_50_15_free rider_information.csv")

### Free riders

fig = plt.figure()
ax = plt.subplot(111)
rateLabel = ["Low income","Middle income"]
ax.scatter(100*(df.loc[df["freeRiderFlag"] == False]["disRate"]+0.005),df.loc[df["freeRiderFlag"] == False]["alt"],
           color = 'orchid',alpha = 0.5)
ax.scatter(100*(df.loc[df["freeRiderFlag"] == True]["disRate"]),df.loc[df["freeRiderFlag"] == True]["alt"],
           color = "r",alpha = 1)
ax.xaxis.set_ticks([0,12,22,30])
ax.yaxis.set_ticks(np.arange(0,10,1))
ax.legend(['Not free rider',"Free rider"],loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel("Residential discount rate (%)")
ax.set_ylabel("Elevation (m)")
#ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))
ax.set_title("Free rider information based on elevation (m)")
print(df)


fig = plt.figure()
ax = plt.subplot(111)
rateLabel = ["Low income","Middle income"]
ax.scatter(100*(df.loc[df["freeRiderFlag"] == False]["disRate"]+0.005),df.loc[df["freeRiderFlag"] == False]["mktValue"],
           color = 'orchid',alpha = 0.5)
ax.scatter(100*(df.loc[df["freeRiderFlag"] == True]["disRate"]),df.loc[df["freeRiderFlag"] == True]["mktValue"],
           color = "r",alpha = 1)
ax.xaxis.set_ticks([0,12,22,30])
#ax.yaxis.set_ticks(np.arange(0,20000,2500))
#ax.set_ylim([0, 20000])
ax.legend(['Not free rider',"Free rider"],loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel("Residential discount rate (%)")
ax.set_ylabel("House market value")
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick) 
#ax.ticklabel_format(useOffset=False, style='plain')
#ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2e'))
ax.set_title("Free rider information based on house market value")

df2 = pd.read_csv(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\NY_Res\4.6\lowDisExpSummary.csv")
fig = plt.figure()
ax = plt.subplot(111)
ax.set_title("Optimal subsidy in different low income discount rate")
ax.scatter(100*df2["lowDisRate"],df2["Param"], color = "black")
ax.set_xlim([0,30])
ax.set_xlabel("Lower-income discount rate (%)")
ax.set_ylabel("Optimal subsidy")
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick) 
ax.set_ylim([0, 300000])
#ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))


df_time1 = df.groupby(df["selfMoveYear"]).agg("count")
df_time2 = df.groupby(df["motMoveYear"]).agg("count")
fig = plt.figure()
ax = plt.subplot(111)
ax.set_title("Motivated moving and self moving time histgram comparison",x=0.5, y=1.1)
ax.bar(df_time2.index[:-1]+0.5,df_time2["disRate"][:-1], color = "green",width=0.7)
ax.bar(df_time1.index[:-1],df_time1["disRate"][:-1], color = "blue",width=0.7)
ax.set_xlabel("Year")
ax.set_ylabel("Number relocating")
ax.xaxis.set_ticks(np.arange(0,100,5))
ax.set_xlim([0, 80])
ax.legend(['With optimal subsidy',"Without subsidy"],loc='center left', bbox_to_anchor=(1, 0.9))


df_time1_cum = df_time1.cumsum()
df_time2_cum = df_time2.cumsum()
fig = plt.figure()
ax = plt.subplot(111)
ax.set_title("Cumulative motivated moving and self moving time distribution comparison",x=0.5, y=1.1)

ax.bar(df_time2_cum.index[:-1],100*df_time2_cum["disRate"][:-1]/df.shape[0],color = "green")
ax.bar(df_time1_cum.index[:-1],100*df_time1_cum["disRate"][:-1]/df.shape[0],color = "blue")

ax.bar(6,100*df_time2_cum["disRate"][5]/df.shape[0],color = "green")
ax.bar(6,100*df_time1_cum["disRate"][5]/df.shape[0],color = "blue")
ax.bar(16,100*df_time2_cum["disRate"][15]/df.shape[0],color = "green")
ax.bar(16,100*df_time1_cum["disRate"][15]/df.shape[0],color = "blue")

for i in range(df_time2_cum.index[-2],81):
    ax.bar(i,100*df_time2_cum["disRate"].tolist()[-2]/df.shape[0],color = "green")
    ax.bar(i,100*df_time1_cum["disRate"].tolist()[-2]/df.shape[0],color = "blue")
    
ax.set_xlabel("Year")
ax.set_ylabel("Cumulative relocations (%)")
ax.xaxis.set_ticks(np.arange(0,100,5))
ax.set_xlim([0, 80])
ax.set_ylim([0,100])
ax.legend(['With optimal subsidy',"Without subsidy"],loc='center left', bbox_to_anchor=(1, 0.9))



df_middle  = df[df["className"]=="M"]
df_low  = df[df["className"]=="L"]
df_middle_mot_cum = df_middle.groupby(df["motMoveYear"]).agg("count").cumsum()
df_low_mot_cum = df_low.groupby(df["motMoveYear"]).agg("count").cumsum()
df_middle_self_cum = df_middle.groupby(df["selfMoveYear"]).agg("count").cumsum()
df_low_self_cum = df_low.groupby(df["selfMoveYear"]).agg("count").cumsum()
fig = plt.figure()
ax = plt.subplot(111)
ax.set_title("Cumulative motivated moving and self moving time number cumulative comparison by class",x=0.5, y=1.1)
ax.scatter(df_middle_mot_cum.index[:-1],df_middle_mot_cum["disRate"][:-1], color="green", marker = "o")
ax.scatter(df_middle_self_cum.index[:-1],df_middle_self_cum["disRate"][:-1],color="blue", marker = "o")
ax.scatter(df_low_mot_cum.index[:-1],df_low_mot_cum["disRate"][:-1],color="green", marker = "x")
ax.scatter(df_low_self_cum.index[:-1],df_low_self_cum["disRate"][:-1],color="blue", marker = "x")

for i in range(df_middle_mot_cum.index[-2]+1,81):
    ax.scatter(i,df_middle_mot_cum["disRate"].tolist()[-2], color="green", marker = "o")
    ax.scatter(i,df_middle_self_cum["disRate"].tolist()[-2],color="blue", marker = "o")
    ax.scatter(i,df_low_mot_cum["disRate"].tolist()[-2],color="green", marker = "x")
    ax.scatter(i,df_low_self_cum["disRate"].tolist()[-2],color="blue", marker = "x")
    
ax.set_xlabel("Year")
ax.set_ylabel("Number relocating")
ax.xaxis.set_ticks(np.arange(0,100,5))
ax.set_xlim([0, 80])
ax.yaxis.set_ticks(np.arange(0,550,50))
ax.set_ylim([0, 550])
ax.legend(['Upper-income with optimal subsidy',"Upper-income without subsidy","Lower-income with optimal subsidy","Lower-income without subsidy"],loc='center left', bbox_to_anchor=(1, 0.9))
### Difference 

df["Diff"] = df["selfMoveYear"] - df["motMoveYear"]
df_1 =  df[df["Diff"]<=30]
fig = plt.figure()
ax = plt.subplot(111)
df_1M = df_1[df_1["className"]=="M"].groupby(["motMoveYear"]).agg("count")
df_1L = df_1[df_1["className"]=="L"].groupby(["motMoveYear"]).agg("count")
ax.scatter(df_1M.index,df_1M["alt"], marker = "o", color ="green" )
ax.scatter(df_1L.index,df_1L["alt"], marker = "x",color="lime")
ax.legend(['Upper-income',"Lower-income"],loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel("Years by which relocation is accelerated")
ax.set_ylabel("Number relocating")
ax.set_ylim([0, 30])
ax.set_xlim([0, 50])
ax.set_title("Accelerated moving time distribution comparison by class",x=0.5, y=1.1)

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df_1[df_1["className"]=="M"]["selfMoveYear"],df_1[df_1["className"]=="M"]["Diff"],marker = "o", color ="green" )

ax.scatter(df_1[df_1["className"]=="L"]["selfMoveYear"],df_1[df_1["className"]=="L"]["Diff"],marker = "x",color="lime")
ax.legend(['Upper-income',"Lower-income"],loc='center left', bbox_to_anchor=(1, 0.9))
ax.set_xlabel("Relocation year with no subsidy")
ax.set_ylabel("Years by which relocation is accelerated")
ax.yaxis.set_ticks(np.arange(0,20, 5))
ax.set_xlim([0, 80])
ax.set_title("Accelerated moving time versus original moving time",x=0.5, y=1.1)


from random import randint
df = pd.read_csv(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\NY_Res\4.6\test.csv")
fig = plt.figure()
ax = plt.subplot(111)

ax.scatter(df.index[:],df["0.18"][:],color ="yellowgreen" )
ax.scatter(df.index[:],df["0.19"][:],color = "forestgreen")
ax.scatter(df.index[:],df["0.2"][:],color = "green")
ax.scatter(df.index[:],df["0.21"][:],color="seagreen")
ax.scatter(df.index[:],df["0.22"][:],color = "lime")
ax.scatter(df.index[:],df["0.23"][:],color="springgreen")
ax.scatter(df.index[:],df["0.24"][:],color="palegreen")
ax.scatter(df.index[:],df["0.25"][:],color="lightgreen")
ax.legend(['0.18',"0.19","0.20","0.21","0.22",'0.23',"0.24","0.25"],loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel("Year")
ax.set_ylabel("Number of relocation")
ax.set_xlim([0, 80])
ax.set_title("Low income cumulative motivated moving year between different discount rate",x=0.5, y=1.1)
