# Ruben Sanduleac
# The Pomodoro app employs a timer to divide work into intervals of 25 minutes each, separated by short breaks.
# This program uses Francesco Cirillo Pomodoro Technique is a time management method. The program utilizes
# concepts such as timeboxing and iterative and incremental development commonly used in software design

import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def reset_timer():
    """This function is responsible for the resetting the game"""
    global reps
    reps = 0
    # sets the timer to None
    window.after_cancel(timer)
    # config the timer to 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # remove all the checkmarks
    check_mark.config(text="")
    # change the label back to being ready
    timer_label.config(text="Ready", font=(FONT_NAME, 36), bg=YELLOW, fg=RED)


def start_timer():
    """This function is responsible for
    the response from the button click"""
    global reps
    # increment the reps with each change
    reps += 1

    work_sec = WORK_MIN
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN

    # if there are 8 reps then we take a long 20 minute break
    if reps % 8 == 0:
        timer_rest()
        count_down(long_break_sec * 60)
    # every two reps we take a 5 minute break
    elif reps % 2 == 0:
        timer_rest()
        count_down(short_break_sec * 60)
    # else we work
    else:
        timer_work()
        count_down(work_sec * 60)


def count_down(count):
    """This function is responsible for displaying the
    minutes and seconds of the timer"""
    global timer
    # minutes logic we multiply milliseconds by 60 then we floor
    minutes = math.floor(count / 60)
    seconds = math.floor(count % 60)
    # if the seocnds are in the last 10 seconds we add a 0
    if seconds < 10:
        seconds = f"0{seconds}"
    # we print the minutes and seonds
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    # if the count is greater than 0 - we count cant be negative
    if count > 0:
        # we loop recursifly through the function
        timer = window.after(1000, count_down, count - 1)
    else:
        # we sart the time and we add a check mark for every two reps (work reps)
        start_timer()
        mark = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            mark += "✔"
        check_mark.config(text=mark)


def timer_work():
    """function responsible for work timer"""
    # Config for the label
    timer_label.config(text="Working", font=(FONT_NAME, 36), bg=YELLOW, fg=GREEN)
    # location
    timer_label.grid(column=2, row=0)


def timer_rest():
    """Function is responsible for rest timer"""
    # Config for the label
    timer_label.config(text="Break", font=(FONT_NAME, 36), bg=YELLOW, fg=PINK)
    # location
    timer_label.grid(column=2, row=0)


def start_screen():
    """Start screen"""
    # Config for the label
    timer_label.config(text="Ready", font=(FONT_NAME, 36), bg=YELLOW, fg=RED)
    # location
    timer_label.grid(column=2, row=0)


def buttons():
    """Buttons that are being displayed and the functions linked to them"""
    start_button = tkinter.Button(text="Start", command=start_timer)
    start_button.config(bd=0, highlightthickness=0, pady=2, padx=1)
    start_button.grid(row=3, column=0)

    reset_button = tkinter.Button(text="Reset", command=reset_timer)
    reset_button.config(bd=0, highlightthickness=0, pady=2, padx=1)
    reset_button.grid(row=3, column=3)


# initialize the tkinter Class
window = tkinter.Tk()
# change the title of the screen
window.title("Pomodoro")
# set the window size and background
window.config(padx=80, pady=80, bg=YELLOW)
# create a new canvas and set the width, height, and change
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# imported the image file to add to canvas
tomato_img = tkinter.PhotoImage(file="img/pomodoro.png")
# adjusted the image on the window
canvas.create_image(100, 112, image=tomato_img)
# added the text layered on top of the picture
timer_text = canvas.create_text(100, 133, text="00:00", fill="white", font=(FONT_NAME, 36, "bold"))
# pack the canvas
canvas.grid(column=2, row=2)
# timer label above the tomato_img
timer_label = tkinter.Label()
# function call to start_screen label
start_screen()
# function call for the buttons to generate to the screen
buttons()
# checkmarks label to be generated
check_mark = tkinter.Label(fg=GREEN, bg=YELLOW)
check_mark.config(text="")
check_mark.grid(column=2, row=4)
# center the window to the middle of the screen
window.eval('tk::PlaceWindow . center')
# prevent the screen from closing
window.mainloop()
