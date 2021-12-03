import sys
input = sys.stdin.readline

N = int(input())

all = list()

for _ in range(N):
    data = int(input())
    all.append(data)

count = 0
start = 0

for i in range(1, N+1):
    target = all[-i]
    if target > start:
        count += 1
        start = target

print(count)


# 첫번째 방법
import sys
input = sys.stdin.readline
 
n = int(input())
sticks = [int(input()) for _ in range(n)]
max_height = sticks[-1]
cnt = 1
 
for i in range(n):
    if max_height < sticks[n-i-1]:
        cnt += 1
        max_height = sticks[n-i-1]
print(cnt)



# 두번째 방법
import sys
input = sys.stdin.readline
 
n = int(input())
sticks = [int(input()) for _ in range(n)]
max_height = sticks[-1]
cnt = 1
 
for i in range(n):
    temp = sticks.pop()
    if max_height < temp:
        cnt += 1
        max_height = temp
print(cnt)