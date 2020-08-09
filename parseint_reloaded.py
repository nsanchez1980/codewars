def parse_int(string):
    digit = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", 
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    twodigits = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    result = 0
    if string=="one million":
        return 1000000
    
    def parse_dashes(numberwithdash):
        x = 0
        if numberwithdash.find("-")!=-1:
            primer_cifra = numberwithdash.split("-")
            x = int(digit.index(primer_cifra[1]))
            x = x + int(twodigits.index(primer_cifra[0])*10)
        else:
            if numberwithdash in twodigits:
                x = int(twodigits.index(numberwithdash))*10
            else:
                x = int(digit.index(numberwithdash))
        return x
    
    def parse_hundreds(hundreds):
        index = 0
        result = 0
        while index<len(hundreds):
            if hundreds[index]=="hundred":
                result = result*100
            elif hundreds[index]=="and":
                pass
            elif hundreds[index]=="":
                pass
            else:
                result = result + parse_dashes(hundreds[index])
            index = index + 1
        return result
    
        
    numero = string.split(" ")
    if "thousand" in numero:
        partido = " ".join(numero).split("thousand")
        result = parse_hundreds(partido[0].split(" "))*1000 + parse_hundreds(partido[1].split(" "))
    else:
        result = parse_hundreds(numero)

    return result




print(parse_int("seven hundred eighty-three thousand nine hundred and nineteen"))
#print(parse_int('one'), 1)
#print(parse_int('twenty'), 20)
#print(parse_int('two hundred forty-six'), 246)