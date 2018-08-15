from behaviours import Behaviour
from sensors.Compass import Heading
from actuators.Motors import MotorPositions


class Simple(Behaviour):

    LIMIT = 30 # JUST SOME BULLSHIT number to test

    def __int__(self, sensors_queue, actuators_queue):
        self.sensors = sensors_queue
        self.actuators = actuators_queue

    async def run(self):

        mp = MotorPositions

        while True:
            val = self.sensors.get()

            if isinstance(val, Heading):
                heading = val.get()
                self.actuator.put(mp.setHeading(heading))
            elif isinstance(val, Distance):
                # Simple obstacle avoidance
                distance = val.get()
                if distance < self.LIMIT:
                    # change course by 90 degrees
                    mp.setHeadingDelta(90)
                    self.actuator.put(mp)
            else:
                raise NotImplementedError
