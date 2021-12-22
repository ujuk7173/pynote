# 회사에있는사람 (백준7785)
n = int(input())
dict = {} # 빈 딕셔너리 생성
# n개의 기록 입력받기
for i in range(n):
	name, el = input().split() # baha enter
	if el == 'enter':
		dict[name] = 1 # baha 1
	else:
		dict[name] = 0
lst = []
for key, value in dict.items():
	if value == 1:
		lst.append(key)
# 역순으로 정렬
lst.sort(reverse=True)
for i in lst:
	print(i)
