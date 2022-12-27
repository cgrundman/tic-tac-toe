# Tic Tac Toe Game

from tkinter import *
from tkinter import messagebox

WHITE = "#f6f6f6"
FONT_NAME = "Arial"

window = Tk()
window.title("Tic-Tac-Toe")
window.config(padx=0, pady=0, bg=WHITE)

# "Website:" Label
website_label = Label(text="Tic-Tac-Toe", bg=WHITE, font=(FONT_NAME, 16, "bold"))
website_label.grid(column=0, row=0)

canvas = Canvas(width=500, height=500, bg=WHITE, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(250, 250, image=logo_img)
canvas.grid(column=0, row=1)


window.mainloop()

# from tkinter import *
# from tkinter import messagebox
# from random import choice, randint, shuffle
# import pyperclip
# import json
#
# WHITE = "#f6f6f6"
# FONT_NAME = "Arial"
#
#
# # ---------------------------- PASSWORD GENERATOR ------------------------------- #
#
#
# def generate_password():
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#                'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
#                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
#     password_letters = [choice(letters) for _ in range(randint(8, 10))]
#     password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
#     password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
#
#     password_list = password_letters + password_symbols + password_numbers
#
#     shuffle(password_list)
#
#     password = "".join(password_list)
#     pw_entry.insert(0, password)
#     pyperclip.copy(password)
#
#
# # ---------------------------- SAVE PASSWORD ------------------------------- #
#
#
# def save_pw():
#
#     website = website_entry.get()
#     email = email_entry.get()
#     password = pw_entry.get()
#     new_data = {
#         website: {
#             "email": email,
#             "password": password
#         }
#     }
#
#     if website == "" or password == "":
#         messagebox.showwarning(title="Empty Fields", message="Please don't leave any fields empty")
#     else:
#         try:
#             with open("data.json", "r") as data_file:
#                 # Reading old data
#                 data = json.load(data_file)
#         except FileNotFoundError or json.decoder.JSONDecodeError:
#             with open("data.json", "w") as data_file:
#                 json.dump(new_data, data_file, indent=4)
#         else:
#             # Updating old data with new data
#             data.update(new_data)
#
#             with open("data.json", "w") as data_file:
#                 # Saving updated data
#                 json.dump(data, data_file, indent=4)
#         finally:
#             pw_entry.delete(0, END)
#             website_entry.delete(0, END)
#             website_entry.focus_set()
#
# # ---------------------------- FIND PASSWORD ------------------------------- #
#
#
# def find_password():
#     website = website_entry.get()
#     try:
#         with open("data.json", "r") as data_file:
#             data = json.load(data_file)
#     except FileNotFoundError:
#         messagebox.showinfo(title="Error", message="No password file exists to search.")
#     else:
#         if website in data:
#             email = data[website]["email"]
#             password = data[website]["password"]
#             messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
#         else:
#             messagebox.showinfo(title=website, message=f"No password for {website} exist yet.")
#
#
# # ---------------------------- UI SETUP ------------------------------- #
#
#
# window = Tk()
# window.title("Password Manager")
# window.config(padx=50, pady=50, bg=WHITE)
#
# canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
# logo_img = PhotoImage(file="logo.png")
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(column=1, row=0)
#
# # "Website:" Label
# website_label = Label(text="Website:", bg=WHITE, font=(FONT_NAME, 12, "bold"))
# website_label.grid(column=0, row=1)
#
# # "Email/Username:" Label
# email_label = Label(text="Email/Username:", bg=WHITE, font=(FONT_NAME, 12, "bold"))
# email_label.grid(column=0, row=2)
#
# # "Password:" Label
# password_label = Label(text="Password:", bg=WHITE, font=(FONT_NAME, 12, "bold"))
# password_label.grid(column=0, row=3)
#
# # "Generate Password" Button
# reset_button = Button(text="Generate Password", font=(FONT_NAME, 12, "bold"), highlightthickness=0,
#                       command=generate_password)
# reset_button.grid(column=2, row=3)
#
# # "Add" Button
# reset_button = Button(text="Add", font=(FONT_NAME, 12, "bold"), highlightthickness=0, width=36, command=save_pw)
# reset_button.grid(column=1, row=4, columnspan=2)
#
# # "Search" Button
# search_button = Button(text="Search", font=(FONT_NAME, 12, "bold"), highlightthickness=0, width=15,
#                        command=find_password)
# search_button.grid(column=2, row=1)
#
# # Password entry
# pw_entry = Entry(width=32)
# # Gets text in entry
# print(pw_entry.get())
# pw_entry.grid(column=1, row=3)
#
# # Email entry
# email_entry = Entry(width=60)
# # Gets text in entry
# print(email_entry.get())
# email_entry.grid(column=1, row=2, columnspan=2)
# email_entry.insert(0, "christian.grundman@gmail.com")
#
# # Website entry
# website_entry = Entry(width=32)
# # Gets text in entry
# print(website_entry.get())
# website_entry.grid(column=1, row=1)
# website_entry.focus_set()
#
# window.mainloop()
