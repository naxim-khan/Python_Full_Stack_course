from turtle import *
ALIGNMENT= "center"
FONT= ("Curior",15,"normal")






class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,270)
        self.hideturtle() 
        self.pu()
        self.score=0
        self.high_score=0
        with open("F:\\U-DEMY-COURSES\My_programms\\2nd_file\\Day_24\\1_SNAKEGAME_improve\\High_Score.txt") as score_file:
            self.high_score = int(score_file.read())
        self.color("white")



    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}\t\tHigh Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.goto(0,270)
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align=ALIGNMENT, font=FONT)
    

    def increase_score(self):
        self.score += 1
        self.clear()
        reset()
        self.update_score()
        


    def reset(self) :
        if self.score > self.high_score:
            self.high_score = self.score
            with open("F:\\U-DEMY-COURSES\My_programms\\2nd_file\\Day_24\\1_SNAKEGAME_improve\\High_Score.txt", mode="w") as score_file:
                score_file.write(str(self.high_score))
        self.score=0
        self.update_score()
        
        
