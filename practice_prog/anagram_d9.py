def is_anagram(s,t):
    if len(s) != len(t):
        return False
    str1 = {}
    str2 = {}
#    s.sort()
#    t.sort()

    for ch in s:
        if ch in str1:
            str1[ch] += 1
        else:
            str1[ch] = 1

    for ch in t:
        if ch in str2:
            str2[ch] += 1
        else:
            str2[ch] = 1

    if str1 == str2:
        return True
    else:
        return False

s = "listen"
t = "silent"
print(is_anagram(s,t))
