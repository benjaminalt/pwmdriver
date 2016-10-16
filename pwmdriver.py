import Adafruit_PCA9685
import time
import math
import argparse

class Servo:

    # Create new servo. CAUTION: Without calling initialize() after, servo might not work properly.
    def __init__(self, channel, pulseMinusPiHalfs, pulsePiHalfs, pulseInitial, address=0x40, freq=40):
        self.pwm = Adafruit_PCA9685.PCA9685(address)
        self.pwm.set_pwm_freq(freq)
        self.channel = channel
        self.pulseZero = pulseMinusPiHalfs + (pulsePiHalfs - pulseMinusPiHalfs) / 2
        self.pulsePerRad = (pulsePiHalfs - pulseMinusPiHalfs) / math.pi
        self.currentPulse = pulseInitial

    # Move servo to initial position. CAUTION: Does this at maximum velocity!!!
    def initialize(self):
        self.pwm.set_pwm(self.channel, 0, self.currentPulse)

    # Move servo to specified angle (in radians)
    def moveTo(self, angle):
        targetPulse = int(self.pulseZero + angle * self.pulsePerRad)
        pulseMin = min(self.currentPulse, targetPulse)
        pulseMax = max(self.currentPulse, targetPulse)
        for pulselen in range(pulseMin, pulseMax):
            self.pwm.set_pwm(self.channel, 0, pulselen)
            time.sleep(0.01) # Make this number smaller for faster angular velocity
        self.currentPulse = targetPulse

# Convert angle in degrees to radians
def toRadians(degrees):
    return degrees * math.pi / 180 
            
# Test client
def main():
    servo = Servo(13, 190, 440, 190)
    servo.initialize()
    #servo.moveTo(toRadians(0))
    
if __name__ == "__main__":
    main()
