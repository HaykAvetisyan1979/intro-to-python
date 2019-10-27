import argparse
parser = argparse.ArgumentParser()
parser.add_argument("text", help="Text", type=str)
parser.add_argument("start_index", help="Text", type=int)
parser.add_argument("end_index", help="Text", type=int)

args = parser.parse_args()

print("The given text: " + args.text)
print("Start index: ", args.start_index)
print("End index: " + str(args.end_index))
print("Output string: ", args.text[args.start_index:args.end_index])

