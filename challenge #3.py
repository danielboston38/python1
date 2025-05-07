jungle_message = "abc12xy7!@#3gh5$$9pq"
def decodeNumbers(jungle_message):
    total = 0
    current_number = ""
    for letter in jungle_message:
        if letter.isdigit():
            current_number += letter
        else:
            if current_number != "":
                total += int(current_number)
                current_number = ""
    if current_number != "":
        total += int(current_number)
    print(total)

decodeNumbers(jungle_message)


