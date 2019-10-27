import argparse
parser = argparse.ArgumentParser()
parser.add_argument("text",help="Initial text to edit", type=str)
parser.add_argument("first_word",help="first word to replace", type=str)
parser.add_argument("second_word", help="the second word to replace with", type=str)
args = parser.parse_args()

print("The given text: ", args.text)
print("First word: ", args.first_word)
print("Second word: " + args.second_word)
print("Output string: ", args.text.replace(args.first_word, args.second_word))
