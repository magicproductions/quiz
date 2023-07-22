from question_model import Question
from quiz_brain import QuizBrain
from logo import game_over, quiz_game
import requests

# from dummy_data import dummy_data

response = requests.get('https://opentdb.com/api.php?amount=10&category=18')
response.raise_for_status()
question_data = response.json()['results']

print(quiz_game)

question_bank = [
    Question(q_text=question['question'],
             q_answer=question['correct_answer'],
             q_wrong_answer=question['incorrect_answers'],
             q_type=question['type']
             )
    for question in question_data
]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(game_over)
print('\n')
print('You\'ve completed the quiz')
print(f'Your final score is: {quiz.score}/{quiz.question_number}')

if quiz.score <= 3:
    print('You are 🤨 Try again!')
elif quiz.score <= 5:
    print('You need to study more 💻 Never give up!')
elif quiz.score <= 8:
    print('You are doing well 🥉 Keep going!')
elif quiz.score < 10:
    print('You are almost there 🥈 Keep going!')
else:
    print('You are a genius 😎 Congratulations 🏆🏆🏆🏆🏆')
