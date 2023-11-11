import tkinter as tk
import threading
import time
import random

root = tk.Tk()

texts = tk.Text(root ,height =20 ,width=45)
texts.pack()

letter = tk.Entry(root ,placeholder='Entre the letter')
letter.pack()
def check():
	n = 0
	text = texts.get("1.0",'end-1c')
	letters = letter.get()
	letterss = letters[0]
	
	for letters in text:
		if letters == letterss:
			n += 1
		else:
			pass
	label = tk.Label(text=f'The letter {letterss} has occured {n} times')
	label.pack()
	
check_btn = tk.Button(text='check',command=check)
check_btn.pack()


root.mainloop()