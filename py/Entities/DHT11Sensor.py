from py.Entities.Sensor import Sensor
import RPi.GPIO as GPIO
import dht11


class DHT11Sensor(Sensor):

    def __init__(self, pin, key):
        Sensor.__init__(self, pin, key)
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()

    def readSensorData(self):
        print('redaing sensor data')
        instance = dht11.DHT11(pin=self.pin)
        result = instance.read()

        if result.is_valid():
            print("Temperature: %d C" % result.temperature)
            print("Humidity: %d %%" % result.humidity)
        else:
            print("Error: %d" % result.error_code)
