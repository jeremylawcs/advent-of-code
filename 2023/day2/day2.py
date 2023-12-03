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
      logging.debug(f"\tParsing color: '{color}'")
      (count, color_name) = color.split(" ")[0:]
      count = int(count)
      color_name = Color.get_color(color_name)
      logging.debug(f"\tColor: {color_name}, count: {count}")
      if most_of_color[color_name] < count:
        logging.debug(f"\tNew highest {color_name}: {count}")
        most_of_color[color_name] = count
  return most_of_color

def debug_print_most_colors(colors, game_number = 0):
  string_stream = ""
  for index, color in enumerate(Color):
    string_stream += f"{color.name}: {colors[color]}"
    if index != len(Color)-1:
      string_stream += " | "
  if game_number != 0:
    string_stream = f"Game number {game_number} colors: " + string_stream
  logging.debug(string_stream)

def part1(input_file):
  result = 0
  for line_index, line in enumerate(input_file):
    line_number = line_index + 1
    line = line.strip()
    logging.debug(f"Parsing '{line}'")
    most_colors = most_colors_in_game(line.split(":")[1])
    debug_print_most_colors(most_colors, line_number)
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
  logging.info(f"Result: {result}")

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

if __name__=="__main__":
  main()
