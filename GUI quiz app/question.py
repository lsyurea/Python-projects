import requests
import html


class Questions:
    def __init__(self):
        # _________API request______
        parameters = {
            'amount': 10,
            'category': 9,  # general knowledge
            'difficulty': 'medium',
            'type': 'boolean'

        }
        r = requests.get(url="https://opentdb.com/api.php", params=parameters)  # interaction with open trivia DB
        r.raise_for_status()
        data = r.json()['results']
        self.score = 0
        self.data = data
        self.question_number = 0
        self.current_question = None

    def still_questions_left(self):
        return self.question_number < len(self.data)

    def next_question(self):
        if self.still_questions_left():
            res = self.data[self.question_number]
            self.question_number += 1
            self.current_question = res
            return html.unescape(res['question'])

    def check_answer(self, user_answer):
        if user_answer == self.current_question['correct_answer']\
                and self.question_number <= 10:
            # note that the bool is represented in string format
            self.score += 1
            return True
        return False


