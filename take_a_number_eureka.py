##Weird weird kata, it fails one random test (with huge numbers), and then
##the next try it passes, without changing a single line of code.
##Quantum computing, here we go!!!!!

def sum_dig_pow(a, b):

    
    import math
    def how_many_digits(num):
        count = 0
        while num>=1:
            num = num//10
            count = count + 1
        return count
    result = []
    digits = 0
    sum = 0
    for index in range(a,b+1):
        nextnumber = index
        if index < 10:
            result.append(index)
        else:
            while nextnumber>9:
                digits = how_many_digits(nextnumber)
                thisnumber = math.fmod(nextnumber,10)
                nextnumber = nextnumber//10
                sum = sum + math.pow(thisnumber,digits)
            sum = sum + nextnumber
        if sum == index:
            result.append(index)
        sum = 0
        index = index + 1

    return result



print(sum_dig_pow(0,12156000))
