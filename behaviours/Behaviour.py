import asyncio


class Behaviour(asyncio.Task):

    def __init__(self):
        super(Behaviour, self).__init__()

    async def run(self):
        raise NotImplementedError

