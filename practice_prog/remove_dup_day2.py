def remove_duplicates(arr):
    dup_rem = []
    arr.sort()
    dup_rem.append(arr[0])
    for i,nums in enumerate(arr):
        if (i == 0):
            continue
        if (arr[i] != arr[i-1]):
            dup_rem.append(arr[i])

    return dup_rem

arr = [1, 2, 2, 3, 1, 4, 3]
print(arr)
print(remove_duplicates(arr))
