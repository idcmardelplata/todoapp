from enum import Enum

class TaskStatus(Enum):
    Pending = 1
    Done = 2

class Task():
    def __init__(self, label:str, status: TaskStatus = TaskStatus.Pending) -> None:
        self._size_of_label(label)
        self._label = label
        self._status = status

    def title(self):
        return self._label

    def status(self):
       return self._status

    def _size_of_label(self, label):
       if len(label) > 255:
          raise ValueError("El largo debe ser menor a 255 caracteres")

    def toggle_task(self):
        if self.status() == TaskStatus.Pending:
            self._status = TaskStatus.Done
        else:
            self._status = TaskStatus.Pending

