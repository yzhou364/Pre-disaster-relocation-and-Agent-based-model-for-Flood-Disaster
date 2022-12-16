import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
from random import randint

fig = plt.figure()
ax = plt.subplot(111)

d1 = np.array([642, 13, 16, 11, 15, 11, 14, 6, 3, 5, 4, 4, 4, 5, 2, 2, 7, 4, 5, 1, 3, 1, 2, 3, 2, 3, 2, 6, 3, 3, 0, 2, 2, 1, 4, 1, 0, 1, 0, 1, 2, 2, 0, 1, 2, 1, 2, 1, 0, 2, 1, 1, 2, 0, 0, 0, 1, 0, 4, 1, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
d2 = np.array([667, 13, 13, 7, 14, 11, 12, 3, 5, 4, 5, 4, 1, 3, 6, 3, 2, 2, 5, 0, 2, 2, 2, 2, 2, 3, 3, 7, 1, 1, 2, 1, 3, 2, 1, 2, 0, 0, 1, 1, 1, 0, 0, 2, 2, 1, 2, 1, 2, 3, 0, 0, 1, 5, 4, 0, 1, 0, 0, 1, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
d3 = np.array([663, 20, 13, 12, 13, 14, 6, 3, 6, 5, 6, 2, 2, 4, 5, 2, 1, 1, 0, 4, 2, 3, 1, 3, 1, 6, 4, 2, 2, 1, 1, 3, 3, 1, 1, 0, 0, 0, 3, 0, 1, 0, 1, 1, 1, 2, 1, 3, 3, 1, 2, 1, 6, 0, 0, 0, 2, 0, 2, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
d4 = np.array([680, 18, 18, 10, 10, 8, 6, 10, 3, 5, 3, 4, 0, 1, 2, 1, 2, 0, 4, 3, 0, 4, 0, 5, 5, 1, 0, 3, 3, 3, 1, 1, 0, 2, 0, 0, 1, 3, 0, 0, 1, 0, 2, 1, 1, 4, 2, 4, 0, 7, 0, 0, 0, 1, 1, 3, 0, 0, 2, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
idx = np.arange(0,79)


ax.scatter(idx,d1.cumsum(),color="seagreen")
ax.scatter(idx,d2.cumsum(),color = "lime")
ax.scatter(idx,d3.cumsum(),color="springgreen")
ax.scatter(idx,d4.cumsum(),color="palegreen")
ax.legend(['0.15',"0.18","0.20","0.22","0.22"],loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel("Year")
ax.set_ylabel("Number relocating")
ax.set_xlim([0, 80])
ax.set_title("Cumulative relocating between different lower-income discount rate",x=0.5, y=1.1)



fig = plt.figure()
ax = plt.subplot(111)

d1 = np.array([592, 25, 19, 16, 13, 13, 9, 11, 9, 11, 4, 4, 5, 5, 6, 2, 4, 2, 4, 8, 7, 2, 4, 3, 1, 1, 4, 2, 5, 5, 3, 3, 1, 2, 1, 0, 5, 0, 1, 1, 0, 1, 1, 2, 1, 1, 1, 1, 3, 1, 0, 0, 1, 1, 2, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
d2 = np.array([597, 28, 31, 17, 9, 12, 7, 9, 7, 5, 8, 5, 6, 4, 4, 4, 5, 2, 2, 6, 5, 1, 3, 1, 4, 3, 3, 3, 4, 8, 1, 1, 2, 1, 1, 2, 3, 2, 0, 0, 0, 1, 2, 0, 0, 1, 1, 2, 1, 2, 0, 3, 0, 3, 0, 0, 0, 1, 4, 2, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
d3 = np.array([621, 21, 24, 15, 11, 11, 8, 12, 9, 4, 7, 1, 4, 2, 8, 4, 1, 5, 4, 3, 1, 3, 3, 2, 4, 1, 4, 2, 5, 5, 1, 1, 3, 0, 4, 0, 2, 0, 0, 1, 0, 2, 1, 1, 0, 1, 1, 1, 1, 2, 2, 3, 1, 0, 2, 3, 4, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
d4 = np.array([634, 20, 25, 15, 11, 11, 11, 9, 5, 4, 5, 4, 8, 3, 0, 4, 3, 4, 1, 1, 3, 1, 4, 2, 3, 3, 3, 5, 2, 2, 2, 3, 1, 2, 0, 2, 0, 1, 0, 1, 2, 1, 0, 0, 1, 2, 0, 2, 3, 2, 1, 3, 0, 6, 1, 0, 0, 1, 2, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
idx = np.arange(0,79)


ax.scatter(idx,d1.cumsum(),color="seagreen")
ax.scatter(idx,d2.cumsum(),color = "lime")
ax.scatter(idx,d3.cumsum(),color="springgreen")
ax.scatter(idx,d4.cumsum(),color="palegreen")
ax.legend(['0.15',"0.18","0.20","0.22","0.22"],loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xlabel("Year")
ax.set_ylabel("Number relocating")
ax.set_xlim([0, 80])
ax.set_title("Cumulative relocating between different lower-income discount rate",x=0.5, y=1.1)



