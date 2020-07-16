def move_zeros(array):
    result = []
    result2 = []
    index = 0

    while index < len(array):
        if type(array[index])==bool:
            result2.append(array[index])
        elif array[index] == 0:
            result.append(0)
        else:
            result2.append(array[index])
        index = index + 1
    return result2 + result
 



print(move_zeros([1,2,0,1,0,1,0,3,0,1]),[ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])
print(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]),[9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
print(move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]),["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
print(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]),["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])
print(move_zeros([0,1,None,2,False,1,0]),[1,None,2,False,1,0,0])
print(move_zeros(["a","b"]),["a","b"])
print(move_zeros(["a"]),["a"])
print(move_zeros([0,0]),[0,0])
print(move_zeros([0]),[0])
print(move_zeros([False]),[False])
print(move_zeros([]),[])