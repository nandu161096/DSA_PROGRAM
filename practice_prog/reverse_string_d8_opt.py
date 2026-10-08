def reverse_str(string):
    string = list(string)
    left = 0 
    right = len(string) - 1
    while left < right:
        string[left], string[right] = string[right], string[left]
        left += 1
        right -= 1
    return ''.join(string)

string = "Embedded"
print(reverse_str(string))
