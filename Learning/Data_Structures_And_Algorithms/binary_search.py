"""
Binary search works on sorted list only.
In binary search we examine the middle value.
If it matches the required value we stop.
Else we have to search on left or right side of middle value.
Depending on whether the searched value is greater or lesser than middle value.
"""


"""
Steps:
1. check if list is sorted.
2. find mid value and check with required value
3. compare if value is greater or lesser.
4. based on above comparison check in left or right.
"""


def is_sorted(lst):
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            return False
    return True


def binary_search(lst, value):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = int((low + high)/2)
        if lst[mid] == value:
            return mid
        elif lst[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return None
