def tgt_sum_index(arr, target):
    seen = set()

    for i, num in enumerate(arr):
        need = target - num

        if need in seen:
            return [seen[need],i+1]
        
        seen[num] = i+1

    return []

arr = [2,7,11,15]
target = 9
print(tgt_sum_index(arr,target))
