def is_happy(n):
    seen = set() 
    while n!= 1 and n not in seen:
        seen.add(n)
        print("seen set ",seen)
        total = 0
        while n > 0:
            print("inside nested while n",n)
            dgt = n % 10
            total += dgt * dgt
            n //= 10
        print("total",total,"dgt",dgt)
        n = total

    return n == 1
    

print(is_happy(19))
#print(is_happy(2))

