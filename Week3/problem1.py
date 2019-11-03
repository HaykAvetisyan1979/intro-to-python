import sys

list1 = ["hello", 1, True]
list2 = sys.argv[1:]
list1.extend(list2)
print(list1)
