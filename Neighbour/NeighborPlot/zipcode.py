import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
import matplotlib
matplotlib.rcParams['legend.fontsize'] =12
         
fig = plt.figure()
ax = plt.subplot(111)
plt.scatter("Zip code",1021,color = 'blue')
plt.hlines(877,"Zip code","Zip code by median",linestyles="solid",color ="blue")
plt.scatter("Zip code",270,color = 'peru')
plt.hlines(116,"Zip code","Zip code by quartile",linestyles="dashed",color ="peru")
plt.hlines(877,"Zip code","Zip code by quartile",linestyles="solid",color ="blue")
plt.scatter("Zip code by median",995,color = 'blue')
plt.scatter("Zip code by median",182,color = 'peru')
plt.scatter("Zip code by quartile",907,color = 'blue')
plt.scatter("Zip code by quartile",164,color = 'peru')


ax.yaxis.set_ticks(np.arange(0,1300,200))

#plt.xticks(rotation)
ax.set_xlabel("\n \n $300,000 relocation cost")
ax.set_ylabel("Number relocating")

fig = plt.figure()
ax = plt.subplot(111)
plt.scatter("Zip code",1014,color = 'blue')
plt.hlines(864,"Zip code","Zip code by median",linestyles="solid",color ="blue")
plt.scatter("Zip code",294,color = 'peru')
plt.hlines(131,"Zip code","Zip code by quartile",linestyles="dashed",color ="peru")
plt.hlines(864,"Zip code","Zip code by quartile",linestyles="solid",color ="blue")
plt.scatter("Zip code by median",909,color = 'blue')
plt.scatter("Zip code by median",154,color = 'peru')
plt.scatter("Zip code by quartile",889,color = 'blue')
plt.scatter("Zip code by quartile",150,color = 'peru')
plt.legend(["Total relocations by zip code","Total relocations with 800m radius",
            "Network relocations by zip code","Network relocations with 800m radius"], bbox_to_anchor=(1, 0.9))

ax.yaxis.set_ticks(np.arange(0,1300,200))

#plt.xticks(rotation)
ax.set_xlabel("\n \n $750,000 relocation cost")
ax.set_ylabel("Number relocating")