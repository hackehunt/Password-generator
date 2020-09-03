from tkinter import *
from tkinter import messagebox as msg
import string
import pyperclip
import random



def generate():
    global scvalue, scvalue2
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.hexdigits
    s5 = string.punctuation
    
    try:
        plen = scvalue2.get()
    except:
        msg.showerror("notification", "Please write any password length below")

    s = []
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    s.extend(s5)
    random.shuffle(s)
    
    scvalue.set("".join(s[0:plen]))
    screen.update()


def clear():
    global scvalue, scvalue2
    scvalue.set("")
    screen.update
    scvalue2.set("")
    screen2.update()

def copied():
    global scvalue
    text = scvalue
    pyperclip.copy(text)
    msg.showinfo("Notification", "Your password has been copied successfully")

root = Tk()
root.geometry("600x300")
root.maxsize(600, 300)
root.minsize(600, 300)
root.configure(bg="maroon")
root.iconbitmap("icon.ico")
root.title("Password generator")

scvalue = StringVar()
scvalue.set("")
scvalue2 = IntVar()
scvalue2.set("")
TextArea = scvalue.get()
##########################Entry box
screen = Entry(root, textvar=scvalue, font="cursive 30 bold", bd=8, width=27)
screen.pack()

screen2 = Entry(root, textvar=scvalue2, font="cursive 18 bold", bd=5, width=15)
screen2.place(x=350, y=120)

##########################Labels
length = Label(root, text="Password length 👉🏻", font="consolas 20 italic underline", bg="maroon", fg="White")
length.place(x=50, y=120)

##########################Button images
erase = PhotoImage(file="2.png")
erase = erase.subsample(2, 2)

password = PhotoImage(file="pass.png")
password = password.subsample(2, 2)

##########################Frames and buttons

b = Button(root, text=" Generate", font="consolas 20 bold", bd=5, activebackground="red", image=password, compound=LEFT, command=generate)
b.place(x=100, y=200)

b = Button(root, text=" Clear", font="consolas 20 bold", bd=5, activebackground="red", image=erase, compound=LEFT, command=clear)
b.place(x=360, y=200)


root.mainloop()