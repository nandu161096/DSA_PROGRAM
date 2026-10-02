def sec_dist_largest(arr):
    largest = second = float("-inf")
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif (num > second) and (num < largest):
            second = num
    return second

arr = [10, 5, 8, 10, 3, 7]
print(sec_dist_largest(arr))
