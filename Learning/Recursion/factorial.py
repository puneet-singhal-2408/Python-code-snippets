""" The Factorial of a non-negative number.
    we have to multiply numbers from 1 to n.
    n! = n * (n-1) * (n-2) * ...... * 1
"""


# iterative approach

def factorial(n: int) -> int:
    """
    objective to compute the factorial of a number.
    n: input of numeric value.
    return: numeric value
    """
    fact = 1
    assert n >= 0
    for i in range(1, n + 1):
        fact = fact * i
    return fact


def factorial_recursion(n: int) -> int:
    """
    objective to compute the factorial of a number.
    if n is 0 or 1 return 1 else n * (n-1)
    n: input of numeric value.
    return: numeric value
    """
    assert n >= 0
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursion(n-1)


def main():
    n = int(input("Enter the number"))
    fact = factorial(n)
    re_fact = factorial_recursion(n)
    print(fact)
    print(re_fact)


if __name__ == "__main__":
    main()
