import math
import csv
import pandas as pd

examples = []
attr = []
with open('congress_train.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    i=0
    for row in csv_reader:
        if i<72:
            examples.append(row)
            i+=1
    attr = examples[0]

# divide it w yes and no, count the r and d, find entropy
def information_gain(attr, examples):
    tlisty = []
    tlistx = []
    rem = 0
    
    df = pd.read_csv('congress_train.csv')
    orig_entropy = original_entropy()
        
    li = df['vote21']
    for i in range(0,72):
        if li[i] == 'Yea':
            tlisty.append(tuple((i, examples[i][42])))
        else:
            tlistx.append(tuple((i, examples[i][42])))
    
    propx = len(tlistx)/(len(tlistx)+len(tlisty))
    propy = len(tlistx)/(len(tlistx)+len(tlisty))
    
    rem += findRD(tlistx)*propx
    rem += findRD(tlisty)*propy
    
    #print(rem)
    info_gain = orig_entropy - rem
    print(info_gain)
    
        
def entropy(p):
        return -1*(p*math.log(p,2) + (1-p)*math.log(1-p,2))

def original_entropy():
    d=0
    r=0
    df = pd.read_csv('congress_train.csv')
    l2 = df['class']
    for i in range(0,72):
        if l2[i] == 'Democrat':
            d+=1
        else:
            r+=1
    return entropy(r/(r+d))


def findRD(tup):
    r=0
    d=0
    for i in tup:
        if i[1] == 'Democrat':
            d+=1
        else:
            r+=1
    return entropy(r/(r+d))

information_gain(attr, examples)