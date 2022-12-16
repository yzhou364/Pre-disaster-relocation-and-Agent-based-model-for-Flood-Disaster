import numpy as np
import math

### Expected loss is probability multiple loss per year
def lossCal(loss, prob):
	tmp = np.array(loss)*np.array(prob)
	return tmp

### Government expected loss is past loss
def govExLoss(dis_gov, calLength, expLoss):
	tmp = []
	tmp1 = []
	tmp.append(0);
	for i in range(1,calLength):
		for j in range(1,i-1):
			tmp1.append(expLoss[j]/math.pow((1+dis_gov),j))
		tmp.append(sum(tmp1))
		tmp1 = []
	return tmp

### Resident expected loss is future loss
def resExLoss(dis_res, calLength, expLoss):
	tmp = []
	tmp1 = []
	for i in range(0,calLength):
		for j in range(i+1,calLength):
			tmp1.append(expLoss[j]/math.pow((1+dis_res),j-i))
		tmp.append(sum(tmp1))
		tmp1 = []
	return tmp

### One time subsidy needed
def subNeeded(movCost,resExLoss,threshold):
	tmp = movCost - np.array(resExLoss)
	#print(tmp)
	for i in range(0,len(resExLoss)):
		if tmp[i] < threshold:
			tmp[i] = threshold
	#print(tmp)
	return tmp

### FixBenefit
def fixBene(movCost,resExLoss,dis_res,threshold):
	tmp = movCost - np.array(resExLoss)
	#print(len(resExLoss))
	for k in range(0,len(resExLoss)):
		if tmp[k] < threshold:
			tmp[k] = threshold
		else:
			fixB = -1*np.pmt(dis_res,len(resExLoss)-k,tmp[k])
			tmp[k] = fixB
	#print(tmp)
	return tmp

### Objective function(Objective is to minimize the government loss)
def subObjCal(subNeeded,govExLoss,dis_gov,calLength):
	tmp = []
	tmp1 = []
	for i in range(0,calLength):
		tmp1.append(subNeeded[i]/math.pow((1+dis_gov),i))
	for i in range(0,calLength):
		tmp.append(govExLoss[i] + tmp1[i])
	#print(tmp)
	return tmp


def fixObjCal(fixBene,govExLoss,dis_gov,calLength):
	tmp = []
	tmp1 = []
	for i in range(0,calLength):
		tmp1.append(-1*np.pv(dis_gov,calLength-i-1,fixBene[i]))
	#print(tmp1)
	for i in range(0,calLength):
		tmp.append(tmp1[i] + govExLoss[i])
	#print(tmp)
	return tmp

### run models
def runModel(prob,calLength,loss,dis_gov,dis_res,movCost):
	expLoss = np.array(prob)*loss
	#print(expLoss)
	gov_Loss = govExLoss(dis_gov,calLength,expLoss)
	#print(gov_Loss)
	res_Loss = resExLoss(dis_res,calLength,expLoss)
	#print(res_Loss)
	sub_Need = subNeeded(movCost,res_Loss,0)
	#print(sub_Need)
	fixB_Need = fixBene(movCost,res_Loss,dis_res,0)
	#print(fixB_Need)
	#hyper_Need = hypNeed(movCost,res_Loss,dis_res,0)
	sub_Obj= subObjCal(sub_Need,gov_Loss,dis_gov,calLength)
	#print(sub_Obj)
	fixB_Obj = fixObjCal(fixB_Need,gov_Loss,dis_gov,calLength)
	#print(fixB_Obj)

	#print(sub_Need)
	for i in range(0,calLength):
		if sub_Need[i] == 0:
			self_Moving = i+1
			break
		else:
			self_Moving = -100

	sub_value = min(sub_Obj)
	sub_year = sub_Obj.index(min(sub_Obj))

	fixB_value = min(fixB_Obj)
	fixB_year = fixB_Obj.index(min(fixB_Obj))

	tmp = []
	tmp.append([self_Moving,sub_year,sub_value,fixB_year,fixB_value,dis_gov,dis_res,movCost])
	return tmp