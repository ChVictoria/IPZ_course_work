from enum import Enum


class Task_type(str, Enum):
    MUL_CHOICE = 'multiple choice'
    MUL_ANSWERS = 'multiple answers'
    FILL_IN_BLANK = 'fill in blank'


class Task:
    def __init__(self, type: Task_type):
        self.type = type
        self.question = None
        self.answer = None
        self.player_answer = None
        self.explanation = None
        if self.type != Task_type.FILL_IN_BLANK:
            self.alternatives = list()

    @property
    def type(self):
        return self.type

    @type.setter
    def type(self, new_type: Task_type):
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

    @property
    def player_answer(self):
        return self.answer

    @answer.setter
    def player_answer(self, new_player_answer):
        self.player_answer = new_player_answer

    @explanation.deleter
    def player_answer(self):
        self.player_answer = None

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

    def check_answer(self):
        if self.type == Task_type.MUL_ANSWERS:
            result = 0
            for alternative in player_answer:
                if alternative in answer:
                    result += 1
            return result / len(answer)
        else:
            if self.answer == self.player_answer:
                return 1
            return 0
