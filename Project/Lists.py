x = [11, 9, 7, 7, 5, 4, 4, 3, 3, 1, 2]
print(x)
m = 7
k = 4
"""
for i in range(0, len(x)):
    if m in x[i:]:
        x.pop(x.index(m, i))
        x.pop(x.index(k, i))

print(x)
"""

print(list(filter(lambda n: n != 7, x)))
