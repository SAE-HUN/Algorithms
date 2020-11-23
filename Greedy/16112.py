n, k = map(int, input().split())
stone, answer = 0, 0

for reward in sorted(map(int, input().split())):
    answer += stone*reward
    
    if stone<k:
        stone += 1

print(answer)
