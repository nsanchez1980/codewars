def alphanumeric(password):
    import re
    return False if password=="" or re.search("[^A-Za-z0-9]",password) else True


print(alphanumeric("hello world_"))#, False),
print(alphanumeric("PassW0rd"))#, True),
print(alphanumeric("     "))#, False)