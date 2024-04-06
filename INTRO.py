from tkinter import *
from PIL import Image,ImageTk,ImageSequence
import time
import pygame 
from pygame import mixer
mixer.init()

root=Tk()
root.geometry("1500x500")

def play_gif():
     root.lift()
     root.attributes("-topmost", True)
     global img
     img = Image.open("luffy.gif")
     lbl = Label(root)
     lbl.place(x=0,y=0)
     i= 0
     
     for img in ImageSequence.Iterator(img):
          img = img.resize((1500,500))
          img - ImageTk.PhotoImage(img)
          lbl.config(img=img)
          root.update()
          time.sleep(1.0)
     root.destroy()  
play_gif()
root.mainloop()  

