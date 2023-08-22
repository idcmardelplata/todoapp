class Task():
    def __init__(self, label:str, status: str) -> None:
        self._label = label
        self._status = status

    def title(self):
        return self._label

    def status(self):
       return self._status
