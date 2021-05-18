import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())
sade = list(map(int, input().split()))
sade.sort()

animals = []
for _ in range(m):
    x, y = map(int, input().split())
    animals.append((x, y))

def binary_search(a, b):
    l = 0
    r = n-1
    
    while l<=r:
        mid = (l+r)//2
        if sade[mid] < a:
            l = mid + 1
        elif a <= sade[mid] <= b:
            return 1
        else:
            r = mid - 1
    
    return 0

answer = 0
for i in range(m):
    x, y = animals[i]
    
    if l >= y:
        min_x = x - (l-y)
        max_x = x + (l-y)
        answer += binary_search(min_x, max_x)

print(answer)
