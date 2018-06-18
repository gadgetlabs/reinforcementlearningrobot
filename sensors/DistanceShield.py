import explorerhat
import time
import VL53L0X

class DistanceShield:

    def __init__(self):
        self.NUMBER_OF_TOF_SENSORS = 0
        self.BASE_I2C_ADDRESS = 0x29
        self.NEW_I2C_ADDRESS_START = 0x30
        self.VL53L0X_REG_I2C_SLAVE_DEVICE_ADDRESS = 0x008a

    def number_sensors(self, number_sensors):
        self.NUMBER_OF_TOF_SENSORS = number_sensors

    def reset_all(self):
        self.__off_all()
        time.sleep(10)
        self.__on_all()

    def change_addresses(self, bus):

        self.__off_all()

        for x in range(self.NUMBER_OF_TOF_SENSORS):
            # Bring up sensor x (not same as x - 1!)
            explorerhat.output[x].on()
            # Going with 0x30 to 0x3F is probably OK.

            self.set_device_address(bus, self.NEW_I2C_ADDRESS_START + x)

    def set_device_address(self, bus, new_addr):
        # Line from ST API (vl53l0x_api.c)
        # Status = VL53L0X_WrByte(Dev, VL53L0X_REG_I2C_SLAVE_DEVICE_ADDRESS, DeviceAddress / 2);
        bus.write_byte_data(self.BASE_I2C_ADDRESS, self.VL53L0X_REG_I2C_SLAVE_DEVICE_ADDRESS, new_addr)

    def get_device_mode(self, bus):


        self.device_mode =


    def __off_all(self):
        for x in range(self.NUMBER_OF_TOF_SENSORS):
            explorerhat.output[x].off()

    def __on_all(self):
        for x in range(self.NUMBER_OF_TOF_SENSORS):
            explorerhat.output[x].on()

        VL53L0X_GETPARAMETERFIELD(Dev, DeviceMode, *pDeviceMode);

        # define VL53L0X_GETPARAMETERFIELD(Dev, field, variable) \
        variable = PALDevDataGet(Dev, CurrentParameters).field


        VL53L0X_Error
        VL53L0X_StartMeasurement(VL53L0X_DEV
        Dev)


