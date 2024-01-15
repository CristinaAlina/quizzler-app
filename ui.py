from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_QUESTION = ("Arial", 15, "italic")
FONT_SCORE = ("Arial", 10, "bold")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.iconbitmap("images/quiz_icon.ico")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", justify="center", bg=THEME_COLOR, font=FONT_SCORE)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(bg="white", height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, font=FONT_QUESTION, fill=THEME_COLOR,
                                                     text="Question text", width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=50)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_image, highlightthickness=0, bg=THEME_COLOR, width=100, height=97,
                                  border=0, command=lambda answer="True": self.check_button_pressed(answer))
        self.true_button.grid(column=0, row=2, pady=10)
        self.false_button = Button(image=false_image, highlightthickness=0, bg=THEME_COLOR, width=100, height=97,
                                   border=0, command=lambda answer="False": self.check_button_pressed(answer))
        self.false_button.grid(column=1, row=2, pady=10)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Gets next question and updates the screen accordingly"""
        question_text = self.quiz.next_question()
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, text=question_text)

    def check_button_pressed(self, answer):
        """If button true or false is pressed, receives as parameter the bool value and compare it with the correct
        answer. Updates the canvas background on the interface for user feedback and check if maximum no of questions is
         reached."""
        is_correct_answer = self.quiz.check_answer(answer)
        self.give_feedback(is_correct_answer)
        self.check_no_questions_left()

    def give_feedback(self, is_correct_answer):
        """Updates the canvas background on the interface for user feedback and update the score if answer is right"""
        if is_correct_answer:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")

    def check_no_questions_left(self):
        """Checks if max no of questions is reached. If yes, shows a final message to user.
        If not, gets the next question"""
        if self.quiz.still_has_questions():
            self.window.after(1000, self.get_next_question)
        else:
            self.window.after(1000, self.quiz_completed_feedback)
            self.window.after(5000, self.exit_program)

    def quiz_completed_feedback(self):
        """Shows a final message to user and set the state of true and false buttons to disabled"""
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text,
                               text=f"You've completed the quiz!\n"
                                    f"Your final score is: {self.quiz.score}/{self.quiz.question_number}.")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def exit_program(self):
        self.window.quit()
