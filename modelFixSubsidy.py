import numpy as np
import pandas as pd
import time
import residentClass
import governmentClass

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
floodType = 3
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
    

    
    
    
"""
House info import
"""
subsidy= 200000
goverDis = 0.025
midResDis=0.12
lowResDis=0.18
midProperty=50000
additionalMoveCost = 300000
housePriceCutoffPer=50

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
    print(governMent.objective)

  
print("One round simulation time:",time.time()-simStartTime)
freeRiderNumber1 = 0
freeRiderNumber2 = 0
for res in resList:
    if res.motMoveYear == res.selfMoveYear:
        #res.freeRiderFlag = True
        freeRiderNumber1 += 1
    if res.freeRiderFlag:
        freeRiderNumber2 += 1

print("Total objective:", governMent.objective)
print("Number of free rider:",freeRiderNumber1)
print("Number of free rider:",freeRiderNumber2)
print("Total number of movement:",sum(totalNumberMovementList))





