num = input("Input number: ")


# returning inputted string as an integer

def atoi(n):
    if len(n) == 1:
        return int(n)

    return int(n[0])*10**(len(n)-1) + atoi(n[1:])


print(atoi(num), type(atoi(num)))
