import argparse, datetime

parser = argparse.ArgumentParser()
parser.add_argument("--num_y", help="the number of years",type=int)
parser.add_argument("--num_d", help="the number of days", type=int)
args = parser.parse_args()

currDate = datetime.datetime.today()
adding = datetime.timedelta(days=0)

print("Current date: ", currDate)

if args.num_y:
    adding += datetime.timedelta(days=args.num_y*365)
    print("Given years: ", args.num_y)
else:
    print("Given years: ", "Not given")

if args.num_d:
    adding += datetime.timedelta(days=args.num_d)
    print("Given days: ", args.num_d)
else:
    print("Given days: ", "Not given")

print("Final date: ", currDate+adding)





