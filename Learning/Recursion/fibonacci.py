""" Fibonacci sequence is a sequence of integers. The first and second numbers in the sequence is 0 and 1.
    The next term is computed sum of immediately proceeding two terms.
    Fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13.......
"""


def iterative_method(n: int) -> int:
    """
    Compute the sum of first n numbers of fibonacci series.
    """
    assert n > 0
    second_last = 0
    last = 1
    result = 0
    if n == 1:
        return second_last
    elif n == 2:
        return last
    for i in range(3, n + 1):
        result = second_last + last
        second_last = last
        last = result
    return result


def recursive_method(n):
    """
        Compute the sum of first n numbers of fibonacci series.
    """
    assert n > 0
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return recursive_method(n-1) + recursive_method(n-2)


def main():
    n = int(input("Enter the number: "))
    series_sum = iterative_method(n)
    re_series_sum = recursive_method(n)
    print(series_sum)
    print(re_series_sum)


if __name__ == "__main__":
    main()
