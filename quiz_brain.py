import html
import random


class QuizBrain:
    """This class is responsible for keeping score and asking & checking the questions."""
    
    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        
        all_answers = [current_question.wrong_answer, [current_question.answer]]
        choices = [item for sublist in all_answers for item in sublist]
        random.shuffle(choices)
        
        self.question_number += 1
        
        options = {chr(ord('A') + i): choice for i, choice in enumerate(choices)}
        correct_letter = [letter for letter, choice in options.items() if choice == current_question.answer][0]
        
        print(f'Q.{self.question_number}: {html.unescape(current_question.text)}')
        
        for letter, choice in options.items():
            print(f'{letter}: {html.unescape(choice)}')
        
        user_answer = input('Your answer: ')
        
        self.check_answer(user_answer, correct_letter)
    
    def check_answer(self, user_answer, correct_letter):
        if user_answer.upper() == correct_letter:
            self.score += 1
            print('\n')
            print('*************************')
            print('You got it right !')
        else:
            print('\n')
            print('*************************')
            print('That\'s wrong!!!')
            print(f'The correct answer was: {correct_letter}.')
        print(f'Your score is: {self.score}/{self.question_number}')
        print('*************************')
        print('\n')
