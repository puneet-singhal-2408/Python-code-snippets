a = [1, 1, 2, 3, 5,1, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for x in b:
    if x in a:
        c.append(x)

print(c)
