def reverse_words(text):

    phrase = []
    phrase2 = []
    count = 0
    for word in text.split():
        phrase.append(word[::-1])
    phrasetogether = "".join(phrase)
    phrase.clear()
    for x in phrasetogether:
        phrase.append(x)
    for x in text:
        if x == " ":
            phrase.insert(count, " ")
        phrase2.append(x)
        count = count + 1
    return("".join(phrase))

print(reverse_words("La    venganza sera   terrible"))

