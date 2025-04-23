import board
import busio
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_ads1x15.ads1115 as ADS


class ADS1115:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1115(self.i2c)
        self.ldr = AnalogIn(self.ads, ADS.P0)

    @property
    def brightness(self):
        try:
            voltage = self.ldr.voltage
            return voltage / 3.3
        except Exception as e:
            print(f"[ADS1115] Brightness read failed: {e}")
