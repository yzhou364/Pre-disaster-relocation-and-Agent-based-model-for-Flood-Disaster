import numpy as np
import pandas as pd
import time
import residentClass
import governmentClass
import csv

def sim(subsidy=10000,goverDis = 0.025,midResDis=0.12, lowResDis=0.18,midProperty=50000,
       additionalMoveCost = 300000,housePriceCutoffPer=50, numofType= 10,cutOffEle = 0):
    """
    Data file path
    """
    tenYearFloodFile = r"C:\Users\yzhou364\Desktop\Dissertation\DissertationPythonModel\floodData\10_NY_RCP45.csv"
    hundredYearFloodFile = r"C:\Users\yzhou364\Desktop\Dissertation\DissertationPythonModel\floodData\100_NY_RCP45.csv"
    housePriceFile = r"C:\Users\yzhou364\Desktop\Dissertation\DissertationPythonModel\houseData\ny_fill.csv"
    
    
    """
    Input the flood data from the data file
    """
    calLength = 80
    tenHeight = 1.11 + 2.84  ## 3.95
    hundredHeight = 1.84 + 2.84  ## 4.68
    floodType = numofType
    floodHeights = np.linspace(tenHeight, hundredHeight,floodType)
    floodProb = pd.DataFrame(np.zeros((calLength,floodType)))
    
    hundredFloodProb = []
    with open(hundredYearFloodFile,'r') as f:
    	for line in f.readlines():
    		hundredFloodProb.append(float(line.split(',')[0]))
    	f.close()
    tenFloodProb = []
    with open(tenYearFloodFile,'r') as f:
    	for line in f.readlines():
    		tenFloodProb.append(float(line.split(',')[0]))
    	f.close()
        
    for i in range(len(hundredFloodProb)):
        floodProb.iloc[i,:] = np.linspace(tenFloodProb[i],hundredFloodProb[i],floodType)
        
    singleFloodProb = floodProb
    singleFloodProb["ex"] = floodProb[floodType-1].shift(0)
    lastYearProb = singleFloodProb["ex"] 
    singleFloodProb = singleFloodProb.diff(-1,axis=1).iloc[:,:-1]
    singleFloodProb.iloc[:,-1] = lastYearProb
        

    
    
    

    lowPropery = midProperty / 2
    housePriceDf = pd.read_csv(housePriceFile)
    housePriceCutoff = np.percentile(housePriceDf["totalmarketvalue"],housePriceCutoffPer)

    resList = []
    resCreationTime = time.time()
    for idx,res in housePriceDf.iterrows():
        if res["totalmarketvalue"] >= housePriceCutoff:
            resDis = midResDis
            className = "M"
            propertyVal  = midProperty
        else:
            resDis = lowResDis
            className = "L"
            propertyVal = lowPropery
        resident = residentClass.resident(idx, res["latitude"], res["longitude"],
                                          res["altitude (m)"], res["improvementmarketvalue"],
                                          res["marketvalueyear"],res["noofstories"],
                                          res["propertyzip"],res["squarefeet"],
                                          res["totalmarketvalue"],propertyVal,className,resDis)
        resident.yearLoss(calLength, singleFloodProb, floodHeights)
        resident.expectedFutureLoss(calLength)
        resList.append(resident)
        
    print("Agent created, time is:", time.time()-resCreationTime)
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
    
    f1 =  open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\NY_Res\6.28\Detail\for_run_combination_{subsidy}_{goverDis}_{midResDis}_{lowResDis}_{midProperty}_{additionalMoveCost}_{housePriceCutoffPer}_{numofType}_free rider_information_{cutOffEle}.csv".format(subsidy=subsidy,goverDis =goverDis,midResDis=midResDis, lowResDis=lowResDis,midProperty=midProperty,additionalMoveCost = additionalMoveCost,housePriceCutoffPer=housePriceCutoffPer, numofType=numofType,cutOffEle=cutOffEle),
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
    return [governMent.objective,freeRiderNumber1,freeRiderNumber2,sum(totalNumberMovementList)]




result_list= []




subsidyRange = np.linspace(0,900000,91)
#subsidyRange = np.linspace(0.05,0.5,10)
lowDisRateRange = np.linspace(0.15,0.22,15)
midDisRateRange = np.linspace(0.07,0.12,11)
govDisRateRange = np.linspace(0.025, 0.045,21)
list(govDisRateRange).append(0.075)
housePriceCutRange = np.linspace(15, 80,14)
reloCostRange =np.linspace(300000, 750000,10)

experiMentList = [subsidyRange,lowDisRateRange,midDisRateRange,govDisRateRange,housePriceCutRange
                  ,reloCostRange]


elevationCutoff  = np.linspace(0,4.6,47)



runningIndex = 0
runningParam = subsidyRange

for j in elevationCutoff:
    #f2 = open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\NY_Res\4.1\10K_interval_200000_relocaiton_300K_750K_{ntype}_types.csv".format(ntype=j),"w", newline='')
    #csvwriter = csv.writer(f2)
    #csvwriter.writerow(["Param","Objective","Number of free rider1","Number of free rider2","Total movement"])
    runningIndex = 0
    f2 = open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\NY_Res\6.28\eleCutOff_{ntype}_750K_15types.csv".format(ntype=j),"w", newline='')
    csvwriter = csv.writer(f2)
    csvwriter.writerow(["Param","Objective","Number of free rider1","Number of free rider2","Total movement"])
    
    for i in runningParam:
        #f2 = open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\NY_Res\4.2\houseCutoffExp_{ntype}_300K_15types.csv".format(ntype=j),"w", newline='')
        #csvwriter = csv.writer(f2)
        #csvwriter.writerow(["Param","Objective","Number of free rider1","Number of free rider2","Total movement"])
        runningIndex +=1
        csvwriter.writerow([i]+sim(subsidy=i,goverDis = 0.025,midResDis=0.12, 
                                   lowResDis=0.18,midProperty=50000,
                                   additionalMoveCost = 300000,housePriceCutoffPer=50,
                                   numofType=15,cutOffEle=j))
        print("Left:", len(runningParam) - runningIndex,"times run")
    print("This is type{num}".format(num = j))
    f2.close()


