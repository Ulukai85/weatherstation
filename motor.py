import RPi.GPIO as gpio

from time import sleep

gpio.setmode(gpio.BCM)

gpio.setup(19, gpio.OUT)
gpio.setup(26, gpio.OUT)
gpio.setup(13, gpio.OUT)

pwm = gpio.PWM(13, 100)
pwm.start(0)

gpio.output(19, True)
gpio.output(26, False)

pwm.ChangeDutyCycle(50)

gpio.output(13, True)

sleep(3)

gpio.output(13, False)

pwm.stop()

gpio.cleanup()
