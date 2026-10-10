#!/usr/bin/env python3
"""
Advent of Code 2022 - Day N Template
"""

from utils.input_loader import load_input

# Specify the day number here
DAY = 4  # Replace N with the day number, e.g., 3


def part_one(data):
    """
    Solve Part One for Day {DAY}.
    :param data: List[str] of puzzle input lines
    :return: Answer for Part One
    """
    elf_pairs = []
    for line in data:
        parts = line.split(",")
        start1, end1 = map(int, parts[0].split("-"))
        start2, end2 = map(int, parts[1].split("-"))
        if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
            elf_pairs.append((start1, end1, start2, end2))
    return len(elf_pairs)


def part_two(data):
    """
    Solve Part Two for Day {DAY}.
    :param data: List[str] of puzzle input lines
    :return: Answer for Part Two
    """
    elf_pairs = []
    for line in data:
        parts = line.split(",")
        start1, end1 = map(int, parts[0].split("-"))
        start2, end2 = map(int, parts[1].split("-"))
        if not (end1 < start2 or end2 < start1):
            elf_pairs.append((start1, end1, start2, end2))



    return len(elf_pairs)


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
