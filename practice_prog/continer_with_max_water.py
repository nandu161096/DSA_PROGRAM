def maxarea(height):
    left = 0
    right = len(height) -1 
    max_area = float("-inf")
    while left < right:
        curr_area = min(height[left], height[right]) * (right - left)
        max_area = max(curr_area, max_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxarea(height))
