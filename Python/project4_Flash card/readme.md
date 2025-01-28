# Flashcard App: French to English Vocabulary Practice

A simple flashcard app built with Python and Tkinter to help users learn and practice common French words and their English translations.

## Features

- Displays a French word on a flashcard, flipping to reveal its English translation after 3 seconds.
- Users can mark words as "Known" or "Unknown."
- Tracks progress and saves unknown words for future practice.

## Data Collection Process

The vocabulary data was collected using the following steps:

1. **Source**: The list of the top 100 most frequently used French words was taken from the [Wiktionary Frequency Lists](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists).
2. **Translation**: The words were pasted into Google Sheets, and the following formula was used to translate them into English:
GOOGLETRANSLATE(text, source_language, target_language)
Example:
- Text: A French word like `bonjour`
- Source Language: `'fr'`
- Target Language: `'en'`
- Formula: `=GOOGLETRANSLATE("bonjour", "fr", "en")`
3. The resulting French-English pairs were exported as a CSV file (`french_words.csv`).

## How It Works

1. **Initial Vocabulary**:
- The app uses `french_words.csv` for the initial set of vocabulary.
- If a progress file (`words_to_learn.csv`) exists, it will load the user's saved progress instead.

2. **Flashcards**:
- French words are displayed first.
- After 3 seconds, the card flips to show the English translation.

3. **User Interaction**:
- Mark a word as "Known" to remove it from the practice set.
- Click "Unknown" to skip the word and keep it in the practice set.

4. **Progress Saving**:
- Words marked as "Known" are removed from the practice set and saved to `words_to_learn.csv`.

## Installation

### Prerequisites

- Python 3.x installed on your system.
- Required libraries:
- `tkinter` (comes with Python)
- `pandas`

## File Structure

- `main.py`: Main application script.
- `data/french_words.csv`: Initial vocabulary data.
- `data/words_to_learn.csv`: Progress tracking file (created automatically).
- `images/`: Folder containing card and button images.


## Future Enhancements

- Add sound pronunciations for French words.
- Include multiple language support.
- Allow users to add custom words.

Happy Learning! 😊
