import numpy as np
import pandas as pd
import time
from residentHyperbolicClass import resident
import governmentClass
import csv
import pickle

def sim(subsidy,goverDis,midResDis,lowResDis,midProperty,additionalMoveCost,housePriceCutoffPer,numofType,alpha):
    calLength = 80
    resFile =  open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\Res\Hyperbolic\resident_objects_{midResDis}_{lowResDis}_{midProperty}_{additionalMoveCost}_{housePriceCutoffPer}_{numofType}_{alpha}.dat".format(midResDis=midResDis,lowResDis=lowResDis,midProperty=midProperty,additionalMoveCost = additionalMoveCost,housePriceCutoffPer=housePriceCutoffPer, numofType=numofType,alpha=alpha),"rb")
    resList = pickle.load(resFile)
    resFile.close()
    governMent = governmentClass.govermemt(goverDis)

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
            term1 = False
            term2 = False
        ### Step 2: Check double moving flag
            if res.selfMoveFlag and res.motiMoveFlag:
                continue
                
        ### Step 3: Calculate the self movement year
            if res.motiMoveFlag and not res.selfMoveFlag:
                #print("********")
                if res.expectedFutureLossList[year+1] >= res.mktValue + additionalMoveCost:
                    res.selfMoveFlag = True
                    res.selfMoveYear = year
                continue
                
            if not res.motiMoveFlag and res.selfMoveFlag:
                print("???????")
            
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
            if res.expectedFutureLossList[year+1] >= res.mktValue + additionalMoveCost - subsidy and not res.motiMoveFlag:
                res.motiMoveFlag = True
                res.motMoveYear = year
                governMent.objective += subsidyNPVGov
                if not res.movedOutFlag:
                    thisYearMovement += 1
                    res.movedOutFlag = True
                term2 = True
                if term1 and term2:
                    res.freeRiderFlag = True

                    
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
    
    #f1 =  open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\NY_Res\Hyperbolic\Detail\HyperExp_for_run_combination_{subsidy}_{goverDis}_{midResDis}_{lowResDis}_{midProperty}_{additionalMoveCost}_{housePriceCutoffPer}_{numofType}_{alpha}_free rider_information.csv".format(subsidy=subsidy,goverDis =goverDis,midResDis=midResDis, lowResDis=lowResDis,midProperty=midProperty,additionalMoveCost = additionalMoveCost,housePriceCutoffPer=housePriceCutoffPer, numofType=numofType,alpha=alpha),
    #          "w",newline='')
    #csvwriter = csv.writer(f1)
    #csvwriter.writerow(['idx', 'lat', 'long', 'alt', 'impValue', 'valYear', 'stories', 'zipCode', 'squareFeet', 'mktValue', 'className', 'disRate', 'selfMoveYear', 'motMoveYear', 'selfMoveFlag', 'motiMoveFlag', 'freeRiderFlag', 'movedOutFlag', 'property', 'cumuLoss', 'expectedFutureLossList', 'cumulativeLoss', 'yearlyLossValList'])
    #for res in resList:
    #    if True:
    #        #print(list(vars(res).values()))
     #       csvwriter.writerow(list(vars(res).values()))
            
    #f1.close()
            
    
    print(subsidy,totalNumberMovementList)
    return [subsidy,governMent.objective,freeRiderNumber2,sum(totalNumberMovementList)]
    



result_list= []




subsidyRange =[470000]
#subsidyRange = np.linspace(0.05,0.5,10)
lowDisRateRange = np.linspace(0.15,0.22,15)
midDisRateRange = np.linspace(0.07,0.12,11)
govDisRateRange = np.linspace(0.025, 0.045,21)
list(govDisRateRange).append(0.075)
housePriceCutRange = np.linspace(15, 80,14)
reloCostRange =np.linspace(300000, 750000,10)

experiMentList = [subsidyRange,lowDisRateRange,midDisRateRange,govDisRateRange,housePriceCutRange
                  ,reloCostRange]
alphaRange = [1,3.5,5.5,8]

runningIndex = 0
runningParam = subsidyRange

optimalCases = []


for i in alphaRange:
    minObj = 10000000000
    #f2 = open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\NY_Res\4.1\10K_interval_200000_relocaiton_300K_750K_{ntype}_types.csv".format(ntype=j),"w", newline='')
    #csvwriter = csv.writer(f2)
    #csvwriter.writerow(["Param","Objective","Number of free rider1","Number of free rider2","Total movement"])
    runningIndex = 0
    #f2 = open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\NY_Res\Hyperbolic\HyperExp_{ntype}_750K_15types.csv".format(ntype=i),"w", newline='')
    #csvwriter = csv.writer(f2)
    #csvwriter.writerow(["Param","Subsidy","Objective","Number of free rider2","Total movement"])
    
    for j in subsidyRange:
        #f2 = open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\NY_Res\4.2\houseCutoffExp_{ntype}_300K_15types.csv".format(ntype=j),"w", newline='')
        #csvwriter = csv.writer(f2)
        #csvwriter.writerow(["Param","Objective","Number of free rider1","Number of free rider2","Total movement"])
        runningIndex +=1
        result = sim(subsidy=j,goverDis = 0.12,midResDis=0.12, 
                                   lowResDis=0.18,midProperty=50000,
                                   additionalMoveCost = 750000,housePriceCutoffPer=50,
                                   numofType=15,alpha=i)
        #csvwriter.writerow([i]+result)
        if result[1] < minObj:
            minObj = result[1]
            optimalData = result
            optimalData.append(i)
        print("Left:", len(runningParam) - runningIndex,"times run")

    optimalCases.append(optimalData)
    print("This is type{num}".format(num = i))
    #f2.close()


    