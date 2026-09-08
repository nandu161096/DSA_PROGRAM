def two_sum_tgt(arr, target):
    seen = {}

    for i, num in enumerate(arr):
        needed = target - num
        print("Before If check num ",num, "i", i,"needed", needed, "seen ", seen)

        if needed in seen:
            print("seen",seen,"i",i)
            return [seen[needed], i]

        seen[num] = i

    return []

arr = [11,1,7,2]
target = 9
print(two_sum_tgt(arr,target))
