import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd


#####750


df1 = np.array([436, 23, 15, 19, 23, 14, 14, 12, 14, 8, 7, 15, 11, 5, 3, 7, 6, 5, 7, 4, 6, 4, 10, 6, 3, 6, 7, 4, 2, 10, 5, 4, 7, 4, 3, 7, 1, 6, 2, 1, 2, 5, 3, 2, 2, 0, 5, 0, 0, 6, 1, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
df2 = np.array([241, 6, 7, 9, 23, 25, 16, 9, 16, 11, 25, 10, 10, 6, 19, 8, 9, 9, 11, 16, 12, 9, 6, 14, 7, 9, 10, 14, 20, 29, 32, 27, 16, 12, 5, 7, 10, 8, 5, 5, 4, 4, 3, 4, 4, 2, 1, 1, 0, 2, 0, 1, 1, 0, 1, 0, 12, 1, 0, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
df3 = np.array([166, 8, 5, 4, 6, 4, 8, 5, 6, 7, 7, 5, 4, 5, 2, 4, 5, 4, 1, 5, 13, 7, 19, 8, 15, 6, 5, 8, 18, 31, 29, 30, 26, 27, 14, 25, 20, 22, 24, 24, 21, 23, 13, 12, 6, 7, 4, 7, 6, 3, 4, 5, 3, 2, 5, 5, 2, 0, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
df4 = np.array([121, 6, 7, 4, 9, 7, 6, 6, 5, 3, 2, 3, 1, 1, 3, 4, 2, 3, 0, 0, 8, 4, 1, 3, 3, 11, 7, 5, 6, 10, 9, 24, 34, 15, 21, 33, 24, 29, 17, 24, 24, 12, 19, 21, 22, 15, 23, 17, 21, 18, 13, 8, 11, 4, 5, 4, 6, 7, 2, 3, 2, 4, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(np.arange(0,79,1),df1.cumsum(),c ="skyblue")
ax.scatter(np.arange(0,79,1),df2.cumsum(),c ="royalblue")
ax.scatter(np.arange(0,79,1),df3.cumsum(),c ="darkblue")
ax.scatter(np.arange(0,79,1),df4.cumsum(),c ="midnightblue")



ax.legend(["Hyperbolic paramater  "+chr(913).lower() + "=1",
           "Hyperbolic paramater  "+chr(913).lower() + "=3.5",
           "Hyperbolic paramater  "+chr(913).lower() + "=5.5",
    "Hyperbolic paramater  "+chr(913).lower() + "=8"
           ])
ax.yaxis.set_ticks(np.arange(0,1300,100))
ax.set_xlim([0, 80])
ax.set_xlabel("Year  \n \n $750,000 relocation cost")
ax.set_ylabel("Number relocating")



#####300

df1 = np.array([571, 19, 12, 16, 13, 11, 10, 10, 6, 1, 6, 3, 6, 3, 7, 3, 8, 4, 0, 1, 2, 4, 4, 1, 1, 4, 1, 6, 5, 5, 5, 3, 0, 4, 1, 5, 1, 7, 1, 5, 1, 2, 2, 0, 1, 0, 5, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
df2 = np.array([596, 7, 13, 21, 11, 6, 11, 7, 14, 9, 10, 14, 10, 9, 7, 5, 3, 8, 3, 4, 3, 3, 0, 2, 2, 2, 2, 1, 8, 9, 4, 8, 4, 3, 3, 0, 1, 1, 0, 1, 1, 1, 2, 2, 0, 0, 1, 2, 0, 1, 0, 1, 1, 3, 0, 1, 0, 1, 1, 1, 2, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
df3 = np.array([495, 5, 7, 13, 9, 8, 6, 8, 8, 11, 11, 6, 4, 5, 5, 6, 7, 4, 3, 8, 9, 7, 4, 4, 4, 5, 5, 7, 9, 22, 35, 14, 14, 7, 2, 3, 3, 11, 8, 3, 7, 2, 4, 3, 5, 1, 0, 0, 1, 2, 0, 1, 1, 1, 0, 2, 0, 0, 0, 2, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0])
df4 = np.array([403, 16, 10, 7, 11, 14, 16, 18, 3, 2, 3, 3, 5, 5, 7, 4, 3, 2, 5, 4, 2, 4, 4, 5, 10, 8, 13, 2, 8, 16, 13, 20, 9, 12, 12, 21, 24, 23, 10, 12, 6, 2, 3, 2, 4, 12, 5, 7, 3, 1, 5, 4, 1, 3, 0, 0, 0, 3, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0])
fig = plt.figure()
ax = plt.subplot(111)
ax.scatter(np.arange(0,79,1),df1.cumsum(),c ="skyblue")
ax.scatter(np.arange(0,79,1),df2.cumsum(),c ="royalblue")
ax.scatter(np.arange(0,79,1),df3.cumsum(),c ="darkblue")
ax.scatter(np.arange(0,79,1),df4.cumsum(),c ="midnightblue")

ax.legend(["Hyperbolic paramater  "+chr(913).lower() + "=1",
           "Hyperbolic paramater  "+chr(913).lower() + "=3.5",
           "Hyperbolic paramater  "+chr(913).lower() + "=5.5",
    "Hyperbolic paramater  "+chr(913).lower() + "=8"
           ])
ax.yaxis.set_ticks(np.arange(0,1300,100))
ax.set_xlim([0, 80])
ax.set_xlabel("Year  \n \n $300,000 relocation cost")
ax.set_ylabel("Number relocating")
