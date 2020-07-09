import math

def is_square(n):  
    
    if n<0: return False 
    else: return(math.sqrt(n) == (math.floor(math.sqrt(n))))


print(is_square(-5))