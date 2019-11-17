import sys
sys.path.append("/Users/G3/Desktop/intro-to-python/Week5")

from pretty_print import simple_print, pro_print


def calculate_cube(x):
    return x**3


def calculate_square(x):
    return x**2


def main():
    result1 = calculate_square(2)
    simple_print(result1)
    result2 = calculate_cube(4)
    pro_print(result2)


if __name__ == '__main__':
    main()
