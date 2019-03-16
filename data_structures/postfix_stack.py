# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 22:15:32 2019

@author: Aryan Singh
"""

'''
A * B + C / D
Applications - Calculator

we push when we have numbers
pop and evaluate when there is a operator

Steps:-
    1.Create an empty stack called operandStack.
    2.Convert the string to a list by using the string method split.
    3.Scan the token list from left to right.
    4.If the token is an operand, convert it from a string to an integer 
    and push the value onto the operandStack.
    5.If the token is an operator, *, /, +, or -, it will need two operands. 
    Pop the operandStack twice. The first pop is the second operand and the 
    second pop is the first operand. Perform the arithmetic operation. 
    Push the result back on the operandStack.

When the input expression has been completely processed, 
the result is on the stack. Pop the operandStack and return 
the value.

'''

import queue 
stack = queue.LifoQueue(maxsize=20) 

def postfix(expression):
    token = expression.split()
    
    for tok in token:
        if tok in "0123456789":
            stack.put(int(tok))
        else:
            op2 = stack.get()
            op1 = stack.get()
            result = doMath(tok,op1,op2)
            stack.put(result)
    return stack.get()

def doMath(op, op2, op1):
    if op == '*':
        return op1*op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
    
    
print(postfix('7 8 + 3 2 + /')) # prints 0.333
print(postfix('2 3 +')) # prints 5
print(postfix('2 3 + 6 *'))    
    