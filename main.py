from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


def search_info():
    searching = web_ent.get()
    try:
        with open("Data.json", 'r') as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File found.")

    else:
        if searching in data:
            password = data[searching]['Password']
            email = data[searching]["Email"]
            messagebox.showinfo(title=searching, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showerror(title=searching, message="There is not any info related to the keyword.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_symbols = [choice(symbols) for i in range(randint(2, 4))]
    password_numbers = [choice(numbers) for i in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = ''.join(password_list)

    pass_ent.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_data():
    website = web_ent.get()
    user = user_ent.get()
    password = pass_ent.get()
    new_data = {website: {'Email': user, 'Password': password}}
    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showerror(title='Error', message="Please don't leave any field empty.")
    else:
        try:
            with open('Data.json', 'r') as file:
                # Reading old data
                data = json.load(file)

        except FileNotFoundError:
            with open('Data.json', 'w') as file:
                json.dump(new_data, file, indent=4)

        else:
            # Updating the old data
            data.update(new_data)

            with open('Data.json', 'w') as file:
                # Writing the updated data to the json file
                json.dump(data, file, indent=4)

        finally:
            web_ent.delete(0, END)
            pass_ent.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


pm_window = Tk()
pm_window.title('Password Manager')
pm_window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
pic = PhotoImage(file='logo.png')

canvas.create_image(100, 100, image=pic)
canvas.grid(column=1, row=0)

web_lab = Label(text="Website:")
web_lab.grid(column=0, row=1)

user_name = Label(text="Email/Username:")
user_name.grid(column=0, row=2)

pass_lab = Label(text="Password:")
pass_lab.grid(column=0, row=3)

web_ent = Entry(width=17)
web_ent.grid(column=1, row=1)

user_ent = Entry(width=35)
user_ent.insert(0, "example@email.com")
user_ent.grid(column=1, row=2, columnspan=2)

pass_ent = Entry(width=17)
pass_ent.grid(column=1, row=3)

search = Button(text="Search", width=12, command=search_info)
search.grid(column=2, row=1)

generate = Button(text="Generate Password", command=password_generator)
generate.grid(column=2, row=3)

add = Button(text='Add', width=36, command=add_data)
add.grid(column=1, row=4, columnspan=2)
pm_window.mainloop()
