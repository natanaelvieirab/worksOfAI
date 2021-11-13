class Population:
    def __init__(self, identification, value):
        self._identification = identification
        self._value = value

    @property
    def identification(self) -> str:
        return self._identification

    @property
    def value(self) -> int:
        return self._value

    @identification.setter
    def identification(self, identification: str):
        self._identification = identification

    @value.setter
    def value(self, value: int):
        self._value = value

    def __str__(self) -> str:
        return f"identification: {self.identification}, value: {self.value}"
