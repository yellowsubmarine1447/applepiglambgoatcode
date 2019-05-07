from tkinter import *

root = Tk()
password = "666"
unlocked = False
index = 0

frame_main = Frame(root, bd=10)
frame_main.pack()

txt = Label(frame_main, text="Enter the password found:", fg="black")
txt.pack()


def pop_up(msg):
    popup = Tk()
    popup.wm_title("Unlocked")
    label = Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    exit_button = Button(popup, text="Okay", command=popup.destroy)
    exit_button.pack()
    popup.mainloop()


class GetSequence:
    def __init__(self, text):
        self.text = text

    def __call__(self):
        global index
        global unlocked
        if password[index] == self.text:
            index += 1
        else:
            index = 0
        if index == len(password):
            root.destroy()
            pop_up("""Roses are red
Violets are fine
You did it! You did it!
The first is: ...""")


frame_right = Frame(root)
frame_right.pack()

numbers = list(range(1, 10))
numbers.append(0)

r = 0
c = 0

for x in range(1, 10):
    if x % 3 == 1 and x != 1:
        r += 1
        c = 0
    elif x != 1:
        c += 1

    globals()["button"+str(x)] = Button(frame_right, text=str(x), fg="black", width=5, command=GetSequence(str(x)))
    globals()["button"+str(x)].grid(row=r, column=c)

button0 = Button(frame_right, text="0", fg="black", width=5, command=GetSequence("0"))
button0.grid(row=3, column=1)

root.mainloop()
