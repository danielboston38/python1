#!/usr/bin/env python3
"""
Advent of Code 2022 - Day Setup
Automates creation of dayN.py template and downloads puzzle input
Usage: python setup.py <day_number>
Example: python setup.py 5
"""

import sys
import os
import requests
from pathlib import Path
from dotenv import load_dotenv


def main():
    # Load environment variables from .env
    load_dotenv()
    session_cookie = os.getenv("SESSION_COOKIE")
    
    if not session_cookie:
        print("ERROR: SESSION_COOKIE not found in .env file")
        print("Please create a .env file with: SESSION_COOKIE=your_cookie_here")
        sys.exit(1)
    
    # Get day number from command line
    if len(sys.argv) != 2:
        print("Usage: python setup.py <day_number>")
        print("Example: python setup.py 5")
        sys.exit(1)
    
    try:
        day = int(sys.argv[1])
    except ValueError:
        print(f"ERROR: '{sys.argv[1]}' is not a valid day number")
        sys.exit(1)
    
    if day < 1 or day > 25:
        print("ERROR: Day must be between 1 and 25")
        sys.exit(1)
    
    day_padded = f"{day:02d}"
    solution_file = f"day{day_padded}.py"
    input_file = f"inputs/day{day_padded}.txt"
    
    # Create solution file if it doesn't exist
    if not os.path.exists(solution_file):
        print(f"Creating {solution_file}...")
        template = f'''#!/usr/bin/env python3
"""
Advent of Code 2022 - Day {day}
"""

from utils.input_loader import load_input

# Specify the day number here
DAY = {day}

def part_one(data):
    """
    Solve Part One for Day {{DAY}}.
    :param data: List[str] of puzzle input lines
    :return: Answer for Part One
    """
    # TODO: implement Part One logic
    return None


def part_two(data):
    """
    Solve Part Two for Day {{DAY}}.
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
    print(f"Day {{DAY}} - Part 1: {{answer1}}")
    print(f"Day {{DAY}} - Part 2: {{answer2}}")


if __name__ == "__main__":
    main()
'''
        with open(solution_file, 'w') as f:
            f.write(template)
        print(f"✓ Created {solution_file}")
    else:
        print(f"✓ {solution_file} already exists, skipping")
    
    # Download puzzle input if it doesn't exist
    if not os.path.exists(input_file):
        print(f"Downloading puzzle input for day {day}...")
        
        # Create inputs directory if needed
        os.makedirs("inputs", exist_ok=True)
        
        url = f"https://adventofcode.com/2022/day/{day}/input"
        headers = {
            "Cookie": f"session={session_cookie}",
            "User-Agent": "github.com/danielboston38/ by mark@dymek.me"
        }
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            with open(input_file, 'w') as f:
                f.write(response.text)
            print(f"✓ Downloaded to {input_file}")
        except requests.exceptions.RequestException as e:
            print(f"ERROR: Failed to download input: {e}")
            sys.exit(1)
    else:
        print(f"✓ {input_file} already exists, skipping")
    
    print(f"\n✓ Day {day} is ready! Start coding in {solution_file}")


if __name__ == "__main__":
    main()