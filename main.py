from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Comic Sans"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
text = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global text, reps
    window.after_cancel(timer)
    label.config(text="Pomodoro app for working")
    canvas.itemconfig(timer_text, text="0.00")
    text = ""
    check_marks.config(text=text)
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    if reps % 8 == 0:
        label.config(text="Nice job, Kapitano")
        count_down(LONG_BREAK_MIN*60)
        reps = 1
    elif reps % 2 != 0:
        label.config(text="Pomodoro is watching you work!")
        count_down(WORK_MIN*60)
        reps += 1
    elif reps % 2 == 0:
        label.config(text="Quick brake")
        count_down(SHORT_BREAK_MIN*60)
        reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global text, timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if reps % 2 != 0:
            text += "✔"
            check_marks.config(text=text)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Kapitan Pomodoro")
window.config(pady=25, padx=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="0.00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

label = Label(text="Pomodoro app for working")
label.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
label.grid(column=1, row=0)

button = Button(text="Start", command=start_timer)
button.grid(column=0, row=2)

button = Button(text="Reset", command=reset_timer)
button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()
