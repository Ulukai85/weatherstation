import board
import adafruit_dht

class DHT11:
    def __init__(self):
        self.sensor = adafruit_dht.DHT11(board.D4, use_pulseio=False)

    @property
    def temperature(self):
        return self.sensor.temperature
    
    @property
    def humidity(self):
        return self.sensor.humidity