class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    
    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        response = input(f"{self.question_number}. {question.text}. (True/False)?: ").lower()
        self.check_answer(response, question.answer)
        
    def check_answer(self, resp, ans):
        if resp.lower() == ans.lower():
            self.score += 1
            print(f"Your answer is correct. Your score is {self.score}/{self.question_number}")
        else:
            print(f"Your answer is incorrect. Your score is {self.score}/{self.question_number}")
        print()