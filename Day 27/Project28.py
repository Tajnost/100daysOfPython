from tkinter import *
from time import sleep

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

sleepy = True
minutez = 0
secs = 0
checkmarks = 1
breakNow = False
# ---------------------------- TIMER RESET ------------------------------- #

def  resetTimer():
   global sleepy, minutez, secs, breakNow, yolo
   breakNow = True
   sleepy = False
   yolo = True
   minutez = 0
   secs = 0
   canvas.itemconfig(timerUpdate, text=f"{minutez:02d}:{secs:02d}")
   window.update()
#


# ---------------------------- TIMER MECHANISM ------------------------------- #


def update_timer():
    global sleepy,minutez,secs,checkmarks,breakNow,yolo
    breakNow = False
    sleepy = True
    while sleepy == True:
        sleep(0.01)
        if secs == 59:
            minutez += 1
            secs = 0
        else:
            secs += 1
            if breakNow == True:
                resetTimer()
                break
        canvas.itemconfig(timerUpdate, text=f"{minutez:02d}:{secs:02d}")
        window.update()
        if minutez == 25:
            checkmarks += 1
            sleepy = False
            yolo = False
            bottomMid["text"] = f"{checkmarks:02d}"
    while checkmarks < 3:
        countdown()
    else:
        minutez = 30
        secs = 00
        helloWorld()

def helloWorld():
    global sleepy, minutez, secs, checkmarks, breakNow, yolo
    while yolo == False:
        if breakNow == True:
            resetTimer()
            break
        if secs == 0:
            minutez -= 1
            secs = 59
            print(secs)
            while secs > 0:
                sleep(0.01)
                secs -= 1
                canvas.itemconfig(timerUpdate, text=f"{minutez:02d}:{secs:02d}")
                window.update()
                if breakNow == True:
                    resetTimer()
                    break
                if secs == 1 and minutez == 0 and checkmarks < 3:
                    sleepy = True
                    yolo = True
                    update_timer()




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown():
    global minutez, secs, sleepy, yolo, breakNow,checkmarks
    minutez = 5
    secs = 0
    while yolo == False:
        if breakNow == True:
            resetTimer()
            break
        if secs == 0:
            minutez -= 1
            secs = 59
            print(secs)
            while secs > 0:
                sleep(0.01)
                secs -= 1
                canvas.itemconfig(timerUpdate, text=f"{minutez:02d}:{secs:02d}")
                window.update()
                if breakNow == True:
                    resetTimer()
                    break
                if secs == 1 and minutez == 0:
                    sleepy = True
                    yolo = True
                    checkmarks = 0
                    update_timer()



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, background=YELLOW)

# ----------------- LABEL TOP
topTimer = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, background=YELLOW)
topTimer.grid(row=0, column=1)

# ------------------- Tomato plus timer
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_imag = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_imag)
timerUpdate = canvas.create_text(100, 132, text="00:00", fill="White", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# ------------------ BOTTOM BUTTONS
bottomLeft = Button(text="Start", font=(FONT_NAME, 15, "bold"), command=update_timer)
bottomLeft.grid(row=2, column=0)

bottomMid = Label(text="✓", font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
bottomMid.grid(row=3, column=1)

bottomRight = Button(text="Reset", font=(FONT_NAME, 15, "bold"), command=resetTimer)
bottomRight.grid(row=2, column=2)

window.mainloop()
