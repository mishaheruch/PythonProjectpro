def dictionaries_keys(dictionary):
    return list(dictionary.keys())

print(dictionaries_keys({'a': 1, 'b': 2, 'c': 3}))

def dictionaries_tu(dictionary1, dictionary2):
    return dictionary1 | dictionary2
print(dictionaries_tu({'a': 1, 'b': 2, 'c': 3}, {'d': 4, 'f': 5}))

