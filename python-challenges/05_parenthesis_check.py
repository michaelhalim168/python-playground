def check_parenthesis(parenthesis):
    stack = []
    for i in parenthesis:
        if i == "(":
            stack.append(i)
        elif i == ")":
            try: 
                stack.pop()
            except:
                return False
    return not stack

print(check_parenthesis('(()((())()))'))


