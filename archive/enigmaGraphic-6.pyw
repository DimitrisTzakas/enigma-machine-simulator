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
root.configure(width=WIDTH,height=HEIGHT,bg='grey15')
root.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y))
#end setting main window
frameLogo=Frame(root,width=WIDTH, height=80,bd=0)
frameLogo.grid(row=0,sticky='wen')
frameSettings = Frame(root,width=WIDTH, height=150,bg="grey20")
frameSettings.grid(row=1,sticky='wen')
frameLightboard = Frame(root,width=500, height=180,bg='grey20')
frameLightboard.grid(row=2,sticky='wen')
frameKeyboard = Frame(root,width=WIDTH, height=180,bg="grey15")
frameKeyboard.grid(row=3,sticky='wen')
framePlugboard = Frame(root,width=WIDTH, height=100,bg="dark goldenrod")
framePlugboard.grid(row=4,sticky='wen')
frameOutText = Frame(root,width=WIDTH, height=30,bg="grey40")
frameOutText.grid(row=5,sticky='wen')
#place logo
img = PhotoImage(file = "enigmaLogo.gif")
logoLabel=Label(frameLogo,width=500, height=80,image=img,bg='grey20',bd=0)
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
    PlaySound('tick.wav',0)
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
        rotorButtonUp[k].place(x=180+k*46,y=25)
        rotorLabel[k]=Label(frameSettings, text='A',bg='grey70',fg='grey20',font=rlFont,width=2,relief="sunken",borderwidth=2)
        rotorLabel[k].place(x=180+k*46, y=55)
        rotorButtonDown[k]=Button(frameSettings,text='▼',font=rbFont,width=4,padx=3,command=lambda x=k:rotorButtonAction(x,'▼'))
        rotorButtonDown[k].place(x=180+k*46,y=100)

#rotor selection and action
def rotorSelectionAction(rotor,arrow):
    PlaySound('tick.wav',0)
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
    k=0
    for r in ['I','II','III']:
        rotorSelectionLabel[k]=Label(frameSettings, text=r,bg='grey',font=rLabelFont,width=3,relief="sunken",borderwidth=2)
        rotorSelectionLabel[k].place(x=360+k*35, y=55)
        k+=1

def placeLightboard():
    global querty,lightKey
    querty='QUERTZUIOASDFGHJKPYXCVBNML'
    lightKey=[None]*26
    lightBoard=Canvas(frameLightboard,width=WIDTH,height=180,bg='grey20',highlightthickness=0)
    lightBoard.place(relx=0.5,rely=0.5,anchor=CENTER)
    cw=int(lightBoard["width"]) #canvas widht
    ch=int(lightBoard["height"]) #canvas height
    x=cw/10
    y=ch/4
    R=cw/30
    for k in range(9):
        x=cw/10*(k+1)
        coords=(x-R,y-R,x+R,y+R)
        lightBoard.create_oval(coords,fill='grey15',outline='grey10')
        lightKey[k]=lightBoard.create_text(x,y,text=querty[k],fill='grey25',font=('BOLD',15))
    x=cw/9
    y=ch/2
    R=cw/30    
    for k in range(8):
        x=cw/10*(k+1)+1.5*R
        coords=(x-R,y-R,x+R,y+R)
        lightBoard.create_oval(coords,fill='grey15',outline='grey10')
        lightKey[k+9]=lightBoard.create_text(x,y,text=querty[k+9],fill='grey25',font=('BOLD',15))
    x=cw/9
    y=ch/1.33
    R=cw/30    
    for k in range(9):
        x=cw/10*(k+1)
        coords=(x-R,y-R,x+R,y+R)
        lightBoard.create_oval(coords,fill='grey15',outline='grey10')
        lightKey[k+17]=lightBoard.create_text(x,y,text=querty[k+17],fill='yellow',font=('BOLD',15))                                             

def placeKeyboard():
    global querty,key
    querty='QUERTZUIOASDFGHJKPYXCVBNML'
    key=[None]*26
    keyBoard=Canvas(frameKeyboard,width=WIDTH,height=180,bg='grey15',highlightthickness=0)
    keyBoard.place(relx=0.5,rely=0.5,anchor=CENTER)
    cw=int(keyBoard["width"]) #canvas widht
    ch=int(keyBoard["height"]) #canvas height
    x=cw/10
    y=ch/4
    R=cw/30
    for k in range(9):
        x=cw/10*(k+1)
        coords=(x-R,y-R,x+R,y+R)
        keyBoard.create_oval(coords,fill='black',outline='grey90',width=2)
        key[k]=keyBoard.create_text(x,y,text=querty[k],fill='grey90',font=('BOLD',15))
    x=cw/9
    y=ch/2
    R=cw/30    
    for k in range(8):
        x=cw/10*(k+1)+1.5*R
        coords=(x-R,y-R,x+R,y+R)
        keyBoard.create_oval(coords,fill='black',outline='grey90',width=2)
        key[k+9]=keyBoard.create_text(x,y,text=querty[k+9],fill='grey90',font=('BOLD',15))
    x=cw/9
    y=ch/1.33
    R=cw/30    
    for k in range(9):
        x=cw/10*(k+1)
        coords=(x-R,y-R,x+R,y+R)
        keyBoard.create_oval(coords,fill='black',outline='grey90',width=2)
        key[k+17]=keyBoard.create_text(x,y,text=querty[k+17],fill='grey90',font=('BOLD',15))      

def placePlugboard():
    global querty,lightKey
    querty='QUERTZUIOASDFGHJKPYXCVBNML'
    plugKey=[None]*26
    plugBoard=Canvas(framePlugboard,width=WIDTH,height=100,bg='dark goldenrod',highlightthickness=0)
    plugBoard.place(relx=0.5,rely=0.5,anchor=CENTER)
    cw=int(plugBoard["width"]) #canvas widht
    ch=int(plugBoard["height"]) #canvas height
    x=cw/10
    y=ch/5
    R=cw/70
    for k in range(9):
        x=cw/10*(k+1)
        coords=(x-R,y-R,x+R,y+R)
        plugKey[k]=plugBoard.create_oval(coords,fill='grey20',outline='grey90',width=2)
        plugBoard.create_text(x-2.5*R,y,text=querty[k],fill='grey20',font=('BOLD',11))
    x=cw/9
    y=ch/2
    R=cw/70    
    for k in range(8):
        x=cw/10*(k+1)+4*R
        coords=(x-R,y-R,x+R,y+R)
        plugKey[k+9]=plugBoard.create_oval(coords,fill='grey20',outline='grey90',width=2)
        plugBoard.create_text(x-2.5*R,y,text=querty[k+9],fill='grey20',font=('BOLD',11))
    x=cw/9
    y=ch/1.25
    R=cw/70    
    for k in range(9):
        x=cw/10*(k+1)
        coords=(x-R,y-R,x+R,y+R)
        plugKey[k+17]= plugBoard.create_oval(coords,fill='grey20',outline='grey90',width=2)
        plugBoard.create_text(x-2.5*R,y,text=querty[k+17],fill='grey20',font=('BOLD',11))           

placeRingControls()
placeRotorControls()
placeRotorSelection()
placeLightboard()
placeKeyboard()
placePlugboard()

root.mainloop()
