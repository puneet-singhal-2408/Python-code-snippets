n = int(input())
m = 3 * n
a = m-3
x =1
c = a//2
thickness = m-7
for i in range(n):
    if i == (n//2):
        print("-" * (thickness//2) + "WELCOME" + "-" * (thickness//2))
    elif i > (n//2):
        c = c+3
        x -= 2
        print("-"* c + ".|."*x +"-"* c)
    else:
        print("-"* c + ".|."*x +"-"* c)
        c = c-3
        x += 2

