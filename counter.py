import threading
import tkinter as tk
import time as tm
import threading
from pygame import mixer



time = []
screen = tk.Tk()
def time_increaser(n,hour,second,minute):

	while True:
		tm.sleep(1)
		second += 1
		if second == 60:
			second -= 60
			minute += 1
		if minute == 60:
			minute -= 60
			hour += 1
			
			
		time[n].config(text=f'{hour}:{minute}:{second}')
		
		
		

def start():

	global time
	global n
	hour = 0
	minute = 0
	second = 0
	times = tk.Label(text=f'{hour}:{minute}:{second}')
	times.pack()
	time.append(times)
	time_increase = threading.	Thread(target=time_increaser,args = [n,hour,second,minute])
	time_increase.start()
	
	n += 1
n = 0
start_btn = tk.Button(text='start',command=start)
start_btn.pack()

screen.mainloop()