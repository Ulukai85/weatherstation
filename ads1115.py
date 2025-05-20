import board
import busio
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_ads1x15.ads1115 as ADS


class ADS1115:
    """
    A class to interface with the ADS1115 analog-to-digital converter for reading brightness via an LDR.

    Attributes:
        i2c (busio.I2C): The I2C bus instance.
        ads (ADS.ADS1115): The ADS1115 ADC instance.
        ldr (AnalogIn): The analog input channel for the LDR sensor.
    """
    def __init__(self):
        """
        Initialize the ADS1115 ADC and configure the LDR input channel.
        """
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1115(self.i2c)
        self.ldr = AnalogIn(self.ads, ADS.P0)

    @property
    def brightness(self):
        """
        Read and return the normalized brightness value from the LDR.

        Returns:
            float: The normalized brightness (0.0 to 1.0), or None if reading fails.
        """
        try:
            voltage = self.ldr.voltage
            return voltage / 3.3
        except Exception as e:
            print(f"[ADS1115] Brightness read failed: {e}")
