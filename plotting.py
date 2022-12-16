import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("mycsvfile.csv",header=None)


rows = []
for idx,res in data.iterrows():
    expType = res[0].strip(")").split(",")[0][:-1]
    param_1 = res[0].strip(")").split(",")[1]
    subsidy = res[0].strip(")").split(",")[2]
    reloNumber = [int(x) for x in res[1].split("]")[0][1:].split(",")]
    freeRider = int(res[1].split("]")[1][1:].split(",")[0])
    objective = float(res[1].split("]")[1][1:].split(",")[1][:-1])
    
    row = [expType,param_1,subsidy,reloNumber,freeRider,objective]
    rows.append(row)
    

df = pd.DataFrame(rows,columns=["expType","param_1","subsidy",
                                "reloNumber","freeRider","objective"])


"""
expType:
    lowDisExp      
    midDisExp      
    govDisExp
    houseCutExp
    reloCostExp
"""
def subsidyPlot(df,expType,param_1):
    df = df[df["expType"]==expType]
    df = df[df["param_1"]==" "+ str(param_1)]
    #print(df)
    df.plot(kind="scatter",x="subsidy",y='objective')
    title = str(expType)+" "+str(param_1)+" subsidy"+" scatter plot"
    plt.title(title)
    
    
def moveTimeLinePlot(df,expType,param_1,subsidy):
    df = df[df["expType"]==expType]
    df = df[df["param_1"]==" "+ str(param_1)]
    df = df[df["subsidy"]==" "+ str(subsidy)]
    for i in df["reloNumber"]:
        move = list(i)
    plt.plot(np.arange(len(move)),move)
    title =  str(expType)+" ="+str(param_1)+" subsidy="+ str(subsidy)+ " line plot"
    plt.title(title)