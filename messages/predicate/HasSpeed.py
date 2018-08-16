from messages.predicate import Predicate

#"The sky has the color blue", consist of a subject ("the sky"), a predicate ("has the color"), and an object ("blue")
class HasSpeed(Predicate):
    def __init__(self):
        super(HasSpeed, self).__init__()