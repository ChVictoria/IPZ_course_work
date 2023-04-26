from enum import Enum
class Task_type(str, Enum):
    MUL_CHOICE = 'multiple choice'
    MUL_ANSWERS = 'multiple answers'
    FILL_IN_BLANK = 'fill in blank'

class Task:
    def __init__(self,type:Task_type):
        self.type = type
        self.question = None
        self.answer = None
        self.explanation = None
        if self.type != Task_type.FILL_IN_BLANK:
            self.alternatives = list()

    @property
    def type(self):
        return self.type

    @type.setter
    def type(self, new_type:Task_type):
        self.type = new_type

    @property
    def question(self):
        return self.question

    @question.setter
    def question(self, new_question):
        self.question = new_question

    @property
    def answer(self):
        return self.answer

    @answer.setter
    def answer(self, new_answer):
        self.answer = new_answer

    def add_alternative(self, alternative):
        self.alternatives.append(alternative)

    def delete_alternative(self, alternative):
        self.alternatives.remove(alternative)

    @property
    def explanation(self):
        return self.explanation

    @explanation.setter
    def explanation(self, explanation):
        self.explanation = explanation

    @explanation.deleter
    def explanation(self):
        self.explanation = None

