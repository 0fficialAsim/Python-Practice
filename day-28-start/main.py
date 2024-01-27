from tkinter import *
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
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset(): 
    global reps 
    global checkMark
    reps = 0
    checkMark = "✓"

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps 
    global checkMark
    reps+=1 

    time_is_done = None
    work_seconds = 5
    short_seconds = 5
    long_seconds = 10

    if(reps % 2 != 0 ):
        time_label.config(text="Work")
        countdown(work_seconds)
    elif(reps % 8 == 0):
        time_label.config(text="Long Break", foreground=RED)    
        countdown(long_seconds)
    elif(reps % 2 == 0 ):
        countdown(short_seconds)
        time_label.config(text="Short Break",foreground=PINK)    


   

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    minute = math.floor( count / 60) 
    seconds  = count % 60 

    if seconds < 10: 
        seconds = f"0{seconds}"
   
    canvas.itemconfig(timerText, text=f"{minute}:{seconds}")
    if(count > 0):
        mainWindow.after(1000, countdown, count - 1)
    else:
        start_timer()
    
        if reps % 2 == 0:
            global checkMark
            checkMark += "✓"
            check_Label.config(text=checkMark)
# ---------------------------- UI SETUP ------------------------------- #
mainWindow = Tk()
mainWindow.title("Pomodoro Timer")
mainWindow.minsize(width=500,height=450)
mainWindow.config(padx=100, pady=50, background=YELLOW)


time_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), background= YELLOW, foreground= GREEN)
time_label.grid(column=2, row=1)

canvas = Canvas(width=220, height= 250, highlightthickness=0, background=YELLOW)
tomato_img = PhotoImage(file="day-28-start/tomato.png")
canvas.create_image(110, 125, image= tomato_img)
timerText = canvas.create_text(110,135, text="00:00", fill="white", font=("Courier", 35, "bold") )
canvas.grid(column=2, row=2)

checkMark = "✓"
check_Label = Label(text=checkMark, background=YELLOW, foreground=GREEN, font=(35))
check_Label.grid(column=2, row= 4)




start_butt = Button(text="Start", command= start_timer)
start_butt.grid(column= 1, row= 3)

reset_butt = Button(text="Reset", command=reset)
reset_butt.grid(column= 3, row=3)

mainWindow.mainloop()