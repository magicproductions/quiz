class Question:
    """A class to represent a question."""
    
    def __init__(self, q_text, q_answer, q_wrong_answer, q_type):
        self.text = q_text
        self.answer = q_answer
        self.wrong_answer = q_wrong_answer
        self.question_type = q_type
