import argparse

parser = argparse.ArgumentParser()
parser.add_argument("arg1", type=int)
args = parser.parse_args()

value = args.arg1
set1 = {1, 2, 3, "a"}
print(set1)
set1.add(value)
print(set1)
