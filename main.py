import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


def generate_password():
    """a function responsible for generating a random password."""
    
    password_entry.delete(0, END)
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    rand_letters = [choice(letters) for _ in range(randint(8, 10))]
    rand_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    rand_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    
    password_list = rand_letters + rand_symbols + rand_numbers
    shuffle(password_list)
    
    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    """a function that save data entry to a Json file"""
    
    with open('data.json') as f:
        data = json.load(f)
    
    data.append(
        {
            'Website' : website_entry.get(),
            'Email'   : email_entry.get(),
            'Password': password_entry.get(),
            
        }
    )
    
    website = website_entry.get()
    email = email_entry.get()
    my_password = password_entry.get()
    
    if len(website) == 0 or len(my_password) == 0:
        messagebox.showinfo(title='Oops', message='Please make sure all field are not empty!!!')
    else:
        is_valid = messagebox.askokcancel(
            title=f'{website}',
            message=f'These are the details entered: Website: {website}\nEmail: {email}\n'
                    f'Password: {my_password}\nIs it ok to save?'
        )
        
        if is_valid:
            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4, separators=(',', ': '), ensure_ascii=False)
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        
        messagebox.showinfo(title='Success', message='Your data has been saved successfully.')


window = Tk()
window.title('Password Manager')
window.config(padx=100, pady=100)

canvas = Canvas(height=300, width=300)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(150, 150, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=38)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'info@my_email.com')

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_btn = Button(text='Generate Password', command=generate_password)
generate_password_btn.grid(row=3, column=2)

add_btn = Button(text='Add', width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
