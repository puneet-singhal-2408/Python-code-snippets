"""
Linear search is sequential search of the list.
that scans the list from the beginning till the required value is found.
or the list is exhausted.
"""


def linear_search(lst, value):
    for i in lst:
        if i == value:
            return i
    return None
