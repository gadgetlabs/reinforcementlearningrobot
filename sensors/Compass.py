from sensors.Sensor import Sensor
from messages.Message import Message
from messages.object import Bearing
from messages.subject import Robot
from messages.predicate import HasHeading


class Compass(Sensor):

    def __init__(self, queue):
        self.queue = queue
        self.initialise()

    def initialise(self):
        pass

    async def run(self):

        msg = Message(Robot(), HasHeading(), Bearing())

        while True:

            raise NotImplemented
            # get the data
            current_heading = self.__get_compass_reading()

            await self.queue.put(msg)

    @staticmethod
    def __get_compass_reading(self):
        raise NotImplemented
        return val