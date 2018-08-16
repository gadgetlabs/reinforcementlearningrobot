class Subject:
    def __init__(self):
        self.value = None
        super() #??

    @property
    def value(self):
        return self.value

    @value.setter
    def value(self, val):
        self.value = val