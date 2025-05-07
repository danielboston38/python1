def load_input(day):
    """
    Loads the input file for the given day.
    Expects a file like 'inputs/day01.txt'.
    """
    filename = f"inputs/day{day:02}.txt"
    try:
        with open(filename, 'r') as f:
            return f.read().splitlines()
    except FileNotFoundError:
        print(f"Input file {filename} not found.")
        return []
