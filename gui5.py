from tkinter import *

root = Tk()
root.geometry("432x234")
root.title("hello")

frame= Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
frame.pack()

# l1=Label(frame,text="Apoorva")
# l1.pack()
def name():
    print("Apoorva")
def hello():
    print("hello")
def him():
    print("i don't like him")
b1=Button(frame,fg="red",text="click",command=hello)
b1.pack(side=LEFT)
b2=Button(frame,fg="red",text="click",command=name)
b2.pack(side=LEFT)
b3=Button(frame,fg="red",text="click",command=him)
b3.pack(side=LEFT)
root.mainloop()