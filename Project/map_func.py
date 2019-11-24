def func1(x, y):
    return x+y

set1 = {2, 6, 5}
set2 = {4, 7, 3}
f2 = map(func1, set1, set2)
print(set1)
print(set2)

print(list(f2))
