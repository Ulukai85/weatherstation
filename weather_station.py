import time

from dht11 import DHT11
from ads1115 import ADS1115
from influx_db import InfluxDB

dht = DHT11()
light = ADS1115()
database = InfluxDB()

while True:
    temp = dht.temperature
    humidity = dht.humidity
    brightness = light.brightness
    print(
        f"Data written: Temp: {temp} | Humidity: {humidity} | Brightness: {brightness}"
    )

    try:
        database.write_record(temp, humidity, brightness) 
    except Exception as error:
        print("DB write failed:", error)
    
    time.sleep(5)