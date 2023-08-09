import tkinter

window = tkinter.Tk()
window.title("Hello GUI World")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I'm a label", font=("Arial", 24))
my_label.pack()
my_label["text"] = "New Text"

# Button
def button_clicked():
    my_label.config(text=ipt.get())
    ipt.delete(0, tkinter.END)

button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()

# Entry

ipt = tkinter.Entry(width=10)
ipt.pack()

window.mainloop()
