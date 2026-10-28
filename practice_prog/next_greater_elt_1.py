def nextGreaterElt(nums1, nums2):
    nxt_greater = {}
    stack = []
    result = []

    for num in nums2:

        while stack and num > stack[-1]:
#        while stack and stack[-1] < num:
            nxt_greater[stack.pop()] = num
        stack.append(num)

    while stack:
        nxt_greater[stack.pop()] = -1 

    for num in nums1:
        result.append(nxt_greater[num])

    return result

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreaterElt(nums1,nums2))
