import time

from dht11 import DHT11
from lightsensor import LightSensor
from influx_db import InfluxDB

dhtDevice = DHT11()
lightsensor = LightSensor()
client = InfluxDB()

while True:
    try:
        temp = dhtDevice.temperature
        humidity = dhtDevice.humidity
        brightness = lightsensor.brightness
        point = client.write_record(temp, humidity, brightness)
        print(f"Data written: {temp:.1f}°C; {humidity}% humidity, Brightness {brightness:.2f}")
    except RuntimeError as error:
        print(error.args[0])
    except Exception as error:
        dhtDevice.exit()
        raise error
    
    time.sleep(10)