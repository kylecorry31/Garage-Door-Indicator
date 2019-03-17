from manager import GarageDoorManager
from indicators import MockGarageDoorIndicator
from sensors import MockGarageDoorSensor
import time

DELAY = 1

if __name__ == '__main__':
    # TODO: Use real sensor and indicator
    door_sensor = MockGarageDoorSensor()
    door_indicator = MockGarageDoorIndicator()
    door_manager = GarageDoorManager(door_sensor, door_indicator)

    while True:
        door_manager.update()
        time.sleep(DELAY)
