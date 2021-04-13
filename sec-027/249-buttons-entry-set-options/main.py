from tkinter import *

window = Tk()

window.title("My First GUI Program in Python")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
#my_label.pack(side="left")
my_label.pack()
my_label["text"] = "new text"
my_label.config(text="label text")

#button
def button_clicked():
    my_label["text"] = input.get()
    print("I got clicked!")
button = Button(text="Click Me", command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()




window.mainloop()