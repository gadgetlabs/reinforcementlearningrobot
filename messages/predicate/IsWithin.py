from messages.predicate import Predicate

#"The sky has the color blue", consist of a subject ("the sky"), a predicate ("has the color"), and an object ("blue")
class IsWithin(Predicate):
    def __init__(self):
        super(IsWithin, self).__init__()