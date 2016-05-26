# pwmdriver
A pulse-width-modulation servo driver for the Adafruit Raspberry Pi Servo HAT.

pwmdriver.py is a Python utility for controlling servos with the [Adafruit Raspberry Pi Servo HAT](https://learn.adafruit.com/adafruit-16-channel-pwm-servo-hat-for-raspberry-pi/overview)
or PCA9685. It wraps the Adafruit Python library to provide an object-oriented way of telling a particular servo to move to a particular angle
using pulse-width modulation.

The required Adafruit Python library can be found here: https://github.com/adafruit/Adafruit_Python_PCA9685

To use the driver, simply create a new driver with the required channel (0-15 if you are using one HAT), address of the HAT (default is 0x40),
PWM frequency in Hz (default is 60), pulse length for "zero" position in ms (default is 0.6) and pulse length for "180" position in ms (default is 2.55):

`driver = ServoDriver(12) # address, frequency, pulseZero and pulsePi are default`
`driver.setAngle(math.pi/2)`
