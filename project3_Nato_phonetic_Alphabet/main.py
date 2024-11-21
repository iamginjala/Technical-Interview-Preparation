import pandas

# Read the NATO phonetic alphabet data from CSV
# Expects a CSV with 'letter' and 'code' columns
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary mapping letters to their phonetic codes
# Using dictionary comprehension with pandas iterrows()
# Example: {'A': 'Alpha', 'B': 'Bravo', ...}
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    """
    Convert user input word to NATO phonetic alphabet representation.
    
    Workflow:
    1. Prompt user for a word
    2. Convert to uppercase
    3. Map each letter to its phonetic code
    4. Handle potential non-letter inputs
    """
    # Get word input and convert to uppercase
    word = input("Enter a word: ").upper()
    
    try:
        # Use list comprehension to convert each letter to phonetic code
        # Raises KeyError if any character is not a letter
        output_list = [phonetic_dict[letter] for letter in word]
    
    except KeyError:
        # If non-letter input is detected, recursively call the function
        print("Sorry, only letters. Please try again.")
        generate_phonetic()
    
    else:
        # Print the phonetic representation of the word
        print(output_list)

# Run the phonetic conversion
generate_phonetic()
