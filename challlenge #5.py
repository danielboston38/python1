def repeater():
    messages = []
    while True:
        msg = input("Say something (or 'quit' to exit): ")
        cleaned = msg.lower().strip()
        if cleaned == "quit":
            break
        elif cleaned == "reset":
            messages.clear()
            print("Messages Cleared")
            continue
        elif cleaned not in messages:
            messages.append(cleaned)
            print("Message recorded.")
        else:
            print("You've already said that!")
repeater()