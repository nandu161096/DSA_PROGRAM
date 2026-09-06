def traverse_arr(arr):
    for num in arr:
        print(num)

def min_arr(arr):
    min_val = arr[0]

    for num in arr[1:]:
        if num < min_val:
            min_val = num

    return min_val

arr = [2,4,5,6,78,1]
traverse_arr(arr)
min_value = min_arr(arr)
print("min value is ",min_value)


