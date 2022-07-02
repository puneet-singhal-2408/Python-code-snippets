from collections import Counter
num_of_shoes = int(input())
size_list = list(map(int, input().split(" ")))
shoe_dic = Counter(size_list)
num_of_customer = int(input())
order_list =[]
total_amount = 0
for i in range(num_of_customer):
	customer_order = list(map(int, input().split(" ")))
	order_list.append(customer_order)
for j in order_list:
	if j[0] in shoe_dic and shoe_dic[j[0]] !=0:
		shoe_dic[j[0]] -=1
		total_amount += j[1]
	elif j[0] not in shoe_dic and shoe_dic[j[0]] ==0:
		print("Shoe not available")

print(total_amount)



