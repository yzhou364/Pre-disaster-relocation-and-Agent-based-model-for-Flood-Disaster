"""
This is the main file that runs the ABM
"""

from model_run import *
import numpy as np
import time

"""
Basic analysis range

"""
lowDisRateRange = np.linspace(0.15,0.22,15)
midDisRateRange = np.linspace(0.07,0.12,11)

govDisRateRange = np.linspace(0.025, 0.045,21)
list(govDisRateRange).append(0.075)

housePriceCutRange = np.linspace(15, 50,8)
reloCostRange = np.linspace(300000, 750000,10)

subsidyRange = np.linspace(50000,150000,16)

resultDict = {}
startTime = time.time()
totalRunNumber = 0
"""
for i in lowDisRateRange:
    for j in subsidyRange:
        resultDict[("lowDisExp",i,j)] = model(floodType = 16,goverDis = 0.025,
                                            midResDis = 0.12,lowResDis = i,
                                            housePriceCutoffPer = 50,additionalMoveCost = 300000,
                                            subsidy = j)
        totalRunNumber += 1
        

for i in midDisRateRange:
    for j in subsidyRange:
        resultDict[("midDisExp",i,j)] = model(floodType = 16,goverDis = 0.025,
                                        midResDis = i,lowResDis = 0.18,
                                        housePriceCutoffPer = 50,additionalMoveCost = 300000,
                                        subsidy = j)
        totalRunNumber += 1
        
        
for i in midDisRateRange:
    for j in subsidyRange:
        resultDict[("govDisExp",i,j)] = model(floodType = 16,goverDis =i,
                                        midResDis = 0.12,lowResDis = 0.18,
                                        housePriceCutoffPer = 50,additionalMoveCost = 300000,
                                        subsidy = j)
        totalRunNumber += 1
        
        
for i in housePriceCutRange:
    for j in subsidyRange:
        resultDict[("houseCutExp",i,j)] = model(floodType = 16,goverDis = 0.025,
                                        midResDis = 0.12,lowResDis = 0.18,
                                        housePriceCutoffPer = i,additionalMoveCost = 300000,
                                        subsidy = j)
        totalRunNumber += 1
 
        
for i in reloCostRange:
    for j in subsidyRange:
        resultDict[("reloCostExp",i,j)] = model(floodType = 16,goverDis = 0.025,
                                        midResDis = 0.12,lowResDis = 0.18,
                                        housePriceCutoffPer = 50,additionalMoveCost = i,
                                        subsidy = j)
        totalRunNumber += 1
"""
for i in subsidyRange:
    print("Run:",totalRunNumber,"Subsidy:",i)
    resultDict[("reloCostExp",300000,i)] = model(floodType = 16,goverDis = 0.025,
                                    midResDis = 0.12,lowResDis = 0.18,
                                    housePriceCutoffPer = 50,additionalMoveCost = 300000,
                                    subsidy = i)
    totalRunNumber +=1
        

print("Total Experiment time:", time.time()-startTime)
print("Total run number:",totalRunNumber)

with open('mycsvfile_0214.csv', 'w') as f:  # You will need 'wb' mode in Python 2.x
    w = csv.DictWriter(f, resultDict.keys())
    w.writeheader()
    w.writerow(resultDict)
    