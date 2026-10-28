def longsubstring(s):
    sub_len = 0
    visited = []
    curr_len = 0
    if not s:
        return None

    for ch in s:
        if ch not in visited:
            curr_len += 1
            visited.append(ch)
        else:
            curr_len = 0
            visited = []
        sub_len = max(curr_len, sub_len) 

    print(sub_len)

def longsubstring1(s):
    visited = set()
    left = 0
    max_len = 0

    for right in range(len(s)):

        while s[right] in visited:
            visited.remove(s[left])
            left += 1

        visited.add(s[right])
        max_len = max(max_len, right-left+1)

    print(max_len)

s = "abcabcbb"
longsubstring1(s)
s = "bbbbb"
longsubstring1(s)
s = "pwwkew"
longsubstring1(s)

