def MIS():
    return map(int, input().split())

n, x = MIS()

if x<n or 26*n<x:
    print('!')
    exit()

answer = ['A']*n
i = n-1; x -= n

while x:
    a = min(25, x)
    x -= a
    answer[i] = chr(65+a)
    i -= 1

print(''.join(answer))
