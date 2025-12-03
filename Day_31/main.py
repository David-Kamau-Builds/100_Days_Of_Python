from tkinter import *
import pandas
import random

RIGHT_IMAGE = "./images/right.png"
WRONG_IMAGE = "./images/wrong.png"
CARD_FRONT = "./images/card_front.png"
CARD_BACK = "./images/card_back.png"

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

# ---------------------------- LOAD DATA ------------------------------- #
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    data = original_data.copy()

data_list = data.to_dict(orient="records")

current_card = {}
flip_timer = None


# ---------------------------- FUNCTIONS ------------------------------- #
def next_card():
    """Pick a new random word and start the flip timer."""
    global current_card, flip_timer

    # Cancel scheduled flip
    if flip_timer is not None:
        window.after_cancel(flip_timer)

    current_card = random.choice(data_list)

    # French side
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(title_label, text="French", fill="black")
    canvas.itemconfig(word_label, text=current_card["French"], fill="black")

    flip_timer = window.after(3000, flip_card)


def flip_card():
    """Flip the card to show English translation."""
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(title_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=current_card["English"], fill="white")


def known_word():
    """Remove known word and save the updated data."""
    data_list.remove(current_card)
    new_data = pandas.DataFrame(data_list)
    new_data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file=CARD_FRONT)
card_back_img = PhotoImage(file=CARD_BACK)

card_background = canvas.create_image(400, 263, image=card_front_img)

title_label = canvas.create_text(400, 150, text="", font=TITLE_FONT)
word_label = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file=RIGHT_IMAGE)
wrong_img = PhotoImage(file=WRONG_IMAGE)

button_style = dict(
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    bg=BACKGROUND_COLOR,
    activebackground=BACKGROUND_COLOR,
    highlightbackground=BACKGROUND_COLOR
)

wrong_button = Button(image=wrong_img, command=next_card, **button_style)
wrong_button.grid(column=0, row=1)

right_button = Button(image=right_img, command=known_word, **button_style)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
