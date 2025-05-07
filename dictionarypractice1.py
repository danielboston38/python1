sentence = "Curious coding bunnies bravely bounce between branches and nibble on bright berries."

letters = {}

for index, letter in enumerate(sentence):
    if not letter.isalpha():
        continue
    if letter not in letters:
        letters[letter] = [index]
    else:
        letters[letter].append(index)

print(letters)