import RPi.GPIO as gpio

class MotorController:
    def __init__(self, input_1=19, input_2=26, enable=13):
        self.input_1 = input_1
        self.input_2 = input_2
        self.enable = enable

        self._running = False
        
        gpio.setup(self.input_1, gpio.OUT)
        gpio.setup(self.input_2, gpio.OUT)
        gpio.setup(self.enable, gpio.OUT)

        self.pwm = gpio.PWM(self.enable, 100)
        self.pwm.start(0)

        gpio.output(self.input_1, True)
        gpio.output(self.input_2, False)

    @property
    def running(self):
        return self._running

    def on(self, speed=50):
        self.pwm.ChangeDutyCycle(speed)
        gpio.output(self.enable, True)
        self._running = True
        print("Motor started")

    def off(self):
        if self._running:
            gpio.output(self.enable, False)
            self.pwm.ChangeDutyCycle(0)
            self._running = False
            print("Motor stopped")

    def stop(self):
        self.off()
        self.pwm.stop()
