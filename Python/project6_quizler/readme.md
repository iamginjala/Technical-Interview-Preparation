# Quiz App

This Python project is a quiz application that dynamically generates questions and tracks the user's progress. It uses object-oriented programming principles to manage quiz logic, question data, and a user-friendly interface.

---

## Features
- Dynamically generates a quiz from a question bank.
- Tracks the user's score and progress.
- User-friendly interface for interacting with the quiz.

---

## Project Structure
The project consists of the following components:

1. **`question_model.py`**  
   Contains the `Question` class to define the structure of each question.

2. **`data.py`**  
   Contains the `question_data` list, which serves as the question bank.

3. **`quiz_brain.py`**  
   Contains the `QuizBrain` class, which handles quiz logic, such as:
   - Moving to the next question.
   - Checking the user's answer.
   - Keeping track of the score.

4. **`ui.py`**  
   Contains the `QuizInterface` class for managing the graphical user interface.

---

## Requirements
- Python 3.x
- A GUI library like `tkinter` (included in standard Python installation)

---

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/your-repo-name/quiz-app.git
    ```
2. Install any additional dependencies (if required):
    ```bash
    pip install -r requirements.txt
    ```

---

## How It Works
1. **Question Bank**: The `data.py` file contains the `question_data` list, where each question is a dictionary with keys:
   - `"question"`: The question text.
   - `"correct_answer"`: The correct answer ("True" or "False").

2. **Question Class**: The `Question` class in `question_model.py` creates objects for each question with its text and answer.

3. **QuizBrain**: The `QuizBrain` class in `quiz_brain.py`:
   - Handles quiz progression.
   - Checks user answers.
   - Tracks the score.

4. **Quiz Interface**: The `QuizInterface` class in `ui.py` provides a graphical user interface for users to interact with the quiz.

5. **Main Script**: The main script:
   - Populates the `question_bank` by creating `Question` objects.
   - Initializes the `QuizBrain` object.
   - Launches the `QuizInterface` for the user.

---

## Running the Application
1. Ensure all files (`question_model.py`, `data.py`, `quiz_brain.py`, `ui.py`) are in the same directory.
2. Run the main script:
    ```bash
    python main.py
    ```
3. Answer the quiz questions through the graphical user interface.

---

## Example Question Data
Here’s a sample format for `question_data` in `data.py`:

```python
question_data = [
    {"question": "The sky is blue.", "correct_answer": "True"},
    {"question": "Cats can fly.", "correct_answer": "False"},
    ...
]
