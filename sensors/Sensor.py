import asyncio

class Sensor(asyncio.Task):
    def __init__(self):
        raise NotImplementedError

    def connect(self):
        raise NotImplementedError