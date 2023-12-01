#!/usr/bin/python3

import sys
import string
import logging

def main():
  debug_mode = False
  break_line = 0
  log_level = logging.INFO
  for i in range(0, len(sys.argv)):
    if sys.argv[i] == '-d':
      log_level = logging.DEBUG
      debug_mode = True
    elif sys.argv[i] == '-n' and len(sys.argv) >= i:
      i += 1
      break_line = int(sys.argv[i])
  logging.basicConfig(level=log_level)
  with open("data.dat", "r", encoding="utf-8") as input_file:
    accumulated_number = 0
    line_number = 1
    for line in input_file:
      num_string = ""
      for char_idx, ea_character in enumerate(line):
        if ea_character in string.digits:
          num_string += ea_character
      first_and_last = int(num_string[0] + num_string[-1]) 
      accumulated_number +=  first_and_last
      logging.debug("Line %d: %s turns into %d", line_number, num_string, first_and_last)

      # Only process a certain amount of lines
      if break_line > 0 and line_number >= break_line:
        break
      line_number +=1
    logging.info("Total accumuated: %d", accumulated_number)


if __name__=="__main__":
  main()
