def reverse_char(s, left, right):
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -=1

def reverse_words(s):
    s = list(s)
    reverse_char(s, 0, len(s)-1)
    start = 0 
    for i in range(len(s)):
        if s[i] == ' ':
            reverse_char(s,start,i-1)
            start = i + 1
    
    reverse_char(s,start,len(s)-1)
    return ''.join(s)


s = "Qualcomm Bangalore"
print(s)
print(reverse_words(s))
