# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 19:08:44 2019

@author: Aryan Singh
"""

# question - merge 2 sorted linked lists

def merged_list(listA, listB):
    newList = list()
    a=0
    b=0
    
    while a<len(listA) and b<len(listB):
        if listA[a]<listB[b]:
            newList.append(listA[a])
            a+=1
        else:
            newList.append(listB[b])
            b+=1
    
    while a<len(listA):
        newList.append(listA[a])
        a+=1
    
    while b<len(listB):
        newList.append(listB[b])
        b+=1
    
    return newList

lista = [1,2,3,4];
listb = [2,3,4,5];
l = merged_list(lista,listb)
print(l)
    