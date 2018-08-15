#!/usr/bin/env python3
import os
import asyncio
import configparser

async def main():

    




    loop = asyncio.get_event_loop()

    sensor_queue = asyncio.Queue(loop=loop)
    actuator_queue = asyncio.Queue(loop=loop)

    # BUILD LIST OF SENSORS

    # BUILD LIST OF ACTUATORS


    #sensor_coro = sensor(queue)
    #actuator_coro = actuator(queue)
    loop.run_until_complete(asyncio.gather(sensor_coro, actuator_coro))
    loop.close()


if __name__ == '__main__':

    CONFIG_FILE = "config.ini"
    config = configparser.ConfigParser()
    if not os.path.exists(CONFIG_FILE):
        raise FileExistsError
    config.read('config.ini')

    main()
