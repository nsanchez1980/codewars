def array_diff(a, b):
    
    c = []
    for n in a: 
        if n not in b: 
            c.append(n)
    return c


print(array_diff([1,2], [1]), "a was [1,2], b was [1], expected [2]")
print(array_diff([1,2,2], [1]), "a was [1,2,2], b was [1], expected [2,2]")
print(array_diff([1,2,2], [2]), "a was [1,2,2], b was [2], expected [1]")
print(array_diff([1,2,2], []), "a was [1,2,2], b was [], expected [1,2,2]")
print(array_diff([], [1,2]), "a was [], b was [1,2], expected []")