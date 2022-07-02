"""
Quick Sort Algorithm.

It works by choosing a value called pivot value.
using which we split the list to be sorted in 2 parts.
First part values are smaller than pivot element.
Second part values are greater than pivot element.
The two parts are further sorted using quick sort in similar manner.
Until the partitions of length 1 or 0 are left.

"""


def partition(lst, start, end):
    pivot_element = lst[end]
    i = start - 1
    for j in range(start, end):
        if lst[j] <= pivot_element:
            i += 1
