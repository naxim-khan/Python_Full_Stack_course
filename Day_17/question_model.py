# this model is used for question asking 
# then it sould contain an attribute text and may also hold the
# answer attribute which was going to check the correct answer.
from data import question_data
class Question:
    def __init__(self,q_text,q_answer):
        self.text=q_text
        self.answer=q_answer 

    