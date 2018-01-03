from abc import abstractmethod

class Sensor:

    def __init__(self, pin, key):
        self.pin = pin
        self.key = key

    @abstractmethod
    def readSensorData(self):
        raise NotImplementedError('No implementation')

