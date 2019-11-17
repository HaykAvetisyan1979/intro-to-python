import sys
sys.path.append("/Users/G3/Desktop/intro-to-python/Week5/Homework")

from Productcheck import check


def buy(product, num, price):
    if check(product, num):
        print("You bought %s and spent %s" % (product, num*price))
    else:
        print("Sorry! We are out of this product.")


def main():
    buy("pen", 51, 2)


if __name__ == "__main__":
    main()
