def count_chars(word):
    res = {}
    for char in word:
        if char in res:
            res[char] += 1
        else:
            res[char] = 1
    return res


word = "Happiness"
print(count_chars(word))
word = "smiles"
print(count_chars(word))
