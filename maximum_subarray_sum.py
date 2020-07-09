def max_sequence(arr):

    #checks if array is all-negative
    negatives = 0
    for x in arr:
        if x<0:
            negatives = negatives + 1
    if len(arr)==negatives:
        print("All negatives")
        return(0)

    #Ok, let's start
    head = 0
    suma = 0
    biggest_sum = 0
    amount = 2
    while head < len(arr):
        while amount <= len(arr):
            suma = sum(arr[head:amount])
            if suma > biggest_sum: biggest_sum = suma
            amount = amount + 1
            print(amount)
        amount = 2
        head = head + 1

    return biggest_sum

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))