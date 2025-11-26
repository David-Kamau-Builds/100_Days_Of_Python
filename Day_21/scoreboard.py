from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")
SCORE_FILE = "Day_21/score_sheet.txt"

try:
    with open(SCORE_FILE) as file:
        highscore = int(file.read())
except (FileNotFoundError, ValueError):
    highscore = 0

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = highscore
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)  # top of screen
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        with open(SCORE_FILE, mode="w") as score_sheet:
            score_sheet.write(f"{self.high_score}")

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(SCORE_FILE, mode="w") as new_file:
                new_file.write(f"{self.high_score}")
        self.score = 0
        self.write_score()

    def increase(self):
        self.score += 1
        self.write_score()