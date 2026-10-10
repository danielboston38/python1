rooms = {
    "foyer": {
        "desc":  "A dusty foyer with a cobweb-choked chandelier.",
        "exits": {"north": "hall"},
        "items": ["rusty key"],
    }
}

direction = []
current_room = "foyer"

inventory = []

look = print(rooms[current_room]["desc"])

go = if direction in rooms[current_room]["exits"]:
def move(direction):
    global current_room
    if direction in rooms[current_room]["exits"]:
        current_room = rooms[current_room]["exits"][direction]
        print(rooms[current_room]["desc"])
    else:
        print("You can't go that way.")

