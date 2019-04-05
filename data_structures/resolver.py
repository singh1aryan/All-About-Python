import itertools
import sys

kb = []
alpha = []
def resolver(clauses, alpha):
    for i in alpha:
        clauses.append(i)
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
                    print('true ' + str(c))
                    return True
                if res not in new:
                    new.append(res)
                    c+=1
            
        # if new clauses then return false
        m=0
        for i in new:
            if i in clauses:
                m+=1
        if m == len(new):
            print('false ' + str(c))
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
            
def negate_alpha(arr):
    l = []
    for i in range(0,len(arr)):
        if not arr[i].isalpha():# not a letter
           l.append(arr[i].split('-')[1])
        else:
            l.append('-'+arr[i])
    
    return l
# recursive
def dnf_cnf(a):
    return list(itertools.product(*a))

def clean(cnf):
    # lists of list - cnf
    a = []
    for i in range(0,len(cnf)):
        b = list(set(cnf[i]))# delete duplicates for all
        found = 0
        for k in b:
            if '-'+k in b:
                found = 1    
        if found == 0:
            a.append(b)
        
    return a
    
with open(sys.argv[2]) as f:
    #print(f.read())
    c=0
    dnf = []
    cnf = []
    lines = f.readlines()
    for i in lines:
        thisline = i.split()
        dnf.append(negate_alpha(thisline))
    
    dnf = dnf_cnf(dnf)
    for i in dnf:
        cnf.append(list(i))
    alpha = clean(cnf)
    
        
''' Reading the KB file '''
with open(sys.argv[1]) as f:
    lines = f.readlines();
    for i in lines:
        thisline = i.split();
        kb.append(thisline)
    resolver(kb,alpha)
