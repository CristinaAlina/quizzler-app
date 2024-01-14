from tkinter import *

THEME_COLOR = "#375362"
FONT_QUESTION = ("Arial", 15, "italic")
FONT_SCORE = ("Arial", 10, "bold")


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.iconbitmap("images/quiz_icon.ico")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", fg="white", justify="center", bg=THEME_COLOR, font=FONT_SCORE)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(bg="white", highlightthickness=0, height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, font=FONT_QUESTION, fill=THEME_COLOR, justify="center",
                                                     text="Question text", width=300)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=50)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_image, highlightthickness=0, bg=THEME_COLOR, width=100, height=97,
                                  border=0)
        self.true_button.grid(column=0, row=2, pady=10)
        self.false_button = Button(image=false_image, highlightthickness=0, bg=THEME_COLOR, width=100, height=97,
                                   border=0)
        self.false_button.grid(column=1, row=2, pady=10)

        self.window.mainloop()
