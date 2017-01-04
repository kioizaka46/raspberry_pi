#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import wiringpi2 as wp
import sys

def main(argv=sys.argv):
  pin_servo = 12 # サーボモータに接続したGPIO端子番号
  input_degree = int(sys.argv[1]) # 0 ~ 180
  min_range = 50;
  max_range = 140;

  wp.wiringPiSetupGpio()
  wp.pinMode(pin_servo, 2) # GPIO -> PWM

  # setting Pulse Width Modulation.
  wp.pwmSetMode(0)
  wp.pwmSetClock(375)
  wp.pwmSetRange(1024)

  # lerping
  move_deg = min_range + (max_range - min_range) * (input_degree - 0) / (180 - 0);

  # check value
  if move_deg <= 0 or max_range < move_deg:
    exit(1);

  # rotate moter
  wp.pwmWrite(pin_servo, move_deg)

if __name__ == '__main__':
  try:
    arg_command = sys.argv[1]
    if len(sys.argv) != 2:
      raise IndexError("Please set only one argment.")
    main()
  except IndexError:
    print("ERROR, invalid argments.")
    print("Usage : python servo_controller.py [SET_DEGREE(0 ~ 180)]")
