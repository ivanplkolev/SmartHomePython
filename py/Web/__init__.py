from flask import Flask, request
from py import Device

app = Flask(__name__)

@app.route('/', methods=['GET'])
def login():
    command = request.args.get('command')
    if command :
        if command == 'switchrelay':
            key = request.args.get('key')
            status = request.args.get('status')
            try:
                Device.switchRelay(key, status)
            except ValueError as e:
                return sendErrorResponce('SchemaError')
        return Device.getDeviceStatus()
    return sendErrorResponce('NoCommandError')

def sendErrorResponce(error):
    return '{\"Error\":\"' + error + '\"}\n'