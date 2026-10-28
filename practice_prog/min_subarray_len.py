def min_sub_arr(nums,target):
    min_len = float("inf")
    left = 0
    curr_sum = 0
    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum >= target:
            min_len = min(min_len, right-left+1)
            curr_sum -= nums[left]
            left += 1

    print("min lenght is ",min_len)

target = 7
nums = [2, 3, 1, 2, 4, 3]
min_sub_arr(nums, target)
