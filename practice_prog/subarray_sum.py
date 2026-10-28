def subarray_sum(nums,k):
    count = 0
    prefix_sum = 0
    prefix_cnt = {0:1}

    for num in nums:
        prefix_sum += num

        if prefix_sum - k in prefix_cnt:
            count += prefix_cnt[prefix_sum - k]

        prefix_cnt[prefix_sum] = prefix_cnt.get(prefix_sum,0) + 1

    print(nums)
    print(prefix_cnt)

    return count

nums = [3, 4, 7, 2, -3, 1, 4, 2]
k = 7
#nums = [1,1,1]
#k = 2
print(subarray_sum(nums,k))


