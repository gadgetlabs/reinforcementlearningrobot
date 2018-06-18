import explorerhat
import time
import VL53L0X

class DistanceShield:

    def __init__(self):
        self.NUMBER_OF_TOF_SENSORS = 0
        self.BASE_I2C_ADDRESS = 0x29
        self.NEW_I2C_ADDRESS_START = 0x30

    def number_sensors(self, number_sensors):
        self.NUMBER_OF_TOF_SENSORS = number_sensors

    def reset_all(self):
        self.__off_all()
        time.sleep(3)
        self.__on_all()

    def change_addresses(self, bus):

        self.__off_all()

        self.sensors = list()
        for x in range(self.NUMBER_OF_TOF_SENSORS):

            tof = VL53L0X.VL53L0X(address=self.NEW_I2C_ADDRESS_START + x)
            self.sensors.append(tof)

            # Bring up sensor x (not same as x - 1!)
            explorerhat.output[x].on()
            # Going with 0x30 to 0x3F is probably OK.

        time.sleep(3)

    def start_ranging(self, bus):

        for x in range(self.NUMBER_OF_TOF_SENSORS):
            self.sensors[x].start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

        distances = list()
        for count in range(1, 101):
            for x in range(self.NUMBER_OF_TOF_SENSORS):
                distance = self.sensors[x].get_distance()
                distances.append(distance)
            print ", ".join([y for y in distances])
            distances = list()


    def __off_all(self):
        for x in range(self.NUMBER_OF_TOF_SENSORS):
            explorerhat.output[x].off()

    def __on_all(self):
        for x in range(self.NUMBER_OF_TOF_SENSORS):
            explorerhat.output[x].on()


