
from dht11 import DHT11
from ads1115 import ADS1115
from influx_db import InfluxDB
from motor import MotorController
from weather_station import WeatherStation
from gpio_setup import setup

import os
from dotenv import load_dotenv

setup()

def main():
    load_dotenv()
    dht = DHT11()
    light = ADS1115()
    database = InfluxDB(
        token=os.getenv("TOKEN"),
        org=os.getenv("ORG"),
        url=os.getenv("URL"),
        bucket=os.getenv("BUCKET")
    )
    fan = MotorController()

    station = WeatherStation(
        temp_sensor=dht,
        humidity_sensor=dht,
        light_sensor=light,
        fan=fan,
        database=database
    )

    station.run()

if __name__ == "__main__":
    main()