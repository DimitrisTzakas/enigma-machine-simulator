import enigma4 as enigma
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
root.configure(width=WIDTH,height=HEIGHT)
root.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y))
#end setting main window
frameLogo=Frame(root,width=WIDTH, height=100)
frameLogo.grid(row=0)
frameSettings = Frame(root,width=WIDTH, height=170,bg="grey15")
frameSettings.grid(row=1)
frameLightboard = Frame(root,width=WIDTH, height=160,bg="green")
frameLightboard.grid(row=2)
frameKeyboard = Frame(root,width=WIDTH, height=160,bg="blue")
frameKeyboard.grid(row=3)
framePlugboard = Frame(root,width=WIDTH, height=100,bg="yellow")
framePlugboard.grid(row=4)
frameOutText = Frame(root,width=WIDTH, height=30,bg="white")
frameOutText.grid(row=5)
#place logo
img = PhotoImage(file = "enigmaLogo.gif")
logoLabel=Label(frameLogo,width=496, height=100,image=img,bg='grey20')
logoLabel.place(relx=0.5,rely=0.5,anchor=CENTER)
#fonts
rButtonFont=Font(size=6,weight='bold')
rLabelFont=Font(size=8,weight='bold')
rbFont=Font(size=10)
rlFont=Font(size=24,weight='bold')

#rings configuration and action
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
    for k in range(3):
        ringButtonUp[k]=Button(frameSettings,text='▲',font=rButtonFont,width=3,padx=2,command=lambda x=k:ringButtonAction(x,'▲'))
        ringButtonUp[k].place(x=40+k*35,y=50)
        ringLabel[k]=Label(frameSettings, text='01',bg='grey',font=rLabelFont,width=3,relief="sunken",borderwidth=2)
        ringLabel[k].place(x=40+k*35, y=70)
        ringButtonDown[k]=Button(frameSettings,text='▼',font=rButtonFont,width=3,padx=2,command=lambda x=k:ringButtonAction(x,'▼'))
        ringButtonDown[k].place(x=40+k*35,y=93)
    for i in range(3): wckToolTips.register(ringLabel[i], "01-A|02-B|03-C|04-D|05-E|06-F|07-G|08-H") 

#rotors configuration and action
def rotorButtonAction(rotor,arrow):
    alphabet=enigma.alphabet
    PlaySound('key-up.wav',0)
    if arrow=='▲':
        enigma.setRotorsSetting(rotor,1)
        rotorLabel[rotor]['text']=alphabet[(alphabet.index(rotorLabel[rotor].cget("text"))+1) % 26]
    elif arrow== '▼':
        enigma.setRotorsSetting(rotor,-1)
        rotorLabel[rotor]['text']=alphabet[(alphabet.index(rotorLabel[rotor].cget("text"))-1) % 26]

def placeRotorControls():
    global rotorLabel
    rotorButtonUp=[None]*3
    rotorLabel=[None]*3
    rotorButtonDown=[None]*3
    for k in range(3):
        rotorButtonUp[k]=Button(frameSettings,text='▲',font=rbFont,width=4,padx=3,command=lambda x=k:rotorButtonAction(x,'▲'))
        rotorButtonUp[k].place(x=180+k*46,y=60)
        rotorLabel[k]=Label(frameSettings, text='A',bg='grey70',fg='grey20',font=rlFont,width=2,relief="sunken",borderwidth=2)
        rotorLabel[k].place(x=180+k*46, y=90)
        rotorButtonDown[k]=Button(frameSettings,text='▼',font=rbFont,width=4,padx=3,command=lambda x=k:rotorButtonAction(x,'▼'))
        rotorButtonDown[k].place(x=180+k*46,y=135)

#rotor selection and action
def rotorSelectionAction(rotor,arrow):
    rotors=['I','II','III','IV','V']
    if arrow=='▲':
        selection=(rotors.index(rotorSelectionLabel[rotor].cget("text"))+1) % 5
        enigma.setRotorsInstall(rotor,selection)
        rotorSelectionLabel[rotor]['text']=rotors[selection]
    elif arrow== '▼':
        selection=(rotors.index(rotorSelectionLabel[rotor].cget("text"))-1) % 5
        enigma.setRotorsInstall(rotor,selection)
        rotorSelectionLabel[rotor]['text']=rotors[selection]
   
        
def placeRotorSelection():
    global rotorSelectionLabel
    rotorSelectionButtonUp=[None]*3
    rotorSelectionLabel=[None]*3
    rotorSelectionButtonDown=[None]*3
    for k in range(3):
        rotorSelectionButtonUp[k]=Button(frameSettings,text='▲',font=rButtonFont,width=3,padx=2,command=lambda x=k:rotorSelectionAction(x,'▲'))
        rotorSelectionButtonUp[k].place(x=360+k*35,y=35)
        rotorSelectionButtonDown[k]=Button(frameSettings,text='▼',font=rButtonFont,width=3,padx=2,command=lambda x=k:rotorSelectionAction(x,'▼'))
        rotorSelectionButtonDown[k].place(x=360+k*35,y=78)
    rotorSelectionLabel[0]=Label(frameSettings, text='I',bg='grey',font=rLabelFont,width=3,relief="sunken",borderwidth=2)
    rotorSelectionLabel[0].place(x=360+0*35, y=55)
    rotorSelectionLabel[1]=Label(frameSettings, text='II',bg='grey',font=rLabelFont,width=3,relief="sunken",borderwidth=2)
    rotorSelectionLabel[1].place(x=360+1*35, y=55)
    rotorSelectionLabel[2]=Label(frameSettings, text='III',bg='grey',font=rLabelFont,width=3,relief="sunken",borderwidth=2)
    rotorSelectionLabel[2].place(x=360+2*35, y=55)


placeRingControls()
placeRotorControls()
placeRotorSelection()
root.mainloop()
