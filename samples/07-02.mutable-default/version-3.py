
def count_vowels(text, counts=[0, 0, 0, 0, 0, 0]):
    vowels = 'aeiouy'
    for c in text.lower():
        index = vowels.find(c)
        if index >= 0:
            counts[index] += 1
    return counts

print(count_vowels('hello'))
print(count_vowels('hello')) # тут будет неожиданность

