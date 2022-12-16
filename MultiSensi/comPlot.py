import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("comSummary.csv")

df15 = df[df["house price seperation"]==15] 
df50 = df[df["house price seperation"]==50] 
df80 = df[df["house price seperation"]==80]

fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(df15["Lowerincome"],df15["Upper income"],c=df15["Optimal subsidy"],cmap="ocean")
ax.scatter(df50["Lowerincome"],df50["Upper income"],c=df50["Optimal subsidy"],cmap="ocean")

plt.show()

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(df15["Lowerincome"],df15["Upper income"],df15["government discount"],c=df15["Optimal subsidy"],cmap="jet")
#ax.scatter(df50["Lowerincome"],df50["Upper income"],df50["government discount"],c=df50["Optimal subsidy"],cmap="jet")  
#plt.colorbar(label="Objective value ($ billion)", orientation="vertical")
plt.show()


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(df15["Lowerincome"],df15["Upper income"],df15["government discount"],s=df15["Optimal subsidy"]/10000,cmap="jet")
ax.scatter(df50["Lowerincome"],df50["Upper income"],df50["government discount"],s=df50["Optimal subsidy"]/10000,cmap="jet")  
#plt.colorbar(label="Objective value ($ billion)", orientation="vertical")
plt.show()


fig = plt.figure(figsize=(12, 12))
ax1 = fig.add_subplot(121, projection='3d')
ax1.bar3d(df15['Lowerincome'], df15['Upper income'],df15["Optimal subsidy"],0.001,0.001,0.1,shade=True)
plt.show()

fig = plt.figure(figsize=(12, 12))
ax1 = fig.add_subplot(121, projection='3d')
ax1.bar3d(df15['Lowerincome'], df15['Upper income'],df15["Optimal subsidy"],0.001,0.001,1000000,shade=True)
ax1.bar3d(df50['Lowerincome']+0.0001, df50['Upper income']+0.0001,df50["Optimal subsidy"],0.001,0.001,1000000,shade=True)

plt.show()


fig = plt.figure(figsize=(12,12))
ax1 = fig.add_subplot(121, projection='3d')
ax1.bar3d(df15['Lowerincome'], df15['Upper income'],0,0.001,0.001,0.001,shade=True)
ax1.bar3d(df50['Lowerincome'], df50['Upper income'],df50["Optimal subsidy"],0.001,0.001,0.001,shade=True)

plt.show()

"""
df.drop('years', axis=1, inplace=True)
df1=df.values
print(df.isnull().sum())
print(df1)
columns = ['Afghanistan', 'Bangladesh', 'Brazil', 'China', 'Nigeria',]
rows = [ 'pad', '2008', '2009', '2010', '2011', '2012', '2013', '2014']
fig = plt.figure(figsize=(8, 6))
ax = Axes3D(fig)
lx = len(df1[0])
ly = len(df1[:,0])
xpos = np.arange(0, lx, 1)
ypos = np.arange(0, ly, 1)
xpos, ypos = np.meshgrid(xpos + 0.25, ypos + 0.25)

xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros(lx*ly)
dx = 0.25*np.ones_like(zpos)
dy = dx.copy()
dz = df1.flatten()
colors = ['red', 'yellow', 'brown', 'cyan', 'green']*ly
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors) 
ax.w_xaxis.set_ticklabels(columns)
ax.w_yaxis.set_ticklabels(rows)
ax.set_xlabel('Countries')
ax.set_ylabel('Over the years')
ax.set_zlabel('Number of cases')
plt.title('Mortality due to injuries', bbox={'facecolor':'red'})
plt.show()
"""