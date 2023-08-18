import tkinter
from tkinter import messagebox
import random
import string
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password(lenght=10):
    charachters = string.ascii_letters + string.digits
    random_string = "".join(random.choice(charachters) for _ in range(lenght))
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, random_string)


# ---------------------------- SAVE random_string------------------------------- #


def write_to_file(website_entered, email_entered, password_entered):
    new_entry = {
        website_entered: {
            "email": email_entered,
            "password": password_entered,
        }
    }
    data = {}
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        pass
    finally:
        with open("data.json", "w") as f:
            data.update(new_entry)
            json.dump(data, f, indent=4)


def save():
    website_entered = website_entry.get()
    email_entered = email_entry.get()
    password_entered = password_entry.get()

    if (
        len(website_entered.strip()) == 0
        or len(email_entered.strip()) == 0
        or len(password_entered.strip()) == 0
    ):
        messagebox.showerror(
            title="Oops", message="Please don't leave any fields empty!"
        )
        return

    else:
        write_to_file(website_entered, email_entered, password_entered)
        website_entry.delete(0, tkinter.END)
        password_entry.delete(0, tkinter.END)


def search():
    website_entered = website_entry.get()
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="No data file found.")
    else:
        if website_entered in data:
            found_email = data[website_entered]["email"]
            found_password = data[website_entered]["password"]
            messagebox.showinfo(
                title=website_entered,
                message=f"Email: {found_email}\nPassword: {found_password}",
            )
        else:
            messagebox.showerror(
                title="Oops", message=f"No details for {website_entered} exists."
            )


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

website_entry = tkinter.Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()
search_button = tkinter.Button(text="Search", command=search, width=12)
search_button.grid(column=2, row=1)
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
