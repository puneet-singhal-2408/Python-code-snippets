import string
alpha = string.ascii_lowercase
n = 5
l = []
for i in range(n):
	s = "-".join(alpha[i:n])
	l.append((s[::-1]+s[1:]).center(n*3-1, "-"))
print('\n'.join(l[:0:-1]+l))
