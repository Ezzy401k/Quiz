class QuizBrain:
    def __init__(self, qlist):
        """
        Initializes a QuizBrain object with a list of questions.

        Args:
        qlist (list): List of Question objects.
        """
        self.question_number = 0  # Current question number
        self.question_list = qlist  # List of Question objects
        self.score = 0  # Current score

    def still_has_questions(self):
        """
        Checks if there are still questions left in the question list.

        Returns:
        bool: True if there are more questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Displays the next question and prompts the user for an answer.
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, current_answer):
        """
        Checks if the user's answer matches the correct answer.

        Args:
        user_answer (str): The user's answer.
        current_answer (str): The correct answer to the current question.
        """
        if user_answer.lower() == current_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        # Display the correct answer and current score
        print(f"The correct answer is: {current_answer}\n"
              f"Your current score is: {self.score}/{self.question_number}")
