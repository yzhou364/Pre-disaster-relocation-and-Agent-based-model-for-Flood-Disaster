from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import matplotlib.ticker as mtick
from matplotlib import style
#style.use('ggplot1)

fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)

matplotlib.rcParams['legend.fontsize'] = 20
fig = plt.figure(figsize=(12,12))
ax1 = fig.add_subplot(111, projection='3d')
ax1.tick_params(axis='x', labelsize=23)
ax1.tick_params(axis='y', labelsize=23)
ax1.tick_params(axis='z', labelsize=23)
x1 = np.array([0.16,0.16,0.16,0.185,0.185,0.185,0.2,0.2,0.2])
y1 = np.array([0.08,0.095,0.105,0.08,0.095,0.105,0.08,0.095,0.105])
z1 = np.zeros(9)

dx1 = np.array([0.001]*9)
dy1 = np.array([0.001]*9)
dz1 = np.array([110000,110000,110000,180000,200000,200000,240000,240000,240000])


x2 = x1+0.001
y2 = y1+0.001
z2 = np.zeros(9)
dz2 = np.array([90000,90000,90000,170000,170000,180000,220000,220000,220000])



x3 = x1+0.002
y3 = y1+0.002
z3 = np.zeros(9)
dz3 = np.array([0,30000,40000,120000,120000,130000,150000,180000,180000])


ax1.bar3d(x1, y1, z1, dx1, dy1, dz1,color='red')
proxy1 = plt.Rectangle((0, 0), 1, 1, fc="red")
ax1.bar3d(x2, y2, z2, dx1, dy1, dz2,color='green')
proxy2 = plt.Rectangle((0, 0), 1, 1, fc="green")
ax1.bar3d(x3, y3, z3, dx1, dy1, dz3,color='blue')
proxy3 = plt.Rectangle((0, 0), 1, 1, fc="blue")


ax1.set_xlabel('Lower-income discount rate',labelpad=40,fontsize=23)
ax1.set_ylabel('Upper-income discount rate',labelpad=40,fontsize=23)
ax1.set_zlabel('Optimal subsidy',labelpad=40,fontsize=23)
ax1.tick_params(axis='x', labelsize=20)
ax1.tick_params(axis='y', labelsize=20)
ax1.tick_params(axis='z', labelsize=20 )
#ax1.set_xlim(0,0.25)
ax1.set_ylim(0.08,0.11,3)
ax1.set_zlim(0,250000)
ax1.zaxis.set_major_formatter(tick) 
ax1.legend([proxy1,proxy2,proxy3],['Government discount rate 0.03','Government discount rate 0.04',"Government discount rate 0.075"])

fig = plt.figure(figsize=(12,12))
ax1 = fig.add_subplot(111, projection='3d')

x1 = np.array([0.16,0.16,0.16,0.185,0.185,0.185,0.2,0.2,0.2])
y1 = np.array([0.08,0.095,0.105,0.08,0.095,0.105,0.08,0.095,0.105])
z1 = np.zeros(9)

dx1 = np.array([0.001]*9)
dy1 = np.array([0.001]*9)
dz1 = np.array([140000,
140000,
150000,
240000,
240000,
240000,
280000,
280000,
280000
])


x2 = x1+0.001
y2 = y1+0.001
z2 = np.zeros(9)
dz2 = np.array([120000,
120000,
130000,
220000,
220000,
220000,
250000,
250000,
260000
])



x3 = x1+0.002
y3 = y1+0.002
z3 = np.zeros(9)
dz3 = np.array([90000,
90000,
90000,
180000,
180000,
180000,
230000,
230000,
230000
])


ax1.bar3d(x1, y1, z1, dx1, dy1, dz1,color='red')
proxy1 = plt.Rectangle((0, 0), 1, 1, fc="red")
ax1.bar3d(x2, y2, z2, dx1, dy1, dz2,color='green')
proxy2 = plt.Rectangle((0, 0), 1, 1, fc="green")
ax1.bar3d(x3, y3, z3, dx1, dy1, dz3,color='blue')
proxy3 = plt.Rectangle((0, 0), 1, 1, fc="blue")
ax1.tick_params(axis='x', labelsize=20)
ax1.tick_params(axis='y', labelsize=20)
ax1.tick_params(axis='z', labelsize=20)
ax1.set_ylim(0.08,0.11,0.01)
ax1.set_xlabel('Lower-income discount rate',labelpad=40,fontsize=23)
ax1.set_ylabel('Upper-income discount rate',labelpad=40,fontsize=23)
ax1.set_zlabel('Optimal subsidy',labelpad=40,fontsize=23)

#ax1.set_xlim(0,0.25)
#ax1.set_ylim(0,0.2)
ax1.set_zlim(0,250000)
ax1.zaxis.set_major_formatter(tick) 
ax1.legend([proxy1,proxy2,proxy3],['Government discount rate 0.03','Government discount rate 0.04',"Government discount rate 0.075"])

    