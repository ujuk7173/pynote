

# 문자열 연습
#1 첫번째, 두번째, 마지막 글자만 출력
str = "It's always darkest before dawn."
result = str[0] + str[1] + str[-1]
print(result)

# 2 (.)을 (!)로 바꾸시오
str = "It's always darkest before dawn."
str = str.replace('.','!')
print(str)

#3
str = "EVERY Strike Brings Me Closer to the Next Home run."
str = str.lower() #소문자로 바꾸기
print(str)

#4
str = "EVERY Strike Brings Me Closer to the Next Home run."
str = str.upper()
print(str)

#5 단어의 첫글자만 대문자로 만들기
str = "It's always darkest before dawn."
str = str.capitalize()

#6 'A'로 시작하는지 확인하여 bool타입의 변수에 저장
print(type(True)) 
str = "There are no traffic jams."
result = str.startswith("A")
print(result)

#7
str = "There are no traffic jams."
result = str.endswith('.')
print(result)

#8 어떤 글자의 인덱스 알아내기, 없다면 에러
str = "There are no traffic jams. h h h"
result = str.index('h')
print(result)

#9 어떤 글자의 익덱스 알아내기, 없다면 -1 반환하기
str = "There are no traffic jams. h h h"
result = str.find("z")
print(result)

#10 글자가 몇개인지 세기
str = "People often say that motivation doesn't last."
res1 = str.count("a")
res2 = str.count("p")
print(res1, res2)

#11 문자열의 형식과 길이 알아내기
str = "1.975.000"
res1 = len(str)
print(res1)
res2 = type(str)
print(res2)