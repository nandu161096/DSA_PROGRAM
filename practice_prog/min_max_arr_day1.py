def min_max_arr(arr):
    min_val = float('+inf')
    max_val = float('-inf')

    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return [min_val, max_val]

arr = [7, 2, 9, 4, 1, 6]
print(min_max_arr(arr))

