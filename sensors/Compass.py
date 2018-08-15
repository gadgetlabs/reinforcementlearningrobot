from sensors import Sensor


class Heading:

    value = 0

    def get(self):
        return self.value

    def set(self, value):
        self.value = value


class Compass(Sensor):

    def __init__(self, queue):
        self.queue = queue

    @staticmethod
    def get_compass_reading(self):
        raise NotImplemented
        return val

    # The pu
    async def connect(self):

        val = Heading()

        while True:

            raise NotImplemented
            # get the data
            current_heading = self.get_compass_reading()
            val.set(current_heading)
            await self.queue.put(val)

