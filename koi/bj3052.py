#나머
# solution1
lst=[]
for i in range(10):
    n = int(input())
    lst.append(n%42)
print(len(set(lst)))

# solution2
nlist = [int(input()) for i in range(0,10)]
nset = {nlist[i]%42 for i in range(len(nlist))}
print(len(nset))
