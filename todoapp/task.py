class Task():
    def __init__(self, label:str, status: str = "Pending") -> None:
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
