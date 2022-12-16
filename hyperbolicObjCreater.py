import residentHyperbolicClass as residentClass
import numpy as np
import pandas as pd
import time 
import pickle

def createRes(midResDis=0.12, lowResDis=0.18,midProperty=50000,additionalMoveCost = 300000,housePriceCutoffPer=50, numofType= 15,alpha=0.001):
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
            resDis = midResDis
            className = "L"
            propertyVal  = lowPropery
        resident = residentClass.resident(idx, res["latitude"], res["longitude"],
                                          res["altitude (m)"], res["improvementmarketvalue"],
                                          res["marketvalueyear"],res["noofstories"],
                                          res["propertyzip"],res["squarefeet"],
                                          res["totalmarketvalue"],propertyVal,className,resDis,alpha)
        resident.yearLoss(calLength, singleFloodProb, floodHeights)
        resident.expectedFutureLoss(calLength)
        resList.append(resident)
        
    print("Agent created, time is:", time.time()-resCreationTime)
    print("Agent_{midResDis}_{lowResDis}_{midProperty}_{additionalMoveCost}_{housePriceCutoffPer}_{numofType}_{alpha}".format(midResDis=midResDis,lowResDis=lowResDis,midProperty=midProperty,additionalMoveCost = additionalMoveCost,housePriceCutoffPer=housePriceCutoffPer, numofType=numofType,alpha=alpha))
    return resList


midResDis=0.12
lowResDis=0.18
midProperty=50000
additionalMoveCost = 300000
housePriceCutoffPer=50
numofType= 15


lowDisRateRange = np.linspace(0.15,0.22,15)
midDisRateRange = np.linspace(0.07,0.12,11)
reloCostRange =np.linspace(300000, 750000,10)
housePriceCutRange = np.linspace(15,80,14)
#alphaRange =[1,3.5,5.5,8]
alphaRange = np.linspace(0.5,8,16)


#createRes(midResDis=0.12, lowResDis=0.18,midProperty=50000,additionalMoveCost = 300000,housePriceCutoffPer=50, numofType= 15)
for i in alphaRange:
    print("Hpyerbolic:",i)
    additionalMoveCost = 300000
    resFile = open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\Res\Hyperbolic\resident_objects_{midResDis}_{lowResDis}_{midProperty}_{additionalMoveCost}_{housePriceCutoffPer}_{numofType}_{alpha}.dat".format(midResDis=midResDis,lowResDis=lowResDis,midProperty=midProperty,additionalMoveCost = additionalMoveCost,housePriceCutoffPer=housePriceCutoffPer, numofType=numofType,alpha=i),"wb")
    resList = createRes(midResDis=0.12, lowResDis=0.18,midProperty=50000,additionalMoveCost = 300000,housePriceCutoffPer=50, numofType= 15,alpha=i)
    pickle.dump(resList, resFile)
    resFile.close()
    additionalMoveCost = 750000
    resFile = open(r"C:\Users\yzhou364\Desktop\Dissertation\Experiment results\Res\Hyperbolic\resident_objects_{midResDis}_{lowResDis}_{midProperty}_{additionalMoveCost}_{housePriceCutoffPer}_{numofType}_{alpha}.dat".format(midResDis=midResDis,lowResDis=lowResDis,midProperty=midProperty,additionalMoveCost = additionalMoveCost,housePriceCutoffPer=housePriceCutoffPer, numofType=numofType,alpha=i),"wb")
    resList = createRes(midResDis=0.12, lowResDis=0.18,midProperty=50000,additionalMoveCost = 750000 ,housePriceCutoffPer=50, numofType= 15,alpha=i)
    pickle.dump(resList, resFile)
    resFile.close()