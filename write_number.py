def expanded_form(num):

    storage = []
    result = ""
    while num != 0:
        storage.append(num%10)
        num = num // 10
    n = 0
    while n < len(storage):
        if storage[len(storage)-n-1]!=0:
            result = result + str(storage[len(storage)-n-1]) + str(10**(len(storage)-n-1)).lstrip("1") + " + "
        n = n + 1    
    return result.rstrip(" + ")

print(expanded_form(12), '10 + 2')
print(expanded_form(42), '40 + 2')
print(expanded_form(70304), '70000 + 300 + 4')