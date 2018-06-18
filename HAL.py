import explorerhat
from sensors.DistanceShield import VL53L0X as tof
import time
import smbus

class HAL:

    def __init__(self):

        self.NUMBER_OF_TOF_SENSORS = 4
        self.tof_addresses = []
        self.bus = smbus.SMBus(1)



    # array of 4 VL53L0X ToF sensors - array returned left to right
    # https://learn.adafruit.com/adafruit-vl53l0x-micro-lidar-distance-sensor-breakout/arduino-code
    def getDistance(self):
        pass

    def initDistance(self):

        tof.number_sensors(self.NUMBER_OF_TOF_SENSORS)
        tof.reset_all()
        self.tof_addresses = tof.change_addresses(self.bus)

    def getIMU(self):
        pass

    def setMotor(self, left_motor, right_motor):
        pass

    # i2c sensors (specifically the time of flight) are daisy chained, they have the same address and therefore this
    # must be changed on initialisation
    def initialise(self):
        pass



