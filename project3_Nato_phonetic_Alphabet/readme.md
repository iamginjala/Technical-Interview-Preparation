# NATO Phonetic Alphabet Converter

## Overview
A Python script that converts user-input words into their corresponding NATO phonetic alphabet representation.

## Features
- Reads NATO phonetic alphabet from CSV
- Converts letters to phonetic codes
- Error handling for non-letter inputs
- Interactive word conversion

## Requirements
- Python 3.x
- Pandas library

## Installation
1. Clone the repository
2. Install required dependencies:
   ```
   pip install pandas
   ```

## Usage
1. Prepare a CSV file with columns: 'letter' and 'code'
2. Run the script
3. Enter a word when prompted
4. Receive phonetic alphabet representation

## Example
```
Enter a word: HELLO
Output: ['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
```

## Error Handling
- Only letters are accepted
- Non-letter inputs will prompt a retry

## Future Improvements
- Support for lowercase input
- Expanded character set support
- GUI interface
