def productFib(prod):
    n1 = 0
    n2 = 1
    n3 = 0
    while True:
        n3 = n1 + n2
        if n1*n2==prod:
            return [n1, n2, True]
        elif n1*n2>prod:
            return [n1, n2, False]
        n1 = n2
        n2 = n3


print(productFib(4895))#, [55, 89, True])
print(productFib(5895))#, [89, 144, False])
