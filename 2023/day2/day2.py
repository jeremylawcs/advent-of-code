#!/usr/bin/python3

import sys
import string
import logging

from enum import IntEnum

class Color(IntEnum):
  RED = 0
  GREEN = 1
  BLUE = 2

  def get_color(string_name):
    string_name = string_name.lower()
    if string_name == "red":
      return Color.RED
    elif string_name == "green":
      return Color.GREEN
    elif string_name == "blue":
      return Color.BLUE
    return ValueError(f"Cannot turn {string_name} into a Color")

game1_config = {Color.RED: 12, Color.GREEN: 13, Color.BLUE: 14}

def get_num_color(color):
  logging.debug(f"\tParsing color: '{color}'")
  (count, color_name) = color.split(" ")[0:]
  count = int(count)
  color_name = Color.get_color(color_name)
  return (count, color_name)

def most_colors_in_game(line):
  # line in format "4 blue, 4 red, 16 green; 14 green, 5 red; 1 blue, 3 red, 5 green"
  most_of_color = [0, 0, 0]
  game_rounds = line.split(";")
  for each_round in game_rounds:
    logging.debug(f"\tParsing round: '{each_round}'")
    split_on_color = each_round.split(",")
    # " 4 red"
    for color in split_on_color:
      color = color.strip()
      (count, color_name) = get_num_color(color)
      logging.debug(f"\tColor: {color_name}, count: {count}")
      if most_of_color[color_name] < count:
        logging.debug(f"\tNew highest {color_name}: {count}")
        most_of_color[color_name] = count
  return most_of_color

def debug_print_colors(colors, game_number = 0):
  if logging.getLogger().getEffectiveLevel() != logging.DEBUG:
    return

  string_stream = ""
  for index, color in enumerate(Color):
    string_stream += f"{color.name}: {colors[color]}"
    if index != len(Color)-1:
      string_stream += " | "
  if game_number != 0:
    string_stream = f"Game number {game_number} colors: " + string_stream
  return string_stream

def part1(input_file):
  result = 0
  for line_index, line in enumerate(input_file):
    line_number = line_index + 1
    line = line.strip()
    logging.debug(f"Parsing '{line}'")
    most_colors = most_colors_in_game(line.split(":")[1])
    string_stream = debug_print_colors(most_colors, line_number)
    logging.debug(string_stream)
    valid_game = True
    for color in Color:
      if most_colors[color] > game1_config[color]:
        valid_game = False
        logging.debug(f"Invalid case: {color.name} ({most_colors[color]}) in game {line_number}"
                      f" bigger than game config {game1_config[color]}")
        break
    if valid_game:
      result += line_number

    logging.debug(f"New result: {result}")
  logging.info(f"Part 1 result: {result}")

def min_power(line):
  color_tracker = [-1, -1, -1]
  game_rounds = line.split(";")
  for each_round in game_rounds:
    logging.debug(f"\tParsing round: '{each_round}'")
    split_on_color = each_round.split(",")
    # " 4 red"
    for color in split_on_color:
      color = color.strip()
      (count, color_name) = get_num_color(color)
      # if initial, just take value
      if color_tracker[color_name] == -1:
        color_tracker[color_name] = count
      elif color_tracker[color_name] < count:
        color_tracker[color_name] = count
  return color_tracker

def part2(input_file):
  result = 0
  for line_index, line in enumerate(input_file):
    line_number = line_index + 1
    line = line.strip()
    logging.debug(f"Parsing '{line}'")
    colors = min_power(line.split(":")[1])
    string_stream = debug_print_colors(colors)
    logging.debug(f"\tMin power: {string_stream}")
    result += colors[0] * colors[1] * colors[2]
    logging.debug(f"New result: {result}")
  logging.info(f"Part 2 result: {result}")
  

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
    part1(input_file)
  with open("data.dat", "r", encoding="utf-8") as input_file:
    part2(input_file)

if __name__=="__main__":
  main()
