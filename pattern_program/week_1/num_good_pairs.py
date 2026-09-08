def num_good_pairs(nums):
    seen = {}
    good_pair = 0
    for num in nums:
        if num in seen:
            good_pair += seen[num]
            seen[num] += 1
        else:
            seen[num] = 1

    return good_pair

nums = [1,2,3,1,1,3]
print(num_good_pairs(nums))
