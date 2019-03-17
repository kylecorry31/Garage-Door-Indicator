class GarageDoorIndicator:
    """
    An indicator which can be turned on or off.
    """

    def on(self):
        """Turn the indicator on"""
        pass

    def off(self):
        """Turn the indicator off"""
        pass

class MockGarageDoorIndicator:

    def __init__(self):
        self.status = False

    def get_status(self):
        return self.status

    def on(self):
        self.status = True

    def off(self):
        self.status = False
