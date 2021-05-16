from functools import reduce

n = list(input())
if reduce(lambda x, y: x+int(y), n, 0)%3 == 0 and '0' in n:
    n.sort(reverse=True)
    print(''.join(n))
else:
    print(-1)
