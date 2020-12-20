import sys

def MIS():
    return map(int, sys.stdin.readline().split())

n, w = MIS()
three, five = [], []

for _ in range(n):
    t, s = MIS()
    
    if t==3:
        three.append(s)
    else:
        five.append(s)

three.sort(reverse=True); five.sort(reverse=True)
three.insert(0, 0); five.insert(0, 0)

for i in range(1, len(three)):
    three[i] += three[i-1]

for i in range(1, len(five)):
    five[i] += five[i-1]

answer = 0

for i in range(len(five)):
    if i*5>w:
        break
    
    j = min((w-i*5)//3, len(three)-1)
    answer = max(answer, three[j]+five[i])

print(answer)
