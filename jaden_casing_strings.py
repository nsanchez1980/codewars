def to_jaden_case(string):

    result = ""
    wasspace = True

    for x in string:
        if x.isalpha():
            if wasspace==True:
                result = result + x.upper()
                wasspace = False
            else:
                result = result + x
        elif x.isspace():
                wasspace = True
                result = result + x
        else:
            result = result + x
 
    return result


print(to_jaden_case("me parece que me voy a la mierda ,ameo"))