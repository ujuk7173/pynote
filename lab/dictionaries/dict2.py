# 딕셔너리 연습문제
# 1번: 플라토가 태어난 곳은?
t = {"name":"Plato" ,"country":"Ancient Greece", "born":-427,"teacher":"Socrates", "student":"Aristotle"}
print(t["country"])
# 2번: 플라토의 출생년도를 -427 에서 -428로 바꾼 다음에 출력하시오
t["born"] = -428
print(t["born"])
# 3번: "work":["Apology","Republic","Symposium"] 새로운 키와 값를 더하시오
t["work"]=["Apology","Replublic","Symposium"]
print(t)
# 4번: son's height 2센티를 더하고 출력해라
dict = {"son's name": "Lucas","son's height":170,"son's eyes":"green"}
#dict["son's height"] = dict["son's height"] + 2
dict["son's height"] += 2
print(dict)
# 5번: 모든 키-값을 튜플로 프린트하시오
print(dict.items())
# 6번: get() 메소드를 사용해서 son's eyes의 값을 프린트해라
color = dict.get("son's eye color") #none
print(color)
# color2 = dict["son's eye color"]
# print(color2)
# 7번: 그 키가 없다면 특정 값을 출력해
ans = dict.get("sos's age",2)
print(ans)
# 8번: clear메소드
dict.clear()
print(dict)
# 9번: len() 함수
ans = len(dict)
print(ans)
# 10번: 제일 큰 값을 찾아내는 함수  max
dict = {"a":1,"b":3,"c":20}
ans = max(dict)
print(ans)
print(min(dict))






