# 슬라이싱 연습
# 1번 python에서 h 까지만 출력하기
word = "python" #pyth
answer = word[0:4]
print(answer)
answer2 = word[:4]
print(answer2)
answer3 = word[:-2]
print(answer3)
# "on"만 출력하기
answer = word[4:]
print(answer)
answer = word[-2:]
print(answer)

#2번 2칸 간격(steps)으로 출력하기
word = "python" #pto
ans = word[::2] #[시작점:끝점:간격]
print(ans)
# 3칸 간격
print(word[::3]) #py


# 3번: 거꾸로 출력하기
lst = [0,1,2,3,4]
print(lst)
print(lst[::-1]) #step
# 1,3 만 출력
ans = lst[1:4:2]
print(ans)
print(lst[::-2])


