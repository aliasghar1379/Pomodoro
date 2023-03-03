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
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    label_1.config(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    if reps==0:
        reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if reps % 8 == 0:
            label_1.config(text="Break", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=RED)
            count_down(long_break_sec)
        elif reps % 2 == 0:
            label_1.config(text="Break", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=PINK)
            count_down(short_break_sec)
        else:
            label_1.config(text="Work", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
            count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    count_min = "{:02d}".format(count_min)
    count_sec = "{:02d}".format(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✓"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# TIMER
label_1 = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
label_1.grid(column=1, row=0)

# start button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# start button
stop_button = Button(text="Stop", highlightthickness=0, command=reset_timer)
stop_button.grid(column=2, row=2)

# check marks
check_marks = Label(font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
check_marks.grid(column=1, row=3)

window.mainloop()
