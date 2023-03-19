
def count_vowels(text, counts=None):
    if counts is None:
        counts = [0, 0, 0, 0, 0, 0]
    vowels = 'aeiouy'
    for c in text.lower():
        index = vowels.find(c)
        if index &ge; 0:
            counts[index] += 1
    return counts

print(count_vowels('hello'))
print(count_vowels('hello'))

