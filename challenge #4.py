spy_message = "aHtbeClldoeG"
def decodeSpyName(spy_message):
    message = []
    for index in range(len(spy_message)):
        if index % 2 ==1:
            message.append(spy_message[index])
        else:
            pass
    print("".join(message))

decodeSpyName(spy_message)