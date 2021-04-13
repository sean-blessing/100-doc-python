from tkinter import *

def button_clicked():
    miles_int = float(miles_text.get())
    print(miles_int)
    km_result_label["text"] = round(miles_int / .62137)

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#miles_text (0,1)
miles_text = Entry(width=10)
miles_text.grid(row=0, column=1)

#miles_label (0,2)
miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(row=0, column=2)

#equals_label (1,0)
equals_label = Label(text="is equal to", font=("Arial", 24, "bold"))
equals_label.grid(row=1, column=0)

#km_result_label (1,1)
km_result_label = Label(text="0", font=("Arial", 24, "bold"))
km_result_label.grid(row=1, column=1)

#km_label (1,2)
km_label = Label(text="Km", font=("Arial", 24, "bold"))
km_label.grid(row=1, column=2)

#button (2,1)
button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)

window.mainloop()