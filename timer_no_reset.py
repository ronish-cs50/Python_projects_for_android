import tkinter as tk
import time as tm
import threading
global second
second = 0

root = tk.Tk()

time = tk.Label(text=f"")
time.pack()

def label(second):
	time.config(text=f'{second} seconds has passed')
		
	
	
	tm.sleep(1)
		
	
	second += 1

	
	label(second)
threading.Thread(target=label ,args = [0]).start()

root.mainloop()
