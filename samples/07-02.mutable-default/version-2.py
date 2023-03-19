
def count_vowels(text, counts):
    vowels = 'aeiouy'
    for c in text.lower():
        index = vowels.find(c)
        if index >= 0:
            counts[index] += 1
    return counts

counts = [0] * 6
print(count_vowels('hello', counts))
print(count_vowels('index', counts))

