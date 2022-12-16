import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
import matplotlib
font = {'size'   : 22}

matplotlib.rc('font', **font)
         
fig = plt.figure()
ax = plt.subplot(111)
plt.scatter("Zip code",1021,color = 'blue')
plt.hlines(877,"Zip code","Zip code by median",linestyles="solid",color ="blue")
plt.scatter("Zip code",270,color = 'peru')
plt.hlines(116,"Zip code","Zip code by quartile",linestyles="dashed",color ="peru")
plt.hlines(877,"Zip code","Zip code by quartile",linestyles="solid",color ="blue")
plt.scatter("Zip code by median",983,color = 'blue')
plt.scatter("Zip code by median",162,color = 'peru')
plt.scatter("Zip code by quartile",911,color = 'blue')
plt.scatter("Zip code by quartile",157,color = 'peru')


ax.yaxis.set_ticks(np.arange(0,1300,100))

plt.xticks(rotation=45)
ax.set_xlabel("\n \n $300,000 relocation cost")
ax.set_ylabel("Number relocating")

fig = plt.figure()
ax = plt.subplot(111)
plt.scatter("Zip code",1014,color = 'blue')
plt.hlines(864,"Zip code","Zip code by median",linestyles="solid",color ="blue")
plt.scatter("Zip code",294,color = 'peru')
plt.hlines(131,"Zip code","Zip code by quartile",linestyles="dashed",color ="peru")
plt.hlines(864,"Zip code","Zip code by quartile",linestyles="solid",color ="blue")
plt.scatter("Zip code by median",903,color = 'blue')
plt.scatter("Zip code by median",148,color = 'peru')
plt.scatter("Zip code by quartile",886,color = 'blue')
plt.scatter("Zip code by quartile",146,color = 'peru')
plt.legend(["Total relocations by zip code","Total relocations with 800m radius",
            "Network relocations by zip code","Network relocations with 800m radius"], bbox_to_anchor=(1, 0.9))

ax.yaxis.set_ticks(np.arange(0,1300,100))

plt.xticks(rotation=45)
ax.set_xlabel("\n \n $750,000 relocation cost")
ax.set_ylabel("Number relocating")