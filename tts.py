from gtts import gTTS
import os
from pygame import mixer
import tkinter as tk
from tkinter import messagebox
import time as tm
from kivymd.toast import toast

mixer.init()
root = tk.Tk()
mytext =tk.Text(root ,width=45,height= 20)
mytext.pack()

def speak():
	text = mytext.get("1.0",'end-1c')
	print(text)
	audio = gTTS(text=text, lang="en", slow=False)

	audio.save("sound.mp3")
	mixer.music.load(f'sound.mp3')
	mixer.music.play()
	os.remove(f'sound.mp3')
	save = messagebox.askyesno(title='save audio',message='Do you want to save audio')
	
	
	
	

	if save:
		time = int(tm.time())
		audio.save(f'{time}.mp3')
		toast(f'Audio saved as {time}.mp3')
	
	
start_btn = tk.Button(text='speak',command = lambda : speak())
start_btn.pack()

root.mainloop()
