def wave(people):

    if people == "": return []
    resultado = []
    resultado2 = []
    index = 0
    index2 = 0
    capitalizar = 0
    palabra = list(people)
    palabra2 = []
    traduccion = ""
    while index < len(people):
        while index2 < len(people):
            if capitalizar == index2:
                palabra2.append(str(palabra[index2]).capitalize())
            else:
                palabra2.append(str(palabra[index2]))
            index2 = index2 + 1
        index = index + 1
        index2 = 0
        capitalizar = capitalizar + 1
        resultado.append("".join(palabra2))
        palabra2 = []
    for x in resultado:
        if x!=people:
            resultado2.append(x)


    return resultado2

print(wave(" gap "))