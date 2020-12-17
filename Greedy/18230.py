n, a, b = map(int, input().split())
A_tile = sorted([*map(int, input().split())])
B_tile = sorted([*map(int, input().split())])

answer = 0
if n%2:
    answer += A_tile.pop()
    n -= 1

while n:
    if len(A_tile)>1 and B_tile and A_tile[-1]+A_tile[-2]>B_tile[-1]:
        answer += A_tile.pop()+A_tile.pop()
        n -= 2
    elif B_tile:
        answer += B_tile.pop()
        n -= 2
    else:
        answer += A_tile.pop()
        n -= 1

print(answer)
