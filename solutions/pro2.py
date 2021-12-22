# 체육복 -greedy
#solution1 
def solution(n, lost, reserve):
    u = [1] * (n + 2)  # initialize with 1
    for i in lost:
        u[i] -= 1
    for i in reserve:
        u[i] += 1
    for i in range(1, n + 1):
        if u[i-1] == 0 and u[i]==2:
            u[i - 1:i + 1] = [1, 1]
        elif u[i]==2 and u[i+1]==0:
            u[i:i + 1] = [1, 1]
    return len([x for x in u[1:-1] if x > 0])

print(solution(5,[2,4],[3]))
print(solution(3,[3],[1]))

# solution2 - set
def solution2(n, lost, reserve):
    s = set(list) & set(reserve)
    l = set(lost) - s
    r = set(reserve) - s
    for x in sorted(r):
        if x - 1 in l:
            l.remove(x - 1)
        elif x + 1 in l:
            l.remove(x + 1)
    return n - len(l)