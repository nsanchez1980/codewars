def revrot(strng, sz):
    if sz<=0 or strng=="" or sz>len(strng):
        return ""
    chunks = []
    result = []
    resultinastring = ""
    n = 0
    while n < len(strng):
        if len(strng)-n<sz:
            break
        chunks.append(strng[n:n+sz])
        n = n + sz
    n = 0
    calculo = 0
    x = 0
    while n < len(chunks):
        while x < sz:
            calculo = calculo + int(chunks[n][x])**3
            x = x + 1
        if calculo%2==0:
            result.append(chunks[n][::-1])
        else:
            result.append(chunks[n][1:] + chunks[n][0:1])
        n = n + 1
        x = 0
        calculo = 0
    n = 0
    while n<len(result):
        resultinastring = resultinastring + result[n]
        n = n + 1

    return resultinastring






print(revrot("123456987654", 6)) #--> "234561876549"
print(revrot("123456987653", 6)) #--> "234561356789"
print(revrot("66443875", 4)) #--> "44668753"
print(revrot("66443875", 8)) #--> "64438756"
print(revrot("664438769", 8))# --> "67834466"
print(revrot("123456779", 8))# --> "23456771"
print(revrot("", 8)) #--> ""
print(revrot("123456779", 0))# --> "" 
print(revrot("563000655734469485", 4)) #--> "0365065073456944"