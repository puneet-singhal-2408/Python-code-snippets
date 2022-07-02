"""
Bubble sort Algorithm

Bubble sort uses straight forward approach that works by,
repeated swapping of the adjacent element if they are found out of order.

Note:
    when you check the element from start to end.
    Sometimes list get sorted before all iteration.
    In such case we can break through.
"""

"""
- iterate over the list from start or end.
- choose any 2 values from start or end of list.
- compare and swap if the values are out of order.
- take a variable and set it True if any swap happen else set it false.
- Repeat till sorted.
"""


def bubble_sort(lst):
    for i in range(0, len(lst) - 1):
        swap = False
        for j in range(len(lst) - 1, i, -1):
            if lst[j] < lst[j - 1]:
                swap = True
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
        if not swap:
            break
    return lst
