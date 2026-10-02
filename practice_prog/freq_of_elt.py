def freq_of_elt(arr):
    count = {}

    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    return count

arr = [1, 2, 2, 3, 1, 2]
print(freq_of_elt(arr))
