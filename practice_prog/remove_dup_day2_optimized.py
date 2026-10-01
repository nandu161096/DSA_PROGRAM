def remove_duplicates(arr):
    seen = set()
    result = []

    for nums in arr:
        if nums not in seen:
            seen.add(nums)
            result.append(nums)
    
    return result

arr = [1, 2, 2, 3, 1, 4, 3]
print(arr)
print(remove_duplicates(arr))
