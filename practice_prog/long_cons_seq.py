def longest_cons_seq(nums):
    if not nums:
        return 0

    nums_sorted = sorted(set(nums))

    curr_len = 1
    max_len = 1
    for i in range(1,len(nums)):
        if (nums_sorted[i] == (nums_sorted[i-1])+1):
            curr_len += 1
        else:
            max_len = max(max_len, curr_len)
            curr_len = 1

    max_len = max(max_len, curr_len)
    return max_len

nums = [100, 4, 200, 1, 3, 2]
print(longest_cons_seq(nums))
