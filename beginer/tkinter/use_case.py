import tkinter


# Buttons
def action():
    print("Do something")


# Creating a new window and configurations
window = tkinter.Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

# Labels
label = tkinter.Label(text="This is old text")
label.config(text="This is new text")
label.grid(column=0, row=0)


# calls action() when pressed
button = tkinter.Button(text="Click Me", command=action)
button.grid(column=1, row=0)

# Entries
entry = tkinter.Entry(width=30)
# Add some text to begin with
entry.insert(tkinter.END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
entry.grid(column=2, row=0)

# Text
text = tkinter.Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(tkinter.END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", tkinter.END))
text.grid(column=0, row=1)


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.grid(column=2, row=1)


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.grid()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(
    text="Is On?", variable=checked_state, command=checkbutton_used
)
checked_state.get()
checkbutton.grid()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(
    text="Option1", value=1, variable=radio_state, command=radio_used
)
radiobutton2 = tkinter.Radiobutton(
    text="Option2", value=2, variable=radio_state, command=radio_used
)
radiobutton1.grid()
radiobutton2.grid()


# Listbox
def listbox_used(_):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid()
window.mainloop()