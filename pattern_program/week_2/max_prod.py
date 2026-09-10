def max_prod(arr):
    n = len(arr)
    max_prod = float('-inf')
    lefttoright = 1
    righttoleft = 1
    for i in range(n):
        if lefttoright == 0:
            lefttoright = 1
        if righttoleft == 0:
            righttoleft = 1

        lefttoright *= arr[i]
        j = n - i - 1
        righttoleft *= arr[j]
        max_prod = max(lefttoright, righttoleft, max_prod)

    return max_prod

arr = [-2, 6, -3, -10, 0, 2]
print(max_prod(arr))

