class Quiz:
    def __init__(self):
        self.tasks = list()
        self.time = None

    @property
    def time(self):
        return self.time

    @time.setter
    def explanation(self, time):
        self.time = time

    @time.deleter
    def time(self):
        self.time = None

    def add_task(self, task:Task):
        self.tasks.append(task)

    def delete_task(self, alternative):
        self.alternatives.remove(alternative)

    def save(self):
        pass

