from time import sleep, strftime, localtime
from gpio_setup import cleanup

class WeatherStation:
    """
    A class to manage the weather station, including sensor readings, fan control, and data logging.

    Attributes:
        temp_sensor: Sensor object for temperature readings.
        humidity_sensor: Sensor object for humidity readings.
        light_sensor: Sensor object for brightness readings.
        fan: MotorController object for fan control.
        database: Database object for storing sensor data.
    """
    def __init__(self, temp_sensor, humidity_sensor, light_sensor, fan, database):
        """
        Initialize the WeatherStation with sensors, fan, and database.

        Args:
            temp_sensor: Temperature sensor instance.
            humidity_sensor: Humidity sensor instance.
            light_sensor: Brightness sensor instance.
            fan: MotorController instance for fan control.
            database: Database instance for data storage.
        """
        self.temp_sensor = temp_sensor
        self.humidity_sensor = humidity_sensor
        self.light_sensor = light_sensor
        self.fan = fan
        self.database = database

    def handle_fan(self, temp, threshold):
        """
        Control the fan based on the temperature and threshold.

        Args:
            temp (float or None): The current temperature.
            threshold (float): The temperature threshold to turn the fan on.
        """
        if temp is None:
            return

        if not self.fan.running and temp >= threshold:
            self.fan.on()
        elif self.fan.running and temp < threshold - 1:
            self.fan.off()

    def run(self, interval=5, temp_threshold=25):
        """
        Main loop to read sensors, control the fan, log data, and print status.

        Args:
            interval (int): Time in seconds between readings (default: 5).
            temp_threshold (float): Temperature threshold for fan control (default: 25).
        """
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

