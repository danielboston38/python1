# heist.py
import sys

# --- 1. Command functions ---------------------------------
def ping(args):
    """ping -> prints PONG"""
    print("PONG!")

def quit_(args):
    """quit -> exits the program"""
    print("Later, hacker!")
    sys.exit(0)

def unknown(args):
    """fallback when verb not recognised"""
    print(f"No such command: {args}")

# --- 2. Dispatcher table ----------------------------------
COMMANDS = {
    "ping": ping,
    "quit": quit_,   # avoid clashing with Python's keyword
}

# --- 3. REPL loop -----------------------------------------
def main():
    while True:
        line = input("bbs> ")
        if not line.strip():
            continue                    # ignore blank lines
        verb, *rest = line.strip().split(maxsplit=1)
        args = rest[0] if rest else ""
        COMMANDS.get(verb, unknown)(args)

if __name__ == "__main__":
    main()