from tkinter import *

def button_clicked():
    my_label["text"] = input.get()
    print("I got clicked!")

window = Tk()
window.title("My First GUI Program in Python")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "new text"
my_label.config(text="label text")
my_label.config(padx=50, pady=50)
my_label.grid(column=0, row=0)

#button
button_1 = Button(text="Click Me", command=button_clicked)
button_1.grid(column=1, row=1)

#button
button_2 = Button(text="New Button", command=button_clicked)
button_2.grid(column=2, row=0)

#input
input = Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()