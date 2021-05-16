import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * 10001

for i in range(n):
    a = int(input())
    arr[a] += 1

for i in range(1, 10001):
    print(f'{i}\n' * arr[i], end='')
