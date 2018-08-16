from messages.subject import Subject


# "The sky has the color blue", consist of a subject ("the sky"), a predicate ("has the color"), and an object ("blue")
class Robot(Subject):
    def __init__(self):
        super(Robot, self).__init__()