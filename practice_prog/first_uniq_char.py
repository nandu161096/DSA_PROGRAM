def first_unique_char(s):
    count = {}

    for ch in s:
        count[ch] = count.get(ch,0) + 1

    for i,ch in enumerate(s):
        if count[ch] == 1:
            return i

    return -1

s = "leetcode"
print(first_unique_char(s))
s = "loveleetcode"
print(first_unique_char(s))
s = "aabbcc"
print(first_unique_char(s))
