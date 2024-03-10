from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import os

# Create a list to store Question objects
question_bank = []

# Populate question_bank with Question objects created from question_data
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Initialize a QuizBrain object with the question_bank
quiz = QuizBrain(question_bank)

# Loop through questions until there are no more questions left
while quiz.still_has_questions():
    quiz.next_question()

# Clear the console screen
os.system('cls')

# Display the final score to the user
print(f"You've completed the quiz. Your final score is: {quiz.score}/{quiz.question_number}")

# Wait for user input before exiting
input("Press Enter to Exit!")
