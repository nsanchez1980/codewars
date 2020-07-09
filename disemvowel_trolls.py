def disemvowel(string):

    input = []
    for x in string:
        if x not in "aeiouAEIOU":
            input.append(x)
    return("".join(input))

print(disemvowel("El estigma del doctor vaporeso"))