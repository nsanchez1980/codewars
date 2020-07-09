def sum_two_smallest_numbers(numbers):

    filtered = []
    for x in numbers:
        if x >= 0 and (x%1)==0:
            filtered.append(x)
    filtered = sorted(filtered)
    return filtered[0]+filtered[1]




print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))