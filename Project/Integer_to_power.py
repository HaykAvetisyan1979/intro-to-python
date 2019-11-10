num = input("Input integer: ")
y = input("power")

# number of ways the inputed integer can be represented as sum of n-th power of uniq natural numbers

def pow_num(number, power):
    sum = 0
    for n in range(number):
        sum += n**power
        if n == number:
            result += 1

    number**power