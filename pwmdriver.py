"""
Author: Benjamin Alt (benjamin_alt@outlook.com)

Servo driver for Rasperry Pi with Adafruit 16-Channel Servo HAT.
Designed to drive 1 servo on 1 channel with special settings
(calibration).

Objectives:
+ Provide function to set servo to specific angle (in radians) at 
  certain angular velocity.
"""

from __future__ import division
import time
import Adafruit_PCA9685
import math

# TODO: Set rotational velocity
    
class ServoDriver:

    def __init__(self, channel, address=0x40, frequency=60, pulseZero=0.6, pulsePi=2.55):
        """Creates a driver with specified characteristics"""
        self.channel = channel
        self.pulseZero = pulseZero
        self.pulsePi = pulsePi
        self.pwm = Adafruit_PCA9685.PCA9685(address)
        self.pwm.set_pwm_freq(frequency)

    def setAngle(self, angle, velocity=None):
        """Sets servio to specified angle (in radians) at the given
        angular velocity (in radians per second)"""
        # I know that pulsePi minus pulseZero is pulsePerDegree
        pulsePerRad = (self.pulsePi - self.pulseZero) / math.pi
        self.__set_servo_pulse(self.channel, self.pulseZero + angle * pulsePerRad)
        
    # Helper function to make setting a servo pulse width simpler.
    def __set_servo_pulse(self, channel, pulse):
        pulse_length = 1000000
        pulse_length //= 60 # 60 Hz
        print('{} units per period'.format(pulse_length))
        pulse_length //= 4096 # 12 bits of resolution
        print('{} units per bit'.format(pulse_length))
        pulse *= 1000
        pulse //= pulse_length
        print(pulse)
        self.pwm.set_pwm(channel, 0, int(pulse))

def main():
    """Test client"""
    driver = ServoDriver(12)
    print('Moving servo on channel 12, press Ctrl-C to quit...')
    # PWM.set_pwm_freq(60)
    print("Zero...")
    driver.setAngle(0)
    time.sleep(2)
    print("45...")
    driver.setAngle(math.pi/4)
    time.sleep(2)
    print("90...")
    driver.setAngle(math.pi/2)
    time.sleep(2)
    print("135..")
    driver.setAngle((3/4) * math.pi)
    time.sleep(2)
    print("180...")
    driver.setAngle(math.pi)

if __name__ == "__main__":
    main()
