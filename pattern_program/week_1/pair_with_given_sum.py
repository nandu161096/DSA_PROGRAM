def pair_with_given_tgt(arr, target):
    seen = set()
    pairs = set()

    for num in arr:
        need = target - num

        if need in seen:
            pairs.add(tuple(sorted((num, need))))

        seen.add(num)

    return pairs

#arr = [1,5,7,-1,5]
arr = [-1,7,1,5,5]
target = 6
print(pair_with_given_tgt(arr, target))
