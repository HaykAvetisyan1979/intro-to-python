import argparse
parser = argparse.ArgumentParser()
parser.add_argument("key1", type=str)
parser.add_argument("val1", type=str)
args = parser.parse_args()
key1 = args.key1
val1 = args.val1

dict1={"first": "text1", "second": "text2","third": "text3"}
print(dict1)
dict1.update({key1: val1})
print(dict1)
