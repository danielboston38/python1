sentence = "Quantum coding bunnies bravely glitch through binary backdrops while sipping synthwave lattes.".lower()
words = sentence.strip().split()

fellowship = {}
for word in words:
    key = word[0]
    if key not in fellowship:
        fellowship[key] = []
    fellowship[key].append(word)
print(fellowship)