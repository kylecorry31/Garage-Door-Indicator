import unittest
from manager import GarageDoorManager
from sensors import MockGarageDoorSensor
from indicators import MockGarageDoorIndicator

class TestGarageDoorManager(unittest.TestCase):

    def test_indicator_off_when_closed(self):
        door_sensor = MockGarageDoorSensor()
        door_indicator = MockGarageDoorIndicator()
        door_manager = GarageDoorManager(door_sensor, door_indicator)

        door_sensor.set_open(False)
        door_manager.update()

        self.assertFalse(door_indicator.get_status())

    def test_indicator_on_when_open(self):
        door_sensor = MockGarageDoorSensor()
        door_indicator = MockGarageDoorIndicator()
        door_manager = GarageDoorManager(door_sensor, door_indicator)

        door_sensor.set_open(True)
        door_manager.update()

        self.assertTrue(door_indicator.get_status())

if __name__ == '__main__':
    unittest.main()
