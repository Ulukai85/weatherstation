import board
import adafruit_dht

class DHT11:
    """
    A class to interface with the DHT11 temperature and humidity sensor.

    Attributes:
        sensor (adafruit_dht.DHT11): The DHT11 sensor instance.
    """
    def __init__(self):
        """
        Initialize the DHT11 sensor on the specified GPIO pin.
        """
        self.sensor = adafruit_dht.DHT11(board.D4, use_pulseio=False)

    @property
    def temperature(self):
        """
        Read and return the temperature from the DHT11 sensor.

        Returns:
            float or None: The temperature in Celsius, or None if reading fails.
        """
        try:
            return self.sensor.temperature
        except Exception as e:
            print(f"[DHT11] Temp read failed: {e.args[0]}")
            return None
    
    @property
    def humidity(self):
        """
        Read and return the humidity from the DHT11 sensor.

        Returns:
            float or None: The relative humidity in percent, or None if reading fails.
        """
        try:
            return self.sensor.humidity
        except Exception as e:
            print(f"[DHT11] Humidity read failed: {e.args[0]}")
            return None