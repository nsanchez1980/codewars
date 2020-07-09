def persistence(n):

    if n<10:
        return(0)
    numero = []
    cuenta = 0
    result = 1
    while True:
        numero.clear()
        for x in str(n):
            numero.append(int(x))
            result = result * int(x)
        numero.clear()
        cuenta = cuenta + 1
        if result < 10:
            return cuenta
        else:
            n = result
            result = 1
            continue


print(persistence(999))