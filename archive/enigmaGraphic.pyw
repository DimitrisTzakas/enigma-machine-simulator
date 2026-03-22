from Tkinter import *
from pip import *

#set main window
WIDTH=500
HEIGHT=720
root=Tk()
root.resizable(False, False)
root.wm_title("Enigma I - WEHRMACHT BY 1ο ΕΠΑΛ ΜΟΛΑΩΝ")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# calculate position x and y coordinates
x = (screen_width/2) - (WIDTH/2)
y = (screen_height/2) - (HEIGHT/2)
root.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y))
#end setting main window

frameSettings = Frame(root,width=500, height=200,bg="black")
frameSettings.grid(row=0)
frameLightboard = Frame(root,width=500, height=180,bg="green")
frameLightboard.grid(row=1)
frameKeyboard = Frame(root,width=500, height=180,bg="blue")
frameKeyboard.grid(row=2)
framePlugboard = Frame(root,width=500, height=130,bg="yellow")
framePlugboard.grid(row=3)
frameOutText = Frame(root,width=500, height=30,bg="white")
frameOutText.grid(row=4)


def ringButtonAction(sender):
    if sender=='ring1Down':
        print 'ok'


def placeRingControls():
    #ring1
    ring1ButtonUp=Button(frameSettings,name='ring1Up',text='▲',width=3,padx=2,command=lambda :ringButtonAction('ring1Up'))
    ring1ButtonUp.place(x=30,y=60)
    ring1Label=Label(frameSettings, text='14',bg='grey',font='bold',width=3,relief="sunken",borderwidth=2)
    ring1Label.place(x=30, y=90)
    ring1ButtonDown=Button(frameSettings,name='ring1Down',text='▼',width=3,padx=2,command=lambda :ringButtonAction('ring1Down'))
    ring1ButtonDown.place(x=30,y=120)
    #ring2
    ring2ButtonUp=Button(frameSettings,name='ring2Up',text='▲',width=3,padx=2)
    ring2ButtonUp.place(x=65,y=60)
    ring2Label=Label(frameSettings, text='14',bg='grey',font='bold',width=3,relief="sunken",borderwidth=2)
    ring2Label.place(x=65, y=90)
    ring2ButtonDown=Button(frameSettings,name='ring2Down',text='▼',width=3,padx=2)
    ring2ButtonDown.place(x=65,y=120)
    #ring3
    ring3ButtonUp=Button(frameSettings,text='▲',width=3,padx=2)
    ring3ButtonUp.place(x=100,y=60)
    ring3Label=Label(frameSettings, text='14',bg='grey',font='bold',width=3,relief="sunken",borderwidth=2)
    ring3Label.place(x=100, y=90)
    ring3ButtonDown=Button(frameSettings,text='▼',width=3,padx=2)
    ring3ButtonDown.place(x=100,y=120)

def placeRotorControls():
    #ring1
    ring1ButtonUp=Button(frameSettings,text='▲',width=3)
    ring1ButtonUp.place(x=31,y=50)
    ring1Label=Label(frameSettings, text='14',bg='grey',font='bold',width=3,relief="sunken",borderwidth=2)
    ring1Label.place(x=30, y=80)
    ring1ButtonDown=Button(frameSettings,text='▼',width=3)
    ring1ButtonDown.place(x=31,y=110)
    #ring2
    ring2ButtonUp=Button(frameSettings,text='▲',width=3)
    ring2ButtonUp.place(x=66,y=50)
    ring2Label=Label(frameSettings, text='14',bg='grey',font='bold',width=3,relief="sunken",borderwidth=2)
    ring2Label.place(x=65, y=80)
    ring2ButtonDown=Button(frameSettings,text='▼',width=3)
    ring2ButtonDown.place(x=66,y=110)
    #ring2
    ring2Label=Label(frameSettings, text='14',bg='grey',font='bold',width=3,relief="sunken",borderwidth=2)
    ring2Label.place(x=65, y=80)
    ring2ButtonUp=Button(frameSettings,text='▲',width=3)
    ring2ButtonUp.place(x=67,y=50)
    ring2ButtonDown=Button(frameSettings,text='▼',width=3)
    ring2ButtonDown.place(x=67,y=110)
    
placeRingControls()
root.mainloop()
