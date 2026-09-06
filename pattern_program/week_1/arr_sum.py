def print_arr(arr):
    for num in arr:
        print(num)

def array_sum(arr):
    total = 0

    for num in arr:
        total = total + num

    return total

arr = [1,2,3,5,6,7]
print_arr(arr)
total = array_sum(arr)
print("Total sum is ",total)
