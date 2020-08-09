def number2words(n):
    onedigits = ["zero","one","two","three","four","five","six","seven","eight","nine",
                "ten", "eleven","twelve","thirteen","fourteen", "fifteen", "sixteen",
                "seventeen","eighteen","nineteen"]
    twodigits = ["", "", "twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    result = ""

    def letrificar(num):
        result = ""
        if num>=100:
            result = onedigits[int(str(num)[0])] + " hundred "
            num = num - int(str(num)[0])*100
            if num==0:
                return result.rstrip()
        if num<100 and num>=20:
            result = result + twodigits[int(str(num)[0])] + "-"
            num = num - int(str(num)[0])*10
            if num==0:
                return result.lstrip("-").rstrip("-")
        if num<20:
            return result + onedigits[num]

    if n<20:
        return onedigits[n]
    if n>=1000:
        n1=n%1000
        n2=n//1000
        result = letrificar(n2) + " thousand"
        if n1>0:
            result = result + " " + letrificar(n1)
        return result
    else:
        return letrificar(n)

    return result




print(number2words(1394))
