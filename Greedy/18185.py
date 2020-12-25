import sys
import heapq

def II():
    return int(sys.stdin.readline().strip())

def MIS():
    return map(int, sys.stdin.readline().split())

n = II()
r = [*MIS()]

answer = 0
for i in range(n-2):
    if r[i+1]>r[i+2]:
        mnt = min(r[i], r[i+1]-r[i+2])
        answer += 5*mnt
        r[i] -= mnt
        r[i+1] -= mnt
        
        mnt = min(r[i], r[i+1], r[i+2])
        answer += 7*mnt
        r[i] -= mnt
        r[i+1] -= mnt
        r[i+2] -= mnt
    else:
        mnt = min(r[i], r[i+1], r[i+2])
        answer += 7*mnt
        r[i] -= mnt
        r[i+1] -= mnt
        r[i+2] -= mnt
        
        mnt = min(r[i], r[i+1])
        answer += 5*mnt
        r[i] -= mnt
        r[i+1] -= mnt
    
    answer += 3*r[i]
    r[i] = 0

mnt = min(r[n-2], r[n-1])
answer += 5*mnt
r[n-2] -= mnt
r[n-1] -= mnt
answer += 3*r[n-2]
answer += 3*r[n-1]

print(answer)
