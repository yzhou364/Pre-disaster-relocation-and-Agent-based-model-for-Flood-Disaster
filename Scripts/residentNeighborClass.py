"""
This is the resident class definition file
"""
import pandas as pd
import numpy as np

class resident:

    # The init method or constructor
    def __init__(self,idx,lat,long,alt,impValue,valYear,stories,zipCode,squareFeet,mktValue,
                 propertyVal,className,disRate):
        self.idx = idx
        self.lat = lat
        self.long = long
        self.alt = alt
        self.impValue = impValue
        self.valYear = valYear
        self.stories = stories
        self.zipCode = zipCode
        self.squareFeet = squareFeet
        self.mktValue = mktValue
        self.className = className
        self.disRate = disRate
        self.selfMoveYear = 200
        self.motMoveYear = 150
        self.selfMoveFlag = False
        self.motiMoveFlag = False
        self.freeRiderFlag = False
        self.neighborsFlag = False
        
        self.movedOutFlag = False
        self.notAffected = False
        self.cutOffed = False
        
        self.property  = propertyVal
        self.cumuLoss = 0
        self.expectedFutureLossList = []
        self.cumulativeLoss = 0
        self.yearlyLossValList = []
        self.neighbors = []
        self.checkYear = 10000
        
    def yearLoss(self,calLength,floodProbMat,floodHeight):
        for year in range(calLength):
            totalLoss = 0
            for i in range(len(floodHeight)):
                inudation = max(0,floodHeight[i]-self.alt)*39
                ### This is the hard code damage function
                if inudation != 0:
                    propertyDamagePert = 0.9817*inudation**3 - 106.8753*inudation**2 + 3997.0122*inudation - 4315.6504
                    structureDamagePert = min(0.009*inudation**3 - 0.533*inudation**2 + 10.4*inudation+13.403,100)
                    #print(propertyDamagePert,structureDamagePert)
                else:
                    propertyDamagePert = 0
                    structureDamagePert = 0
                if self.className == "L":
                    propertyDamagePert /= 2
                damage = structureDamagePert/100*self.impValue*floodProbMat.iloc[year,i] + propertyDamagePert*floodProbMat.iloc[year,i]
                totalLoss += damage

            self.yearlyLossValList.append(totalLoss)
    


                     
    def expectedFutureLoss(self,calLength):
        for i in range(calLength):
            expectedLoss = 0
            for j in range(i,calLength):
                expectedLoss += self.yearlyLossValList[j]/(1+self.disRate)**(j-i)
            self.expectedFutureLossList.append(expectedLoss)
            