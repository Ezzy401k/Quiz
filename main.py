from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import os
question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():

    quiz.next_question()

os.system('cls')
print(f"You've completed the quiz, Your final score was : {quiz.score}/{quiz.question_number}")
input("Tap Enter to Exit!")