from time import sleep
from gpio_setup import cleanup

class WeatherStation:
    def __init__(self, temp_sensor, humidity_sensor, light_sensor, fan, database):
        self.temp_sensor = temp_sensor
        self.humidity_sensor = humidity_sensor
        self.light_sensor = light_sensor
        self.fan = fan
        self.database = database

    def handle_fan(self, temp, threshold):
        if temp is not None and temp > threshold:
            if not self.fan.running:
                self.fan.on()
            else:
                if self.motor.running:
                    self.fan.off()

    def run(self, interval=5, temp_threshold=30):
        try:
            while True:
                temp = self.temp_sensor.temperature
                humidity = self.humidity_sensor.humidity
                brightness = self.light_sensor.brightness

                print(f"Data written: Temp: {temp} | Humidity: {humidity} | Brightness: {brightness}")

                try:
                    self.database.write_record(temp, humidity, brightness) 
                except Exception as error:
                    print("DB write failed:", error)
                
                self.handle_fan(temp, temp_threshold)

                sleep(interval)

        except KeyboardInterrupt:
            print("Stopping weather station...")
        finally:
            self.fan.stop()
            cleanup()