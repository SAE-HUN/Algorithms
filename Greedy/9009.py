from bisect import *

def get_fibo(n):
    sqrt_5 = 5 ** (1/2)
    ans = 1 / sqrt_5 * ( ((1 + sqrt_5) / 2) ** n  - ((1 - sqrt_5) / 2) ** n )
    return int(ans)
    
t = int(input())
cases = [int(input()) for _ in range(t)]
fibonaccies, n = [], 0
max_case = max(cases)

while True:
	fibonacci = get_fibo(n)
	if fibonacci > max_case:
		break
	fibonaccies.append(fibonacci)
	n += 1
	
for case in cases:
	answer = []
	while case:
		max_fibonacci = fibonaccies[bisect(fibonaccies, case)-1]
		case -= max_fibonacci
		answer.append(max_fibonacci)
	answer.sort()
	for a in answer:
		print(a, end=' ')
	print()
