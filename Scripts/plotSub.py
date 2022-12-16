# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 11:47:33 2022

@author: yzhou364
"""


"""
fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df.loc[df["freeRiderFlag"] == False]["disRate"]+0.0015,df.loc[df["freeRiderFlag"] == False]["mktValue"],
           color = 'g',alpha = 0.5)
ax.scatter(df.loc[df["freeRiderFlag"] == True]["disRate"],df.loc[df["freeRiderFlag"] == True]["mktValue"],
           color = "r",alpha = 1)

ax.xaxis.set_ticks([0.12,0.18])
ax.legend(['Not Free rider',"Free rider"],loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel("Residential discount rate(%)")
ax.set_ylabel("House marketvalue($)")
ax.set_title("free rider_information")


### summary
df2 = pd.read_csv(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\NY_Res\4.6\lowDisExpSummary.csv")
fig = plt.figure()
ax = plt.subplot(111)
ax.set_title("Optimal subsidy in different low income discount rate")
ax.scatter(df2["lowDisRate"],df2["Param"])
ax.set_xlabel("Low income discount rate")
ax.set_ylabel("Optimal subsidy")
#ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))


fig = plt.figure()
ax = plt.subplot(111)
ax.set_title("Optimal objective value in different low income discount rate",x=0.5, y=1.1)
ax.scatter(df2["lowDisRate"],df2["Objective"])
ax.set_xlabel("Low income discount rate")
ax.set_ylabel("Objective")

fig = plt.figure()
ax = plt.subplot(111)
ax.set_title("Total number of movement and free riders",x=0.5, y=1.1)
ax.scatter(df2["lowDisRate"],df2["Number of free rider"])
ax.scatter(df2["lowDisRate"],df2["Total movement"])
ax.legend(['Free rider',"Total number of movement"],loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel("Low income discount rate")
ax.set_ylabel("Movement number")
ax.yaxis.set_ticks(np.arange(0,1000, 100))


#### Time related 
fig = plt.figure()
ax = plt.subplot(111)
df_time1 = df.groupby(df["selfMoveYear"]).agg("count")
ax.set_title("Self moving time",x=0.5, y=1.1)
ax.bar(df_time1.index[:-1],df_time1["disRate"][:-1])
ax.set_xlabel("Time")
ax.set_ylabel("Moving number")
ax.xaxis.set_ticks(np.arange(0,100, 10))


fig = plt.figure()
ax = plt.subplot(111)
df_time2 = df.groupby(df["motMoveYear"]).agg("count")
ax.set_title("Motivated moving time",x=0.5, y=1.1)
ax.bar(df_time2.index[:-1],df_time2["disRate"][:-1])
ax.set_xlabel("Time")
ax.set_ylabel("Moving number")
ax.xaxis.set_ticks(np.arange(0,100, 10))


fig = plt.figure()
ax = plt.subplot(111)
ax.set_title("Motivated moving and self moving time distribution comparison",x=0.5, y=1.1)
ax.bar(df_time2.index[:-1],df_time2["disRate"][:-1])
ax.bar(df_time1.index[:-1],df_time1["disRate"][:-1])
ax.set_xlabel("Time")
ax.set_ylabel("Moving number")
ax.xaxis.set_ticks(np.arange(0,100, 10))
ax.legend(['Motivated',"Original"],loc='center left', bbox_to_anchor=(1, 0.5))


df_time1_cum = df_time1.cumsum()
df_time2_cum = df_time2.cumsum()
fig = plt.figure()
ax = plt.subplot(111)
ax.set_title("Cumulative motivated moving and self moving time distribution comparison",x=0.5, y=1.1)
ax.bar(df_time2_cum.index[:-1],df_time2_cum["disRate"][:-1])
ax.bar(df_time1_cum.index[:-1],df_time1_cum["disRate"][:-1])
ax.set_xlabel("Time")
ax.set_ylabel("Moving number")
ax.xaxis.set_ticks(np.arange(0,100, 10))
ax.legend(['Motivated',"Original"],loc='center left', bbox_to_anchor=(1, 0.5))



df_middle  = df[df["className"]=="M"]
df_low  = df[df["className"]=="L"]
df_middle_mot_cum = df_middle.groupby(df["motMoveYear"]).agg("count").cumsum()
df_low_mot_cum = df_low.groupby(df["motMoveYear"]).agg("count").cumsum()
df_middle_self_cum = df_middle.groupby(df["selfMoveYear"]).agg("count").cumsum()
df_low_self_cum = df_low.groupby(df["selfMoveYear"]).agg("count").cumsum()
fig = plt.figure()
ax = plt.subplot(111)
ax.set_title("Cumulative motivated moving and self moving time distribution comparison by class",x=0.5, y=1.1)
ax.scatter(df_middle_mot_cum.index[:-1],df_middle_mot_cum["disRate"][:-1])
ax.scatter(df_low_mot_cum.index[:-1],df_low_mot_cum["disRate"][:-1])

ax.scatter(df_middle_self_cum.index[:-1],df_middle_self_cum["disRate"][:-1])
ax.scatter(df_low_self_cum.index[:-1],df_low_self_cum["disRate"][:-1])
ax.set_xlabel("Time")
ax.set_ylabel("Moving number")
ax.xaxis.set_ticks(np.arange(0,100, 10))
ax.legend(['Middle motivated',"Low motivated","Middle original","Low original"],loc='center left', bbox_to_anchor=(1, 0.5))
### Difference 

df["Diff"] = df["selfMoveYear"] - df["motMoveYear"]
df_1 =  df[df["Diff"]<=30]
fig = plt.figure()
ax = plt.subplot(111)
ax.hist(df_1[df_1["className"]=="M"]["Diff"],bins=15)
ax.hist(df_1[df_1["className"]=="L"]["Diff"],bins=15)
ax.legend(['Middle',"Low"],loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel("Accelerated time")
ax.set_ylabel("Total Number")
ax.set_title("Accelerated moving time distribution comparison by class",x=0.5, y=1.1)

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df_1[df_1["className"]=="L"]["selfMoveYear"],df_1[df_1["className"]=="L"]["Diff"])
ax.scatter(df_1[df_1["className"]=="M"]["selfMoveYear"],df_1[df_1["className"]=="M"]["Diff"])
ax.set_xlabel("Original time")
ax.set_ylabel("Accelerated time")
ax.yaxis.set_ticks(np.arange(0,20, 5))