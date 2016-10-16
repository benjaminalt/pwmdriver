# pwmdriver
A pulse-width-modulation servo driver for the Adafruit Raspberry Pi Servo HAT.

pwmdriver.py is a Python utility for controlling servos with the [Adafruit Raspberry Pi Servo HAT](https://learn.adafruit.com/adafruit-16-channel-pwm-servo-hat-for-raspberry-pi/overview)
or PCA9685. It wraps the Adafruit Python library to provide an object-oriented way of telling a particular servo to move to a particular angle
using pulse-width modulation.

The required Adafruit Python library can be found here: https://github.com/adafruit/Adafruit_Python_PCA9685

To use the driver, simply create a new driver with the required channel (0-15 if you are using one HAT), address of the HAT (default is 0x40),
PWM frequency in Hz (default is 60), pulse length for "-90" position  and pulse length for "180" position. The pulse lengths depend on the servo you are using; for a Hitec HS-485B, they would be 100 and 420.

**You should call `initialize()` before the first call of `moveTo`. This will move the servo to its initial position.**  

The driver has rudimentary support for different rotational velocities (you can set a constant in the `moveTo` function to make the servo move faster or slower).

    servo = Servo(13, 190, 440, 190)
    servo.initialize()
    servo.moveTo(toRadians(0))   
