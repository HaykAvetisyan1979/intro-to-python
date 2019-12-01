def Dec_toBin(n):   # Binary converter via recursion
    if n//2==0:
        return 0
    else:
        n //= 2
        Dec_toBin()
