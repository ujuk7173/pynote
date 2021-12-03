# 괄호
t = int(input())
stack = []
for i in range(t):
    p = input()
    if p == "(":
        stack.append(p)
    else:
        stack.pop()
