# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 21:55:44 2019

@author: Aryan Singh
"""

'''
inference by rejection sampling and likelihood weighting
i. P(rain)
ii. P(tired | ¬happy)
iii. P(happy | sunny)
iv. P(snow | happy, ¬tired)

'''

import random
import sys



# these are the answers, from the table
x1 = 0.2
x2 = 0.367
x3 = 0.64
x4 = 0.1635
    
            
# P(rain)        
# print(sampling(10,None, 0.2))

'''
P(rain) - 0.2
P(tired | ¬happy) - 0.2071 / 0.564
P(happy | sunny) -  0.256 / 0.400
P(snow | happy, ¬tired) - 0.0561 / 0.3431

rejection sampling
we need to reject the evidence and not care about any other variable
look at the bayes net and then sample the points
in rejection sampling, we go over the samples one by one
whereas in the likelihood weighting, we look at one sample till we force it

rejection, accept/trials - 
tired - 0.3,0.7
weather -0.4,0.7,0.9,1
happy is conditional - happy|weather, tired - make from table
sample 1 - w, sample 2 - tired, sample 3 - H|W,T
do we need the table for H|W,T ? do we make it ? do we use q1?
sample 3 would be accding to sample 1 and 2 - we want +h from that


likelihood - happy | sunny
we know that evidence is sunny, therefore we would force it for sunny
even if it is not
and then multiply 0.4, which is the prob for the evidence to the weight
then we need weight for that variable / total weight

'''

# make the table yourself, for the H|W,T

def weatherCalc(n):
    if n < 0.4:
        return "Sunny"
    elif n>=0.4 and n<0.7:
        return "Cloudy"
    elif n>=0.7 and n<0.9:
        return "Rain"
    else: 
        return "Snow"
        
def makeTable(num):
    l=[]
    for i in range(0, num):
        table = []
        s=random.random()
        table.append(weatherCalc(s))
        if s < 0.3:
            table.append(True)
        else:
            table.append(False)
        # solve for happy now
        if s<0.564:
            table.append(True)
        else:
            table.append(False)
        l.append(table)
    return l
            

a = makeTable(10)
#print(a)


# P(rain)
def reject1(num):
    rain=0
    for i in range(0,num):
        s = random.random()
        if s>=0.7 and s<0.9:
            rain+=1
    return float(rain)/num        

#print("P(rain) =>0.2, ", reject1(1000))

# P(tired | -happy)
# trials when t|-h, and -t|-h, but accept t|-h
def reject2(num, accept, trials):
    for i in range(0,num):
        s1 = random.random()
        if s1<0.4: # sunny 
            if random.random()<0.3: #tired
                if random.random()>=0.5:# not happy
                    trials+=1
                    accept+=1
            else:# not tired
                if random.random()>=0.7:# not happy
                    trials+=1
        
        elif s1>=0.4 and s1<0.7:
            if random.random()<0.3:# tired
                if random.random()>=0.1: # not happy
                    trials+=1
                    accept+=1
            else:# not tired
                if random.random()>=0.3:# not happy
                    trials+=1
        
        elif s1>=0.7 and s1<0.9:
            if random.random()<0.3:#tired 
                if random.random()>=0.1:#not happy
                    trials+=1
                    accept+=1    
            else:
                if random.random()>=0.2: #not happy    
                    trials+=1
        else:
            if random.random()<0.3:
                if random.random()>=0.6:
                    trials+=1
                    accept+=1
            else:
                if random.random()>=0.8:
                    trials+=1
    
    return float(accept)/trials

#print("P(tired | -happy) =>0.367, ", reject2(1000,1,1))

# rejection for h | sunny, reject when not sunny, accept otherwise
# P(h,s)/P(s) = 0.256/0.4        
# 3 random samples, check one by one
def reject3(num, accept, trials):
    for i in range(0,num):
        if random.random() < 0.4: # first sample is sunny, this is the evidence
            trials+=1
            s = random.random()
            if s < 0.3:# tired
                if random.random() < 0.5:# conditional probs for H|t,sunny
                    accept+=1
            else:# -tired
                if random.random() < 0.7:# conditional for H|-t, sunny
                    accept+=1
    return float(accept)/trials

#print("P(happy | sunny) =>0.64, ", reject3(1000,1,1))

# snow|happy,-tired
def reject4(num, accept, trials):
    for i in range(0,num):
        s1 = random.random()
        if s1<0.4: # sunny 
            if random.random()>=0.3: # not tired
                if random.random()<0.7:# happy
                    trials+=1
        
        elif s1>=0.4 and s1<0.7:#cloudy
            if random.random()>=0.3:# not tired
                if random.random()<0.3:# happy
                    trials+=1
        
        elif s1>=0.7 and s1<0.9:#rainy
            if random.random()>=0.3:# not tired 
                if random.random()<0.2:# happy
                    trials+=1    
                    
        elif s1>=0.9: # snow
            if random.random()>=0.3:# not tired
                if random.random()<0.8:# happy
                    accept+=1
                    trials+=1
        
    return float(accept)/trials
#print("P(snow | happy, -tired) =>0.1635, ",rejection4(1000,1,1))

#P(rain)
def like1(num):
    rain=0
    for i in range(0,num):
        s = random.random()
        if s>=0.7 and s<0.9:
            rain+=1
    return float(rain)/num        

#print(like1(1000))

# tired | -happy, we want to fix not happy values
def like2(num):
    weights=[]
    w=[]
    for i in range(0,num):
        s = random.random()
        if s<0.4:# sunny
            if random.random()<0.3:
                weights.append(0.5)# tired and not happy
                w.append(0.5)
            else:
                weights.append(0.3)
                
        elif s>0.4 and s<=0.7:
            if random.random()<0.3:
                weights.append(0.9)# tired and not happy
                w.append(0.9)
            else:
                weights.append(0.7)
                
        elif s>0.7 and s<=0.9:
            if random.random()<0.3:
                weights.append(0.9)# tired and not happy
                w.append(0.9)
            else:
                weights.append(0.8)
                
        else:
            if random.random()<0.3:
                weights.append(0.4)# tired and not happy
                w.append(0.4)
            else:
                weights.append(0.2)
               
    totalW=0            
    weight=0
    for i in range(0,len(weights)):
        totalW+=weights[i]
    for i in range(0,len(w)):
        weight+=w[i]
    return float(weight)/totalW
                
#print(like2(10000))          
                
# happy | sunny, weights that have h,s / weights having s
def like3(num):
    weight=0
    totalW=0
    for i in range(0,num):
        s=random.random()
        totalW += 0.4
        if s < 0.3: #tired
            if random.random() < 0.5:#happy
                weight += 0.4
        else:# not tired
            if random.random() < 0.7:#happy
                weight+=0.4
    return float(weight)/totalW
            

#print(like3(10000))
            

# snow | happy, -tired
def like4(num):
    weights = []
    totalW = []
    for i in range(0,num):
        s = random.random()
        if s<0.4: # sunny
            totalW.append(0.7*0.7)
        elif s>0.4 and s<=0.7:
            totalW.append(0.7*0.3)
        elif s>0.7 and s<=0.9:
            totalW.append(0.7*0.2)
        else:
            totalW.append(0.7*0.8)
            weights.append(0.7*0.8)
    weight=0
    totalw=0
    for i in range(0,len(totalW)):
        totalw+=totalW[i]
    for i in range(0,len(weights)):
        weight+=weights[i]
    
    return float(weight)/totalw
  
#print(like4(10000))      



arg1 = sys.argv[1]
arg2 = sys.argv[2]

if arg1 == 'reject':
    print("P(Rain) => " + str(reject1(int(arg2))))
    print("P(tired | not happy) => " + str(reject2(int(arg2),1,1)))
    print("P(happy | sunny) => " + str(reject3(int(arg2),1,1)))
    print("P(snow | happy, not tired) => " + str(reject4(int(arg2),1,1)))
if arg1 == 'like':
    print("P(Rain) => " + str(like1(int(arg2))))
    print("P(tired | not happy) => " + str(like2(int(arg2))))
    print("P(happy | sunny) => " + str(like3(int(arg2))))
    print("P(snow | happy, not tired) => " + str(like4(int(arg2))))

