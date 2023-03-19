
def count_vowels(text, counts):
    vowels = 'aeiouy'
    for c in text.lower():
        index = vowels.find(c)
        if index >= 0:
            counts[index] += 1

counts = [0] * 6
count_vowels('hello', counts)
print(counts)
count_vowels('index', counts)
print(counts)

