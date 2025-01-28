from tkinter import *  # GUI toolkit
import pandas  # For handling CSV files
import random  # For random selection of flashcards

# Set up the background color
BACKGROUND_COLOR = "#B1DDC6"

# Initialize variables for the current card and the words to learn
current_card = {}
to_learn = {}

# Load the data
try:
    # Try to load the words the user still needs to learn
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    # If the file doesn't exist, load the original list of French words
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")  # Convert to a list of dictionaries
else:
    to_learn = data.to_dict(orient="records")  # Convert to a list of dictionaries

# Function to display the next card
def next_card():
    """
    Displays the next flashcard with a French word.
    The card flips after 3 seconds to show the English translation.
    """
    global current_card, flip_timer
    # Cancel the previous flip timer to avoid overlap
    window.after_cancel(flip_timer)
    # Select a random word from the list
    current_card = random.choice(to_learn)
    # Update the card with the French word
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    # Set a timer to flip the card
    flip_timer = window.after(3000, func=flip_card)

# Function to flip the card and show the English translation
def flip_card():
    """
    Flips the current flashcard to show the English translation of the word.
    """
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

# Function to handle marking a word as known
def is_known():
    """
    Removes the current card from the list of words to learn and updates the CSV file.
    """
    to_learn.remove(current_card)  # Remove the word from the list
    data = pandas.DataFrame(to_learn)  # Create a DataFrame with the updated list
    data.to_csv("data/words_to_learn.csv", index=False)  # Save the updated list
    next_card()  # Show the next card

# Set up the main application window
window = Tk()
window.title("Flashy")  # Set the window title
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  # Set padding and background color

# Set a timer to flip the card
flip_timer = window.after(3000, func=flip_card)

# Set up the canvas for flashcards
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")  # Load the front card image
card_back_img = PhotoImage(file="images/card_back.png")  # Load the back card image
card_background = canvas.create_image(400, 263, image=card_front_img)  # Add the front card image
# Add text elements to the canvas
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)  # Remove border
canvas.grid(row=0, column=0, columnspan=2)

# Add "Unknown" button
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

# Add "Known" button
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# Display the first card
next_card()

# Run the application
window.mainloop()
