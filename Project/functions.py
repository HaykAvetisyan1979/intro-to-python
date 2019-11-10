num_list = [0, 1, 2, 3, 4, 5]

double_list = map(lambda n: n * 2, num_list)

print(list(double_list))


def custom(changer, list1):
    return changer(list1)


list2 = [1, 2, 3, 4, 5]
print(list2)
print(custom(lambda m: max(m), list2))


def mapping_func(list1):
    return list(map(lambda x: x**3, list1))


print(custom(mapping_func, list2))
print(list(custom(lambda y_list: map(lambda x: x**3, y_list), list2)))

