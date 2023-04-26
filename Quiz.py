from Task import *
class Quiz:
    def __init__(self):
        self.tasks = list()
        self.time = None

    @property
    def time(self):
        return self.time

    @time.setter
    def time(self, time):
        self.time = time

    @time.deleter
    def time(self):
        self.time = None

    def add_task(self, task_type:Task_type):
        task = Task(task_type)
        self.tasks.append(task)

    def delete_task(self, task:Task):
        self.tasks.remove(task)

    def save(self):
        return Memento(self.tasks, self.time)
    def restore(self, memento:Memento):
        self.tasks = memento.tasks
        self.time = memento.time

class Memento():
    def __init__(self, tasks, time):
        self.tasks = tasks
        self.time = time

    @property
    def time(self):
        return self.time

    @property
    def tasks(self):
        return self.tasks