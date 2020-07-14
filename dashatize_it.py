def dashatize(num):
    if num == None: return "None"
    num = abs(num)
    previous = False
    n = 0
    result = ""
    while n < len(str(num)):
        if str(num)[n] == "-":
            break
        if int(str(num)[n])%2!=0:
            if n==0:
                if len(str(num))==1:
                    result = str(num)[n]
                else:
                    result = str(num)[n] + "-"
                    previous = True
            elif n==len(str(num))-1:
                if previous:
                    result = result + str(num)[n]
                else:
                    result = result + "-" + str(num)[n]
            else:
                if previous:
                    result = result + str(num)[n] + "-"
                else:
                    result = result + "-" + str(num)[n] + "-"
                    previous = True
        else:
            result = result + str(num)[n]
            previous = False
        n = n + 1
    
    return result





print(dashatize(274))#,"2-7-4", "Should return 2-7-4")
print(dashatize(5311))#,"5-3-1-1", "Should return 5-3-1-1")
print(dashatize(86320))#,"86-3-20", "Should return 86-3-20")
print(dashatize(974302))#,"9-7-4-3-02", "Should return 9-7-4-3-02")
print(dashatize(None))#,"None", "Should return None");
print(dashatize(0))#,"0", "Should return 0");
print(dashatize(-1))#,"1", "Should return 1");
print(dashatize(-28369))#,"28-3-6-9", "Should return 28-3-6-9");