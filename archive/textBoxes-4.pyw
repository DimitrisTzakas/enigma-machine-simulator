# -*- coding: utf-8 -*-

from tkinter import *


twWIDTH=700
twHEIGHT=500
textWindow= Tk()
screen_width = textWindow.winfo_screenwidth()
screen_height = textWindow.winfo_screenheight()
textWindow.resizable(False, False)
textWindow.wm_title("")
x = (screen_width/2) - (twWIDTH/2)
y = (screen_height/2) - (twHEIGHT/2)
textWindow.configure(width=twWIDTH,height=twHEIGHT)
textWindow.geometry('%dx%d+%d+%d' % (twWIDTH, twHEIGHT, x, y))
#textWindow.lift(root)
#textWindow.focus_set()
textWindow.grid_columnconfigure(0,weight=1)
textWindow.grid_columnconfigure(1,weight=1)

textFrame1=Frame(textWindow)
textFrame1.grid(row=0,column=0,sticky=EW)

textFrame2=Frame(textWindow)
textFrame2.grid(row=0,column=1,sticky=EW)

buttonFrame=Frame(textWindow,bg='grey40')
buttonFrame.grid(row=1,column=0,columnspan=2,sticky=EW)


textIn = Text(textFrame1,bg='red')
textIn.pack( side = LEFT,fill=None,expand=True )  

textOut= Text(textFrame2,bg='yellow')
textOut.pack( side = LEFT )  



scroll1 = Scrollbar(textFrame1)
scroll1.pack(side = RIGHT, fill = Y)  
scroll2 = Scrollbar(textFrame2)
scroll2.pack(side = RIGHT, fill = Y)


scroll1.config(command=textIn.yview)
scroll2.config(command=textOut.yview)
textIn.config(yscrollcommand=scroll1.set)
textOut.config(yscrollcommand=scroll2.set)
'''


cypherButton=Button(buttonFrame,text='Κρυπτογράφησε--->')
cypherButton.place(relx=0.5,rely=0.5,anchor=CENTER)
copyButton=Button(buttonFrame,text='Αντιγραφή',width=10)
copyButton.place(relx=0.75,rely=0.5,anchor=CENTER)
pasteButton=Button(buttonFrame,text='Επικόλληση',width=10)
pasteButton.place(relx=0.25,rely=0.5,anchor=CENTER)

'''
quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished.
HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished.
HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished.
"""

#textIn.insert(END, quote)
#textOut.insert(END, quote)
textWindow.mainloop()
