"""
Insertion Sort Algorithm

In insertion sort the list is divided into two parts.
Sorted and unsorted list then element of unsorted list are compared to elements of sorted list.
The values are then inserted at correct place if found out of order.

"""

"""
Steps:
- divide list in two parts(sorted and unsorted lists).
- assign the first value of unsorted list to temp variable.
- compare the temp. value with list values.
- Insert temp. value at current value if the current value is greater than temp/value.
- Repeat again.
"""


def insertion_sort(lst):
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i-1
        while j >= 0 and lst[j] > temp:
            lst[j+1] = lst[j]
            j = j-1
        lst[j+1] = temp
    return lst
