from tkinter import *
import math
import os
# import required module


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps = 0
check = '✓'
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    label.config(text="Timer")
    check_mark.config(text='')
    canvas.itemconfig(canvas_text, text="00:00")
    global reps
    reps = 0
    start_button.config(state='normal')
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    # window.after_cancel(timer)
    if True:
        print("True")
        start_button.config(state="disabled")
    
    reset_button.config(state="normal")
    global reps
    global check
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN)
        label.config(text="Break", fg = RED)
    elif reps % 2 == 0:  
        count_down(SHORT_BREAK_MIN)
        label.config(text="Break", fg = PINK)
        after_work = 'odu.wav'

        print('playing sound using native player')
        os.system("afplay " + after_work)
        
        
    else:
        
        count_down(WORK_MIN)
        work_session = math.floor(reps / 2)
        label.config(text="Work", fg = GREEN)
        window.bell()
        marks = ''
        for _ in range(work_session):
            marks += '✓'
        check_mark.config(text=marks)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(canvas_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
        
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- # 

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
label.grid(row=0, column=1)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
check_mark.grid(row=2, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text='start', highlightbackground=YELLOW, command=start_timer, state='normal')
start_button.grid(row=2, column=0)

reset_button = Button(text='reset', highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()

# window.attributes('-topmost', 1)
#  window.attributes('-topmost', 0)