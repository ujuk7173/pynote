#비밀번호찾기
n, m = map(int, input().split())
# dictionary comprehension
d = { a:p for a,p in (input().split() for _ in range(n)) }
# d={}
# for _ in range(n):
#     a, p = input().split()
#     d[a] = p
for _ in range(m):
    print(d[input()])

