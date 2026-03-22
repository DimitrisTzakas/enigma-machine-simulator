from tkinter import *

root = Tk()
f1=Frame(root)
f1.pack(side=RIGHT, fill=Y)
f2=Frame(root)
f2.pack(side=RIGHT, fill=Y)
S1 = Scrollbar(f1)
S2 = Scrollbar(f2)
T1 = Text(f1, height=30, width=40)
T2 = Text(f2, height=2, width=50)
S1.pack(side=RIGHT, fill=Y)
S2.pack(side=RIGHT, fill=Y)
T1.pack(side=LEFT, fill=Y)
T2.pack(side=LEFT, fill=Y)
S1.config(command=T1.yview)
S2.config(command=T2.yview)
T1.config(yscrollcommand=S1.set)
T2.config(yscrollcommand=S2.set)


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
