from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

class InfluxDB:
    def __init__(
            self,
            token="C7gIwzESgxk-Su8xRm1LDxGXYi6vDbMq5_EJNJ3HbOvH5BU168VBs8iJ3bdsFJ4ghCA7Yoh_NxMtCYFLt-e3zw==",
            org="StrawberryTau",
            url="http://192.168.2.109:8086",
            bucket="strawberrytau"):
        self.org = org
        self.bucket = bucket
        self.client = InfluxDBClient(url=url, token=token, org=org)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)

    def write_record(self, temperature, humidity, brightness):
        point = Point("environment")
        if temperature is not None:
            point.field("temperature", temperature)
        if humidity is not None:
            point.field("humidity", humidity)
        if brightness is not None:
            point.field("brightness", brightness)
        self.write_api.write(bucket=self.bucket, org=self.org, record=point)