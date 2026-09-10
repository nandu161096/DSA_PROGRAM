def suffix_sum(arr):
    length = len(arr)
    print("length of arr",length)
    suffix = [0] * len(arr)
    suffix[length-1] = arr[length-1]
    for i in range(length-2,-1,-1):
        suffix[i] = suffix[i+1] + arr[i]
    return suffix

arr = [2,4,1,7,3]
print(arr)
print(suffix_sum(arr))
