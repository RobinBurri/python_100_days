import tkinter


def calculate():
    new_text = str(round(float(entry.get()) * 1.609, 2))
    label4.config(text=new_text)

window = tkinter.Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=500, height=500)

label1 = tkinter.Label(text="Miles")
label1.grid(column=2, row=0)
label2 = tkinter.Label(text="is equal to")
label2.grid(column=0, row=1)
label3 = tkinter.Label(text="Kms")
label3.grid(column=2, row=1)
label4 = tkinter.Label(text="")
label4.grid(column=1, row=1)

entry = tkinter.Entry(width=30)
entry.insert(tkinter.END, string="Enter miles.")
entry.grid(column=1, row=0)

button = tkinter.Button(text="Calulate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
