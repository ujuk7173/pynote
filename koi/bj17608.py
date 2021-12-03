# 막대기 (정올 초등부)
n = int(input())
stack = []
result = 1
for i in range(n):
    x = int(input())
    stack.append(x)
max = stack[-1]
for i in range(n-1, -1, -1):
    if stack[i] > max:
        result += 1
        max = stack[i]
print(result)