# Pomodoro Timer Application

A simple Pomodoro Timer built with Python and Tkinter. This application helps users manage their work sessions using the Pomodoro Technique, a time management method that uses a timer to break work into intervals.

## Features

- Work sessions of 25 minute
- Short breaks of 5 minute
- Long breaks of 20 minutes
- Visual timer display
- Track completed work sessions with checkmarks
- Start and reset functionality
- Visual feedback for different session types (work/break)

## Dependencies

- Python 3.x
- Tkinter (usually comes with Python)
- Required assets: `tomato.png` file in the same directory

## How It Works

The application follows the Pomodoro Technique pattern:
1. 1-minute work sessions
2. 1-minute short breaks after each work session
3. 20-minute long break after 4 work sessions
4. Visual checkmarks (✔) track completed work sessions

## Code Structure

The code is organized into several main components:

1. **Constants and Global Variables**
   - Color schemes
   - Font settings
   - Time intervals
   - Session tracking variables

2. **Timer Functions**
   - `reset_timer()`: Resets the timer and clears checkmarks
   - `start_timer()`: Manages the timer sequence and session types
   - `count_down()`: Handles the countdown mechanism

3. **UI Components**
   - Main window with tomato image
   - Timer display
   - Start/Reset buttons
   - Session progress indicators

## Usage

1. Run the script
2. Click "start" to begin a Pomodoro session
3. Timer will automatically cycle between work and break periods
4. Use "Reset" to stop and clear the timer

## Customization

You can modify the following constants at the top of the file to adjust the timer intervals:
```python
WORK_MIN = 25          # Duration of work sessions
SHORT_BREAK_MIN = 5    # Duration of short breaks
LONG_BREAK_MIN = 20    # Duration of long breaks
```


## Note
Make sure to have the `tomato.png` file in the same directory as the script for the timer image to display properly.
