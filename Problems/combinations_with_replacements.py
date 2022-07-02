from itertools import combinations_with_replacement

a, b = map(str, input().split())
empty_list = []
required_combinations = list(combinations_with_replacement(a, int(b)))
required_combinations.sort()
list2 = []
for ele in required_combinations:
    new_list = list(ele)
    new_list.sort()
    list2.append("".join(new_list))
    list2.sort()
empty_list.append(list2)

for new_el in empty_list:
    for elements in new_el:
        print(elements)
