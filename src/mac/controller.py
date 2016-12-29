#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from time import time, sleep
import sys

def main(argv=sys.argv):
  # initialize
  fps = 24
  executable_time = 1.0 / fps
  now = time()
  next_start_time = now + executable_time

  # main loop
  while now < next_start_time:
    # do command
    print ("do anything")

    # frame update
    print ("executing time is : %s" % (now - time()))
    sleep(next_start_time - now)
    now = time()
    next_start_time += executable_time

  # timeout error
  try:
    raise Exception('Timeout Error')
  except Exception:
    raise

if __name__ == '__main__':
  main()
