#!/usr/bin/env python3
import os
import asyncio
import json


class SensorNotFound(Exception):
    pass


class ActuatorNotFound(Exception):
    pass


class BehaviourNotFound(Exception):
    pass


def main(config):

    loop = asyncio.get_event_loop()
    sensor_queue = asyncio.Queue(loop=loop)
    actuator_queue = asyncio.Queue(loop=loop)

    try:
        module = __import__("behaviours")
        behaviour_class = getattr(module, config["Behaviour"])
        loop.create_task(behaviour_class(sensor_queue, actuator_queue))
    except BehaviourNotFound:
        exit(-1)

    sensors = config["Sensors"]
    actuators = config["Actuators"]

    for sensor in sensors:
        # Instanstiate the sensor and pass the sensor queue
        try:
            module = __import__("sensors")
            sensor_class = getattr(module, sensor["name"])
            loop.create_task(sensor_class(sensor_queue))
        except SensorNotFound:
            exit(-1)

    for actuator in actuators:
        # Instanstiate the sensor and pass the sensor queue
        try:
            module = __import__("actuators")
            actuator_class = getattr(module, actuator["name"])
            loop.create_task(actuator_class(actuator_queue))
        except ActuatorNotFound:
            exit(-1)

    loop.run_forever()
    loop.close()


if __name__ == '__main__':

    CONFIG_FILE = "config.json"
    if not os.path.exists(CONFIG_FILE):
        raise FileExistsError
    config = json.load(CONFIG_FILE)

    main(config)
