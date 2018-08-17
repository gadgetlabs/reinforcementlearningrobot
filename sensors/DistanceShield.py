import explorerhat
import time
import VL53L0X
import smbus
from sensors.Sensor import Sensor
from messages.Message import Message
from messages.object import Distance
from messages.subject import Robot
from messages.predicate import IsWithin


class DistanceShield(Sensor):

    async def run(self):
        msg = Message(Robot(), IsWithin(), Distance())

        while True:

            raise NotImplemented
            # get the data
            current_distance = self.__get_distance_reading()



            await self.queue.put(msg)

    def initialise(self):
        pass

    def __get_distance_reading(self):
        pass

    #
    # def __init__(self):
    #
    #     self.NUMBER_OF_TOF_SENSORS = 4
    #     self.ds_addresses = []
    #     self.bus = smbus.SMBus(1)
    #
    #
    # # array of 4 VL53L0X ToF sensors - array returned left to right
    # # https://learn.adafruit.com/adafruit-vl53l0x-micro-lidar-distance-sensor-breakout/arduino-code
    # def getDistance(self):
    #     ds.start_ranging(self, self.bus)
    #
    # def initDistance(self):
    #
    #     ds.number_sensors(self.NUMBER_OF_TOF_SENSORS)
    #     ds.reset_all()
    #     self.tof_addresses = ds.change_addresses(self.bus)




    def __init__(self, queue):
        self.NUMBER_OF_TOF_SENSORS = 0
        self.BASE_I2C_ADDRESS = 0x29
        self.NEW_I2C_ADDRESS_START = 0x30
        self.queue = queue
        self.initialise()




    def number_sensors(self, number_sensors):
        self.NUMBER_OF_TOF_SENSORS = number_sensors

    def reset_all(self):
        self.__off_all()
        time.sleep(3)
        self.__on_all()

    # check is an i2c address exists
    def __exists(self, bus, address):
        try:
            bus.read_byte(address)
            return True
        except:
            return False

    def change_addresses(self, bus):
        pass
#        # first look for 0x29 - does anything exist?
#        if self.__exists(bus, 0x29):
#            self.__change_addresses(bus)
#        # Sensors might of already had their addresses changed - check what needs changing
#        else:
#            # do some exploration

    def __change_addresses(self, bus):

        self.__off_all()

        self.sensors = list()
        for x in range(self.NUMBER_OF_TOF_SENSORS):

            print("1")
            tof = VL53L0X.VL53L0X(address=self.NEW_I2C_ADDRESS_START + x)
            print("2")
            self.sensors.append(tof)

            # Bring up sensor x (not same as x - 1!)
            explorerhat.output[x].on()
            # Going with 0x30 to 0x3F is probably OK.

        time.sleep(3)

    def start_ranging(self, bus):

        for x in range(self.NUMBER_OF_TOF_SENSORS):
            print("3")
            self.sensors[x].start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)
            print("4")

        distances = list()
        for count in range(1, 101):
            for x in range(self.NUMBER_OF_TOF_SENSORS):
                distance = self.sensors[x].get_distance()
                distances.append(distance)
            print(", ".join([y for y in distances]))
            distances = list()

    def __off_all(self):
        for x in range(self.NUMBER_OF_TOF_SENSORS):
            explorerhat.output[x].off()

    def __on_all(self):
        for x in range(self.NUMBER_OF_TOF_SENSORS):
            explorerhat.output[x].on()


