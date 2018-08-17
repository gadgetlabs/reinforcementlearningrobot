from abc import ABCMeta, abstractmethod

class Actuator:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    async def run(self):
        pass

    @abstractmethod
    def initialise(self):
        pass
