import numpy as np
import pandas as pd
import time
import governmentClass
import csv
import pickle



def sim(subsidy=10000,goverDis = 0.025,midResDis=0.12, lowResDis=0.18,midProperty=50000,
       additionalMoveCost = 300000,housePriceCutoffPer=50, numofType= 10,cutOffEle = 0):
    calLength = 80
    resFile = open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\TX_Gal\resident_objects_{midResDis}_{lowResDis}_{midProperty}_{additionalMoveCost}_{housePriceCutoffPer}_{numofType}.dat".format(midResDis=midResDis,lowResDis=lowResDis,midProperty=midProperty,additionalMoveCost = additionalMoveCost,housePriceCutoffPer=housePriceCutoffPer, numofType=numofType),"rb")
    resList = pickle.load(resFile)
    resFile.close()
    governMent = governmentClass.govermemt(goverDis)

    """
    Simulation process
    """
    tenHeight = 1.11 + 2.84  ## 3.95
    hundredHeight = 1.84 + 2.84  ## 4.68
    simStartTime = time.time()
    """
    Simulation process
    """
    
    simStartTime = time.time()
    
    totalNumberMovementList = []
    for year in range(calLength-1):
        ### Step 1: Get subsidy NPVs
        #subsidyNPVRes = subsidy / (1+resDis)**year
        subsidyNPVGov = subsidy / (1+goverDis)**year
        thisYearMovement = 0
        #print(subsidyNPVGov,subsidyNPVRes)
        
        
        for res in resList:
            
            if res.alt >= hundredHeight:
                res.notAffected = True
                continue
            if res.alt <= cutOffEle:
                res.cutOffed = True
                
            
            term1 = False
            term2 = False
        ### Step 2: Check double moving flag
            if res.selfMoveFlag and res.motiMoveFlag:
                continue
                
            if res.cutOffed and res.selfMoveFlag:
                continue
            
        ### Step 3: Calculate the self movement year
            if (res.motiMoveFlag and not res.selfMoveFlag):
                #print("********")
                if res.expectedFutureLossList[year+1] >= res.mktValue + additionalMoveCost:
                    res.selfMoveFlag = True
                    res.selfMoveYear = year
                continue
            
            
            ### Add the damage to the government
            governMent.objective += res.yearlyLossValList[year] / (1+goverDis)**year
        
        ### Step : Check self movement
            if res.expectedFutureLossList[year+1] >= res.mktValue + additionalMoveCost and not res.selfMoveFlag:
                res.selfMoveFlag = True
                res.selfMoveYear = year
                if not res.movedOutFlag:
                    thisYearMovement += 1
                    res.movedOutFlag = True
                term1 = True

        ### Step : Check motivated movement        
        
        ### Step : Check the elevation cutoff
            
            if  res.expectedFutureLossList[year+1] >= res.mktValue + additionalMoveCost - subsidy and not res.motiMoveFlag:
                res.motiMoveFlag = True
                res.motMoveYear = year
                if res.cutOffed:
                    res.motMoveYear = 70000
                    res.motiMoveFlag = False
                    continue
                
                
                governMent.objective += subsidyNPVGov
                if not res.movedOutFlag:
                    thisYearMovement += 1
                    res.movedOutFlag = True
                term2 = True
                if term1 and term2:
                    res.freeRiderFlag = True

                       
            if not res.motiMoveFlag and res.selfMoveFlag and not res.cutOffed:
                print("???????")     
        #print(thisYearMovement)
        totalNumberMovementList.append(thisYearMovement)
    
      
    print("One round simulation time:",time.time()-simStartTime)
    freeRiderNumber1 = 0
    freeRiderNumber2 = 0
    for res in resList:
        if res.motMoveYear == res.selfMoveYear:
            #res.freeRiderFlag = True
            freeRiderNumber1 += 1
        if res.freeRiderFlag:
            freeRiderNumber2 += 1
    
 
            
    #print("Total objective:", governMent.objective)
    #print("Number of free rider1:",freeRiderNumber1)
    #print("Number of free rider2:",freeRiderNumber2)
    #print("Total number of movement:",sum(totalNumberMovementList))
    return [governMent.objective,freeRiderNumber1,freeRiderNumber2,sum(totalNumberMovementList)]




result_list= []




subsidyRange = np.linspace(0,900000,91)
housePriceCutRange = np.linspace(15, 80,14)



elevationCutoff  = np.linspace(0,4.6,47)
optimalSum = []


runningIndex = 0
runningParam = subsidyRange

for j in elevationCutoff:
    #f2 = open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\NY_Res\4.1\10K_interval_200000_relocaiton_300K_750K_{ntype}_types.csv".format(ntype=j),"w", newline='')
    #csvwriter = csv.writer(f2)
    #csvwriter.writerow(["Param","Objective","Number of free rider1","Number of free rider2","Total movement"])
    runningIndex = 0
    minObj = 10000000000
    f2 = open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\Res\tx\eleCutOff_{ntype}_750K_15types.csv".format(ntype=j),"w", newline='')
    csvwriter = csv.writer(f2)
    csvwriter.writerow(["Param","Objective","Number of free rider1","Number of free rider2","Total movement"])
    
    for i in runningParam:
        #f2 = open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\NY_Res\4.2\houseCutoffExp_{ntype}_300K_15types.csv".format(ntype=j),"w", newline='')
        #csvwriter = csv.writer(f2)
        #csvwriter.writerow(["Param","Objective","Number of free rider1","Number of free rider2","Total movement"])
        runningIndex +=1
        result = sim(subsidy=i,goverDis = 0.025,midResDis=0.12, 
                                   lowResDis=0.18,midProperty=50000,
                                   additionalMoveCost = 750000,housePriceCutoffPer=50,
                                   numofType=15,cutOffEle=j)
        csvwriter.writerow([i]+result)
        if result[0] < minObj:
                minObj = result[0]
                optimalData = result
                optimalData.append(i)
                optimalData.append(j)
    optimalSum.append(optimalData)
        
        #print("Left:", len(runningParam) - runningIndex,"times run")
    print("This is type{num}".format(num = j))
    f2.close()


with open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\Res\tx\sum\750KeleSummary.csv","w",newline='') as f:
    writer = csv.writer(f)
    writer.writerows(optimalSum)