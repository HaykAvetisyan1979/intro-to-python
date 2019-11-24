class Vector(list):
    def __init__(self, vec):
        super().__init__()
        self.vector = vec
        self.m = len(vec)

    # making vector type objects iterable i.e defining for them __iter__() and __next__() magic functions (methods)
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.m:
            result = self.vector[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

# defining __mul__ built in method which works with operand "*" on objects of class <vector> inherited from class <list>
    def __mul__(self, another):
        return sum(list(map(lambda x, y: x * y, self.vector, another)))


v = Vector([1, 2, 3, 4])
z = Vector([5, 1, 3, 2])
# v.product(z)
for item in v:
    print(item)
print(v.vector, "*", z.vector, "=", v*z)
