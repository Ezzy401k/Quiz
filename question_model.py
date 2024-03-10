class Question:
    def __init__(self, question, answer):
        """
        Initializes a Question object with the provided question and answer.

        Args:
        question (str): The text of the question.
        answer (str): The correct answer to the question.
        """
        self.text = question  # Stores the question text
        self.answer = answer  # Stores the correct answer
