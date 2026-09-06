def move_zeros(arr):
    pos = 0

    for num in arr:
        if num != 0:
            arr[pos] = num
            pos = pos + 1

    while pos < len(arr):
        arr[pos] = 0
        pos = pos +1

    return arr

arr = [0,1,0,3,0,2,4,15,0]
print(move_zeros(arr))
