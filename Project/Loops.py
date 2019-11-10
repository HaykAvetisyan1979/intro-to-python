def check_balance(brackets):  # The argument is a string

    if brackets == "":
        return True

    brackets = list(brackets)

    count1 = brackets.count("[")
    count2 = brackets.count("]")

    if brackets[0] == "]" or count1 != count2:
        return False

    for i in range(len(brackets)):
        if brackets[i] == "[":
            for j in range(i+1, len(brackets)):
                if brackets[j] == "]":
                    brackets[i] = "0"
                    brackets[j] = "0"
                    break
                else:
                    continue

    if brackets.count("[") + brackets.count("]") > 0:
        return False
    else:
        return True


cont = 1

# Engine body:
while cont != 0:
    brs = input("Input brackets string: ")
    print(check_balance(brs))
    cont = input("Continue? 1-Yes; 0-No  :")
