from tkinter import *  # Importing tkinter for GUI
from tkinter import messagebox  # For displaying message boxes
from random import randint, choice, shuffle  # For generating random password components
import pyperclip  # To copy text to clipboard
import json  # For handling JSON file operations

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password():
    """
    Generates a random password consisting of letters, symbols, and numbers.
    Inserts the generated password into the password entry field and copies it to the clipboard.
    """
    letters = [chr(c) for c in range(65, 91)] + [chr(c) for c in range(97, 123)]  # A-Z and a-z
    numbers = [str(n) for n in range(10)]  # 0-9
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']  # Common special characters

    # Creating randomized parts of the password
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Combine and shuffle password parts
    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)
    strong_password = "".join(password_list)

    # Display and copy password
    password_entry.insert(0, strong_password)
    pyperclip.copy(f'{strong_password}')

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """
    Saves the website, email/username, and password to a JSON file.
    If any field is empty, a warning is displayed.
    If the JSON file doesn't exist, it creates one.
    """
    web = website_entry.get().lower()  # Get website name and convert to lowercase
    username = Email_entry.get()  # Get email/username
    passwords = password_entry.get()  # Get password

    # New data structure for saving
    new_data = {web: {'email': username, 'password': passwords}}

    # Validate inputs
    if len(web) == 0 or len(username) == 0 or len(passwords) == 0:
        messagebox.showwarning(title='Password Manager', message="Don't leave any fields empty")
    else:
        try:
            # Load existing data from JSON file
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            # Create a new file if none exists
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update existing data with new entry
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # Clear input fields
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    """
    Searches for a saved password by website.
    If found, displays the email/username and password.
    If not found, displays an appropriate message.
    """
    website = website_entry.get().lower()  # Get website name
    try:
        # Load data from JSON file
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No Data File Found')
    else:
        if website in data:
            # Display the found credentials
            messagebox.showinfo(
                title=website, 
                message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}"
            )
        else:
            messagebox.showinfo(title=website, message="No details for the website exist")

# ---------------------------- UI SETUP ------------------------------- #
# Create main window
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

# Canvas for logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')  # Load logo image
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website = Label(text='Website:')
website.grid(row=1, column=0)
Email = Label(text='Email/Username:')
Email.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)  # Website entry field
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()  # Focus cursor on this field
Email_entry = Entry(width=35)  # Email/username entry field
Email_entry.grid(row=2, column=1, columnspan=2)
Email_entry.insert(0, 'default@email.com')  # Pre-fill with default email
password_entry = Entry(width=35)  # Password entry field
password_entry.grid(row=3, column=1, columnspan=2)

# Buttons
search_button = Button(text='Search', command=find_password, width=10)  # Search button
search_button.grid(row=1, column=2)
password_button = Button(text='Generate Password', command=password)  # Generate password button
password_button.grid(row=3, column=2)
add_button = Button(text='Add', width=30, command=save)  # Save password button
add_button.grid(row=4, column=1, columnspan=2)

# Run the application
window.mainloop()
