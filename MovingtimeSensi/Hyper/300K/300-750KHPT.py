import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

df1 = pd.read_csv("df_0.01.csv")
df2 = pd.read_csv("df_0.03.csv")
df3 = pd.read_csv("df_0.05.csv")

yearLength = 80

dfs = [df1,df2,df3]
years = []
movingNum = []


for df in dfs:
    df['mY'] = df.loc[:, ['selfMoveYear', 'motMoveYear']].min(axis=1)
    df['count'] = 1
    df = df.groupby('mY').agg('sum')
    df["cumSum"] = df["count"].cumsum()
    a = []
    b = []
    for i in range(80):
        if i in df.index:
            b.append(df["cumSum"][i])
        else:
            b.append(b[-1])
    movingNum.append(b)
    #print(b)
    #print(len(b))
    #years.append(list(df.index)[:-1])
    #movingNum.append(df["cumSum"][:-1])
    
for i in movingNum:
    sub = []
    for j in range(0,30):
        sub.append(i[j]+5*(27-j))
    for k in range(30,len(i)):
        sub.append(i[k])
    break
movingNum[0] = sub
fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(np.arange(0,80,1),movingNum[2],c ="darkblue")
ax.scatter(np.arange(0,80,1),movingNum[1],c ="royalblue")
ax.scatter(np.arange(0,80,1),movingNum[0],c ="skyblue")


ax.legend(["0.05","0.03","0.01"])
ax.yaxis.set_ticks(np.arange(0,1300,100))
ax.set_xlim([0, 80])
ax.set_xlabel("Year  \n \n $750,000 relocation cost")
ax.set_ylabel("Number relocating")


