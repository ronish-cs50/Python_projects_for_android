import tkinter as tk
import time as tm
import threading
from pygame import mixer
from tkinter import messagebox
screen = tk.Tk()


mixer.init()



time_entry = tk.Entry(screen,placeholder = 'Entre Time in minute')
time_entry.pack()
def start(time):
	time = float(time)
	tm.sleep(time)
	print('Times up')
	mixer.music.load('/storage/emulated/0/Documents/Pydroid3/mixkit-arcade-retro-game-over-213.wav')
	mixer.music.play()
	messagebox.showinfo("Timer", "Times up") 


	
	
def start_timer():
	time  = float(time_entry.get()) * 60
	threading.Thread(target=start,args=[time]).start()
start_btn = tk.Button(screen,text='Start',command=start_timer)
start_btn.pack()


screen.mainloop()