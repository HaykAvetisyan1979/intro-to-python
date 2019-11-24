
def decorator(fn):
    def wrapper(*args, **kwargs):
        print("1")
        k = fn(*args, **kwargs)
        k.append('*')
        print("2")
        return k

    return wrapper

@decorator
def sq(lst):
    return list(map(lambda x: x**2, lst))


l1 = [5, 3]
res = sq(l1)
print(res)
