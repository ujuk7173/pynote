# bj ATM: 11399

n = int(input())
s = list(map(int, input().split()))
cnt = 0
s.sort()
for i in range(n):
    for j in range(i + 1):
        cnt += s[j]
print(cnt)
