# -*- coding: utf-8 -*-

from tkinter import *

textWindow = Tk()
textWindow.resizable(False, False)

textFrame1=Frame(textWindow)
textFrame1.grid(row=0,column=0)
textFrame2=Frame(textWindow)
textFrame2.grid(row=0,column=1)

scroll1 = Scrollbar(textFrame1)
scroll2 = Scrollbar(textFrame2)
textIn = Text(textFrame1, height=20, width=30,bg='grey80',font=('courier',14),wrap=WORD)
textOut= Text(textFrame2, height=20, width=30,bg='grey80',font=('courier',14),wrap=WORD)

scroll1.grid(row=0,column=1,sticky=NS)
scroll2.grid(row=0,column=1,sticky=NS)
textIn.grid(row=0,column=0)
textOut.grid(row=0,column=0)

scroll1.config(command=textIn.yview)
scroll2.config(command=textOut.yview)
textIn.config(yscrollcommand=scroll1.set)
textOut.config(yscrollcommand=scroll2.set)

textWindow.update()

buttonFrame=Frame(textWindow,height=60,width=textWindow.winfo_width(),bg='grey60')
buttonFrame.grid(row=1,column=0,columnspan=2)

cypherButton=Button(buttonFrame,text='Κρυπτογράφησε--->')
cypherButton.place(relx=0.5,rely=0.5,anchor=CENTER)
copyButton=Button(buttonFrame,text='Αντιγραφή',width=10)
copyButton.place(relx=0.75,rely=0.5,anchor=CENTER)
pasteButton=Button(buttonFrame,text='Επικόλληση',width=10)
pasteButton.place(relx=0.25,rely=0.5,anchor=CENTER)


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

textIn.insert(END, quote)
textOut.insert(END, quote)
print textIn.get(1.0,END)
textWindow.update()
winWidth=textWindow.winfo_width()
winHeight=textWindow.winfo_height()
textWindow.geometry('%dx%d+%d+%d' % (winWidth, winHeight, 400, 200))
mainloop()
