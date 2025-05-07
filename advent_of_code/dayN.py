#!/usr/bin/env python3
"""
Advent of Code 2022 - Day N Template
"""

from utils.input_loader import load_input

# Specify the day number here
DAY = N  # Replace N with the day number, e.g., 3

def part_one(data):
    """
    Solve Part One for Day {DAY}.
    :param data: List[str] of puzzle input lines
    :return: Answer for Part One
    """
    # TODO: implement Part One logic
    return None


def part_two(data):
    """
    Solve Part Two for Day {DAY}.
    :param data: List[str] of puzzle input lines
    :return: Answer for Part Two
    """
    # TODO: implement Part Two logic
    return None


def main():
    # Load the input for this day
    data = load_input(DAY)
    
    # Compute answers
    answer1 = part_one(data)
    answer2 = part_two(data)

    # Print results
    print(f"Day {DAY} - Part 1: {answer1}")
    print(f"Day {DAY} - Part 2: {answer2}")


if __name__ == "__main__":
    main()
