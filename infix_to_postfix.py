print("Welcome to the Infix to Postfix conversion by the use of Stacks concept \n The output will be a list")
operators  = {"+": 1, "-": 1, "*": 2, "/": 2,  "%": 2, "^": 3}

parenthesis = ["(", ")"]

def infix_to_postfix(infix):
    stack = []
    postfix = []

    for c in infix:
        if c in operators:

            if len(stack) > 0:                
                top = stack[-1]

                if top in operators.keys():
                    if operators[c] > operators[top]:
                        stack.append(c)
                    else:
                        while top in operators.keys() and operators[top] >= operators[c]:
                            op = stack.pop()
                            postfix.append(op)

                            if len(stack) > 0:
                                top = stack[-1]
                            else:
                                break
                        stack.append(c)
                else:
                    stack.append(c)
            else:
                stack.append(c)

        elif c in parenthesis:

            if c == ")":
                if len(stack) > 0:
                    top = stack[-1]

                    while top != "(":
                        try:
                            r = stack.pop()
                            postfix.append(r)
                            top = stack[-1]
                        except IndexError:
                            raise ValueError(" '(' not found when popping")

                    stack.pop() 
                else:
                    raise ValueError(" ')' cannot be added to the stack if it is empty") 
            else:
                stack.append(c)
        else:

            postfix.append(c)

        #print("Stack:", stack)
        #print("Postfix:", postfix)

    while len(stack) > 0:
        top = stack.pop()

        if top in operators.keys():
            postfix.append(top)

    return postfix
infix = input("Enter an infix expression to be converted into postfix : ")
print(infix_to_postfix(infix))


