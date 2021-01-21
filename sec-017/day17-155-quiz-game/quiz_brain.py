class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.score = 0
        self.questions_list = list

    def next_question(self):
        q = self.questions_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {q.text} (True or False)? ")
        self.check_answer(ans, q.answer)

    def still_has_questions(self):
        return len(self.questions_list) > self.question_number

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is: {self.score} / {self.question_number}")
        print("\n")


