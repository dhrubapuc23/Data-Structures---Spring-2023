# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 11:49:22 2023

@author: User
"""



def push(val,S):
    S.append(val)
    #print('After push operation', S)
    
def pop(S):
    S_size = len(S)
    if S_size == 0:
        print('Stack is empty')
    else:
        item = S.pop()
        #print('Deleted item: ',item)
        #print('After pop operation: ',S)
    return item

def infix_to_postfix(S,string):
    op = ['+','-','*','/']
    P = {'+':1,'-':1,'*':2,'/':2}
    B = ['(',')']
    exp = ''
    
    for i in string:
        if i not in op and i not in B:
            exp = exp + i   
        elif i == '(':
            push(i,S)
        elif i == ')':
            while S and S[-1] != '(':
                exp = exp + pop(S)
            pop(S)
        else:
            while S and S[-1] != '(' and P[i] < P[S[-1]]:
                exp = exp + pop(S)
            push(i,S)
    while stack:
        exp = exp + pop(S)
    print(evaluate_postfix(S,exp))

def evaluate_postfix(S,string):
    op = ['+','-','*','/']
    for i in string:
        if i not in op:
            push(i,S)
        else:
            a = pop(S)
            b = pop(S)
            if i == '+':
                res = int(a)+int(b)
                push(res,S)
            if i == '-':
                res = int(a)-int(b)
                push(res,S)
            if i == '*':
                res = int(a)*int(b)
                push(res,S)
            if i == '/':
                res = int(a)/int(b)
                push(res,S)                
    return S
                
stack = []
string = "6+(5*9)"
infix_to_postfix(stack,string)
#evaluate_postfix(stack,string)
# =============================================================================
# push(5,stack)
# push(10,stack)
# push(15,stack)
# pop(stack)
# =============================================================================
    
    
    
    
    
    
    
    
    
    