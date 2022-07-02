#task
#You are given a string S. 
#Your task is to print all possible combinations, up to size K
#,of the string in lexicographic sorted order.



from itertools import combinations
a, b = map(str,input().split())
empty_list = []
for i in range(int(b)):
    required_combinations = list(combinations(a,(i+1)))
    required_combinations.sort()
    if i <= 0 :
        list1 = []
        for element in required_combinations:
            list1.append(element[0])
            list1.sort()
        empty_list.append(list1)      
    elif i >  0:
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
