def list_squared(m, n):
    import math
    result = []
    sum = 0
    i = m
    x = 1
    while i<=n:
        while x<=math.sqrt(i):
            if i%x==0:
                if i/x==x:
                    sum = sum + x*x
                else:
                    sum = sum + x*x + math.pow(i/x,2)
            x = x + 1
        if int(math.sqrt(sum))==math.sqrt(sum):
            result.append([i,sum])
        x = 1
        sum = 0
        i = i + 1
    return result

print(list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]])
print(list_squared(42, 250), [[42, 2500], [246, 84100]])
print(list_squared(250, 500), [[287, 84100]])
    