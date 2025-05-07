import string
sentence_ru = "Князь Андрей Болконский часто размышлял о смысле жизни.".lower()
sentence = sentence_ru.translate(str.maketrans('', '', string.punctuation))
words_ru = sentence_ru.split()
#print(words)
russian_vowels = "аеёиоуыэюя"
vowel_count_ru = {}
for word in words_ru:
    count = 0
    for char in word:
        if char in russian_vowels:
            count += 1
    vowel_count_ru[word] = count
print(vowel_count_ru)
