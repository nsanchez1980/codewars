def is_interesting(number, awesome_phrases):

    def all_zeroes(n):
        stripped = str(n)[1:]
        for x in stripped:
            if x!="0":
                return False
        return True

    def same_digits(n):
        if n<100:
            return False
        stringed = str(n)
        a = stringed[0]
        for x in stringed:
            if x!=a:
                return False
        return True

    def sequential(n):
        if n<100:
            return False
        stringed = str(n)
        x = 0
        while x<len(stringed)-1:
            to_comp = int(stringed[x])
            to_comp_next = int(stringed[x+1])
            if to_comp==0:
                to_comp = 10
            if to_comp_next==0:
                to_comp_next = 10
            if to_comp+1!=to_comp_next:
                return False
            x = x + 1
        return True
    
    def reverse_sequential(n):
        if n<100:
            return False
        stringed = str(n)
        x = 0
        while x<len(stringed)-1:
            to_comp = int(stringed[x])
            to_comp_next = int(stringed[x+1])
            if to_comp-1!=to_comp_next:
                return False
            x = x + 1
        return True        

    def palindrome(n):
        if n<100:
            return False
        stringed = str(n)
        if len(stringed)%2==0:
            if stringed[:len(stringed)//2][::-1] == stringed[len(stringed)//2:]:
                return True
        else:
            if stringed[:len(stringed)//2][::-1] == stringed[len(stringed)//2+1:]:
                return True
        return False
        

    if number<98:
        return 0
    x = 0
    interestingness = 2
    first_iteration = True
    while x<3:
        if all_zeroes(number)==True:
            return interestingness
        if same_digits(number)==True:
            return interestingness
        if sequential(number)==True:
            return interestingness
        if reverse_sequential(number)==True:
            return interestingness
        if palindrome(number)==True:
            return interestingness
        if number in awesome_phrases:
            return interestingness
        if first_iteration==True:
            interestingness = 1
            first_iteration==False
        x = x + 1
        number = number + 1

    return 0

print(is_interesting(3210, [1337, 256])," 'expected': 2")
print(is_interesting(3, [1337, 256])," 'expected': 0")
print(is_interesting(1336, [1337, 256])," 'expected': 1")
print(is_interesting(1337, [1337, 256])," 'expected': 2")
print(is_interesting(11208, [1337, 256])," 'expected': 0")
print(is_interesting(11209, [1337, 256])," 'expected': 1")
print(is_interesting(11211, [1337, 256])," 'expected': 2")