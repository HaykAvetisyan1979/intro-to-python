import argparse

parser = argparse.ArgumentParser()
parser.add_argument("arg1", type=int)
args = parser.parse_args()

list4 = [1, 2, 3, 3, 4, "a"]
value = args.arg1

print("Before", list4)
list4.remove(value)
print("After: ", list4)

