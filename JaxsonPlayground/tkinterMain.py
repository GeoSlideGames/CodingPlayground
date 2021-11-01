from tkinter import *

root = Tk()
entry = Entry(root,width=50,)
entry.pack()


def myClick():
    hello = "hello " + entry.get()
    Label1 = Label(root, text=hello).pack()
root.title('what??')
myButton = Button(root, text='Click me', padx=50, pady=60, command=myClick,)
myButton.pack()






root.mainloop()

