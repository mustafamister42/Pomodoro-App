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
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    text1.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec="0{}".format(count_sec)
    canvas.itemconfig(timer_text,text="{}:{}".format(count_min,count_sec))
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start()
        mark=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            mark+="✔"
            check_mark.config(text=mark)
def start():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps%8==0:
        count_down(long_break_sec)
        text1.config(text="Break",fg=RED)
    elif reps%2==0:
        count_down(short_break_sec)
        text1.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        text1.config(text="Work",fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=112,bg=YELLOW)
text1=Label(text="Timer",fg=GREEN,font=(FONT_NAME,55,"bold"))
text1.grid(row=1,column=2)
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
photo=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=photo)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
#canvas.pack()
canvas.grid(row=2,column=2)
check_mark=Label(highlightthickness=0,bg=YELLOW,fg=GREEN)
check_mark.grid(row=6,column=2)
start_button=Button(text="Start",highlightthickness=0,command=start)
start_button.grid(row=5,column=1)
reset_button=Button(text="Reset",highlightthickness=0,command=reset)
reset_button.grid(row=5,column=3)


window.mainloop()

