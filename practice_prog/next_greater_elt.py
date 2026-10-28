def nextGreaterElt(nums1, nums2):
    stack = []
    nxt_greater = {}
    print(nums1)
    print(nums2)

    for num in nums2:
        while stack and stack[-1] < num:
            prev = stack.pop()
            nxt_greater[prev] = num
            print("nxt greater",nxt_greater)
        stack.append(num)
        print("in the num2",stack)

    print(stack,"\n")
    print(nxt_greater)

    while stack:
        nxt_greater[stack.pop()] = -1

    print("after stack",nxt_greater)
    result = []

    for num in nums1:
        result.append(nxt_greater[num])

    return result

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreaterElt(nums1,nums2))
