def freq_of_arr(arr):
    freq = {}

    for num in arr:
        freq[num] = freq.get(num,0) + 1

    return freq

arr = [1,1,2,3,2,3,1,3,4,3]
print(freq_of_arr(arr))
