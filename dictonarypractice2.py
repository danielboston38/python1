# dictionarypractice2.py

# 1. Lowercase & split into words
sentence = "Curious coding bunnies bravely bounce between branches and nibble on bright berries".lower()
words = sentence.strip().split()

# 2. Build the bigram map
bigrams = {}
for i in range(len(words) - 1):
    w1 = words[i]
    w2 = words[i + 1]
    if w1 not in bigrams:
        bigrams[w1] = []
    bigrams[w1].append(w2)

# 3. Inspect the result
print(bigrams)