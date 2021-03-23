from __future__ import division
import random


OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRIORITY = {'+':1, '-':1, '*':2, '/':2}

def infix_to_postfix(formula):
    stack = []  
    output = ''
    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop() 
        else:
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
   
    while stack: output += stack.pop()
    print(output)
    return output

def evaluate_postfix(formula):
    stack = []
    for ch in formula:
        if ch not in OPERATORS:
            stack.append(float(ch))
        else:
            b = stack.pop()
            a = stack.pop()
            c = {'+':a+b, '-':a-b, '*':a*b, '/':a/b}[ch]
            stack.append(c)
    print(stack[-1])
    return stack[-1]

if __name__ == '__main__':
    infix_to_postfix('1+(3+4*6+6*1)*2/3')
    print(evaluate_postfix('1346*+61*+2*3/+'))
    
