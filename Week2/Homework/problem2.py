import argparse
parser = argparse.ArgumentParser()
parser.add_argument("text", help="Text 7 or more characters long and has an odd number of characters", type=str)

args = parser.parse_args()

mid_pos = int((len(args.text)-1)/2)
mid_chars = args.text[mid_pos-1:mid_pos+2]
new_string = args.text[0:mid_pos-1] + mid_chars.upper() + args.text[mid_pos+2:]
print("The old string: ", args.text)
print("Middle 3 characters: ", mid_chars)
print("The new string: ", new_string)
