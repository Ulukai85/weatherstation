import RPi.GPIO as gpio

def setup():
    gpio.setmode(gpio.BCM)

def cleanup():
    gpio.cleanup()