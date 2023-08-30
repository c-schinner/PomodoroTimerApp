from tkinter import *
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
timer = ""


# ---------------------------- TIMER RESET ----------------------------------- #
def reset_button():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    completion_label.config(text=" ")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_button():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        timer_label.config(text="Work Time", fg=RED)
        countdown(work_sec)
    elif reps % 8 == 0:
        timer_label.config(text="Big Break", fg=GREEN)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break Time", fg=PINK)
        countdown(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_button()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "I"
            completion_label.config(text=marks)


# Our window setup
window = Tk()
window.title("Work Timer")
window.config(padx=50, pady=50, bg=YELLOW)

# Our canvas setup with the image and timer on the image
canvas = Canvas(width=250, height=250, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(125, 125, image=photo)
timer_text = canvas.create_text(125, 150, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Our Labels, timer and completion of sessions
timer_label = Label(window, text="Timer", bg=YELLOW, fg=GREEN, font=("Italic", 30, "bold"))
timer_label.grid(column=1, row=0)
timer_label.config(padx=5, pady=5)

completion_label = Label(window, bg=YELLOW, fg=GREEN, font=("Italic", 20, "bold"))
completion_label.grid(column=1, row=3)
completion_label.config(padx=5, pady=5)


# Our button setup, start and reset
start = Button(window, text="Start", bg=YELLOW, fg="black", font=("Italic", 10, "bold"), command=start_button)
start.grid(column=0, row=2)
start.config(padx=5, pady=5)

reset = Button(window, text="Reset", bg=YELLOW, fg="black", font=("Italic", 10, "bold"), command=reset_button)
reset.grid(column=2, row=2)
reset.config(padx=5, pady=5)


window.mainloop()
