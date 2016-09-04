"""
Author: Benjamin Alt (benjamin_alt@outlook.com)
"""

from __future__ import print_function
import pwmdriver
import argparse
import math

def main(args):
    driver = pwmdriver.ServoDriver(int(args.channel), pulseZero=float(args.pulse_zero), pulsePi=float(args.pulse_pi))
    print("Setting angle on channel {} to {} degrees.".format(args.channel, args.target))
    driver.setAngle(math.radians(float(args.target)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Test program for servo calibration.")
    parser.add_argument("channel", help="The channel on which the servo is running")
    parser.add_argument("pulse_zero", help="The zero position, in ms")
    parser.add_argument("pulse_pi", help="The 180 degrees position, in ms")
    parser.add_argument("target", help="The target position, in degrees")
    main(parser.parse_args())
