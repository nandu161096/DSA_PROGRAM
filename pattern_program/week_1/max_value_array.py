def traverse_arr(arr):
    for num in arr:
        print(num)

def max_arr(arr):
    max_val = arr[0]

    for num in arr[1:]:
        if num > max_val:
            max_val = num

    return max_val

arr = [1,4,5,6,78]
traverse_arr(arr)
max_value = max_arr(arr)
print("max value is ",max_value)


