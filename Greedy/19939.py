n, k = map(int, input().split())
a = sum(range(k+1))

if a>n:
    print(-1)
else:
    print(k-1+int((n-a)%k!=0))
