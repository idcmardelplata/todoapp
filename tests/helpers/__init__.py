from todoapp.task import Task, TaskStatus

class MakeTask:
    def __init__(self):
        self._label = "Default task"
        self._status = TaskStatus.Pending

    def with_default_values(self):
        return self.build()

    def with_title(self, title = "Default title"):
        self._label = title
        return self

    def with_long_title(self, title = "Default title"):
        self._label = title * 500
        return self

    def with_status(self, status = TaskStatus.Pending):
        self._status = status
        return self

    def build(self):
        return Task(label=self._label, status=self._status)



