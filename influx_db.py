from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

class InfluxDB:
    def __init__(self, token, org, url, bucket):
        self.org = org
        self.bucket = bucket
        self.client = InfluxDBClient(url=url, token=token, org=org)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)

    def write_record(self, temperature, humidity, brightness, motor_on):
        point = Point("environment")
        if temperature is not None:
            point.field("temperature", temperature)
        if humidity is not None:
            point.field("humidity", humidity)
        if brightness is not None:
            point.field("brightness", brightness)
        point.field("motor_on", motor_on)
        self.write_api.write(bucket=self.bucket, org=self.org, record=point)