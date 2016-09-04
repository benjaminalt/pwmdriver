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
from __future__ import print_function
import time
import Adafruit_PCA9685
import math
import sys

# TODO: Set rotational velocity
    
class ServoDriver:

    def __init__(self, channel, address=0x40, frequency=40, pulseZero=0.8, pulsePi=2.9):
        """Creates a driver with specified characteristics"""
        self.channel = channel
        self.pulseZero = pulseZero
        self.pulsePi = pulsePi
        self.pwm = Adafruit_PCA9685.PCA9685(address)
        self.pwm.set_pwm_freq(frequency)
        
    def setAngle(self, angle, velocity=None):
        """Sets servo to specified angle (in radians) at the given
        angular velocity (in radians per second)"""
        pulsePerRad = (self.pulsePi - self.pulseZero) / math.pi
        self.__set_servo_pulse(self.channel, self.pulseZero + angle * pulsePerRad)
        
    # Helper function to make setting a servo pulse width simpler.
    def __set_servo_pulse(self, channel, pulse):
        pulse_length = 1000000
        pulse_length //= 40 # 60 Hz
        #print('{} units per period'.format(pulse_length))
        pulse_length //= 4096 # 12 bits of resolution
        #print('{} units per bit'.format(pulse_length))
        pulse *= 1000
        pulse //= pulse_length
        #print(pulse)
        
        self.pwm.set_pwm(channel, 0, int(pulse))

############################# TEST CLIENTS #################################
        
def calibrate():
    """Moves servo in 45 degree increments. If the servo moves differently, you may have to tweak parameters
    such as pulseZero, pulsePi or frequency in the ServoDriver constructor."""
    channel = int(sys.argv[2])
    driver = ServoDriver(channel)
    print('Moving servo on channel {}, press Ctrl-C to quit...'.format(channel))
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

def main():
    """Test client"""
    channel = int(sys.argv[1])
    degrees = float(sys.argv[2])
    driver = ServoDriver(channel)
    print('Setting servo on channel {} to {} degrees, press Ctrl-C to quit...'.format(channel, degrees))
    # PWM.set_pwm_freq(60)
    driver.setAngle(math.radians(degrees))

if __name__ == "__main__":
    if len(sys.argv) < 3 or "-h" in sys.argv or "--help" in sys.argv:
        print("Usage: python pwmdriver.py [--calibrate] CHANNEL ANGLE_IN_DEGREES")
        sys.exit(0)
    elif "-c" in sys.argv or "--calibrate" in sys.argv:
        calibrate()
    else:
        main()
