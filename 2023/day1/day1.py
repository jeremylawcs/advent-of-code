#!/usr/bin/python3

import sys
import string
import logging

def find_numbers(line):
  array=["1", "2", "3", "4", "5", "6", "7", "8", "9", 
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
  # Tuples in the order of (index, value)
  low = [-1, -1]
  high = [-1, -1]
  for index, number_string in enumerate(array):
    number = int(number_string if number_string.isdigit() else array[index-9])
    logging.debug("\tSearching for %s", number_string)

    find_index = line.find(number_string)
    if find_index >= 0:
      if low[0] == -1: # has not found anything
        low[0] = find_index
        low[1] = number
      elif find_index < low[0]: # after initial find
        low[0] = find_index
        low[1] = number

      if low[1] == number:
        logging.debug("\tNew low found: %s", number_string);


    rfind_index = line.rfind(number_string)
    if rfind_index >= 0:
      if high[0] == -1: # has not found anything
        high[0] = rfind_index
        high[1] = number
      elif rfind_index > high[0]: # after initial find
        high[0] = rfind_index
        high[1] = number

      if high[1] == number:
        logging.debug("\tNew high found: %s", number_string);

  return (low[1], high[1])


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
      line = line.strip()
      logging.debug("Line %d: '%s'.", line_number, line)
      num_string = ""
      lowest, highest = find_numbers(line)
      logging.debug("\tLowest: %s, highest: %s", lowest, highest)
      low_high_string = f"{lowest}{highest}"
      first_and_last = int(low_high_string) 
      accumulated_number +=  first_and_last
      logging.debug("\tNew accumulated value: %s", accumulated_number)

      # Only process a certain amount of lines
      if break_line > 0 and line_number >= break_line:
        break
      line_number +=1
    logging.info("Total accumuated: %d", accumulated_number)


if __name__=="__main__":
  main()
