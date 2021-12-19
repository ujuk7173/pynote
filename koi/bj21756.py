# 2021년 1차 초등부 1번 
# 지우개
n=int(input())
x=[item for item in range(1,n+1)]
while True:
    if len(x)==1:
        break
    del x[0:len(x):2]
print(x[0])