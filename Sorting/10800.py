import sys
input = sys.stdin.readline

n = int(input())
players = []

for i in range(n):
    color, size = map(int, input().split())
    players.append((i, color, size))

players.sort(key=lambda x: (x[2], x[1]))
answer = [0]*n
acc = 0
color_acc = [0]*(n+1)
j = 0

for i in range(n):
    a = players[i]
    b  = players[j]
    
    while b[2]<a[2]:
        acc += b[2]
        color_acc[b[1]] += b[2]
        j += 1
        b = players[j]
    
    answer[a[0]] = acc - color_acc[a[1]]

for a in answer:
    print(a)
