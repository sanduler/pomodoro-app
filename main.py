# Ruben Sanduleac
# The Pomodoro app employs a timer to divide work into intervals of 25 minutes each, separated by short breaks.
# This program uses Francesco Cirillo Pomodoro Technique is a time management method. The program utilizes
# concepts such as timeboxing and iterative and incremental development commonly used in software design

import tkinter
import time
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

# TODO: ---------------------------- TIMER RESET ------------------------------- #

# TODO: ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """This function is responsible for
    the response from the button click"""
    count_down(5*60)

# TODO: ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """This function is responsible for displaying the
    minutes and seconds of the timer"""
    minutes = math.floor(count / 60)
    seconds = math.floor(count % 60)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        window.after(1000, count_down, count - 1)
# TODO: ---------------------------- UI SETUP ------------------------------- #
# initilize the tkinter Class
window = tkinter.Tk()
# change the title of the screen
window.title("Pomodoro")
# set the window size and background
window.config(padx=140, pady=50, bg=YELLOW)


# create a new canvas and set the windth, hieght, and change
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# imported the image file to add to canvas
tomato_img = tkinter.PhotoImage(file="img/pomodoro.png")
# adjisted the image on the window
canvas.create_image(100, 112, image=tomato_img)
# added the text layered on top of the picture
timer_text = canvas.create_text(100, 133, text="00:00", fill="white", font=(FONT_NAME, 36, "bold"))
# pack the canvas
canvas.grid(column=2, row=2)
# timer label above the tomato_img
timer_label = tkinter.Label()
# Config for the label
timer_label.config(text="Timer", font=(FONT_NAME, 36), bg=YELLOW, fg=GREEN)
# location
timer_label.grid(column=2, row=0)

# count_down(5)

start_button = tkinter.Button(text="Start", command=start_timer)
start_button.grid(row=3, column=0)

reset_button = tkinter.Button(text="Reset")
reset_button.grid(row=3, column=3)

check_mark = tkinter.Label(text="✔", fg=GREEN, bg=YELLOW)
check_mark.grid(column=2, row=4)
# center the window to the middle of the screen
window.eval('tk::PlaceWindow . center')
# prevent the screen from closing
window.mainloop()
