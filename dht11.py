import board
import adafruit_dht

class DHT11:
    def __init__(self):
        self.sensor = adafruit_dht.DHT11(board.D4, use_pulseio=False)

    @property
    def temperature(self):
        try:
            return self.sensor.temperature
        except Exception as e:
            print(f"[DHT11] Temp read failed: {e.args[0]}")
            return None
    
    @property
    def humidity(self):
        try:
            return self.sensor.humidity
        except Exception as e:
            print(f"[DHT11] Humidity read failed: {e.args[0]}")
            return None