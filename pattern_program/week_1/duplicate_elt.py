def duplicate_elt(arr):
#    seen = {}
    seen = set()
    for i,num in enumerate(arr):
        if num in seen:
            return True
        seen.add(num)

    return False 

arr = [1,2,3,5,5]    
print(duplicate_elt(arr))
