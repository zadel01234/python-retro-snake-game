from turtle import Turtle
# import pyfiglet

# art3= pyfiglet.figlet_format("Game over", font = 'BLOODY')
# art = '''
#
#   ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███
#  ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
# ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
# ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄
# ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
#  ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
#   ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
# ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░
#       ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░
#                                                      ░
#
#
# '''




class Scoreboard(Turtle):
    def __init__(self,):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as highscore:
            content = highscore.read()
        self.highscore = int(content)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align = "center", font = ("Arial", 24, "normal"))
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as highscore:
                highscore.write(f"{self.highscore}")

        self.score = 0
        self.update_scoreboard()


    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write(f"GAME OVER !!!", align = "center",font = ("Arial", 24, "normal") )


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        # print(self.score)

