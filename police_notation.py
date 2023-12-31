# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 11:36:55 2023

@author: User
"""
def push_st(S,val):
    S.append(val)
    print('After Push operation, Stack: ',S)

def pop_st(S):
    N  = len(S)
    if N == 0:
        print('Stack underflow!')
        return
    else:
        print('Deleted item: ',S[-1])
        S.pop()
    print('After Pop operation, Stack: ',S)
    
def top_st(S):
    if S:  
        print('Top of stack: ',S[-1])
    else:
        print('Stack is empty!')

def reverse_st(name):
    st = []
    result = ''
    for ch in name:
        st.append(ch)
    while st:
        result = result + st.pop()
    print(result)
    
def infix_to_postfix(exp):
    operators = ['+', '-', '*', '/', '**','(',')']
    pr = {'**':3, '*':2, '/':2, '+':1,'-':1}
    result = ''
    stack = []
    for ch in exp:
        if ch not in operators:
            result = result + ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                result = result + stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and pr[ch] <= pr[stack[-1]]:
                result = result + stack.pop()
            stack.append(ch)
    while stack:
        result = result + stack.pop()
    return result
 
def evaluate_postfix(exp):
    operators = ['+', '-', '*', '/', '**','(',')']
    stack = []
    for i in exp:
        if i not in operators:
            stack.append(i)
        else:
            m = int(stack.pop())
            n = int(stack.pop())
            if i == '+':
                result = m + n
            elif i == '-':
                result = m - n
            elif i == '*':
                result = m * n
            elif i == '/':
                result = n // m
            elif i == '**':
                result = m ** n
            stack.append(result)
    return stack.pop()

    
    
exp = "(6+5)*9"
exp2 = infix_to_postfix(exp)
print(exp2)
print(evaluate_postfix(exp2))   
    
    
    
    

# =============================================================================
# name = "Hello World"
# reverse_st(name)
# =============================================================================
# =============================================================================
# S = []
# push_st(S, 10)
# push_st(S, 20)
# push_st(S, 30)
# push_st(S, 40)
# pop_st(S)
# pop_st(S)
# pop_st(S)
# pop_st(S)
# pop_st(S)
# =============================================================================


