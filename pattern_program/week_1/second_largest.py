def second_largest(arr):
    largest = float('-inf')
    second = float('-inf')

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num

    return second

arr = [1,2,3,4,5,8,10]
print(second_largest(arr))
