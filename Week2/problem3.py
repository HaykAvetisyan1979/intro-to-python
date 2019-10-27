import argparse
parser = argparse.ArgumentParser()
parser.add_argument("name", help="Input your name: ", type=str)

args = parser.parse_args()

print("Welcome, " + args.name)

