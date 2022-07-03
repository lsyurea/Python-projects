import tkinter
from question import Questions

# _________COLORS___________
GOLD = '#C5A554'
TEAL = '#49AA7c'


# _________Config screen_____
class QuizInterface:
    def __init__(self, quiz: Questions):
        self.quiz = quiz
        self.window = tkinter.Tk()
        self.window.title('Quizzler')

        self.window.config(bg=GOLD, padx=20, pady=20)

        self.score_label = tkinter.Label(text='Score: 0', fg='white', bg=GOLD)
        self.score_label.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250, bg=TEAL)
        self.question_text = self.canvas.create_text(150, 125, text='hello', fill='white',
                                                     width=250, font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        correct = tkinter.PhotoImage(file='images/true.png')
        wrong = tkinter.PhotoImage(file='images/false.png')
        self.correct_button = tkinter.Button(image=correct, highlightthickness=0, command=
        lambda: self.press_correct())
        self.correct_button.grid(row=2, column=0)
        self.wrong_button = tkinter.Button(image=wrong, highlightthickness=0, command=
        lambda: self.press_incorrect())
        self.wrong_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        qn = self.quiz.next_question()
        self.canvas.itemconfig(tagOrId=self.question_text, text=str(qn))

    def update_score(self):
        self.score_label.config(text=f'Score: {self.quiz.score}')

    def press_correct(self):
        res = self.quiz.check_answer('True')
        self.feedback(res)

    def press_incorrect(self):
        res = self.quiz.check_answer('False')
        self.feedback(res)

    def feedback(self, answer):
        if answer:
            self.update_score()
            self.flash('green')

        else:
            self.flash('red')

    def flash(self, color):
        self.canvas.config(bg=color)

        def helper():
            self.canvas.config(bg=TEAL)
            if self.quiz.still_questions_left():
                self.get_next_question()
            else:
                self.canvas.itemconfig(tagOrId=self.question_text, text=f'You scored {self.quiz.score}/10')
                self.correct_button.config(state='disabled')
                self.wrong_button.config(state='disabled')

        self.window.after(1000, helper)



