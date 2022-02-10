# Ruben Sanduleac
# The Pomodoro app employs a timer to divide work into intervals of 25 minutes each, separated by short breaks.
# This program uses Francesco Cirillo Pomodoro Technique is a time management method. The program utilizes
# concepts such as timeboxing and iterative and incremental development commonly used in software design

import tkinter

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

# TODO: ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# TODO: ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")

canvas = tkinter.Canvas(width=200, height=224)
tomato_img = tkinter.PhotoImage(file="img/pomodoro.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.pack()

# center the window to the middle of the screen
window.eval('tk::PlaceWindow . center')
window.mainloop()