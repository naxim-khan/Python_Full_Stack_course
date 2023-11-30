# Ask Question from user (Also show them if the question is wrong or right)
# Give them a score 
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[] 

for question in question_data:
    question_text = question["question"]
    correct_answer = question["correct_answer"]
    new_question=Question(question_text,correct_answer)
    question_bank.append(new_question)
quiz=""
quiz=QuizBrain(question_bank)

while quiz.still_has_question:
    quiz.next_question()
print(f"You've completed the quiz\nYour final score was: {quiz.score}/{quiz.question_number}")