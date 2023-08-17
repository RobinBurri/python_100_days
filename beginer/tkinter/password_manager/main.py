import tkinter
from tkinter import messagebox
import random
import string


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password(lenght=10):
    charachters = string.ascii_letters + string.digits
    random_string = "".join(random.choice(charachters) for _ in range(lenght))
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, random_string)


# ---------------------------- SAVE random_string------------------------------- #


def write_to_file(website_entered, email_entered, password_entered):
    entry = f"{website_entered} | {email_entered} | {password_entered}\n"
    with open("pswd.txt", "a", encoding="utf-8") as file:
        file.write(entry)


def save():
    website_entered = website_entry.get()
    email_entered = email_entry.get()
    password_entered = password_entry.get()

    if (len(website_entered.strip()) == 0 or len(email_entered.strip()) == 0 or len(password_entered.strip()) == 0):
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(
        title=website_entered,
        message=f"These are the details entered: \nEmail: {email_entered} "
        f"\nPassword: {password_entered} \nIs it ok to save?",
    )
    if is_ok:
        write_to_file(website_entered, email_entered, password_entered)
        website_entry.delete(0, tkinter.END)
        password_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = tkinter.Canvas(width=200, height=200)
lock_image = tkinter.PhotoImage(file="logo.gif")
canvas.create_image(100, 100, image=lock_image)

canvas.grid(column=1, row=0)

website = tkinter.Label(text="Website:")
website.grid(column=0, row=1)
email = tkinter.Label(text="Email/Username:")
email.grid(column=0, row=2)
password = tkinter.Label(text="Password:")
password.grid(column=0, row=3)

website_entry = tkinter.Entry(width=38)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = tkinter.Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "EzW2j@example.com")

password_entry = tkinter.Entry(width=21)
password_entry.grid(column=1, row=3)
button_generate = tkinter.Button(text="Generate Password", command=generate_password)
button_generate.grid(column=2, row=3)

button_add = tkinter.Button(text="Add", command=save, width=36)
button_add.grid(column=1, row=4, columnspan=2)


window.mainloop()
