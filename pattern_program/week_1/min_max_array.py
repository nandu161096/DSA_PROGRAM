def traverse_arr(arr):
    for num in arr:
        print(num)

def min_max_arr(arr):
    min_val = arr[0]
    max_val = arr[0]

    for num in arr[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return min_val, max_val

arr = [2,4,5,6,78,1]
traverse_arr(arr)
min_value, max_value = min_max_arr(arr)
print("min value is ",min_value,"Max value is ",max_value)


