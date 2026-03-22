from tkinter import *

root = Tk()
f1=Frame(root)
f1.grid(row=0,column=0)
f2=Frame(root)
f2.grid(row=0,column=1)
S1 = Scrollbar(f1)
S2 = Scrollbar(f2)
T1 = Text(f1, height=30, width=40)
T2 = Text(f2, height=30, width=40)
S1.grid(row=0,column=1,sticky=NS)
S2.grid(row=0,column=1,sticky=NS)
T1.grid(row=0,column=0)
T2.grid(row=0,column=0)
S1.config(command=T1.yview)
S2.config(command=T2.yview)
T1.config(yscrollcommand=S1.set)
T2.config(yscrollcommand=S2.set)
f3=Frame(root)
f3.grid(row=1,column=0,columnspan=2,sticky=EW)
b=Button(f3,text='hi')
b.grid(sticky=EW)


quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""

T1.insert(END, quote)
T2.insert(END, quote)
mainloop()
