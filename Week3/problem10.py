import argparse
parser = argparse.ArgumentParser()
parser.add_argument("val", type=int)
args = parser.parse_args()

value = args.val

set2 = {1, 2, 3, 4, "a"}
print(set2)
set2.discard(value)
print(set2)
