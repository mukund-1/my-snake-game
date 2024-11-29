from turtle import Turtle
ALLIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
           self.high_score = int(data.read())
        self.color("#e5f1e3")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score {self.high_score}", align=ALLIGNMENT, font=FONT)

    def reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
            with open("data.txt","w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def Game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALLIGNMENT , font= FONT)


    def increase_score(self):
        self.score+= 1
        self.update_scoreboard()
       