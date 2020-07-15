def dig_pow(n, p):
    
    storage = []
    result = 0
    x = n
    while x != 0:
        storage.append(x%10)
        x = x // 10
    storage.reverse()
    x = 0
    while x<len(storage):
        result = result + storage[x]**(x+p)
        x = x + 1
    return result/n if (result/n)==int(result/n) else - 1

print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(695,2))
print(dig_pow(46288, 3))