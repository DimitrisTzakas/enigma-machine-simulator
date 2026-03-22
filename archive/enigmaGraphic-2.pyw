import enigma
from Tkinter import *
from tkFont import Font
from winsound import PlaySound
import wckToolTips
#set main window
WIDTH=500
HEIGHT=720
root=Tk()
root.resizable(False, False)
root.wm_title("Enigma I - WEHRMACHT BY 1ο ΕΠΑΛ ΜΟΛΑΩΝ")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (WIDTH/2)
y = (screen_height/2) - (HEIGHT/2)
root.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y))
#end setting main window
frameLogo=Frame(root,width=500, height=100,bg="black")
frameLogo.grid(row=0)
frameSettings = Frame(root,width=500, height=170,bg="black")
frameSettings.grid(row=1)
frameLightboard = Frame(root,width=500, height=160,bg="green")
frameLightboard.grid(row=2)
frameKeyboard = Frame(root,width=500, height=160,bg="blue")
frameKeyboard.grid(row=3)
framePlugboard = Frame(root,width=500, height=100,bg="yellow")
framePlugboard.grid(row=4)
frameOutText = Frame(root,width=500, height=30,bg="white")
frameOutText.grid(row=5)
#place logo
img = PhotoImage(file = "enigmaLogo.gif")
logoLabel=Label(frameLogo,width=496, height=100,image=img,bg='black')
logoLabel.grid()

rFont=Font(size=20)

def ringButtonAction(ring,arrow):
    PlaySound('tick.wav',0)
    if arrow=='▲':
        enigma.setRotorsRing(ring,1)
        ringLabel[ring]['text']=str(int(ringLabel[ring].cget("text")) % 26 + 1)
    elif arrow== '▼':
        enigma.setRotorsRing(ring,-1)
        ringLabel[ring]['text']=str(int(ringLabel[ring].cget("text"))-1)
        if ringLabel[ring].cget("text")=='0': ringLabel[ring]['text']='26'
    if len(ringLabel[ring].cget("text"))==1:
        ringLabel[ring]['text']='0'+ringLabel[ring].cget("text")  # keep 2 digits on ring labels

def placeRingControls():
    global ringLabel
    ringButtonUp=[None]*3
    ringLabel=[None]*3
    ringButtonDown=[None]*3
    rButtonFont=Font(size=6)
    rLabelFont=Font(size=8,weight='bold')
    for k in range(3):
        ringButtonUp[k]=Button(frameSettings,text='▲',font=rButtonFont,width=3,padx=2,command=lambda x=k:ringButtonAction(x,'▲'))
        ringButtonUp[k].place(x=40+k*35,y=60)
        ringLabel[k]=Label(frameSettings, text='01',bg='grey',font=rLabelFont,width=3,relief="sunken",borderwidth=2)
        ringLabel[k].place(x=40+k*35, y=80)
        ringButtonDown[k]=Button(frameSettings,text='▼',font=rButtonFont,width=3,padx=2,command=lambda x=k:ringButtonAction(x,'▼'))
        ringButtonDown[k].place(x=40+k*35,y=103)
    for i in range(3): wckToolTips.register(ringLabel[i], "01-A 02-B 03-C 04-D 05-E 06-F 07-G 08-H") 

def placeRotorControls():
    rotorButtonUp=[None]*3
    rotorLabel=[None]*3
    rotorButtonDown=[None]*3
    for k in range(3):
        rotorButtonUp[k]=Button(frameSettings,text='▲',width=3,padx=2,command=lambda x=k:ringButtonAction(x,'▲'))
        rotorButtonUp[k].place(x=200+k*35,y=60)
        rotorLabel[k]=Label(frameSettings, text='A',bg='grey',font=rFont,width=2,relief="sunken",borderwidth=2)
        rotorLabel[k].place(x=200+k*45, y=90)
        rotorButtonDown[k]=Button(frameSettings,text='▼',width=3,padx=2,command=lambda x=k:ringButtonAction(x,'▼'))
        rotorButtonDown[k].place(x=200+k*35,y=120)

def placeRotorSelection():
    rotorSelectionButtonUp=[None]*3
    rotorSelectionLabel=[None]*3
    rotorSelectionButtonDown=[None]*3
    rButtonFont=Font(size=6)
    rLabelFont=Font(size=8,weight='bold')
    for k in range(3):
        rotorSelectionButtonUp[k]=Button(frameSettings,text='▲',font=rButtonFont,width=3,padx=2,command=lambda x=k:ringButtonAction(x,'▲'))
        rotorSelectionButtonUp[k].place(x=380+k*35,y=60)
        rotorSelectionLabel[k]=Label(frameSettings, text='01',bg='grey',font=rLabelFont,width=3,relief="sunken",borderwidth=2)
        rotorSelectionLabel[k].place(x=380+k*35, y=90)
        rotorSelectionButtonDown[k]=Button(frameSettings,text='▼',font=rButtonFont,width=3,padx=2,command=lambda x=k:ringButtonAction(x,'▼'))
        rotorSelectionButtonDown[k].place(x=380+k*35,y=120)


placeRingControls()
placeRotorControls()
placeRotorSelection()
root.mainloop()
