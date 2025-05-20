import RPi.GPIO as gpio

class MotorController:
    """
    A class to control a DC motor using GPIO pins and PWM.

    Attributes:
        input_1 (int): GPIO pin for motor input 1.
        input_2 (int): GPIO pin for motor input 2.
        enable (int): GPIO pin for motor enable (PWM).
        pwm (gpio.PWM): PWM instance for speed control.
        _running (bool): Internal state of the motor (on/off).
    """
    def __init__(self, input_1=19, input_2=26, enable=13):
        """
        Initialize the motor controller and configure GPIO pins.

        Args:
            input_1 (int): GPIO pin for input 1 (default: 19).
            input_2 (int): GPIO pin for input 2 (default: 26).
            enable (int): GPIO pin for enable/PWM (default: 13).
        """
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
        """
        bool: Indicates if the motor is currently running.
        """
        return self._running

    def on(self, speed=50):
        """
        Start the motor at the specified speed.

        Args:
            speed (int): PWM duty cycle (0-100), default is 50.
        """
        self.pwm.ChangeDutyCycle(speed)
        gpio.output(self.enable, True)
        self._running = True
        print("Motor started")

    def off(self):
        """
        Stop the motor if it is running.
        """
        if self._running:
            gpio.output(self.enable, False)
            self.pwm.ChangeDutyCycle(0)
            self._running = False
            print("Motor stopped")

    def stop(self):
        """
        Stop the motor and clean up the PWM instance.
        """
        self.off()
        self.pwm.stop()
