from py.Mock import Hardware
from py.Entities.Relay import Relay
from py.Entities.Sensor import Sensor
import json

relays = {Relay(1, 'r1'), Relay(2, 'r2')}
sensors = {Sensor(12, 'keyyy')}


def getDeviceStatus():
    respObj = {}
    respObj['Error'] = ''
    for sensor in sensors:
        respObj[sensor.key] = Hardware.getSensorValue(sensor)
    for relay in relays:
        respObj[relay.key] = relay.status
    json_str = json.dumps(respObj)
    return json_str

def switchRelay(key, status):
    foundRelay = None
    for relay in relays:
        if relay.key == key:
            foundRelay= True
            Hardware.switchRelay(relay, status)
            break
    if not foundRelay:
        raise ValueError('Schema Error')