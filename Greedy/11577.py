def MIS():
    return map(int, input().split())

n, k = MIS()
lights = [*MIS()]
answer = 0

for i in range(n-k+1):
    if lights[i]==1:
        answer += 1
        
        for j in range(i, i+k):
            lights[j] = -lights[j]+1

print('Insomnia' if 1 in lights else answer)
