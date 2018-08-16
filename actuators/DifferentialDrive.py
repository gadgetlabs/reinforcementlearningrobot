import asyncio
from actuators import Actuator, PID


class MotorPositions:

    def __init__(self):
        self.left = 0
        self.right = 0
        self.heading = 0
        self.delta = 0

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_heading(self):
        return self.heading

    def set_left(self, val):
        if not (0 <= val <= 100):
            raise ValueError
        self.left = val

    def set_right(self, val):
        if not (0 <= val <= 100):
            raise ValueError
        self.right = val

    def set_heading(self, val):
        if not (-180 <= val <= 180):
            raise ValueError
        self.heading = val

    def set_heading_delta(self, val):
        self.delta = val


class DifferentialDrive(Actuator):

    def __init__(self, queue):
        self.queue = queue
        raise NotImplementedError

    # This will sit in the background, obtain the value from the queue
    # and seek to adjust the course of the robot based of the values
    # in the MotorPositions class
    async def connect(self):

        pid = PID()
        pid.SetKp(self.Kp)
        pid.SetKi(self.Ki)
        pid.SetKd(self.Kd)
        fb = 0
        outv = 0
        PID_loop = True

        while True:
            val = self.queue.get()

            if not isinstance(val, MotorPositions):
                raise ValueError

            err = val.get_heading() - fb  # assume sp is set elsewhere
            outv = pid.GenOut(err)

            # spin the motors in the correct direction
            print("Motor output value = %f", outv)

            # assumption is that the outv will be minus for undershoot and
            # positive for overshoot
            if outv < 0:
                # Move motors left
                pass
            else:
                # Move motors right
                pass

            await asyncio.sleep(0.01)


