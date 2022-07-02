"""
Merge Sort Algorithm.

It is based on divide and conquer strategy.
It takes a list of N input and keep on dividing it until a list if length 1 is obtained.
Then it compare the first element of the list and merge hem in sorted order.

"""

"""
Steps:
- Divide a list into two equal parts till the list of length 1 is obtained.
- call a merge function on the divided two list.
- In merge function:
    - create an empty list.
    - compare the first element of both list.
    - append lower value to empty list and remove it from original list.
    - once one of the two list is empty append the remaining list to empty list.
    - return sorted list.
"""


def merge(lst1, lst2):
    sorted_lst = []
    while len(lst1) != 0 and len(lst2) != 0:
        if lst1[0] < lst2[0]:
            sorted_lst.append(lst1[0])
            lst1.remove(lst1[0])
        else:
            sorted_lst.append(lst2[0])
            lst2.remove(lst2[0])
    if len(lst1) == 0:
        sorted_lst.append(lst2)
    else:
        sorted_lst.append(lst1)
    return sorted_lst


def merge_sort(lst):
    mid = len(lst)//2
    if len(lst) <= 1:
        return lst
    else:
        lst1 = merge_sort(lst[:mid])
        lst2 = merge_sort(lst[mid:])
        return merge(lst1, lst2)
