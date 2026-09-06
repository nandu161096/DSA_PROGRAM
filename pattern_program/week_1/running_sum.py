def running_sum(arr):
    running = []
    current_sum = 0

    for num in arr:
        current_sum = num + current_sum
        running.append(current_sum)

    return running

def print_arr(arr):
    for num in arr:
        print(num)

arr = [1,3,4,5,8]
print_arr(arr)
print(arr)
print(running_sum(arr))
