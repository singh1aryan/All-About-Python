# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:36:00 2019

@author: Aryan Singh
"""

'''
Your code should output a single line of text, starting with “true” (the theorem was proved) or
“false”, followed by a space and a integer indicating the number of times the your code applied
the resolution rule while attempting to prove the theorem.
For example:
false 42

A V -B

we have the alpha and we negate it always
we then use the kb and then add alpha to it
we prove by contradiction always

we take c1 and c2, solve that to find c3 and do that recursively
R
-R V S

empty clause, resolution rule kills it
'''     

kb = []
alpha = ['-F']
def resolver(clauses):
    #clauses = KB.clauses + conjuncts(~alpha)
    c=0
    new = []
    while True:
        n = len(clauses)
        pairs = [(clauses[i],clauses[j]) for i in range(n) for j in range(i+1,n)]
        for (ci, cj) in pairs:
            resolvents = pl_resolve(ci, cj)# list of list
            # check if tautology or not
            if resolvents == 9:#if not resolved
                continue
            # check for tautologies
            # if there is a clause with i and -i, don't add it
            for res in resolvents:
                if len(res) == 0:
                    print(c)
                    return True
                if res not in new:
                    new.append(res)
                    c+=1
            
        # if new ⊆ clauses then return false
        m=0
        for i in new:
            if i in clauses:
                m+=1
        if m == len(new):
            print(c)
            return False
            
        # adding to clauses
        for i in new:
            if i not in clauses:
                clauses.append(i)
                
        # removing duplicates from clauses using set
        set(tuple(row) for row in clauses)
        clauses = [list(item) for item in set(tuple(row) for row in clauses)]    
        
    return clauses
    
    
def pl_resolve(ci, cj):
    ll = []
    c=0
    # if ci is p and cj has -p
    # ['-P','Q','R','S'],['P','Q','-R','-S']
    for i in range(0,len(ci)):
        rem = []
        if '-'+ci[i] in cj:
            c=1
            l=[]
            rem.append('-'+ci[i])#-r
            rem.append(ci[i])#r
            for j in ci:
                if j not in rem:
                    l.append(j)
            for j in cj:
                if j not in rem and j not in l:
                    l.append(j)
            if l not in ll:
                ll.append(l)
    
    for i in range(0,len(cj)):
        rem = []
        if '-'+cj[i] in ci:
            c=1
            l=[]
            rem.append('-'+cj[i])#-r
            rem.append(cj[i])#r
            for j in ci:
                if j not in rem:
                    l.append(j)
            for j in cj:
                if j not in rem and j not in l:
                    l.append(j)
            if l not in ll:
                ll.append(l)
            
              
    ''' 
    we check for the repititions as well
    ''' 
    if c == 0:
        return 9
    # removing duplicates from ll - list for the resolved clauses
    set(tuple(row) for row in ll)
    ll = [list(item) for item in set(tuple(row) for row in ll)]    
        
    return ll
            
    
with open('test2.txt') as f:
    #print(f.read())
    c=0
    cnf = ""
    lines = f.readlines();
    for i in lines:
        thisline = i.split();
        kb.append(thisline)
    cnf = cnf[0:len(cnf)-1]
    kb.append(alpha)
    print(resolver(kb)) 
   
'''
a = 'a'
print(a.split('-'))

[R] and [-R] - [R][]

print(pl_resolve(['R'],['Q','-R'])) # Q

print(pl_resolve(['-P','-R'],['Q','R']))# -P,Q

print(pl_resolve(['-P','R'],['Q','-R']))# -P, R

print(pl_resolve(['-P','Q'],['P','Q']))# Q

print(pl_resolve(['-P','-Q'],['P','Q']))# -Q , Q, do we return P -P here?

print(pl_resolve(['-P'],['P']))# []

print(pl_resolve(['-P','Q','R','S'],['P','Q','R','-S']))# gives 2

#print(pl_resolve(['-P','Q','-R','S'],['P','Q','R','-S']))# gives 3

'''
mat = [[1,2,3],[4,5,6],[1,2,3],[7,8,9],[4,5,6]]
set(tuple(row) for row in mat)
a = [list(item) for item in set(tuple(row) for row in mat)]
print(a)