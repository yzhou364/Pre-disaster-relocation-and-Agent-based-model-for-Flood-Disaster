import numpy as np
import pandas as pd
import time
import governmentClass
import csv
import pickle
import matplotlib.pyplot as plt
import random

random.seed(0)

def sim(subsidy,goverDis,midResDis,lowResDis,midProperty,additionalMoveCost,housePriceCutoffPer,numofType,distanceThres):
    calLength = 80
    resFile = open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\Res\Neighbor\hyperbolic0.04.dat".format(
        distanceThres=distanceThres,midResDis=midResDis,lowResDis=lowResDis,midProperty=midProperty,additionalMoveCost = additionalMoveCost,housePriceCutoffPer=housePriceCutoffPer, numofType=numofType),"rb")
    resList = pickle.load(resFile)
    resFile.close()
    governMent = governmentClass.govermemt(goverDis)

    """
    Simulation process
    """
    
    simStartTime = time.time()
    
    totalNumberMovementList = []
    neighM = 0
    ncntlist = []
    for year in range(calLength-1):
        ncnt = 0
        ### Step 1: Get subsidy NPVs
        #subsidyNPVRes = subsidy / (1+resDis)**year
        subsidyNPVGov = subsidy / (1+goverDis)**year
        thisYearMovement = 0
        #print(subsidyNPVGov,subsidyNPVRes)
        
        for res in resList:
            term1 = False
            term2 = False
        
                
        ### Step 2: Check double moving flag
            if res.selfMoveFlag and res.motiMoveFlag:
                res.checkYear = year
                continue
            if res.neighborsFlag:
                res.checkYear = year
                continue
            
            ### Check neighbor effect:     
            neighMoveSum = 0
            for neighbor in res.neighbors:
                if neighbor.movedOutFlag == True and neighbor.checkYear == year - 1:
                    neighMoveSum += 1
            if len(res.neighbors)!= 0 and neighMoveSum / len(res.neighbors) >= 0.5 and random.random()>0.5:
                res.selfMoveFlag = True
                res.neighboursFlag = True
                res.movedOutFlag = True
                res.motiMoveFlag = True
                res.selfMoveYear = year
                res.checkYear = year
                res.motMoveYear = -100
                thisYearMovement += 1
                neighM +=1
                ncnt += 1
                continue
                
            if random.random() > 0.9:
                res.selfMoveFlag = True
                res.movedOutFlag = True
                res.motiMoveFlag = True
                res.selfMoveYear = year


                    
        #print(thisYearMovement)
        totalNumberMovementList.append(thisYearMovement)
        ncntlist.append(ncnt)
        print(ncnt)
    
      
    print("One round simulation time:",time.time()-simStartTime)
    freeRiderNumber1 = 0
    freeRiderNumber2 = 0
    for res in resList:
        if res.motMoveYear == res.selfMoveYear:
            #res.freeRiderFlag = True
            freeRiderNumber1 += 1
        if res.freeRiderFlag:
            freeRiderNumber2 += 1
    
    f1 =  open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\NY_Res\5.27\Detail\govDisExp_for_run_combination_{subsidy}_{goverDis}_{midResDis}_{lowResDis}_{midProperty}_{additionalMoveCost}_{housePriceCutoffPer}_{numofType}_free rider_information.csv".format(subsidy=subsidy,goverDis =goverDis,midResDis=midResDis, lowResDis=lowResDis,midProperty=midProperty,additionalMoveCost = additionalMoveCost,housePriceCutoffPer=housePriceCutoffPer, numofType=numofType),
              "w",newline='')
    csvwriter = csv.writer(f1)
    csvwriter.writerow(['idx', 'lat', 'long', 'alt', 'impValue', 'valYear', 'stories', 'zipCode', 'squareFeet', 'mktValue', 'className', 'disRate', 'selfMoveYear', 'motMoveYear', 'selfMoveFlag', 'motiMoveFlag', 'freeRiderFlag', 'movedOutFlag', 'property', 'cumuLoss', 'expectedFutureLossList', 'cumulativeLoss', 'yearlyLossValList'])
    for res in resList:
        if True:
            #print(list(vars(res).values()))
            csvwriter.writerow(list(vars(res).values()))
            
    f1.close()
            
    print("Total objective:", governMent.objective)
    print("Number of free rider1:",freeRiderNumber1)
    print("Number of neighborhood effect:",neighM)
    print("Total number of movement:",sum(totalNumberMovementList))
    print(governMent.objective,freeRiderNumber1,neighM,sum(totalNumberMovementList))
    
    plt.plot(np.arange(len(ncntlist)),ncntlist)
    #print(ncntlist)
    #print(sum(ncntlist))
    return [subsidy,governMent.objective,freeRiderNumber2,neighM,sum(totalNumberMovementList)]




result_list= []




subsidyRange = np.linspace(0,900000,91)
subsidyRange = [0]
lowDisRateRange = np.linspace(0.15,0.22,15)
midDisRateRange = np.linspace(0.07,0.12,11)
govDisRateRange = np.linspace(0.025, 0.045,21)
list(govDisRateRange).append(0.075)
housePriceCutRange = np.linspace(15, 80,14)
reloCostRange =np.linspace(300000, 750000,10)

experiMentList = [subsidyRange,lowDisRateRange,midDisRateRange,govDisRateRange,housePriceCutRange
                  ,reloCostRange]


runningIndex = 0
runningParam = subsidyRange
distanceThres = 500

for i in [0.025]:
    #f2 = open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\NY_Res\4.1\10K_interval_200000_relocaiton_300K_750K_{ntype}_types.csv".format(ntype=j),"w", newline='')
    #csvwriter = csv.writer(f2)
    #csvwriter.writerow(["Param","Objective","Number of free rider1","Number of free rider2","Total movement"])
    runningIndex = 0
    f2 = open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\NY_Res\5.27\0.04_0.5_0.8_{ntype}_750K_15types.csv".format(ntype=i),"w", newline='')
    csvwriter = csv.writer(f2)
    csvwriter.writerow(["Param","Subsidy","Objective","Number of free rider2","Neighbour movement","Total movement"])
    
    for j in subsidyRange:
        #f2 = open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\NY_Res\4.2\houseCutoffExp_{ntype}_300K_15types.csv".format(ntype=j),"w", newline='')
        #csvwriter = csv.writer(f2)
        #csvwriter.writerow(["Param","Objective","Number of free rider1","Number of free rider2","Total movement"])
        runningIndex +=1
        csvwriter.writerow([i]+sim(subsidy=j,goverDis = i,midResDis=0.12, 
                                   lowResDis=0.18,midProperty=50000,
                                   additionalMoveCost = 750000,housePriceCutoffPer=50,
                                   numofType=15,distanceThres=500))
        print("Left:", len(runningParam) - runningIndex,"times run")
    print("This is type{num}".format(num = j))
    f2.close()


