# color game
# 모듈
import tkinter
import random

# 색깔 리스트
colors = ['Red','Blue','Green','Pink','Black','Yellow', 'Orange','White','Purple','Brown']
# 점수
score = 0
# 타이머, 시간제한
timeleft = 30
# 함수: 게임 시작
def startGame(event):
	if timeleft == 30:
		countdown()
	# 다음 색깔 선택
	nextColor()

# 함수: 다음 색깔 보여주기
def nextColor():
	# 전역변수, global variables 선언
	global score
	global timeleft
	# 게임 실행 중이라면
	if timeleft > 0:
		e.focus_set() # 텍스트 entry 박스를 활성화
		# 정답이라면
		if e.get().lower() == colors[1].lower():
			score = score + 1
		# entry 상자 비우기
		e.delete(0, tkinter.END)
		
		random.shuffle(colors)

		#글자의 색깔을 설정
		# colors리스트의 원소를 사용
		label.config(fg = str(colors[1]), text = str(colors[0]))

		# 점수 업데이트
		scoreLabel.config(text="Score: "+str(score))
	
	# 카운트다운 타이머 함수
	def countdown():
		global timeleft
		# 게임 실행 중이라면
		if timeleft > 0:
			timeleft = timeleft - 1 # 타이머 숫자 감소
			# 남은 시간 라벨 업데이트
			timeLabel.config(text="Time left: "+str(timeleft))
			# 1초마다 함수 실행
			timeLabel.after(1000, countdown)

# driver code

# GUI 윈도우 생성
root = tkinter.Tk()
root.title("COLOR GAME")
root.geometry("375x200")

# 설명 라벨 생성
instructions = tkinter.Label(root, text="Type in the color\nof the words, and not the word text!", font = ('Helvetica',12))
instructions.pack()
# 점수 라벨 생성
scoreLabel = tkinter.Label(root, text = "Press enter to start", font=('Helvetica',12))
scoreLabel.pack()
# 남은 시간 라벨 생성
timeLabel = tkinter.Label(root, text="Time left: "+str(timeleft),font=('Helvetica',12))
timeLabel.pack()
# 색깔 이름 라벨 생성
label = tkinter.Label(root, font=('Helvetica',60))
label.pack()
# 입력하는 entry 상장 생성
e = tkinter.Entry(root)
# 엔터키를 누르면 startGame 함수 실행
root.bind('<Return>',startGame)
e.pack()
# 엔트리 상자에 포커스 두기
e.focus_set()

# 시작
root.mainloop()