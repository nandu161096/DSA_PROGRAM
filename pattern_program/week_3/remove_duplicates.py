def remove_dup(arr):
    length = len(arr)
    
    if length <= 1:
        return arr
    idx = 1

    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            arr[idx] = arr[i]
            idx += 1
    return idx

arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
print(arr)
uniq = remove_dup(arr)
for i in range(0,uniq):
    print(arr[i])

print(arr)
