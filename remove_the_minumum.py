def remove_smallest(numbers):

    intermedio = []
    resultado = []
    if len(numbers)== 0:
        return resultado
    index = 0
    menor = numbers[0]
    while index<len(numbers):
        if numbers[index]<menor:
            menor = numbers[index]
        intermedio.append(numbers[index])
        index = index + 1
    index = 0
    while index<len(numbers):
        if index != (numbers.index(menor)):
            resultado.append(numbers[index])
        index = index + 1

    return(resultado)


print(remove_smallest([2,2,1,2,1]))