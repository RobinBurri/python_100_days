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
timer = ""
reps = 0
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps == 9:
        return
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
    else:
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.after(1000, count_down)

tomato_image = tkinter.PhotoImage(file="tomato.gif")

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(
    103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

title = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title.grid(column=1, row=0)

button_start = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)
button_reset = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=2)

checkmark = tkinter.Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmark.grid(column=1, row=3)


window.mainloop()