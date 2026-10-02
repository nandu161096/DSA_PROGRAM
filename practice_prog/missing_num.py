def missing_num(arr):
    max_val = max(arr)
    for i in range(max_val):
        if i not in arr:
            return i

arr = [3, 0, 1]
print(missing_num(arr))
