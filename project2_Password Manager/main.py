from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password():
    """
    Generate a strong, random password with mix of letters, numbers, and symbols.
    Copies generated password to clipboard and inserts into password entry field.
    """
    # Character sets for password generation
    letters = ['a', 'b', 'c', ..., 'Z']  # Full alphabet (lowercase and uppercase)
    numbers = ['0', '1', '2', ..., '9']  # Digits 0-9
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']  # Special characters

    # Generate random number of characters for each type
    password_letters = [choice(letters) for _ in range(randint(8, 10))]   # 8-10 letters
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]    # 2-4 symbols
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]    # 2-4 numbers

    # Combine and shuffle password characters
    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)
    
    # Convert list to string
    strong_password = "".join(password_list)
    
    # Insert password into entry and copy to clipboard
    password_entry.insert(0, strong_password)
    pyperclip.copy(f'{strong_password}')

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """
    Save website credentials to a text file after validation.
    Displays confirmation dialog and clears entry fields after saving.
    """
    # Retrieve entry values
    web = website_entry.get()
    username = Email_entry.get()
    passwords = password_entry.get()

    # Validate that no fields are empty
    if len(web) == 0 or len(username) == 0 or len(passwords) == 0:
        messagebox.showwarning(title='Password Manager', 
                                message="Don't leave any fields empty")
    else:
        # Confirm details before saving
        is_ok = messagebox.askokcancel(title='Password Manager',
                                        message=f'Confirm details:\n'
                                               f'Website: {web}\n'
                                               f'Email: {username}\n'
                                               f'Password: {passwords}')
        
        if is_ok:
            # Append credentials to data file
            with open('data.txt', 'a') as data_file:
                data_file.write(f"{web} | {username} | {passwords}\n")
            
            # Clear entry fields after saving
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
# Create main application window
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

# Create canvas for logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Website Entry
website = Label(text='Website:')
website.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()  # Set cursor focus to website entry

# Email/Username Entry
Email = Label(text='Email/Username:')
Email.grid(row=2, column=0)
Email_entry = Entry(width=35)
Email_entry.grid(row=2, column=1, columnspan=2)
Email_entry.insert(0, 'default@email.com')  # Pre-fill default email

# Password Entry and Generate Button
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)
password_entry = Entry(width=17)
password_entry.grid(row=3, column=1)
password_button = Button(text='Generate Password', command=password)
password_button.grid(row=3, column=2)

# Add Button to Save Credentials
add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# Start the application
window.mainloop()
