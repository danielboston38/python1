#find secret message in the string

message = "XyzcHatGptbEstuDENTm"
def decodeMessage(message):
    decoded = ""
    for letter in message:
        if letter.isupper():
            decoded += letter
    print(decoded)

decodeMessage(message)




