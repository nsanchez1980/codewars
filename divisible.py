def is_divisible(n,x,y):

    if n%x == 0 and n%y == 0:
        return True
    else:
        return False


print(is_divisible(12,7,5))
