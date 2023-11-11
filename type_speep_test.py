import tkinter as tk
import time as tm
import threading

screen = tk.Tk()
def timer():
	tm.sleep(60)
	text = texts.get("1.0",'end-1c')
	texts.destroy()
	n = 0
	for letter in text:
		n += 1
	print(f'{n}/m')
	global k
	k = tk.Label(text=f'{n}/m')
	k.pack()
def start():
	try:
		k.destroy()
	except:
		pass
	global texts
	texts = tk.Text(screen ,height =20 ,width=45)
	texts.pack()
	
	threading.Thread(target=timer).start()
	
	
start_btn = tk.Button(text='Start' ,command = start)
start_btn.pack()


screen.mainloop()



