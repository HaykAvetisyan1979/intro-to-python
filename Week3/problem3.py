import argparse

parser = argparse.ArgumentParser()
parser.add_argument("arg1", type=int)
args = parser.parse_args()

list2 = [1, 2, 3, 3, 4, "a"]
value = args.arg1

print("in this example user input is %s , the list2 is" % value, list2)
print("\n")
print("list2=", list2)
count = list2.count(value)
print("Number of %s s =" % value, count)

