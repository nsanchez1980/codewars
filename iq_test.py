def iq_test(numbers):

    numeros = []
    index = 1
    cuantospares = 0

    for x in numbers.split():
        numeros.append(int(x))
    
    for i in numeros:
        if i%2==0:
            cuantospares = cuantospares + 1
            indexpar = index
        else:
            indeximpar = index
        index = index + 1

    if cuantospares == 1:
        return (indexpar)
    else:
        return (indeximpar)
    


print(iq_test("2 2 1 2"))