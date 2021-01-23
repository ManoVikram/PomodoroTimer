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
reps = 1

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
def startTimer():
    global reps

    workSeconds = WORK_MIN * 60
    shortBreakSeconds = SHORT_BREAK_MIN * 60
    longBreakSeconds = LONG_BREAK_MIN * 60

    # countDown(5 * 60)

    if reps % 2:
        reps += 1
        titleLabel.config(text="WORK WORK WORK", bg=YELLOW, fg=RED, font=(24))
        countDown(workSeconds)
    elif reps % 2 == 0 and reps < 8:
        reps += 1
        titleLabel.config(text="TAKE A BREAK", bg=YELLOW, fg=GREEN, font=(24))
        countDown(shortBreakSeconds)
    else:
        reps = 1
        titleLabel.config(text="TAKE A LONG BREAK", bg=YELLOW, fg=PINK, font=(24))
        countDown(longBreakSeconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countDown(count):
    countMinutes = math.floor(count / 60)
    countSeconds = count % 60
    # if countSeconds == 0:
    #     countSeconds = "00"
    if countSeconds < 10:
        countSeconds = "0" + str(countSeconds)
    canvas.itemconfig(timerText, text=f"{countMinutes}:{countSeconds}")
    if count > 0:
        window.after(1000, countDown, count - 1)
    else:
        startTimer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=70, bg=YELLOW)

titleLabel = Label(text="Pomodoro Timer", bg=YELLOW, fg=RED)
titleLabel.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoImage = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomatoImage)
timerText = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 36, "bold"))
# canvas.pack()
canvas.grid(column=1, row=1)

startButton = Button(text="Start", highlightthickness=0, command=startTimer)
startButton.grid(column=0, row=2)

resetButton = Button(text="Reset", highlightthickness=0)
resetButton.grid(column=2, row=2)

checkmark = Label(text="✔", fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

window.mainloop()