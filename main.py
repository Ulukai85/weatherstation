
from dht11 import DHT11
from ads1115 import ADS1115
from influx_db import InfluxDB
from motor import MotorController
from weather_station import WeatherStation
from gpio_setup import setup

setup()

def main():
    dht = DHT11()
    light = ADS1115()
    database = InfluxDB()
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