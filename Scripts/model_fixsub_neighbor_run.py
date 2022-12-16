import numpy as np
import pandas as pd
import time
import governmentClass
import csv
import pickle
import matplotlib.pyplot as plt
import random

random.seed(42)

def sim(subsidy,goverDis,midResDis,lowResDis,midProperty,additionalMoveCost,housePriceCutoffPer,numofType,distanceThres,vacancy,decisionProb):
    calLength = 80
    resFile = open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\Res\Neighbor\resident_objects_{distanceThres}_{additionalMoveCost}.dat".format(
        distanceThres=distanceThres,additionalMoveCost =additionalMoveCost),"rb")
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
    motilist = []
    selflist = []
    ccntlist = []
    fcntlist = []
    
    for year in range(calLength-1):
        ncnt = 0
        motit = 0
        selft = 0
        ccnt = 0
        fcnt = 0
        

        ### Step 1: Get subsidy NPVs

        subsidyNPVGov = subsidy / (1+goverDis)**year
        thisYearMovement = 0
        
        for res in resList:
            term1 = False
            term2 = False
            fflag = False
                
        ### Step 2: Check double moving flag
            if res.selfMoveFlag or res.motiMoveFlag:
                res.checkYear = year
                continue

            
            ### Check neighbor effect:     
            neighMoveSum = 0
            for neighbor in res.neighbors:
                if neighbor.movedOutFlag == True and neighbor.checkYear <= year - 1:
                    neighMoveSum += 1
            if len(res.neighbors)!= 0 and neighMoveSum / len(res.neighbors) >= vacancy:
                ccnt += 1
                fflag = True
                if random.random() <= decisionProb:
                    res.selfMoveFlag = True
                    res.neighboursFlag = True
                    res.movedOutFlag = True
                    
                    res.selfMoveYear = year
                    res.checkYear = year
                    res.motMoveYear = -100
                    thisYearMovement += 1
                    neighM +=1
                    ncnt += 1
                    continue
                
            
            ### Add the damage to the government
            governMent.objective += res.yearlyLossValList[year] / (1+goverDis)**year
        
        ### Step : Check self movement
            if res.expectedFutureLossList[year+1] >= res.mktValue + additionalMoveCost and not res.selfMoveFlag:
                res.selfMoveFlag = True
                res.selfMoveYear = year
                res.checkYear = year
                if fflag:
                    fcnt += 1
                selft += 1

                thisYearMovement += 1
                res.movedOutFlag = True
                term1 = True
        
        ### Step : Check motivated movement        
            if res.expectedFutureLossList[year+1] >= res.mktValue + additionalMoveCost - subsidy and not res.motiMoveFlag:
                res.motiMoveFlag = True
                res.motMoveYear = year
                res.checkYear = year
                governMent.objective += subsidyNPVGov
                motit += 1
                if fflag:
                    fcnt += 1
                    
                if not res.selfMoveFlag:
                    thisYearMovement += 1
                    res.movedOutFlag = True
                term2 = True
                if term1 and term2:
                    res.freeRiderFlag = True

                    
        #print(thisYearMovement)
        totalNumberMovementList.append(thisYearMovement)
        ncntlist.append(ncnt)
        motilist.append(motit)
        selflist.append(selft)
        ccntlist.append(ccnt)
        fcntlist.append(fcnt)
      
    print("One round simulation time:",time.time()-simStartTime)
    freeRiderNumber1 = 0
    freeRiderNumber2 = 0
    for res in resList:
        if res.motMoveYear == res.selfMoveYear:
            #res.freeRiderFlag = True
            freeRiderNumber1 += 1
        if res.freeRiderFlag:
            freeRiderNumber2 += 1
    
    #f1 =  open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\NY_Res\neigh\Detail\govDisExp_for_run_combination_{subsidy}_{goverDis}_{midResDis}_{lowResDis}_{midProperty}_{additionalMoveCost}_{housePriceCutoffPer}_{numofType}_free rider_information.csv".format(subsidy=subsidy,goverDis =goverDis,midResDis=midResDis, lowResDis=lowResDis,midProperty=midProperty,additionalMoveCost = additionalMoveCost,housePriceCutoffPer=housePriceCutoffPer, numofType=numofType),
    #         "w",newline='')
    #csvwriter = csv.writer(f1)
    #csvwriter.writerow(['idx', 'lat', 'long', 'alt', 'impValue', 'valYear', 'stories', 'zipCode', 'squareFeet', 'mktValue', 'className', 'disRate', 'selfMoveYear', 'motMoveYear', 'selfMoveFlag', 'motiMoveFlag', 'freeRiderFlag', 'movedOutFlag', 'property', 'cumuLoss', 'expectedFutureLossList', 'cumulativeLoss', 'yearlyLossValList'])
    
    #for res in resList:
        #if True:
            #print(list(vars(res).values()))
            #csvwriter.writerow(list(vars(res).values()))
            
    #f1.close()
            
    #print("Total objective:", governMent.objective)
    #print("Number of free rider1:",freeRiderNumber1)
    #print("Number of neighborhood effect:",neighM)
    #print("Total number of movement:",sum(totalNumberMovementList))
    #print(freeRiderNumber1,freeRiderNumber2,neighM,sum(totalNumberMovementList))
    
    #plt.plot(np.arange(len(ncntlist)),ncntlist)
    #plt.plot(np.arange(len(ncntlist)),motilist)
    #plt.plot(np.arange(len(ncntlist)),selflist)
    #plt.plot(np.arange(len(ncntlist)),ccntlist)
    #plt.plot(np.arange(len(ncntlist)),fcntlist)
    #plt.legend(['Neigh','Self','Can be affected',"Reach neigh but motivated or self"])
    #print(ncntlist)
    #print(sum(ncntlist))
    return [subsidy,governMent.objective,freeRiderNumber2,freeRiderNumber1,neighM,sum(totalNumberMovementList)]




result_list= []




subsidyRange = np.linspace(0,900000,91)


runningIndex = 0
runningParam = subsidyRange
distanceThres = np.linspace(500,1500,11)
vacanRange = np.linspace(0.1,0.4,7)
dpRange = np.linspace(0.1,0.25,4)
amc = [300000,750000]

optimalSum = []

for i in  distanceThres:
    for k in amc:
        for m in vacanRange:
            for n in dpRange:
    #f2 = open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\NY_Res\4.1\10K_interval_200000_relocaiton_300K_750K_{ntype}_types.csv".format(ntype=j),"w", newline='')
    #csvwriter = csv.writer(f2)
    #csvwriter.writerow(["Param","Objective","Number of free rider1","Number of free rider2","Total movement"])
                runningIndex = 0
                minObj = 10000000000
                f2 = open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\Res\Neighbor\result\exp_resident_objects_{distanceThres}_{additionalMoveCost}_{vacancy}_{dp}.csv".format(
                    distanceThres=i,additionalMoveCost =k,vacancy=m,dp=n),"w", newline='')
                csvwriter = csv.writer(f2)
                csvwriter.writerow(["Param","Subsidy","Objective","Number of free rider2","Number of free rider2","Neighbour movement","Total movement"])
                
                for j in subsidyRange:
                    #f2 = open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\NY_Res\4.2\houseCutoffExp_{ntype}_300K_15types.csv".format(ntype=j),"w", newline='')
                    #csvwriter = csv.writer(f2)
                    #csvwriter.writerow(["Param","Objective","Number of free rider1","Number of free rider2","Total movement"])
                    runningIndex +=1
                    result = sim(subsidy=j,goverDis = 0.025,midResDis=0.12, 
                                               lowResDis=0.18,midProperty=50000,
                                               additionalMoveCost = k,housePriceCutoffPer=50,
                                               numofType=15,distanceThres=i,vacancy=m,decisionProb=n)
                    csvwriter.writerow([i]+result)
                    if result[1] < minObj:
                            minObj = result[1]
                            optimalData = result
                            optimalData.append(i)
                            optimalData.append(k)
                            optimalData.append(m)
                            optimalData.append(n)
                optimalSum.append(optimalData)
                #print("Left:", len(runningParam) - runningIndex,"times run")
                f2.close()
    print("This is type{num}".format(num = i))
            

with open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\Res\Neighbor\neiSummary.csv","w",newline='') as f:
    writer = csv.writer(f)
    writer.writerows(optimalSum)