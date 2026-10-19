def contains_dup(nums):
    count = {}

    for num in nums:
        count[num] = count.get(num,0) + 1

        if count[num] > 1:
            return True

    return False

nums = [1, 2, 3, 1]
print(contains_dup(nums))
