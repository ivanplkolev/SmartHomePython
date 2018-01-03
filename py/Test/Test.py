from py import Device as Device

try:
    Device.switchRelay('r1', 1)
    print(Device.getDeviceStatus())
    Device.switchRelay('r1', 0)
    print(Device.getDeviceStatus())
    Device.switchRelay('r1', 1)
    print(Device.getDeviceStatus())
    Device.switchRelay('r1', 0)
except ValueError as e:
    print('there was a Schema Error')

print(Device.getDeviceStatus())
