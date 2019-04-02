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
from utils import *
Expr = []
_NaryExprTable = {'&':TRUE, '|':FALSE, '+':ZERO, '*':ONE}
def NaryExpr(op, *args):
    """Create an Expr, but with an nary, associative op, so we can promote
    nested instances of the same op up to the top level.
    >>> NaryExpr('&', (A&B),(B|C),(B&C))
    (A & B & (B | C) & B & C)
    """
    arglist = []
    for arg in args:
        if arg.op == op: arglist.extend(arg.args)
        else: arglist.append(arg)
    if len(args) == 1:
        return args[0]
    elif len(args) == 0:
        return _NaryExprTable[op]
    else:
        return Expr(op, *arglist)
    
def conjuncts(s):
    """Return a list of the conjuncts in the sentence s.
    >>> conjuncts(A & B)
    [A, B]
    >>> conjuncts(A | B)
    [(A | B)]
    """
    if isinstance(s, Expr) and s.op == '&':
        return s.args
    else:
        return [s]
    
def disjuncts(s):
    """Return a list of the disjuncts in the sentence s.
    >>> disjuncts(A | B)
    [A, B]
    >>> disjuncts(A & B)
    [(A & B)]
    """
    if isinstance(s, Expr) and s.op == '|':
        return s.args
    else:
        return [s]
    
def pl_resolve(ci,cj):
    clauses = []
    for di in disjuncts(ci):
        for dj in disjuncts(cj):
            if di == ~dj or ~di == dj:
                dnew = unique(removeall(di, disjuncts(ci)) + removeall(dj, disjuncts(cj)))
                clauses.append(NaryExpr('|', *dnew))
    return clauses

def resolver(KB, alpha):
    clauses = KB.clauses + conjuncts(~alpha)
    new = set()
    while True:
        n = len(clauses)
        pairs = [(clauses[i],clauses[j]) for i in range(n) for j in range(i+1,n)]
        for (ci, cj) in pairs:
            resolvents = pl_resolve(ci, cj)
            if False in resolvents: return True
            new.union_update(set(resolvents))
        if new.issubset(set(clauses)): return False
        for c in new:
            if c not in clauses: clauses.append(c)
        


# & - and, | for union, ~ for negate
# Example is ~(A|B) -- ~A & ~B
def negate(alpha):
    # we have to pass in the ~
    newl = []
    i=0
    while True:
        if alpha[i] == '~':
            newl.append('~')
            if alpha[i+1] == '(':# enter inside parenthesis
                newl.append('(')
                newl.append('~')
            else:
                newl.append('')
                
        
            