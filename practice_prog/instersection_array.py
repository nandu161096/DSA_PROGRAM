def intersec_arr(nums1, nums2):
    inter_sec = []

    for num in nums1:
        if num in nums2 and num not in inter_sec:
            inter_sec.append(num)

    return inter_sec

def intersec_arr_opt(nums1, nums2):
    inter_sec = []
    nums2_set = set(nums2)
    result = set()

    for num in nums1:
        if num in nums2_set:
            result.add(num)

    return list(result)

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
#print(intersec_arr(nums1,nums2))
print(intersec_arr_opt(nums1,nums2))
