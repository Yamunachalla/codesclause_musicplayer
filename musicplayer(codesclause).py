import pygame
import tkinter
from tkinter.filedialog import askdirectory
import os

player = tkinter.Tk()
player.title("Music Player")
player.geometry("500x300+290+130")

var = tkinter.StringVar()
var.set("Select Your Song")

os.chdir(askdirectory())
songlist = os.listdir()

playing = tkinter.Listbox(player,font="Algerian 12",width=50,bg="light pink",fg="green",selectmode=tkinter.SINGLE)

for item in songlist:
    playing.insert(0,item)

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playing.get(tkinter.ACTIVE))
    name = playing.get(tkinter.ACTIVE)
    var.set(f"{name[:16]}..." if len(name)>18 else name)
    pygame.mixer.music.play()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()
def queue() :
    pygame.mixer.music.queue()

text = tkinter.Label(player,font="Algerian",textvariable=var).grid(row=0,columnspan=3)
playing.grid(columnspan=3)

playB = tkinter.Button(player,width=6,height=1,font="Helvetica",text="Play",command=play,bg="light blue").grid(row=2,column=0)
pauseB = tkinter.Button(player, width=6, height=1, font="Helvetica", text="Pause", command=pause, bg="light gray", fg="black").grid(row=2,column=1)
resumeB = tkinter.Button(player, width=8, height=1, font="Helvetica", text="Resume", command=resume, bg="light yellow", fg="black").grid(row=3,column=0)
queue1 = tkinter.Button(player, width=6, height=1, font="Helvetica", text="Queue", command=queue, bg="light green", fg="black").grid(row=3,column=1)

player.mainloop()








