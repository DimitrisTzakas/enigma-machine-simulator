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


textFrame1=Frame(textWindow,width=twWIDTH/2,bg='grey40',height=450)
textFrame1.grid(row=0,column=0,sticky=EW)

textFrame2=Frame(textWindow,width=twWIDTH/2,bg='grey40',height=450)
textFrame2.grid(row=0,column=1)

buttonFrame=Frame(textWindow,bg='grey40',width=twWIDTH,height=50)
buttonFrame.grid(row=1,column=0,columnspan=2,sticky=EW)


textIn = Text(textFrame1,bg='grey80',width=42,height=27)
textIn.place(relx=0.5,rely=0.5,anchor=CENTER)

textOut= Text(textFrame2,bg='grey80',width=42,height=27)
textOut.place(relx=0.5,rely=0.5,anchor=CENTER)



scroll1 = Scrollbar(textFrame1)
scroll1.place(relx=1,rely=0,anchor=N)
#scroll2 = Scrollbar(textFrame2)
#scroll2.grid(row=0,column=1,sticky=NS)


scroll1.config(command=textIn.yview)
#scroll2.config(command=textOut.yview)
textIn.config(yscrollcommand=scroll1.set)
#textOut.config(yscrollcommand=scroll2.set)
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
