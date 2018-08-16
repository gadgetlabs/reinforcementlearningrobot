class Message:

    def __init__(self, subject=None, predicate=None, obj=None):

        # "The sky has the color blue", consist of a subject ("the sky"), a predicate ("has the color"), and an object ("blue")
        self.subject = subject
        self.predicate = predicate
        self.obj = obj

    @property
    def subject(self):
        return self.subject

    @subject.setter
    def subject(self, value):
        self.subject = value

    @property
    def predicate(self):
        return self.predicate

    @predicate.setter
    def predicate(self, value):
        self.predicate = value

    @property
    def obj(self):
        return self.obj

    @obj.setter
    def obj(self, value):
        self.obj = value

