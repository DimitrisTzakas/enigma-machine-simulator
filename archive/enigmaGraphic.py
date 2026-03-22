from Tkinter import *
from pip import *

#set main window
WIDTH=500
HEIGHT=720
root=Tk()
root.resizable(False, False)
root.wm_title("Enigma")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# calculate position x and y coordinates
x = (screen_width/2) - (WIDTH/2)
y = (screen_height/2) - (HEIGHT/2)
root.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y))
#end setting main window

frameSettings = Frame(root,width=500, height=160,bg="red")
frameSettings.grid(row=0)
frameLightboard = Frame(root,width=500, height=200,bg="green")
frameLightboard.grid(row=1)
frameKeyboard = Frame(root,width=500, height=200,bg="blue")
frameKeyboard.grid(row=2)
framePlugboard = Frame(root,width=500, height=130,bg="yellow")
framePlugboard.grid(row=3)
frameOutText = Frame(root,width=500, height=30,bg="white")
frameOutText.grid(row=4)



ring1ButtonUp=Button(frameSettings)
ring1ButtonDown=Button(frameSettings)
ring1ButtonUp.place(x=30,y=30)

ring2ButtonUp=Button(frameSettings)
ring2ButtonDown=Button(frameSettings)
ring3ButtonUp=Button(frameSettings)
ring3ButtonDown=Button(frameSettings)

root.mainloop()
