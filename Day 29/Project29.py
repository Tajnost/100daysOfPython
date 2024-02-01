from tkinter import *
from tkinter import messagebox
from time import sleep
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)      
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_file():
    name = website_entry.get()
    username = email_entry.get()
    password = password_entry.get()

    if len(name) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo("Error", "Please check if you have any more stuff to fill")
    else:
        is_ok = messagebox.askyesno(title=username, message=f"This are you credentials :Name: {name} \n Username: {username} \n Password: {password} \n Is it ok to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(name + " | " + username + " | " + password + "\n")
                sleep(0.5)
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

###Website

website_label = Label(text="Website:", font=("Arial"))
website_label.grid(column=0, row=1)
website_entry = Entry(width=55)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus() # This starts the typing in this label

## Email/Username

email = Label(text="Email/Username:", font=("Arial"))
email.grid(column=0, row=2,)
email_entry = Entry(width=55)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "vid@tajnost.si")   # 0 is insert your email at start

## Password

password_generate = Label(text="Password:", font=("Arial"))
password_generate.grid(column=0, row=3)
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

## Add
add_button = Button(text="Add", width=47, command=save_file)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()