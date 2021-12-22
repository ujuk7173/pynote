from tkinter import *
from tkinter import ttk
from tkinter import messagebox




root = Tk()
root.geometry("500x500")

# Create Tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)


# Create Two Frames
currency_frame = Frame(my_notebook, width=480, height=480)
conversion_frame = Frame(my_notebook, width=480, height=480)
login_frame = Frame(my_notebook, width=480, height=480)

currency_frame.pack(fill="both", expand=1)
conversion_frame.pack(fill="both", expand=1)
login_frame.pack(fill="both", expand=1)

# Add our Tabs
my_notebook.add(currency_frame, text="Currencies")
my_notebook.add(conversion_frame, text="Convert")
my_notebook.add(login_frame, text="Abby stuff")

# Disable 2nd tab
my_notebook.tab(1, state='disabled')

#######################
# CURRENCY STUFF
#######################
def lock():
	if not home_entry.get() or not conversion_entry.get() or not rate_entry.get():
		messagebox.showwarning("WARNING!", "You Didn't Fill Out All The Fields")
	else:
		# Disable entry boxes
		home_entry.config(state="disabled")
		conversion_entry.config(state="disabled")
		rate_entry.config(state="disabled")
		# Enable tab
		my_notebook.tab(1, state='normal')
		# Change Tab Field
		amount_label.config(text=f'Amount of {home_entry.get()} To Convert To {conversion_entry.get()}')
		converted_label.config(text=f'Equals This Many {conversion_entry.get()}')
		convert_button.config(text=f'Convert From {home_entry.get()}')
def unlock():
	# Enable entry boxes
	home_entry.config(state="normal")
	conversion_entry.config(state="normal")
	rate_entry.config(state="normal")
	# Disable Tab
	my_notebook.tab(1, state='disabled')
home = LabelFrame(currency_frame, text="Your Home Currency")
home.pack(pady=20)


# Home currency entry box
home_entry = Entry(home, font=("Helvetica", 24))
home_entry.pack(pady=10, padx=10)


# Conversion Currency Frame
conversion = LabelFrame(currency_frame, text="Conversion Currency")
conversion.pack(pady=20)

# convert to label
conversion_label = Label(conversion, text="Currency To Convert To...")
conversion_label.pack(pady=10)

# Convert To Entry
conversion_entry = Entry(conversion, font=("Helvetica", 24))
conversion_entry.pack(pady=10, padx=10)

# rate label
rate_label = Label(conversion, text="Current Conversion Rate...")
rate_label.pack(pady=10)

# Rate To Entry
rate_entry = Entry(conversion, font=("Helvetica", 24))
rate_entry.pack(pady=10, padx=10)

# Button Frame
button_frame = Frame(currency_frame)
button_frame.pack(pady=20)

# Create Buttons
lock_button = Button(button_frame, text="Lock", command=lock)
lock_button.grid(row=0, column=0, padx=10)

unlock_button = Button(button_frame, text="Unlock", command=unlock)
unlock_button.grid(row=0, column=1, padx=10)


#######################
# CONVERSION STUFF
#######################
def convert():
	# Clear Converted Entry Box
	converted_entry.delete(0, END)

	# Convert
	conversion = float(rate_entry.get()) * float(amount_entry.get())
	# Convert to two decimals
	conversion = round(conversion,2)
	# Add commas
	conversion = '{:,}'.format(conversion)
	# Upodate entry box
	converted_entry.insert(0, f'${conversion}')
def clear():
	amount_entry.delete(0, END)
	converted_entry.delete(0, END)

amount_label = LabelFrame(conversion_frame, text="Amount To Conver")
amount_label.pack(pady=20)

# Entry Box For Amount
amount_entry = Entry(amount_label, font=("Helvetica", 24))
amount_entry.pack(pady=10, padx=10)

# Convert Button
convert_button = Button(amount_label, text="Convert", command=convert)
convert_button.pack(pady=20)

# Equals Frame
converted_label = LabelFrame(conversion_frame, text="Converted Currency")
converted_label.pack(pady=20)

# Converted entry
converted_entry = Entry(converted_label, font=("Helvetica", 24), bd=0)
converted_entry.pack(pady=10, padx=10)

# Clear Button
clear_button = Button(conversion_frame, text="Clear", command=clear)
clear_button.pack(pady=20)

# Fake Label for spacing
spacer = Label(conversion_frame, text="", width=68)
spacer.pack()

##################
##### login #####
#################
def login():
	global message
	username = username_entry.get()
	password = password_entry.get()
	if username == 'abby' and password == '123':
		message.set("LOGIN SUCCESS")
	else:
		message.set("Wrong username or password!")

login_home = LabelFrame(login_frame, text="LOGIN HERE")
login_home.pack(pady=20)

# login entry - id
# convert to label
username_label = Label(login_home, text="ENTER USERNAME")
username_label.pack(pady=10)
username_entry = Entry(login_home, font=("Helvetica",24))
username_entry.pack(pady=10, padx=10)
# convert to label
password_label = Label(login_home, text="ENTER PASSWORD")
password_label.pack(pady=10)
password_entry = Entry(login_home, font=("Helvetica",24))
password_entry.pack(pady=10, padx=10)
# button
login_button = Button(login_home, text="LOGIN", command=login)
login_button.pack(pady=10, padx=10)
# label
message=StringVar()
result_label = Label(login_home, textvariable=message)
result_label.pack()

root.mainloop()