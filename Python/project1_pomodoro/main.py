import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
# Color scheme for the application
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# Timer durations in minutes
WORK_MIN = 1          # Duration for work sessions
SHORT_BREAK_MIN = 1   # Duration for short breaks
LONG_BREAK_MIN = 20   # Duration for long breaks
reps = 0             # Counter for tracking number of sessions
timer = None         # Variable to store timer object

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    """Resets the timer and clears all progress indicators"""
    global reps
    window.after_cancel(timer)  # Cancel any running timer
    canvas.itemconfig(timer_text, text='00:00')  # Reset display
    label1.config(text='Timer', fg=GREEN)        # Reset header
    check_mark.config(text='')                   # Clear checkmarks
    reps = 0                                     # Reset session counter

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    """Starts the timer and manages the flow between work and break sessions"""
    global reps
    reps += 1
    
    # Convert minutes to seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    # Determine which type of session to start
    if reps % 8 == 0:  # Every 4th work session, take long break
        count_down(long_break_sec)
        label1.config(text='Break', fg=RED)
    elif reps % 2 == 0:  # After each work session, take short break
        count_down(short_break_sec)
        label1.config(text='Break', fg=PINK)
    else:  # Work session
        count_down(work_sec)
        label1.config(text='Work', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    """Manages the countdown display and timer updates"""
    # Convert seconds to minutes and seconds for display
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    # Format seconds to always show two digits
    if count_sec < 10:
        count_sec = f'0{count_sec}'
        
    # Update timer display
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    
    if count > 0:
        global timer
        # Schedule next update in 1 second
        timer = window.after(1000, count_down, count - 1)
    else:
        # Start next session when timer reaches 0
        start_timer()
        # Update checkmarks for completed work sessions
        mark = ''
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            mark += '✔'
        check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
# Create main window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Create canvas for tomato image and timer
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Create and configure UI elements
label1 = Label(text="Timer", font=(FONT_NAME, 40), fg=GREEN)
label1.config(pady=10, padx=10, bg=YELLOW, fg=GREEN)
label1.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)

# Start the application
window.mainloop()
