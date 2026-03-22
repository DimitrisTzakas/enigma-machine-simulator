
from Tkinter import *

#set main window

root=Tk()
root.configure(width=500,height=500,background='grey')
root.resizable(False, False)
root.wm_title("Enigma I - WEHRMACHT BY 1ο ΕΠΑΛ ΜΟΛΑΩΝ")
root.geometry("500x500")

f1=Frame(root,width=root["width"]/3,height=root["height"],bg='yellow')
f2=Frame(root,width=root["width"]/3,height=root["height"],bg='red')
f3=Frame(root,width=root["width"]/3,height=root["height"],bg='pink')
f1.grid(row=0,column=0)
f2.grid(row=0,column=1)
f3.grid(row=0,column=2)
labelFrame=Frame(f1,width=f1["width"]/2,height=f1["height"]/4,bg='black')
labelFrame.place(relx=0.5,rely=0.5,anchor=CENTER)
label1=Label(f1,text='label1',width=10,relief='sunken')
label2=Label(f2,text='label2',width=10,relief='sunken')

label1.place(relx=0.5,rely=0.5,anchor=CENTER)
label2.place(relx=0.5,rely=0.5,anchor=CENTER)

overFrame=Frame(f2,width=root["width"]/3,height=root["height"],bg='green')
overFrame.grid()
overFrame.grid_forget()
overFrame.grid()
root.mainloop()
