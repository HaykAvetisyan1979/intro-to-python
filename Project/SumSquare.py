
lst1 = [2, 5, 12, 25, 37, 56, 1254, 1454, 1147, 1937564]

list2 = list(map(lambda x: x**3, lst1))
print(list2)
for i in range(len(lst1)):
    print(lst1[i], "=>", list2[i])
