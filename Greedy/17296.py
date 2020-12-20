def II():
    return int(input())

def MIS():
    return map(int, input().split())

n = II()
A = [*map(float, input().split())]
answer = 0

for i, a in enumerate(A):
    if a!=0.0:
        answer = 1
        A[i] -= 0.5
        break

for a in A:
    a -= 0.5
    
    if a>0:
        answer += round(a+0.1)

print(answer)
