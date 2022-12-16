import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)


fig = plt.figure()
ax = plt.subplot(111)
plt.scatter("Zip code",1021,color='blue',marker = "^")
plt.scatter("Zip code",270,color='black')

plt.hlines(877,"Zip code","Zip code with 2 categories",linestyles ="solid")
plt.hlines(116,"Zip code","Zip code with 2 categories",linestyles ="dashdot")

plt.scatter("Zip code with 2 categories",182,color='black')
plt.scatter("Zip code with 2 categories",955,color='blue',marker="^")
plt.scatter("Zip code with 4 categories",169,color='black')
plt.scatter("Zip code with 4 categories",921,color='blue',marker = "^")

plt.hlines(877,"Zip code","Zip code with 4 categories",linestyles ="solid")
plt.hlines(116,"Zip code","Zip code with 4 categories",linestyles ="dashdot")
#ax.legend(['Total relocations','Network relocations'])

#plt.legend(['Total relocations','Network relocations','Total relocations with 800m radius','Network relocations with 800m radius'])
plt.ylim(0,1200)
plt.xlabel("Neighbor with house price categories \n \n $300,000 relocation cost")
plt.ylabel("Number relocating")


fig = plt.figure()
ax = plt.subplot(111)
plt.scatter("Zip code",1014,color='blue',marker = "^")
plt.scatter("Zip code",294,color='black')

plt.hlines(949,"Zip code","Zip code with 2 categories",linestyles ="solid")
plt.hlines(193,"Zip code","Zip code with 2 categories",linestyles ="dashdot")

plt.scatter("Zip code with 2 categories",203,color='black')
plt.scatter("Zip code with 2 categories",987,color='blue',marker="^")
plt.scatter("Zip code with 4 categories",198,color='black')
plt.scatter("Zip code with 4 categories",975,color='blue',marker = "^")

plt.hlines(949,"Zip code","Zip code with 4 categories",linestyles ="solid")
plt.hlines(193,"Zip code","Zip code with 4 categories",linestyles ="dashdot")
#ax.legend(['Total relocations','Network relocations'])

plt.legend(['Total relocations','Network relocations','Total relocations with 800m radius','Network relocations with 800m radius'],bbox_to_anchor=(1.7, 0.5))
plt.ylim(0,1200)
plt.xlabel("Neighbor with house price categories \n \n $750,000 relocation cost")
plt.ylabel("Number relocating")

