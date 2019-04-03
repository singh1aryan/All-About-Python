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
'''     

kb = []
alpha = ['-S']
def resolver(clauses):
    #clauses = KB.clauses + conjuncts(~alpha)
    c=0
    new = set()
    while True:
        n = len(clauses)
        pairs = [(clauses[i],clauses[j]) for i in range(n) for j in range(i+1,n)]
        for (ci, cj) in pairs:
            resolvents = pl_resolve(ci, cj)
            # if we have the empty clause in resolvents, return true
            
            if False in resolvents: return True
            new.union_update(set(resolvents))
        if new.issubset(set(clauses)): return False
        for c in new:
            if c not in clauses: 
                clauses.append(c)
    
    
def pl_resolve(ci, cj):
    l = []
    rem = []
    c=0
    # if ci is p and cj has -p
    for i in range(0,len(ci)):
        if '-'+ci[i] in cj:
            c=1
            rem.append(ci[i])
            rem.append('-'+ci[i])
            # if ci is -p and cj has p
        if len(ci[i].split('-')) > 1:
            s = ci[i].split('-')
            if s[1] in cj:
                c=1
                rem.append(s[1])
                rem.append('-'+s[1])
                
    if c==1:
        for i in range(0,len(ci)):
            if ci[i] not in rem:
                l.append(ci[i])
                
        for i in range(0,len(cj)):
            if cj[i] not in rem:
                l.append(cj[i])
                
    return l
            
    
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
    resolver(kb)
    print(kb) 
   
'''
a = 'a'
print(a.split('-'))
'''
print(pl_resolve(['-P','-R'],['Q','R']))
print(pl_resolve(['-P','R'],['Q','-R']))