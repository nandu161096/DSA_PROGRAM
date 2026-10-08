def reverse_str(string):
    rev_str = []
    k = 0
    for i in range(len(string)-1,-1,-1):
        rev_str.append(string[i])

    return ''.join(rev_str)

string = "Embedded"
print(reverse_str(string))
