def  max_cnt_in_arr(nums):
    cnt = {}
    for num in nums:
        cnt[num] = cnt.get(num,0) + 1
    print(cnt)

    max_cnt = 0
    max_value = None
    for num, count in cnt.items():
        if count > max_cnt:
            max_cnt = count
            max_value = num

    return max_value


nums = [2,2,1,1,1,2,2,1,2,1,1,1]
print(max_cnt_in_arr(nums))
