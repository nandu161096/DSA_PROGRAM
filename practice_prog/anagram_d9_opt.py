def is_anagram(s,t):
    if len(s) != len(t):
        return False
    str1 = {}
    str2 = {}
#    s.sort()
#    t.sort()

    for ch in s:
        str1[ch] = str1.get(ch,0) + 1

    for ch in t:
        if ch not in str1:
            return False

        str1[ch] -= 1

        if str1[ch] == 0:
            del str1[ch]

    return len(str1) == 0

s = "listen"
t = "silent"
print(is_anagram(s,t))
s = "listen"
t = "abcdfr"
print(is_anagram(s,t))
