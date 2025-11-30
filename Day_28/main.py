from tkinter import *
from tkinter import ttk
import math
import threading
import platform
import subprocess
import os
from plyer import notification
import pystray
from pystray import MenuItem as item
from PIL import Image

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

CANVAS_FONT = ("Courier", 35, "bold")
LABEL_FONT = ("Courier", 35, "normal")
CHECKMARKS_FONT = ("Courier", 25, "normal")

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

REPS = 0
timer = None
tray_icon = None
window_hidden = False

# ---------------------------- DEFAULT CROSS-PLATFORM SOUND ------------------------------- #
def play_sound():
    system = platform.system()

    try:
        # Windows → built-in alert beep
        if system == "Windows":
            import winsound
            winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)

        # macOS → built-in system audio
        elif system == "Darwin":
            subprocess.run(["afplay", "/System/Library/Sounds/Glass.aiff"])

        # Linux → use common freedesktop, PulseAudio, or ALSA fallsbacks
        else:
            # PulseAudio (Ubuntu, Mint, KDE, etc.)
            if os.system("paplay /usr/share/sounds/freedesktop/stereo/complete.oga") != 0:
                # ALSA fallback
                os.system("aplay /usr/share/sounds/alsa/Front_Center.wav >/dev/null 2>&1")

    except Exception as e:
        print("Sound error:", e)

# ---------------------------- POPUP NOTIFICATION ------------------------------- #
def show_notification(title, message):
    try:
        notification.notify(title=title, message=message, timeout=5)
    except:
        print("Notification failed.")

# ---------------------------- TRAY ICON ------------------------------- #
def create_tray_icon():
    global tray_icon

    image = Image.open("tray_icon.png")  # Your tray icon file

    tray_icon = pystray.Icon(
        "Pomodoro",
        image,
        "Pomodoro Timer",
        menu=pystray.Menu(
            item("Show", on_show_window),
            item("Exit", on_exit_app)
        )
    )

    tray_icon.run()

def hide_window_to_tray():
    global window_hidden

    window.withdraw()
    window_hidden = True

    threading.Thread(target=create_tray_icon, daemon=True).start()

def on_show_window():
    global window_hidden, tray_icon

    if tray_icon:
        tray_icon.stop()
    window_hidden = False
    window.deiconify()

def on_exit_app():
    global tray_icon
    if tray_icon:
        tray_icon.stop()
    window.destroy()

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS, timer

    if timer:
        window.after_cancel(timer)
    REPS = 0

    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmarks_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
        show_notification("Pomodoro", "Long Break Started 🧘")
    elif REPS % 2 == 0:
        timer_label.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
        show_notification("Pomodoro", "Short Break Time ☕")
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
        show_notification("Pomodoro", "Work Session Started 💻")

# ---------------------------- COUNTDOWN ------------------------------- #
def count_down(count):
    global timer

    minutes = count // 60
    seconds = count % 60

    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        play_sound()

        if REPS % 2 == 1:
            marks = "✔" * (REPS // 2)
            checkmarks_label.config(text=marks)

        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Rounded button style
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "RoundedButton.TButton",
    font=("Arial", 14),
    padding=10,
    relief="flat",
    background=GREEN,
)

style.map("RoundedButton.TButton",
    background=[("active", "#7ecf93")]
)

# Timer label
timer_label = Label(text="Timer", font=LABEL_FONT, fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# Tomato canvas
canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=CANVAS_FONT)
canvas.grid(column=1, row=1)

# Buttons
start_button = ttk.Button(text="Start", style="RoundedButton.TButton", command=start_timer)
start_button.grid(column=0, row=2, padx=10)

reset_button = ttk.Button(text="Reset", style="RoundedButton.TButton", command=reset_timer)
reset_button.grid(column=2, row=2, padx=10)

minimize_button = ttk.Button(
    text="Minimize to Tray",
    style="RoundedButton.TButton",
    command=hide_window_to_tray
)
minimize_button.grid(column=1, row=4, pady=15)

# Checkmarks
checkmarks_label = Label(fg=GREEN, bg=YELLOW, font=CHECKMARKS_FONT)
checkmarks_label.grid(column=1, row=3)

window.mainloop()