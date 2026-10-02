def move_zeros(arr):
    #modified_arr = [0] * len(arr)
    modified_arr = []
    cnt = 0

    for num in arr:
        if num != 0:
            modified_arr.append(num)
            cnt += 1
    for i in range(len(arr)-cnt):
        modified_arr.append(0)

    return modified_arr

arr = [0, 1, 0, 3, 12]
print(move_zeros(arr))
