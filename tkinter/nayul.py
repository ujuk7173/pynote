from tkinter import *
from tkinter import ttk # 테마위젯
from tkinter import messagebox 

root = Tk()
root.title("my currency converter")
root.geometry("500x500")

# tab 생성
my_notebook = ttk.Notebok(root)
my_notebook.pack(pady=5)

# frame 생성
currency_frame = Frame(my_notebook, width=480,height=480) #화폐
conversion_frame = Frame(my_notebook, width=480,height=480) #환산
currency_frame.pack(fill="both", expand=1)
conversion_frame.pack(fill="both", expand=1)

# tab 더하기
my_notebook.add(currency_frame, text = "Currencies")
my_notebook.add(conversion_frame, text = "Convert")

# Disable the 2nd tab
my_notebook.tab(1, state="disabled")

##################
# 화폐 관련
##################
def lock():
	# 입력값이 없을 경우
	if not home_entry.get() or not conversion_entry.get() or not rate_entry.get():
		messagebox.showwarning("WARNING! 모두 입력하세요.")
	else: # 입력값이 모두 있는 경우
		# diable entry boxes
		home_entry.config(state="disabled")
		conversion_entryconfig(state="disabled")
		rate_entry.config(state="disabled")
		# enable tab
		my_notebook.tab(1,state="normal")
		# tab 값을 변경
		amount_label.config(text=f'Amount of {home_entry.get()} To convert To {conversion_entry.get()}')
		converted_label.config(text=f"Equals This Many {conversion_entry.get()}")
		convert_button.config(text=f"Convert From {home_entry.get()}")
		







##################
# 환산 관련
##################


# 마지막줄
root.mainloop()