#!/usr/bin/env python3
"""
Advent of Code 2022 - Day N Template
"""

from utils.input_loader import load_input
# Specify the day number here
DAY = 5  # Replace N with the day number, e.g., 3


def part_one(data):
    """
    Solve Part One for Day {DAY}.
    :param data: List[str] of puzzle input lines
    :return: Answer for Part One
    """
    crates = {}

    # 1. Split drawing vs instructions
    split_index = data.index("")  # empty line separates them
    drawing = data[:split_index]

    # 2. Last line of drawing = stack numbers
    number_line = drawing[-1]
    num_stacks = int(number_line.strip().split()[-1])

    # 3. Initialize stacks
    crates = {i: [] for i in range(1, num_stacks + 1)}

    # 4. Process crate lines (bottom → top)
    for line in reversed(drawing[:-1]):  # skip number line
        for i in range(1, num_stacks + 1):
            pos = 1 + (i - 1) * 4  # magic position formula

            # Make sure we don't go out of bounds
            if pos < len(line):
                char = line[pos]
                if char != " ":
                    crates[i].append(char)

    # Move the crates
    instructions = data[split_index + 1:]
    for move in instructions:
        parts = move.split()
        num_to_move = int(parts[1])
        from_stack = int(parts[3])
        to_stack = int(parts[5])
        for i in range(num_to_move):
            if crates[from_stack]:
                crates[to_stack].append(crates[from_stack].pop())

    # Get the top crate from each stack
    result = ""
    for i in range(1, 10):
        result += crates[i][-1]
    return result

def part_two(data):
    crates = {}

    # 1. Split drawing vs instructions
    split_index = data.index("")  # empty line separates them
    drawing = data[:split_index]

    # 2. Last line of drawing = stack numbers
    number_line = drawing[-1]
    num_stacks = int(number_line.strip().split()[-1])

    # 3. Initialize stacks
    crates = {i: [] for i in range(1, num_stacks + 1)}

    # 4. Process crate lines (bottom → top)
    for line in reversed(drawing[:-1]):  # skip number line
        for i in range(1, num_stacks + 1):
            pos = 1 + (i - 1) * 4  # magic position formula

            # Make sure we don't go out of bounds
            if pos < len(line):
                char = line[pos]
                if char != " ":
                    crates[i].append(char)

    # Move the crates
    instructions = data[split_index + 1:]
    for move in instructions:
        parts = move.split()
        num_to_move = int(parts[1])
        from_stack = int(parts[3])
        to_stack = int(parts[5])
        grabbed = crates[from_stack][-num_to_move:]
        crates[to_stack].extend(grabbed)
        crates[from_stack] = crates[from_stack][:-num_to_move]

    result = ""
    for i in range(1, 10):
        result += crates[i][-1]
    return result

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
