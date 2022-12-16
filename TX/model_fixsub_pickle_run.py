import numpy as np
import pandas as pd
import time
import governmentClass
import csv
import pickle

def sim(subsidy,goverDis,midResDis,lowResDis,midProperty,additionalMoveCost,housePriceCutoffPer,numofType):
    calLength = 80
    resFile = open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\TX_Gal\resident_objects_{midResDis}_{lowResDis}_{midProperty}_{additionalMoveCost}_{housePriceCutoffPer}_{numofType}.dat".format(midResDis=midResDis,lowResDis=lowResDis,midProperty=midProperty,additionalMoveCost = additionalMoveCost,housePriceCutoffPer=housePriceCutoffPer, numofType=numofType),"rb")
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
    
    f1 =  open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\TX_Gal\Detail\govDisExp_for_run_combination_{subsidy}_{goverDis}_{midResDis}_{lowResDis}_{midProperty}_{additionalMoveCost}_{housePriceCutoffPer}_{numofType}_free rider_information.csv".format(subsidy=subsidy,goverDis =goverDis,midResDis=midResDis, lowResDis=lowResDis,midProperty=midProperty,additionalMoveCost = additionalMoveCost,housePriceCutoffPer=housePriceCutoffPer, numofType=numofType),
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
    print("Number of free rider2:",freeRiderNumber2)
    print("Total number of movement:",sum(totalNumberMovementList))
    return [subsidy,governMent.objective,freeRiderNumber2,sum(totalNumberMovementList)]




result_list= []




subsidyRange = np.linspace(0,900000,91)
#subsidyRange = np.linspace(0.05,0.5,10)
lowDisRateRange = np.linspace(0.15,0.22,15)
midDisRateRange = np.linspace(0.07,0.12,11)
govDisRateRange = [0.025]
list(govDisRateRange).append(0.075)
housePriceCutRange = np.linspace(15, 80,14)
reloCostRange =np.linspace(300000, 750000,10)

experiMentList = [subsidyRange,lowDisRateRange,midDisRateRange,govDisRateRange,housePriceCutRange
                  ,reloCostRange]


runningIndex = 0
runningParam = subsidyRange

for i in govDisRateRange:
    #f2 = open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\NY_Res\4.1\10K_interval_200000_relocaiton_300K_750K_{ntype}_types.csv".format(ntype=j),"w", newline='')
    #csvwriter = csv.writer(f2)
    #csvwriter.writerow(["Param","Objective","Number of free rider1","Number of free rider2","Total movement"])
    runningIndex = 0
    f2 = open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\TX_Gal\Exp_{ntype}_750K_15types.csv".format(ntype=i),"w", newline='')
    csvwriter = csv.writer(f2)
    csvwriter.writerow(["Param","Subsidy","Objective","Number of free rider2","Total movement"])
    
    for j in subsidyRange:
        #f2 = open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\NY_Res\4.2\houseCutoffExp_{ntype}_300K_15types.csv".format(ntype=j),"w", newline='')
        #csvwriter = csv.writer(f2)
        #csvwriter.writerow(["Param","Objective","Number of free rider1","Number of free rider2","Total movement"])
        runningIndex +=1
        csvwriter.writerow([i]+sim(subsidy=j,goverDis = 0.025,midResDis=0.12, 
                                   lowResDis=0.18,midProperty=50000,
                                   additionalMoveCost = 750000,housePriceCutoffPer=50,
                                   numofType=15))
        print("Left:", len(runningParam) - runningIndex,"times run")
    print("This is type{num}".format(num = j))
    f2.close()


