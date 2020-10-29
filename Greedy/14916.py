n = int(input())

if n < 5:
	if n % 2 != 0:
		print(-1)
	else:
		print(n//2)
else:
	a = n // 5
	b = (n-5*a) // 2
	if 5*a + 2*b != n:
		a -= 1
		b = (n-5*a) // 2
	print(a+b)
