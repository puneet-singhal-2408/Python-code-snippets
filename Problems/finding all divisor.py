x = int(input("enter number : "))
a = range(2, x)
b = []
for element in a:
    if x% element == 0:
       b.append(element)
print(b)
