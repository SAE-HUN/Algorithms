n = int(input())
children = list(map(int, input().split()))
lis = [0] * (n+1)

for child in children:
	lis[child] = lis[child-1] + 1
	
print(n-max(lis))
