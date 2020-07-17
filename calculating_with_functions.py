def computa(bienputa, num):
    if bienputa[0] == "+":
        return num + bienputa[1]
    elif bienputa[0] == "-":
        return num - bienputa[1]
    elif bienputa[0] == "*":
        return num * bienputa[1]
    else:
        return num // bienputa[1]

def zero(argument=""):
    return 0 if argument=="" else computa(argument,0)
        
def one(argument=""):
    return 1 if argument=="" else computa(argument,1)
        
def two(argument=""):
    return 2 if argument=="" else computa(argument,2)

def three(argument=""):
    return 3 if argument=="" else computa(argument,3)

def four(argument=""):
    return 4 if argument=="" else computa(argument,4)

def five(argument=""):
    return 5 if argument=="" else computa(argument,5)

def six(argument=""):
    return 6 if argument=="" else computa(argument,6)

def seven(argument=""):
    return 7 if argument=="" else computa(argument,7)

def eight(argument=""):
    return 8 if argument=="" else computa(argument,8)

def nine(argument=""):
    return 9 if argument=="" else computa(argument,9)

def plus(num):
    return ["+", num]

def minus(num):
    return ["-", num]

def times(num):
    return ["*", num]

def divided_by(num):
    return ["/", num]


print(seven(times(five())))#, 35)
print(four(plus(nine())))#, 13)
print(eight(minus(three())))#, 5)
print(six(divided_by(two())))#, 3)