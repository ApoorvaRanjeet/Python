from tkinter import *

root = Tk()
root.geometry("432x234")
root.title("hello")

frame= Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
frame.pack(side=LEFT,fill="y")

l1 = Label(frame,text="hey apoorva this side")
l1.pack(pady=142)

root.mainloop()