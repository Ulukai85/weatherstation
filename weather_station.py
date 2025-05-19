from time import sleep, strftime, localtime
from gpio_setup import cleanup

class WeatherStation:
    def __init__(self, temp_sensor, humidity_sensor, light_sensor, fan, database):
        self.temp_sensor = temp_sensor
        self.humidity_sensor = humidity_sensor
        self.light_sensor = light_sensor
        self.fan = fan
        self.database = database

    def handle_fan(self, temp, threshold):

        if temp is None:
            return

        if not self.fan.running and temp >= threshold:
            self.fan.on()
        elif self.fan.running and temp < threshold - 1:
            self.fan.off()

    def run(self, interval=5, temp_threshold=25):
        timeformat = "%Y-%m-%d %H:%M:%S"
        try:
            while True:
                time = strftime(timeformat, localtime())
                temp = self.temp_sensor.temperature
                humidity = self.humidity_sensor.humidity
                brightness = self.light_sensor.brightness
                brightness_formatted = f"{brightness:.2f}" if brightness is not None else "None"

                self.handle_fan(temp, temp_threshold)
                motor_on = self.fan.running
                print(f"{time} |  Temp: {temp} | Humidity: {humidity} | Brightness: {brightness_formatted} | Fan: {motor_on}")

                try:
                    self.database.write_record(temp, humidity, brightness, motor_on) 
                except Exception as error:
                    print("DB write failed:", error)

                sleep(interval)

        except KeyboardInterrupt:
            print("Stopping weather station...")
        finally:
            self.fan.stop()
            cleanup()

