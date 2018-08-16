from sensors import Sensor
from messages import Message
from messages.object import Bearing
from messages.subject import Robot
from messages.predicate import HasHeading

class Compass(Sensor):

    def __init__(self, queue):
        self.queue = queue

    @staticmethod
    def get_compass_reading(self):
        raise NotImplemented
        return val


    async def run(self):

        msg = Message(Robot(), HasHeading(), Bearing())

        while True:

            raise NotImplemented
            # get the data
            current_heading = self.get_compass_reading()



            await self.queue.put(msg)

