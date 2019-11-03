import argparse
parser = argparse.ArgumentParser()
parser.add_argument("val", type=int)
args = parser.parse_args()

value = args.val

set3 = {1, 2, 3, 4, 5, 6, 7}

if (value > min(set3)) and (value < max(set3)):
    print("Yes it is between %d and %d" % (min(set3), max(set3)))
else:
    print("Unfortunately it is not between %d and %d" % (min(set3), max(set3)))
