#!/usr/bin/env python3
"""
Advent of Code 2022 - Day 6
"""

from utils.input_loader import load_input

# Specify the day number here
DAY = 6

def part_one(data):
    for i in range(len(data)):
        comm = set(data[i:i+4])
        if len(comm) == 4:
            return i+4


def part_two(data):
        for i in range(len(data)):
            comm = set(data[i:i + 14])
            if len(comm) == 14:
                return i + 14


def main():
    # Load the input for this day
    data = load_input(DAY)
    data = "".join(data)

    # Compute answers
    answer1 = part_one(data)
    answer2 = part_two(data)

    # Print results
    print(f"Day {DAY} - Part 1: {answer1}")
    print(f"Day {DAY} - Part 2: {answer2}")



if __name__ == "__main__":
    main()
