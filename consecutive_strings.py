def longest_consec(strarr, k):


    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ""
    result = []
    stringy = ""
    n = 0
    x = 0
    y = 0
    lenght = 0
    index = 0
    while x<len(strarr)-k+1:
        while y<k:
            stringy = stringy + strarr[x+y]
            y = y + 1
        result.append(stringy)
        y = 0
        x = x + 1
        stringy = ""
    while n<len(result):
        if len(result[n])>lenght:
            index = n
            lenght = len(result[n])
        n = n + 1
    
    
    return result[index]


        
    

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))#, "abigailtheta")
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))#, "oocccffuucccjjjkkkjyyyeehh")
print(longest_consec([], 3))#, "")
print(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2))#, "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
print(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2))#, "wlwsasphmxxowiaxujylentrklctozmymu")
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2))#, "")
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))#, "ixoyx3452zzzzzzzzzzzz")
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15))#, "")
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0))#, "")