from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

class InfluxDB:
    """
    A class to interact with an InfluxDB database for storing weather station data.

    Attributes:
        org (str): The InfluxDB organization.
        bucket (str): The InfluxDB bucket to write data to.
        client (InfluxDBClient): The InfluxDB client instance.
        write_api: The API for writing data to InfluxDB.
    """
    def __init__(self, token, org, url, bucket):
        """
        Initialize the InfluxDB connection.

        Args:
            token (str): The authentication token for InfluxDB.
            org (str): The organization name in InfluxDB.
            url (str): The URL of the InfluxDB instance.
            bucket (str): The bucket name to write data to.
        """
        self.org = org
        self.bucket = bucket
        self.client = InfluxDBClient(url=url, token=token, org=org)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)

    def write_record(self, temperature, humidity, brightness, motor_on):
        """
        Write a single environment record to InfluxDB.

        Args:
            temperature (float or None): The temperature value to store.
            humidity (float or None): The humidity value to store.
            brightness (float or None): The brightness value to store.
            motor_on (bool): The state of the motor (on/off).
        """
        point = Point("environment")
        if temperature is not None:
            point.field("temperature", temperature)
        if humidity is not None:
            point.field("humidity", humidity)
        if brightness is not None:
            point.field("brightness", brightness)
        point.field("motor_on", motor_on)
        self.write_api.write(bucket=self.bucket, org=self.org, record=point)