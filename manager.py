class GarageDoorManager:
    """A class which can activate the indicator if the door is open."""

    def __init__(self, door_sensor, door_indicator):
        """
        Default constructor of the Garage Door Manager.

        Arguments:
        door_sensor (GarageDoorSensor): the garage door open sensor
        door_indicator (GarageDoorIndicator): the garage door open indicator
        """
        self.door_sensor = door_sensor
        self.door_indicator = door_indicator

    def update(self):
        """Turn the indicator on if the garage door is open"""
        is_open = self.door_sensor.is_open()

        if is_open:
            self.door_indicator.on()
        else:
            self.door_indicator.off()
