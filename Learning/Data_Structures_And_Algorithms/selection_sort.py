"""

Selection Sort Algorithm:

In selection sort we find the smallest value in the list,
and interchange it with the first value in the list.
Next, we find the smallest value out of remaining entries in the list.
and interchange it with second value in the list and so on.

"""

"""
Steps:
- iterate over the list and assume smallest value is at index 0.
- iterate over the complete list & compare each element with value at minimum index.
- if other value is not greater than minimum index assign minimum index to index of smaller value.
- once you have compared all value and have final value of min index.
- swap the values of first index with min index.
- repeat for remaining list.
"""


def selection_sort(lst):
    for i in range(0, len(lst) - 1):
        min_index = i
        for j in range(i, len(lst) - 1):
            if lst[j] < lst[min_index]:
                min_index = j
        if min_index != i:
            lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst
