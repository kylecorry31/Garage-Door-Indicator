class GarageDoorSensor:
    """A sensor which can determine if a garage door is open."""

    def is_open(self):
        """Determine if the garage door is open.

        Returns True if the door is open otherwise False
        """
        pass

class MockGarageDoorSensor(GarageDoorSensor):

    def __init__(self):
        self.open = False

    def set_open(self, open):
        self.open = open

    def is_open(self):
        return self.open
