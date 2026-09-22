from collections import Counter
def checkperm(s1,s2):
    n = len(s1)
    
    need = Counter(s1)
    window = Counter(s2[:n])
    
    if need == window:
        return True
    
    for i in range(n, len(s2)):
        window[s2[i]] += 1
        left_char = s2[i-n]
        print(left_char,i,n)
        window[left_char] -= 1
        
        if window[left_char] == 0:
            del window[left_char]
        
        if need == window:
            return True
    
    return False

print(checkperm("ab","eidbaooo"))
