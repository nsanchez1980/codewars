def count(string):

    result = {}
    for letter in string:
        result[letter] = result.get(letter, 0) + 1
    return result

print(count("aba"))