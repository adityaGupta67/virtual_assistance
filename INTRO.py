from tkinter import *
from PIL import Image,ImageTk,ImageSequence
import time
import pygame 
from pygame import mixer
mixer.init()

root=Tk()
root.geometry("500x500")

def play_gif():
     root.lift()
     root.attributes("-topmost", True)
     global img
     img = Image.open("luffy.gif.gif")
     lbl = Label(root)
     lbl.place(x=0,y=0)
     i= 0
     mixer.music.load("luffyvoice.mp3")
     mixer.music.play()
     
     for img in ImageSequence.Iterator(img):
          img = img.resize((500,500))
          img = ImageTk.PhotoImage(img)
          lbl.config(image=img)
          root.update()
          time.sleep(0.05)
     root.destroy()  
play_gif()
root.mainloop()  

