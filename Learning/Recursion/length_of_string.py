""" Finding length of a string using recursion.
    we will simply slice the string and add 1 for it until the string is empty.
"""


def length(n: str) -> int:
    """compute the length of string"""
    if n == '':
        return 0
    else:
        return 1 + length(n[1:])


def main():
    n = input(" Enter the string: ")
    length_of_string = length(n)
    print(length_of_string)


if __name__ == "__main__":
    main()
