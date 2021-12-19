# 369
n = int(input())
count = 0
for i in range(1,n+1):
    str_n = str(i)
    if '3' in str_n:
        count += str_n.count('3')
    if '6' in str_n:
        count+= str_n.count('6')
    if '9' in str_n:
        count+= str_n.count('9')
print(count)