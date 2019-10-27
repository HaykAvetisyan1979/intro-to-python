import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", help="Inputing text",type=str)
args = parser.parse_args()

print("Thegiven string is:", args.text)
print("All lowercase: ", args.text.lower())
print("All uppercase: ", args.text.upper())

