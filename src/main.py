import engine as enigma
from tkinter import *
from tkinter.font import Font
from winsound import PlaySound
import wckToolTips
import tkinter.messagebox as tkMessageBox
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.normpath(os.path.join(BASE_DIR, '..', 'assets'))

def asset_path(name):
    return os.path.join(ASSETS_DIR, name)

#set main window
WIDTH=500
HEIGHT=720
root=Tk()
root.resizable(False, False)
root.wm_title("Enigma Kriegsmarine M3 ---by Dimitris Tzakas")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (WIDTH/2)
y = (screen_height/2) - (HEIGHT/2)
root.configure(width=WIDTH,height=HEIGHT)
root.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y*.25))
#end setting main window
frameLogo=Frame(root,width=WIDTH, height=60,bd=0,bg="grey20")
frameLogo.grid(row=0,sticky='wen')
frameSettings = Frame(root,width=WIDTH, height=150,bg="grey20")
frameSettings.grid(row=1,sticky='wen')
frameLightboard = Frame(root,width=WIDTH, height=180)
frameLightboard.grid(row=2,sticky='wen')
frameKeyboard = Frame(root,width=WIDTH, height=180)
frameKeyboard.grid(row=3,sticky='wen')
framePlugboard = Frame(root,width=WIDTH, height=100)
framePlugboard.grid(row=4,sticky='wen')
frameOutText = Frame(root,width=WIDTH, height=50)
frameOutText.grid(row=5,sticky='wen')

#------place ring frame inside settings frame---
ringFrame=Frame(frameSettings,height=150,width=WIDTH/3)
ringFrame.place(relx=0.17,rely=0.15,anchor=N)
#------
#------place rotor controls frame inside settings frame---
rotorFrame=Frame(frameSettings,height=150,width=WIDTH/3)
rotorFrame.place(relx=0.5,rely=0.15,anchor=N)
#------
#------place rotor selection frame inside settings frame---
rotorSelectFrame=Frame(frameSettings,height=150,width=WIDTH/3)
rotorSelectFrame.place(relx=0.82,rely=0.15,anchor=N)
#------
#------place reflector selection frame inside settings frame---
reflectorFrame=Frame(frameSettings,height=150,width=WIDTH/3)
reflectorFrame.place(relx=0.82,rely=0.85,anchor=S)
#------
#------place text entries, clear and reset  buttons at the bottom----
textFont=Font(family="Courier",size=16,weight="bold")
textInVar=StringVar()
textOutVar=StringVar()
textIn=Entry(frameOutText,font=textFont,state='readonly',readonlybackground='grey40',fg='black',textvariable=textInVar)
textIn.place(relx=0.5,rely=0,height=25,width=400,anchor=N)
textOut=Entry(frameOutText,font=textFont,state='readonly',readonlybackground='grey40',fg='gold',textvariable=textOutVar)
textOut.place(relx=0.5,rely=1,anchor=S,height=25,width=400)

def clearTextAction():
    textInVar.set('')
    textOutVar.set('')
textClearButton=Button(frameOutText,text='Clear Text',bg='grey20',fg='silver',wraplength=30,command=clearTextAction)
textClearButton.place(relx=1,rely=0.5,anchor=E,height=50,width=50)

def machineResetAction():
    enigma.initialize()
    removePlugBoardCables()
    initRotors=['I','II','III']
    for k in range(3):
        rotorLabel[k]["text"]='A'
        ringLabel[k]["text"]='01'
        rotorSelectionLabel[k]['text']=initRotors[k]
    reflectorLabel['text']='B'
machineResetButton=Button(frameOutText,text='Reset',bg='grey20',fg='silver',wraplength=30,command=machineResetAction)
machineResetButton.place(relx=0,rely=0.5,anchor=W,height=50,width=50)

def updateTextBoxes(char,newChar):
    textInVar.set(textInVar.get()+char)  
    textIn.xview_scroll(1,UNITS)
    textOutVar.set(textOutVar.get()+newChar)
    textOut.xview_scroll(1,UNITS)

def updateRotorDisplays():
    displays=[enigma.rotor1Display,enigma.rotor2Display,enigma.rotor3Display]
    for i in range(3): rotorLabel[i]["text"]=enigma.charFromReducedOrd(displays[i]-1)
    
def userKeyboardPressedAction(event):
    char=(event.char).upper()
    if char in qwerty:
        PlaySound(asset_path('key-down.wav'),1)
        newChar=enigma.encryptChar(char)
        updateTextBoxes(char,newChar)
        updateRotorDisplays()

keyRange=[]  #LIST OF KEY BINDINGS ----> <key-A> to <key-Z> and <key-a> to <key-z>
for i in range(65,91): keyRange.append('<Key-'+chr(i)+'>')
for i in range(97,123): keyRange.append('<Key-'+chr(i)+'>')
for i in range(52): root.bind(keyRange[i], userKeyboardPressedAction)
#------------------------------------------------------------------------

# create text window for large text cipher invoked by enigma logo
def createTextWindow(event):
    textWindow = Toplevel()
    textWindow.resizable(False, False)
    
    textFrame1=Frame(textWindow)
    textFrame1.grid(row=0,column=0)
    textFrame2=Frame(textWindow)
    textFrame2.grid(row=0,column=1)

    scroll1 = Scrollbar(textFrame1)
    scroll2 = Scrollbar(textFrame2)
    textIn = Text(textFrame1, height=20, width=30,bg='BLACK',fg='yellow',font=('courier',14),wrap=WORD,insertbackground='yellow')
    textOut= Text(textFrame2, height=20, width=30,bg='BLACK',fg='yellow',font=('courier',14),wrap=WORD,state='disabled')

    scroll1.grid(row=0,column=1,sticky=NS)
    scroll2.grid(row=0,column=1,sticky=NS)
    textIn.grid(row=0,column=0)
    textOut.grid(row=0,column=0)

    scroll1.config(command=textIn.yview)
    scroll2.config(command=textOut.yview)
    textIn.config(yscrollcommand=scroll1.set)
    textOut.config(yscrollcommand=scroll2.set)

    textWindow.update()
    buttonFrame=Frame(textWindow,height=60,width=textWindow.winfo_width(),bg='grey5')
    buttonFrame.grid(row=1,column=0,columnspan=2)

    cypherButton=Button(buttonFrame,text='Κρυπτογράφησε--->',font=('courier',10),bg='grey60',command=lambda :textWindowEncrypt(event))
    cypherButton.place(relx=0.5,rely=0.5,anchor=CENTER)
    copyButton=Button(buttonFrame,text='Αντιγραφή',bg='grey60',command=lambda: copy_clipboard(event))
    copyButton.place(relx=0.75,rely=0.5,anchor=CENTER)
    pasteButton=Button(buttonFrame,text='Επικόλληση',bg='grey60',command=lambda: paste_clipboard(event))
    pasteButton.place(relx=0.25,rely=0.5,anchor=CENTER)

    textWindow.update()
    winWidth=textWindow.winfo_width()
    winHeight=textWindow.winfo_height()
    xt = (screen_width/2) - (winWidth/2)
    yt = (screen_height/2) - (winHeight/2)
    textWindow.geometry('%dx%d+%d+%d' % (winWidth, winHeight, xt, yt))
    tkMessageBox.showinfo('Προειδοποίηση!','Χαρακτήρες που δεν ανήκουν στο σύνολο [A έως Z] θα αγνοούνται κατά την κρυπτογράφηση!',parent=textWindow)

    def textWindowEncrypt(event):
        s=textIn.get(1.0,'end-1c') # must omit last character because it is not valid
        s=enigma.encryptPhrase(s)
        textOut.config(state='normal')
        textOut.delete('1.0', END)
        textOut.insert(END, s)
        textOut.config(state='disabled')
        updateRotorDisplays()

    def copy_clipboard(event):
        value = textOut.get("1.0", 'end-1c')  # get text
        textWindow.clipboard_clear()  # clear clipboard contents
        textWindow.clipboard_append(value)  # append new value to clipbaord

    def paste_clipboard(event):
        value = textWindow.clipboard_get()  # get text
        textIn.delete('1.0', END)
        textIn.insert(END, value)  # paste clipboard contents
#end Textwindow-------------------------------------------------------------------------       
    
#place logo
img = PhotoImage(file=asset_path("enigmaLogo.gif"))
logoLabel=Label(frameLogo,image=img,bg='grey20',bd=0)
logoLabel.place(relx=0.5,rely=0.5,anchor=CENTER)
logoLabel.bind("<Button-1>",createTextWindow)
#----------------------------------------------------------------------
#place variant
logoFont=Font(weight="bold",size=12,family='courier')
variantLabel=Label(frameSettings,text='Kriegsmarine M3 Dimitris Tzakas',fg='lightSkyBlue1',bg='grey20',font=logoFont,wraplength=180)
variantLabel.place(relx=0.17,rely=0.76,anchor='center')

#fonts
rButtonFont=Font(size=6,weight='bold')
rLabelFont=Font(size=8,weight='bold')
rbFont=Font(size=10)
rlFont=Font(size=24,weight='bold')

#reflector selection and action
def reflectorButtonAction():
    PlaySound(asset_path('tick.wav'),1)
    if reflectorLabel['text']=='B':
        reflectorLabel['text']='C'
        enigma.reflector=enigma.reflectors[1]
    else:
        reflectorLabel['text']='B'
        enigma.reflector=enigma.reflectors[0]

def placeReflectorSelection():
    global reflectorLabel
    reflectorButtonLeft=Button(reflectorFrame,text='◄',font=rButtonFont,width=3,padx=1,command=reflectorButtonAction)
    reflectorButtonLeft.grid(row=0,column=0)
    reflectorLabel=Label(reflectorFrame, text='B',bg='grey',font=rLabelFont,width=3,padx=0,relief="sunken")
    reflectorLabel.grid(row=0,column=1)
    reflectorButtonLeft=Button(reflectorFrame,text='►',font=rButtonFont,width=3,padx=1,command=reflectorButtonAction)
    reflectorButtonLeft.grid(row=0,column=2)
    wckToolTips.register(reflectorLabel, "Umkehrwalze (UKW)-Επιλογή Ανακλαστήρα-Reflector Selection")
    
#rings configuration and action
def ringButtonAction(ring,arrow):
    PlaySound(asset_path('tick.wav'),1)
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
        ringButtonUp[k]=Button(ringFrame,text='▲',font=rButtonFont,width=3,padx=1,command=lambda x=k:ringButtonAction(x,'▲'))
        ringButtonUp[k].grid(row=0,column=k)
        ringLabel[k]=Label(ringFrame, text='01',bg='grey',font=rLabelFont,width=3,padx=0,relief="sunken")
        ringLabel[k].grid(row=1,column=k)
        ringButtonDown[k]=Button(ringFrame,text='▼',font=rButtonFont,width=3,padx=1,command=lambda x=k:ringButtonAction(x,'▼'))
        ringButtonDown[k].grid(row=2,column=k)
    for i in range(3): wckToolTips.register(ringLabel[i], "RingStellung-Ρύρμιση Δακτυλίου-Ring Setting") 

#rotors configuration and action
def rotorButtonAction(rotor,arrow): 
    alphabet=enigma.alphabet
    PlaySound(asset_path('tick.wav'),1)
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
        rotorButtonUp[k]=Button(rotorFrame,text='▲',font=rbFont,width=4,padx=2,command=lambda x=k:rotorButtonAction(x,'▲'))
        rotorButtonUp[k].grid(row=0,column=k)
        rotorLabel[k]=Label(rotorFrame, text='A',bg='grey70',fg='grey20',font=rlFont,width=2,relief="raised")
        rotorLabel[k].grid(row=1,column=k)
        rotorButtonDown[k]=Button(rotorFrame,text='▼',font=rbFont,width=4,padx=2,command=lambda x=k:rotorButtonAction(x,'▼'))
        rotorButtonDown[k].grid(row=2,column=k)
    for i in range(3): wckToolTips.register(rotorLabel[i], "Spruchschlussel-Αρχική Θέση Ροτόρων-Rotor Start Position")
    
#rotor selection and action
def rotorSelectionAction(rotor,arrow):
    saveRotorsInstalled=enigma.rotorsInstall # save rotors installed before initialization
    saveReflector=enigma.reflector # save reflector installed before initialization
    saveplugBoard=enigma.plugBoard
    #reset the machine if any rotor is replaced by another
    enigma.initialize()
    for k in range(3):
        rotorLabel[k]["text"]='A'
        ringLabel[k]["text"]='01'
    textInVar.set('')
    textOutVar.set('')
    #end reseting
    enigma.rotorsInstall=saveRotorsInstalled #restore rotors installed before initialization
    enigma.reflector=saveReflector #restore reflector installed before initialization
    enigma.plugBoard=saveplugBoard
    PlaySound(asset_path('tick.wav'),1)
    rotors=['I','II','III','IV','V','VI','VII','VIII']
    if arrow=='▲':
        selection=(rotors.index(rotorSelectionLabel[rotor].cget("text"))+1) % len(rotors)
        enigma.setRotorsInstall(rotor,selection)
        rotorSelectionLabel[rotor]['text']=rotors[selection]
    elif arrow== '▼':
        selection=(rotors.index(rotorSelectionLabel[rotor].cget("text"))-1) % len(rotors) 
        enigma.setRotorsInstall(rotor,selection)
        rotorSelectionLabel[rotor]['text']=rotors[selection]
    
def placeRotorSelection():
    global rotorSelectionLabel
    rotorSelectionButtonUp=[None]*3
    rotorSelectionLabel=[None]*3
    rotorSelectionButtonDown=[None]*3
    for k in range(3):
        rotorSelectionButtonUp[k]=Button(rotorSelectFrame,text='▲',font=rButtonFont,width=3,padx=2,command=lambda x=k:rotorSelectionAction(x,'▲'))
        rotorSelectionButtonUp[k].grid(row=0,column=k)
        rotorSelectionButtonDown[k]=Button(rotorSelectFrame,text='▼',font=rButtonFont,width=3,padx=2,command=lambda x=k:rotorSelectionAction(x,'▼'))
        rotorSelectionButtonDown[k].grid(row=2,column=k)
    k=0
    for r in ['I','II','III']:
        rotorSelectionLabel[k]=Label(rotorSelectFrame, text=r,bg='grey',font=rLabelFont,width=3,relief="sunken",borderwidth=2)
        rotorSelectionLabel[k].grid(row=1,column=k)
        k+=1
    for i in range(3): wckToolTips.register(rotorSelectionLabel[i], "Walzenlage-Επιλογή Ροτόρων-Rotor Selection")
    
def placeLightboard():
    global lightKey,lightBoard
    lightKeyFont=Font(size=16,weight='bold')
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
        lightKey[k]=lightBoard.create_text(x,y,text=qwerty[k],fill='grey25',font=lightKeyFont)
    x=cw/9
    y=ch/2
    R=cw/30    
    for k in range(8):
        x=cw/10*(k+1)+1.5*R
        coords=(x-R,y-R,x+R,y+R)
        lightBoard.create_oval(coords,fill='grey15',outline='grey10')
        lightKey[k+9]=lightBoard.create_text(x,y,text=qwerty[k+9],fill='grey25',font=lightKeyFont)
    x=cw/9
    y=ch/1.33
    R=cw/30    
    for k in range(9):
        x=cw/10*(k+1)
        coords=(x-R,y-R,x+R,y+R)
        lightBoard.create_oval(coords,fill='grey15',outline='grey10')
        lightKey[k+17]=lightBoard.create_text(x,y,text=qwerty[k+17],fill='grey25',font=lightKeyFont)                                             


def keyPressAction(event,x):
    global keyLit       #key lit to be used by keyReleaseAction() to shut the key light
    keyBoard.itemconfigure(key[x],fill='black',outline='grey40')            #change key outline effect
    keyBoard.itemconfigure(keyText[x],fill='grey40',font=('NORMAL',14))      #change keyText color effect
    PlaySound(asset_path('key-down.wav'),1)
    newChar=enigma.encryptChar(qwerty[x])
    updateTextBoxes(qwerty[x],newChar)
    keyLit=qwerty.index(newChar)
    lightBoard.itemconfigure(lightKey[keyLit],fill='yellow')
    displays=[enigma.rotor1Display,enigma.rotor2Display,enigma.rotor3Display]
    for i in range(3): rotorLabel[i]["text"]=enigma.charFromReducedOrd(displays[i]-1)

def keyReleaseAction(event,x):
    PlaySound(asset_path('key-up.wav'),1)
    lightBoard.itemconfigure(lightKey[keyLit],fill='grey25')
    keyBoard.itemconfigure(key[x],fill='grey10',outline='grey90')        #change key outline effect return to normal
    keyBoard.itemconfigure(keyText[x],fill='grey90',font=('BOLD',15))    #change keyText color effect return to normal
    
def placeKeyboard():
    global keyText,key,keyBoard
    key=[None]*26
    keyText=[None]*26
    keyBoard=Canvas(frameKeyboard,width=WIDTH,height=180,bg='grey18',highlightthickness=0)
    keyBoard.place(relx=0.5,rely=0.5,anchor=CENTER)
    cw=int(keyBoard["width"]) #canvas widht
    ch=int(keyBoard["height"]) #canvas height
    x=cw/10
    y=ch/4
    R=cw/30
    for k in range(9):
        x=cw/10*(k+1)
        coords=(x-R,y-R,x+R,y+R)
        key[k]=keyBoard.create_oval(coords,fill='grey10',outline='grey90',width=2,tags=qwerty[k])
        keyText[k]=keyBoard.create_text(x,y,text=qwerty[k],fill='grey90',font=('BOLD',15),tags=qwerty[k])
    x=cw/9
    y=ch/2
    R=cw/30    
    for k in range(8):
        x=cw/10*(k+1)+1.5*R
        coords=(x-R,y-R,x+R,y+R)
        key[k+9]=keyBoard.create_oval(coords,fill='grey10',outline='grey90',width=2,tags=qwerty[k+9])
        keyText[k+9]=keyBoard.create_text(x,y,text=qwerty[k+9],fill='grey90',font=('BOLD',15),tags=qwerty[k+9])
    x=cw/9
    y=ch/1.33
    R=cw/30    
    for k in range(9):
        x=cw/10*(k+1)
        coords=(x-R,y-R,x+R,y+R)
        key[k+17]=keyBoard.create_oval(coords,fill='grey10',outline='grey90',width=2,tags=qwerty[k+17])
        keyText[k+17]=keyBoard.create_text(x,y,text=qwerty[k+17],fill='grey90',font=('BOLD',15),tags=qwerty[k+17])      
    for k in range(26): keyBoard.tag_bind(qwerty[k],'<Button-1>',lambda event,x=k: keyPressAction(event,x))
    for k in range(26): keyBoard.tag_bind(qwerty[k],'<ButtonRelease-1>',lambda event,x=k: keyReleaseAction(event,x))
    
def removePlugBoardCables():
    global plug1,plug2,plugColors
    enigma.plugBoard=[]
    for i in range(26): plugBoard.itemconfigure(plugKey[i],fill='black')
    plug1=[]
    plug2=[]
    plugColors=[]

def plugPressAction(event,k):
    PlaySound(asset_path('tick.wav'),1)
    colors=['red','spring green','orchid1','orange','deep sky blue','purple','maroon','blue2','khaki3','brown4','magenta2','green','lightBlue2']
    if (k not in plug1) and (k not in plug2): # if key is not selected
        if len(plug1) == len(plug2):  # if a pair exists take a new color
            nextColor=0
            while nextColor in plugColors: nextColor=(nextColor+1) % len(colors) #select a color not used
            plugBoard.itemconfigure(plugKey[k],fill=colors[nextColor])
            plug1.append(k)
            plugColors.append(nextColor)
        else:                         # pair does not exist, so make pair and update enigma machine
            plugBoard.itemconfigure(plugKey[k],fill=colors[plugColors[len(plugColors)-1]]) # fill last used color to make a pair
            plug2.append(k)
            enigma.plugBoard.append(alphabet[plug1[len(plug1)-1]]+alphabet[plug2[len(plug2)-1]]) #update enigma machine plugboard
    else:     # if a key is allready selected
        if  (k == plug1[len(plug1)-1]) and (len(plug1)>len(plug2)):  # if key selected is not a paired one then delete it - the last selected
            plugBoard.itemconfigure(plugKey[plug1.pop()],fill='black')
            plugColors.pop()
        else: # if key selected is a paired one then delete pair but first find it
            if k in plug1:
                position=plug1.index(k)
            else:
                position=plug2.index(k)
            plugBoard.itemconfigure(plugKey[plug1.pop(position)],fill='black') # return to original state of the item poped from plug1 list
            plugBoard.itemconfigure(plugKey[plug2.pop(position)],fill='black') # return to original state of the item poped from plug2 list
            plugColors.pop(position)
            enigma.plugBoard.pop(position)  #update enigma machine plugboard


def placePlugboard():
    global plugBoard,plugKey,plug1,plug2,plugColors
    plug1=[] # plug1 and plug2 make a connection (pair) 
    plug2=[] # plug1 and plug2 make a connection (pair)
    plugColors=[] # colors used
    plugKey=[None]*26
    plugBoard=Canvas(framePlugboard,width=WIDTH,height=100,bg='grey10',highlightthickness=0)
    plugBoard.place(relx=0.5,rely=0.5,anchor=CENTER)
    cw=int(plugBoard["width"]) #canvas widht
    ch=int(plugBoard["height"]) #canvas height
    x=cw/10
    y=ch/5
    R=cw/70
    for k in range(9):
        x=cw/10*(k+1)
        coords=(x-R,y-R,x+R,y+R)
        plugKey[k]=plugBoard.create_oval(coords,fill='black',outline='grey90',width=2,tags=alphabet[k])
        plugBoard.create_text(x-2.5*R,y,text=alphabet[k],fill='white',font=('BOLD',13))
    x=cw/9
    y=ch/2
    R=cw/70    
    for k in range(8):
        x=cw/10*(k+1)+4*R
        coords=(x-R,y-R,x+R,y+R)
        plugKey[k+9]=plugBoard.create_oval(coords,fill='black',outline='grey90',width=2,tags=alphabet[k+9])
        plugBoard.create_text(x-2.5*R,y,text=alphabet[k+9],fill='white',font=('BOLD',13))
    x=cw/9
    y=ch/1.25
    R=cw/70    
    for k in range(9):
        x=cw/10*(k+1)
        coords=(x-R,y-R,x+R,y+R)
        plugKey[k+17]= plugBoard.create_oval(coords,fill='black',outline='grey90',width=2,tags=alphabet[k+17])
        plugBoard.create_text(x-2.5*R,y,text=alphabet[k+17],fill='white',font=('BOLD',13))
    for k in range(26): plugBoard.tag_bind(alphabet[k],'<Button-1>',lambda event,x=k: plugPressAction(event,x))    
    wckToolTips.register(plugBoard, "Steckerverbindungen-Επιλογές Πίνακα Αναγραμματισμού-Plugboard Settings")
    


#----------------------------------
alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
qwerty='QWERTZUIOASDFGHJKPYXCVBNML'
placeRingControls()
placeRotorControls()
placeRotorSelection()
placeReflectorSelection()
placeLightboard()
placeKeyboard()
placePlugboard()

root.mainloop()

