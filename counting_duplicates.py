def duplicate_count(text):

    a = dict()
    count = 0

    for x in text.lower():
        a[x] = a.get(x, 0) + 1
    for y in a:
        if a.get(y) > 1:
            count = count + 1

    return count

print(duplicate_count("ABBA"))