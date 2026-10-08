def is_palin(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

string = "madam"
print(is_palin(string))
string = "embedded"
print(is_palin(string))
