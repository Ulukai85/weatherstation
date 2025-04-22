import board
import busio
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_ads1x15.ads1115 as ADS

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

ldr = AnalogIn(ads, ADS.P0)

class LightSensor:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1115(i2c)
        self.ldr = AnalogIn(ads, ADS.P0)

    @property
    def brightness(self):
        voltage = self.ldr.voltage
        return voltage / 3.3
